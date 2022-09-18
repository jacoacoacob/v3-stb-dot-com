from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.models import Page
from wagtail.fields import StreamField

from blocks.models import HeroBlock


class HomePage(Page):
    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("article", RichTextBlock(features=["h2", "h3", "h4", "bold", "italic", "ol", "ul", "link"]))
        ],
        blank=True,
        use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]

    parent_page_types = []
    subpage_types = [
        "blog.BlogPostListingPage",
        "events.EventListingPage",
        "useful_links.UsefulLinksPage",
    ]