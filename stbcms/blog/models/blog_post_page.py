import uuid

from django.db import models

from wagtailseo.models import SeoMixin, SeoType, TwitterCard

from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock, StructBlock, TextBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page

BODY_TEXT_FEATURES = [
  "h2",
  "h3",
  "h4",
  "bold",
  "italic",
  "ol",
  "ul",
  "link"
]

class BlogPostPage(SeoMixin, Page):
  # Database fields
  uid_slug = models.UUIDField(default=uuid.uuid4)
  teaser = RichTextField(max_length=240, features=[])
  body = StreamField(
    [
      ("text", RichTextBlock(features=BODY_TEXT_FEATURES)),
      (
        "photo",
        StructBlock(
          [
            ("image",  ImageChooserBlock()),
            ("caption", TextBlock(max_length=300, required=False))
          ]
        )
      )
    ],
    use_json_field=True
  )
  ts_created = models.DateTimeField(
    auto_created=True,
    auto_now_add=True,
  )
  ts_updated = models.DateTimeField(
    auto_created=True,
    auto_now=True,
  )

  # Editor panels config
  content_panels = Page.content_panels + [
    FieldPanel("teaser"),
    FieldPanel("body")
  ]

  promote_panels = SeoMixin.seo_meta_panels + SeoMixin.seo_menu_panels

  # Parent page / subpage type rules
  parent_page_types = ["blog.BlogPostListingPage"]
  subpage_types = []

  # SEO config
  seo_content_type = SeoType.ARTICLE
  seo_twitter_card = TwitterCard.SUMMARY

  def clean(self):
    self.slug = str(self.uid_slug)
    return super().clean()
    