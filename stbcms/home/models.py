from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField

from blocks.models import HeroBlock


class HomePage(Page):
    body = StreamField(
        [
            ("hero", HeroBlock())
        ],
        blank=True,
        use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]