from django import forms
from django.forms.utils import ErrorList
from django.utils.functional import cached_property

from wagtail.blocks import StructBlock, URLBlock, PageChooserBlock, ChoiceBlock, CharBlock
from wagtail.blocks.struct_block import StructValue, StructBlockAdapter, StructBlockValidationError
from wagtail.telepath import register

class LinkBlockValidator:
  def __init__(self, value) -> None:
    self.value = value
    self.errors = {}

  def check_is_some(self, field):
    if not self.value.get(field):
      self.errors.update({ field: ErrorList(["This field is required."]) })
  
  def assert_valid(self):
    if len(self.errors.keys()) > 0:
      raise StructBlockValidationError(self.errors)


class LinkBlockValue(StructValue):
  def href(self):
    if self.get("_kind") == "PAGE":
      return self.get("_page").url
    return self.get("_url")

  def text(self):
    if self.get("_kind") == "PAGE":
      return self.get("_text") or self.get("_page").title
    return self.get("_text")


class LinkBlock(StructBlock):
  _text = CharBlock(max_length=240, required=False, label="Text")
  _kind = ChoiceBlock(
    label="Kind",
    required=True,
    default="URL",
    choices=[
      ("URL", "URL"),
      ("PAGE", "Page"),
    ],
    help_text='If you want to link to a page on some other website (e.g. twitter.com) chose "URL". If you want to link to a page on this site, choose "Page"'
  )
  _page = PageChooserBlock(required=False, label="Page")
  _url = URLBlock(required=False, label="URL")

  def clean(self, value):
    validator = LinkBlockValidator(value)
    kind = value.get("_kind")
    if kind == "PAGE":
      validator.check_is_some("_page")
      validator.assert_valid()
      value.update({ "_url": None })
    if kind == "URL":
      validator.check_is_some("_text")
      validator.check_is_some("_url")
      validator.assert_valid()
      value.update({ "_page": None })
    return super().clean(value)

  class Meta:
    form_classname = "struct-block link-block"
    value_class = LinkBlockValue


class LinkBlockAdapter(StructBlockAdapter):
  js_constructor = "blocks.models.LinkBlock"

  @cached_property
  def media(self):
    struct_block_media = super().media
    return forms.Media(
      js=struct_block_media._js + ["link-block.js"]
    )

register(LinkBlockAdapter(), LinkBlock)
