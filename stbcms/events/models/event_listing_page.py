from wagtail.models import Page

from .event_page import EventPage

class EventListingPage(Page):
  parent_page_types = ["home.HomePage"]
  subpage_types = ["events.EventPage"]
  
  def get_context(self, request, *args, **kwargs):
    context = super().get_context(request, *args, **kwargs)
    context["upcoming_events"] = EventPage.objects.child_of(self).live()
    return context