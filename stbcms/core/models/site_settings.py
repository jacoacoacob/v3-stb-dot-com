from django.db import models

from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

@register_setting
class SiteSettings(BaseSiteSetting):
  facebook_group_name = models.CharField(max_length=100, blank=True, null=True)
  twitter_handle = models.CharField(max_length=100, blank=True, null=True)
  email = models.EmailField(blank=True, null=True)
  brand_name = models.CharField(max_length=100)

  @property
  def facebook_url(self):
    if self.facebook_group_name:
      return f"https://facebook.com/{self.facebook_group_name}"

  @property
  def twitter_url(self):
    if self.twitter_handle:
      return f"https://twitter.com/{self.twitter_handle}"

  panels = [
    MultiFieldPanel(
      [
        FieldPanel("brand_name")
      ],
    ),
    MultiFieldPanel(
      [
        FieldPanel("facebook_group_name"),
        FieldPanel("twitter_handle"),
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


