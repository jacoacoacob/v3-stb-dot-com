from django.db.models.signals import pre_delete

from wagtail.signals import page_published, page_unpublished
from wagtail.contrib.frontend_cache.utils import PurgeBatch

from .models import UsefulLinkPage, UsefulLinkListingPage

def purge_useful_link_listing_page_cache(page: UsefulLinkPage):
  batch = PurgeBatch()
  for listing_page in UsefulLinkListingPage.objects.live():
    page_itmes = listing_page.get_useful_links()
    if page in page_itmes:
      batch.add_page(listing_page)
  print("Purging UsefulLinkListingPage URLs:", batch.urls)
  batch.purge()


def handler(instance: UsefulLinkPage, **kwargs):
  purge_useful_link_listing_page_cache(instance)


def register_signal_handlers():
  page_published.connect(handler, sender=UsefulLinkPage)
  page_unpublished.connect(handler, sender=UsefulLinkPage)
  pre_delete.connect(handler, sender=UsefulLinkPage)
  