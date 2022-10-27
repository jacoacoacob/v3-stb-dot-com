from wagtail.models import Page

from .useful_link_page import UsefulLinkPage
from .useful_link_category import UsefulLinkCategories, UsefulLinkCategory

class UsefulLinkListingPage(Page):
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
