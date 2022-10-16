from wagtail.models import Page

from .useful_link_page import UsefulLinkPage


class UsefulLinkListingPage(Page):
  parent_page_types = ["home.HomePage"]
  subpage_types = ["useful_links.UsefulLinkPage"]

  def get_context(self, request, *args, **kwargs):
    context = super().get_context(request, *args, **kwargs)
    context["links"] = UsefulLinkPage.objects.child_of(self).live()
    return context
