from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import HelpPanel

# Create your models here.
class UsefulLinksPage(Page):
  parent_page_types = ["home.HomePage"]
  subpage_types = []
