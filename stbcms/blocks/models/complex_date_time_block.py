from wagtail.blocks import StreamBlock, StructBlock, DateTimeBlock, CharBlock

class ComplexDateTimeBlock(StructBlock):
  date_time = DateTimeBlock(required=False, blank=True, null=True, label="Date/Time")
  time_override = CharBlock(required=False, max_length=140, label="Time Override")
  # TODO: This field (date_time_override) should be renamed to something like custom_date_time_message
  # because that more closely describes how it relates to the other fields in this block
  date_time_override = CharBlock(
    required=False,
    max_length=140,
    label="Custom Date/Time Message",
    help_text="Leave the 'Date/Time' field blank and enter a custom message here if you want more flexibility in how you describe when an event starts. Use the preview to verify the event will display in the way you expect."
  )


