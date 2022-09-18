from django.db import models

from wagtail.models import Page

# Create your models here.
class UsefulLinksPage(Page):
  parent_page_types = ["home.HomePage"]
  subpage_types = []