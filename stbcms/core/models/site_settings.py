from django.db import models

from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

@register_setting
class SiteSettings(BaseSiteSetting):
  facebook = models.URLField(blank=True, null=True)
  twitter = models.URLField(blank=True, null=True)
  email = models.EmailField(blank=True, null=True)
  brand_name = models.CharField(max_length=100)

  panels = [
    MultiFieldPanel(
      [
        FieldPanel("brand_name")
      ],
    ),
    MultiFieldPanel(
      [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
      ],
      heading="Social Media"
    ),
    MultiFieldPanel(
      [
        FieldPanel("email"),
      ],
      heading="Contact",
    ),
  ]


