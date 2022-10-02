from tabnanny import verbose
from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from taggit.models import TaggedItemBase, TagBase, ItemBase
from taggit.managers import TaggableManager

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.search.index import Indexed, SearchField
from wagtail.snippets.models import register_snippet

@register_snippet
class UsefulLink(Indexed, ClusterableModel):
  categories = TaggableManager(
    through="useful_links.UsefulLinkCategories",
    blank=True
  )
  tags = TaggableManager(
    through="useful_links.UsefulLinkTag",
    blank=True
  )
  link_url = models.URLField(unique=True)
  link_text = models.CharField(max_length=140)
  description = models.TextField(max_length=2000, blank=True)
  is_live = models.BooleanField(
    default=False,
    help_text="This link will not appear to site visitors unless this box is checked"
  )
  ts_created = models.DateTimeField(
    auto_created=True,
    auto_now_add=True,
    verbose_name="Date Created"
  )
  ts_updated = models.DateTimeField(
    auto_created=True,
    auto_now=True,
    verbose_name="Date Updated"
  )

  search_fields = [
    SearchField("link_text", partial_match=True),
    SearchField("link_url", partial_match=True),
    SearchField("description", partial_match=True)
  ]

  panels = [
    MultiFieldPanel(
      [
        FieldPanel("link_url"),
        FieldPanel("link_text"), 
        FieldPanel("description"),
      ],
      heading="Details",
      classname="collapsible"
    ),
    FieldPanel("is_live"),
    MultiFieldPanel(
      [
        FieldPanel("categories", heading="Categories (type)"),
        FieldPanel("tags", heading="Tags (subject)"),
      ],
      heading="Categories & Tags",
      classname="collapsible"
    )
  ]

  class Meta:
    verbose_name = "Useful Link"
    verbose_name_plural = "Useful Links"
