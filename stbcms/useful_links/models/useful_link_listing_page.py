from email.policy import default
from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.models import Page

from .useful_link_page import UsefulLinkPage
from .useful_link_category import UsefulLinkCategories, UsefulLinkCategory

class UsefulLinkListingPage(Page):
  header_text = models.TextField(max_length=500)
  disable_tags = models.BooleanField(
    default=False,
    help_text="Check this box to hide UI elements that show useful link Categories or Topics"
  )

  content_panels = Page.content_panels + [
    FieldPanel("header_text"),
    MultiFieldPanel(
      [
        FieldPanel("disable_tags"),
      ],
      heading="Feature Flags"
    )
  ]
  

  parent_page_types = ["home.HomePage"]
  subpage_types = ["useful_links.UsefulLinkPage"]

  def get_useful_links(self):
    return UsefulLinkPage.objects.child_of(self).live()

  def get_categories(self, links):
    categories = []
    for link in links:
      categories += [category for category in link.categories.all() if category not in categories]
    return categories

  def get_topics(self, links):
    topics = []
    for link in links:
      topics += [topic for topic in link.topics.all() if topic not in topics]
    return topics

  def get_context(self, request, *args, **kwargs):
    context = super().get_context(request, *args, **kwargs)
    context["links"] = self.get_useful_links()
    context["categories"] = self.get_categories(context["links"])
    context["topics"] = self.get_topics(context["links"])
    return context
