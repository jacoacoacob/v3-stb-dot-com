from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.models import Page

from .useful_link_page import UsefulLinkPage
from .useful_link_category import UsefulLinkCategories, UsefulLinkCategory

class UsefulLinkListingPage(RoutablePageMixin, Page):
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

  def get_useful_links(self, category_slug=None, topic_slug=None):
    # if category_slug:
    #   return UsefulLinkPage.objects.child_of(self).live().filter(categories__slug=category_slug)
    # if topic_slug:
    #   return UsefulLinkPage.objects.child_of(self).live().filter(topics__slug=topic_slug)
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

  @path("")
  def useful_links(self, request):
    links = self.get_useful_links()
    categories = self.get_categories(links)
    topics = self.get_topics(links)
    return self.render(
      request,
      context_overrides={
        "links": links,
        "categories": categories,
        "topics": topics,
      }
    )

  @path("category/<category_slug>/")
  def category_useful_links(self, request, category_slug):
    """View function for useful links page displaying links of a given category"""
    links = self.get_useful_links()
    categories = self.get_categories(links)
    topics = self.get_topics(links)
    return self.render(
      request,
      context_overrides={
        "links": links,
        "categories": categories,
        "topics": topics,
      }
    )

  
  @path("topic/<topic_slug>/")
  def topic_useful_links(self, request, topic_slug):
    """View function for useful links page displaying links of a given topic"""
    all_links = self.get_useful_links()
    topic_links = all_links.filter(topics__slug=topic_slug)
    categories = self.get_categories(all_links)
    topics = self.get_topics(topic_links)
    return self.render(
      request,
      context_overrides={
        "links": topic_links,
        "categories": categories,
        "topics": topics,
      }
    )
  