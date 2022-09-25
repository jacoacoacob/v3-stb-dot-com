from wagtail.models import Page

from .useful_link import UsefulLink
from .useful_link_category import UsefulLinkCategory
from .useful_link_tag import UsefulLinkTag


class UsefulLinksPage(Page):
  parent_page_types = ["home.HomePage"]
  subpage_types = []

  def get_context(self, request, *args, **kwargs):
    context = super().get_context(request, *args, **kwargs)
    context["links"] = UsefulLink.objects.filter(is_live__exact=True)
    return context