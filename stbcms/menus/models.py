from django.db import models

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.blocks import StreamBlock, StructBlock, ListBlock, CharBlock, PageChooserBlock, BooleanBlock
from wagtail.fields import StreamField
from wagtail.models import Orderable
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.models import register_snippet

from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from blocks.models import LinkBlock


class MenuSectionItem(Orderable):
  text = models.CharField(max_length=80)
  external_url = models.URLField(blank=True)
  page = models.ForeignKey(
    "wagtailcore.Page",
    null=True,
    blank=True,
    related_name="+",
    on_delete=models.CASCADE
  )

  @property
  def href(self):
    return self.external_url or self.page.url

  @property
  def is_external(self):
    return self.page is None

  panels = [
    FieldPanel("text"),
    FieldPanel("external_url"),
    FieldPanel("page"),
  ]

  parent = ParentalKey("MenuSection", related_name="items")

  def __str__(self) -> str:
    return self.text


@register_snippet
class MenuSection(ClusterableModel):
  title = models.CharField(max_length=140)
  slug = AutoSlugField(populate_from="title", editable=True)

  panels = [
    FieldPanel("title"),
    FieldPanel("slug"),
    InlinePanel("items", heading="Links", label="Link"),
  ]

  def __str__(self) -> str:
    return f"[menu-section] {self.title}"


class NavbarBlock(StructBlock):
  brand = CharBlock(max_length=32)
  pages = ListBlock(PageChooserBlock())
  call_to_action = ListBlock(LinkBlock(), max_num=2)


class MobileMenuBlock(StructBlock):
  brand = CharBlock(max_length=32)
  pages = ListBlock(PageChooserBlock())
  call_to_action = ListBlock(LinkBlock(), max_num=2)
  include_social_media = BooleanBlock(required=False)


class MenuSectionBlock(StructBlock):
  title = CharBlock(max_length=64, blank=True, null=True, label="Section Title")
  items = ListBlock(LinkBlock())

class FooterBlock(StructBlock):
  sections = ListBlock(MenuSectionBlock())
  include_social_media = BooleanBlock(required=False)


class MenuVariantBlock(StreamBlock):
  footer = FooterBlock()
  mobile_menu = MobileMenuBlock()
  navbar = NavbarBlock()



class Menu(ClusterableModel):
  title = models.CharField(max_length=140, unique=True)
  slug = AutoSlugField(populate_from="title", editable=True)

  variant = StreamField(
    [
      ("footer", FooterBlock()),
      ("mobile_menu", MobileMenuBlock()),
      ("navbar", NavbarBlock()),
    ],
    min_num=1,
    max_num=1,
    null=True,
    use_json_field=True
  )

  panels = [
    FieldPanel("title"),
    FieldPanel("slug"),
    FieldPanel("variant"),
  ]

  def __str__(self) -> str:
    return f"[menu] {self.title}"