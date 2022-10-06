from django.forms.utils import ErrorList

from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock, PageChooserBlock, StructBlock
from wagtail.blocks.struct_block import StructBlockValidationError
from wagtail.models import Page
from wagtail.fields import StreamField

from blocks.models import HeroBlock


class FeaturedPagesBlock(StructBlock):
    blog_post_page = PageChooserBlock(required=False, page_type="blog.BlogPostPage")
    event_page = PageChooserBlock(required=False, page_type="events.EventPage")
    
    def clean(self, value):
        errors = {}
        blog_post_page = value.get("blog_post_page")
        event_page = value.get("event_page")

        if blog_post_page and not blog_post_page.live:
            errors["blog_post_page"] = ErrorList(["You may only choose published pages."])

        if event_page and not event_page.live:
            errors["event_page"] = ErrorList(["You may only choose published pages."])

        if any(errors):
            raise StructBlockValidationError(errors)

        return super().clean(value)


class HomePage(Page):
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
        collapsed=True,
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
