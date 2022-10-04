from django.db.models.signals import pre_delete

from wagtail.signals import page_published, page_unpublished
from wagtail.contrib.frontend_cache.utils import PurgeBatch

from .models import EventPage, EventListingPage

def purge_event_listing_page_cache(event_page: EventPage):
  batch = PurgeBatch()
  for event_listing_page in EventListingPage.objects.live():
    if event_page in event_listing_page.get_events():
      batch.add_page(event_listing_page)
  print("Purging EventListingPage URLs:", batch.urls)
  batch.purge()


def handler(instance: EventPage, **kwargs):
  purge_event_listing_page_cache(instance)


def register_signal_handlers():
  page_published.connect(handler, sender=EventPage)
  page_unpublished.connect(handler, sender=EventPage)
  pre_delete.connect(handler, sender=EventPage)
  