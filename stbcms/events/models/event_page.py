
from wagtail.models import Page

class EventPage(Page):
  parent_page_types = ["events.EventListingPage"]
  subpage_types = []
