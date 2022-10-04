from django.db.models.signals import pre_delete

from wagtail.signals import page_published, page_unpublished
from wagtail.contrib.frontend_cache.utils import PurgeBatch

from .models import BlogPostPage, BlogPostListingPage


def purge_blog_post_listing_page_cache(blog_post_page: BlogPostPage):
  batch = PurgeBatch()
  for blog_post_listing_page in BlogPostListingPage.objects.live():
    if blog_post_page in blog_post_listing_page.get_blog_posts():
      batch.add_page(blog_post_listing_page)
  print("Purging BlogPostListingPage URLS:", batch.urls)
  batch.purge()


def blog_post_page_unpublished(instance: BlogPostPage, **kwargs):
  purge_blog_post_listing_page_cache(instance)


def blog_post_page_published(instance: BlogPostPage, **kwargs):
  purge_blog_post_listing_page_cache(instance)


def blog_post_page_deleted(instance: BlogPostPage, **kwargs):
  purge_blog_post_listing_page_cache(instance)


def register_signal_handlers():
  page_published.connect(blog_post_page_published, sender=BlogPostPage)
  page_unpublished.connect(blog_post_page_unpublished, sender=BlogPostPage)
  pre_delete.connect(blog_post_page_deleted, sender=BlogPostPage)
  