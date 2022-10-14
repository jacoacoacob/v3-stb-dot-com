from django.db import models
from django.http import Http404

from modelcluster.contrib.taggit import ClusterTaggableManager

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class UsefulLinkPage(Page):
  categories = ClusterTaggableManager(
    through="useful_links.UsefulLinkCategories",
    blank=True
  )
  tags = ClusterTaggableManager(
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

  parent_page_types = ["useful_links.UsefulLinkListingPage"]
  subpage_types = []

  content_panels = Page.content_panels + [
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

  def get_sitemap_urls(self, request=None):
    return []
  
  def serve(self, request, *args, **kwargs):
    return Http404

  