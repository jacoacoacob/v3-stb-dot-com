from django.db import models

from wagtail.models import Page


class BlogPostPage(Page):
  parent_page_types = ["blog.BlogPostListingPage"]
  subpage_types = []


class BlogPostListingPage(Page):
  parent_page_types = ["home.HomePage"]
  subpage_types = ["blog.BlogPostPage"]
