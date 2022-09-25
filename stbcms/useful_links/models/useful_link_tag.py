from django.db import models

from modelcluster.fields import ParentalKey

from taggit.models import TaggedItemBase

class UsefulLinkTag(TaggedItemBase):
  content_object = ParentalKey(
    "useful_links.UsefulLink",
    on_delete=models.CASCADE,
    related_name="tagged_items"
  )
