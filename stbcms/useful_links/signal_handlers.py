from django.db.models.signals import pre_delete

from wagtail.signals import page_published, page_unpublished
from wagtail.contrib.frontend_cache.utils import PurgeBatch

from .models import UsefulLinkPage, UsefulLinkListingPage, UsefulLinkCategory, UsefulLinkTopic

def purge_useful_link_listing_page_cache(page: UsefulLinkPage):
  batch = PurgeBatch()
  for listing_page in UsefulLinkListingPage.objects.live():
    page_itmes = listing_page.get_useful_links()
    if page in page_itmes:
      base_url = listing_page.full_url
      batch.add_url(base_url)
      batch.add_urls([
        base_url + listing_page.reverse_subpage("category_useful_links", args=(category.slug,))
        for category
        in UsefulLinkCategory.objects.all()
      ])
      batch.add_urls([
        base_url + listing_page.reverse_subpage("topic_useful_links", args=(topic.slug,))
        for topic
        in UsefulLinkTopic.objects.all()
      ])
  print("Purging UsefulLinkListingPage URLs:", batch.urls)
  batch.purge()


def handler(instance: UsefulLinkPage, **kwargs):
  purge_useful_link_listing_page_cache(instance)


def register_signal_handlers():
  page_published.connect(handler, sender=UsefulLinkPage)
  page_unpublished.connect(handler, sender=UsefulLinkPage)
  pre_delete.connect(handler, sender=UsefulLinkPage)
  