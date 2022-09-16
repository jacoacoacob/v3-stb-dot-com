from django import forms
from django.forms.utils import ErrorList
from django.utils.functional import cached_property

from wagtail.blocks import StructBlock, URLBlock, PageChooserBlock, ChoiceBlock, CharBlock
from wagtail.blocks.struct_block import StructBlockAdapter, StructBlockValidationError
from wagtail.telepath import register


class LinkBlock(StructBlock):
  text = CharBlock(max_length=240)
  kind = ChoiceBlock(
    default="url",
    choices=[
      ("url", "URL"),
      ("page", "Page"),
    ],
    help_text='If you want to link to a page on some other website (e.g. twitter.com) chose "URL". If you want to link to a page on this site, choose "Page"'
  )
  page = PageChooserBlock(required=False)
  url = URLBlock(required=False, label="URL")

  def clean(self, value):
    kind = value.get("kind")
    page = value.get("page")
    url = value.get("url")
    if kind == "page":
      if not page:
        raise StructBlockValidationError({
          "page": ErrorList(["You must select a page"])
        })
      value.update({ "url": None })
    elif kind == "url":
      if not url:
        raise StructBlockValidationError({
          "url": ErrorList(["You must enter a url"])
        })
      value.update({ "page": None })
    return super().clean(value)

  class Meta:
    form_template = "link_block.html"
    form_classname = "struct-block link-block"


class LinkBlockAdapter(StructBlockAdapter):
  js_constructor = "blocks.models.LinkBlock"

  @cached_property
  def media(self):
    struct_block_media = super().media
    return forms.Media(
      js=struct_block_media._js + ["link-block.js"]
    )


register(LinkBlockAdapter(), LinkBlock)
