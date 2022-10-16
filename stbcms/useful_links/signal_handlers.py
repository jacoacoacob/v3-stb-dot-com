from django.db.models.signals import pre_delete

from wagtail.signals import page_published, page_unpublished
from wagtail.contrib.frontend_cache.utils import PurgeBatch

from .models import UsefulLinkPage, UsefulLinkListingPage

def purge_event_listing_page_cache(event_page: UsefulLinkPage):
  batch = PurgeBatch()
  for event_listing_page in UsefulLinkListingPage.objects.live():
    if event_page in event_listing_page.get_events():
      batch.add_page(event_listing_page)
  print("Purging UsefulLinkListingPage URLs:", batch.urls)
  batch.purge()


def handler(instance: UsefulLinkPage, **kwargs):
  purge_event_listing_page_cache(instance)


def register_signal_handlers():
  page_published.connect(handler, sender=UsefulLinkPage)
  page_unpublished.connect(handler, sender=UsefulLinkPage)
  pre_delete.connect(handler, sender=UsefulLinkPage)
  