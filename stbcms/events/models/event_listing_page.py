from wagtail.models import Page

from .event_page import EventPage

class EventListingPage(Page):
  parent_page_types = ["home.HomePage"]
  subpage_types = ["events.EventPage"]
  
  def get_events(self):
    return EventPage.objects.child_of(self).live()

  def get_context(self, request, *args, **kwargs):
    context = super().get_context(request, *args, **kwargs)
    events = self.get_events()
    context["upcoming_events"] = [event for event in events if event.countdown_status != "is_over"]
    context["has_upcoming_events"] = len(context["upcoming_events"]) > 0
    context["past_events"] = [event for event in events if event.countdown_status == "is_over"]
    return context