
import uuid

from django.db import models

from wagtail.fields import RichTextField, StreamField
from wagtail.blocks import ListBlock
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from blocks.models import ComplexDateTimeRangeBlock


class EventPage(Page):
  uid_slug = models.UUIDField(default=uuid.uuid4)
  listing_description = models.TextField(
    max_length=2000,
    help_text="A description of the event that will appear on the event listing page."
  )
  detail_description = RichTextField(
    features=["ol", "ul", "bold", "italic", "link"],
    help_text="The description that will appear on the event detail page"
  )
  when = StreamField(
    [
      ("current", ComplexDateTimeRangeBlock(label="Currently scheduled for...")),
      (
        "previous",
        ListBlock(
          ComplexDateTimeRangeBlock(
            label="Previously scheduled date/time"
          ),
          label="Previously scheduled for..."
        )
      )
    ],
    blank=True,
    block_counts={ "current": { "min_num": 1, "max_num": 1 } },
    use_json_field=True,
  )
  location_description = models.CharField(max_length=100, default="TBD")
  location_link = models.URLField(
    blank=True,
    help_text="If provided, this link will be embedded in the location description text"
  )
  list_as_upcoming = models.BooleanField(blank=True, default=False)
  include_contact_link = models.BooleanField(default=True)
  ts_created = models.DateTimeField(
    auto_created=True,
    auto_now_add=True,
  )
  ts_updated = models.DateTimeField(
    auto_created=True,
    auto_now=True,
  )

  content_panels = Page.content_panels + [
    FieldPanel("listing_description"),
    FieldPanel("detail_description"),
    FieldPanel("list_as_upcoming"),
    FieldPanel("when"),
    FieldPanel("location_description"),
    FieldPanel("location_link"),
    # FieldPanel("include_contact_link"),
  ]

  parent_page_types = ["events.EventListingPage"]
  subpage_types = []

  @property
  def countdown_status(self):
    return self.when.first_block_by_name("current").value.countdown_status(self.list_as_upcoming)

  @property
  def countdown_status_message(self):
    return self.when.first_block_by_name("current").value.countdown_status_message(self.list_as_upcoming)

  @property
  def when_message(self):
    return self.when.first_block_by_name("current").value.message()

  def clean(self):
    self.slug = str(self.uid_slug)
    return super().clean()
