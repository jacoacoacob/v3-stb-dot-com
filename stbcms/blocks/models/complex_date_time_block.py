from wagtail.blocks import StreamBlock, StructBlock, DateTimeBlock, CharBlock

class ComplexDateTimeBlock(StructBlock):
  date_time = DateTimeBlock(required=False, blank=True, null=True, label="Date/Time")
  date_time_override = CharBlock(required=False, max_length=140, label="Date/Time Override")
  time_override = CharBlock(required=False, max_length=140, label="Time Override")


