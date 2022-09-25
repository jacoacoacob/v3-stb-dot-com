from django.db import models

from modelcluster.fields import ParentalKey

from taggit.models import ItemBase

class UsefulLinkCategories(ItemBase):
  tag = models.ForeignKey(
    "useful_links.UsefulLinkCategory",
    related_name="categorized_useful_links",
    on_delete=models.CASCADE
  )
  content_object = ParentalKey(
    to="useful_links.UsefulLink",
    related_name="categorized_items",
    on_delete=models.CASCADE
  )
