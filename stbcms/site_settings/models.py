from operator import mod
from django.db import models

from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSiteSetting):
  facebook = models.URLField(blank=True, null=True)
  twitter = models.URLField(blank=True, null=True)
  email = models.EmailField(blank=True, null=True)

  panels = [
    MultiFieldPanel(
      [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("email"),
      ],
      heading="Social Media Settings"
    )
  ]