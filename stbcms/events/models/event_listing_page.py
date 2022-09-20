from wagtail.models import Page

class EventListingPage(Page):
  parent_page_types = ["home.HomePage"]
  subpage_types = ["events.EventPage"]
  