import json

from django.db.models.signals import pre_delete, pre_save

from wagtail.signals import page_published, page_unpublished
from wagtail.contrib.frontend_cache.utils import PurgeBatch
from wagtail.contrib.routable_page.models import RoutablePageMixin

from .models import UsefulLinkPage, UsefulLinkListingPage, UsefulLinkCategory, UsefulLinkTopic

def get_subpage_url(page: RoutablePageMixin, view_name: str, *args):
  page_url = page.full_url
  return page_url + page.reverse_subpage(view_name, args=args)


def purge_useful_links_cache(**kwargs):
  batch = PurgeBatch()
  for listing_page in UsefulLinkListingPage.objects.live():
    batch.add_page(listing_page)
    batch.add_urls([
      get_subpage_url(listing_page, "category_useful_links", category.slug)
      for category
      in UsefulLinkCategory.objects.all()
    ])
    batch.add_urls([
      get_subpage_url(listing_page, "topic_useful_links", topic.slug)
      for topic
      in UsefulLinkTopic.objects.all()
    ])
  print("Purging UsefulLink URLs:", json.dumps(batch.urls, indent=2))
  batch.purge()


def register_signal_handlers():
  for signal in page_published, page_unpublished:
    signal.connect(purge_useful_links_cache, sender=UsefulLinkPage)

  for signal in pre_delete, pre_save:
    signal.connect(purge_useful_links_cache, sender=UsefulLinkCategory)
    signal.connect(purge_useful_links_cache, sender=UsefulLinkTopic)
