
from django.db import models

from django_extensions.db.fields import AutoSlugField

from taggit.models import TagBase

from wagtail.search.index import Indexed, SearchField
from wagtail.snippets.models import register_snippet

@register_snippet
class UsefulLinkCategory(Indexed, TagBase):
  free_tagging = False
  name = models.CharField(max_length=60, unique=True)
  slug = AutoSlugField(populate_from="name", editable=True)
  description = models.CharField(max_length=500, blank=True)

  search_fields = [
    SearchField("name", partial_match=True)
  ]

  class Meta:
    verbose_name = "Useful Link Category"
    verbose_name_plural = "Useful Link Categories"
  