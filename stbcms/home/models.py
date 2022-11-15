from django.db import models
from django.forms import ValidationError

from wagtailseo.models import SeoMixin

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.blocks import RichTextBlock, PageChooserBlock, StructBlock, ListBlock
from wagtail.models import Page
from wagtail.fields import StreamField

from blocks.models import HeroBlock


class PublishedPageChooserBlock(PageChooserBlock):
    def clean(self, value):
        page = super().clean(value)
        if page and not page.live:
            raise ValidationError("You may only choose published pages.")
        return page
        

class FeaturedPagesBlock(StructBlock):
    blog_post_page = PublishedPageChooserBlock(
        required=False,
        page_type="blog.BlogPostPage",
        label="Featured Blog Post"
    )
    event_page = PublishedPageChooserBlock(
        required=False,
        page_type="events.EventPage",
        label="Featured Event",
    )
    useful_link_pages = ListBlock(
        PublishedPageChooserBlock(
            required=True,
            page_type="useful_links.UsefulLinkPage",
        ),
        label="Featured Useful Link",
        collapsed=True,
    )
    

class HomePage(SeoMixin, Page):
    # Database fields
    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("article", RichTextBlock(features=["h2", "h3", "h4", "bold", "italic", "ol", "ul", "link"])),
            ("featured_pages", FeaturedPagesBlock())
        ],
        block_counts={
            "hero": { "min_num": 1, "max_num": 1 },
            "article": { "max_num": 1 },
            "featured_pages": { "max_num": 1 },
        },
        blank=True,
        use_json_field=True
    )
    disable_scroll_prompt = models.BooleanField(
        default=False,
        help_text="Check this box to hide the bouncing arrow that appears below the hero section."
    )

    # Editor panels config
    content_panels = Page.content_panels + [
        FieldPanel("body"),
        MultiFieldPanel(
            [
                FieldPanel("disable_scroll_prompt"),
            ],
            heading="Feature Flags"
        )
    ]

    promote_panels = SeoMixin.seo_meta_panels

    # Parent page / subpage type rules
    parent_page_types = []
    subpage_types = [
        "blog.BlogPostListingPage",
        "events.EventListingPage",
        "useful_links.UsefulLinkListingPage",
    ]
