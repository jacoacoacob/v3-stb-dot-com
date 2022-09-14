from django.db import models

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail.models import Orderable
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.models import register_snippet

from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


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
  name = models.CharField(max_length=140)
  slug = AutoSlugField(populate_from="name", editable=True)

  panels = [
    FieldPanel("name"),
    InlinePanel("items", heading="Links", label="Link"),
  ]

  def __str__(self) -> str:
    return f"[menu-section] :: {self.name}"


class Menu(ClusterableModel):
  name = models.CharField(max_length=140)
  slug = AutoSlugField(populate_from="name", editable=True)

  sections = StreamField(
    [
      ("section", SnippetChooserBlock("menus.MenuSection"))
    ],
    use_json_field=True
  )

  panels = [
    FieldPanel("name"),
    FieldPanel("slug"),
    FieldPanel("sections"),
  ]