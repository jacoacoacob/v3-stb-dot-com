import math
from datetime import datetime, timedelta

from django.forms import ValidationError
from django.forms.utils import ErrorList, ErrorDict
from django.utils import timezone

from wagtail.blocks import StructBlock, StructValue
from wagtail.blocks.struct_block import StructBlockValidationError

from ..helpers import complex_date_time_range_message
from .complex_date_time_block import ComplexDateTimeBlock


class ComplexDateTimeRangeBlockValue(StructValue):
  def countdown_status(self, force_upcoming = False):
    if force_upcoming:
      return "upcoming"

    now = timezone.localtime()

    block_start = self.get("start")
    start_date_time: datetime | None = block_start.get("date_time")
    # start_date_time_override: str | None = block_start.get("date_time_override")
    start_time_override: str | None = block_start.get("time_override")
    block_end = self.get("end")
    end_date_time: datetime | None = block_end.get("date_time")
    # end_date_time_override: str | None = block_end.get("date_time_override")
    end_time_override: str | None = block_end.get("time_override")

    def is_happening_now():
      if (
        start_date_time and
        end_date_time and
        # not start_date_time_override and
        not start_time_override and
        # not end_date_time_override and
        not end_time_override
      ):
        return now >= start_date_time and now <= end_date_time
      return False

    def is_happening_today():
      if not is_happening_now() and start_date_time:
        return now.date() == start_date_time.date()
      return False
    
    def is_happening_tomorrow():
      if not is_happening_now() and not is_happening_today() and start_date_time:
        return now.date() == start_date_time.date() - timedelta(days=1)
      return False

    def is_upcoming():
      if (
        not is_happening_now() and 
        not is_happening_today() and
        not is_happening_tomorrow() and
        start_date_time
      ):
        return now.date() < start_date_time.date()
      return False

    # def is_over():
    #   if not is_upcoming() and end_date_time:
    #     if end_time_override:
    #       return now.date() > end_date_time.date()
    #     return now > end_date_time
    #   elif start_date_time:
    #     return now.date() > start_date_time.date() + timedelta(days=1)
    #   return False

    if is_happening_now(): return "happening_now"
    if is_happening_today(): return "happening_today"
    if is_happening_tomorrow(): return "happening_tomorrow"
    if is_upcoming(): return "upcoming"
    # if is_over(): return "is_over"
    return "is_over"

  def countdown_status_message(self, force_upcoming=False):
    status = self.countdown_status(force_upcoming)
    if status in ["happening_tomorrow", "happening_today", "happening_now"]:
      return " ".join(status.split("_"))

  def duration(self):
    pass

  def message(self):
    block_start = self.get("start")
    start_date_time: datetime | None = block_start.get("date_time")
    start_date_time_override: str | None = block_start.get("date_time_override")
    start_time_override: str | None = block_start.get("time_override")
    block_end = self.get("end")
    end_date_time: datetime | None = block_end.get("date_time")
    end_date_time_override: str | None = block_end.get("date_time_override")
    end_time_override: str | None = block_end.get("time_override")
    return complex_date_time_range_message(
      start_date_time,
      start_date_time_override,
      start_time_override,
      end_date_time,
      end_date_time_override,
      end_time_override
    )



class ComplexDateTimeRangeBlock(StructBlock):
  start = ComplexDateTimeBlock()
  end = ComplexDateTimeBlock()

  class Meta:
    value_class = ComplexDateTimeRangeBlockValue

  # def clean(self, value):
  #   errors = ErrorDict({
  #     "start": ErrorDict(),
  #     "end": ErrorDict(),
  #   })

  #   start = value.get("start")
  #   start_date_time = start.get("date_time")
  #   end = value.get("end")
  #   end_date_time = end.get("date_time")

  #   if start_date_time and end_date_time:
  #     if end_date_time <= start_date_time:
  #       errors["end"]["date_time"] = ErrorList(["The end must come after the start"])
  #       # errors["end"] = "The end must come after the start"
  #   elif end_date_time:
  #     errors["start"]["date_time"] = ErrorList(["There can be no end without a start"])
  #     # errors["start"] = "There can be no end without a start"

  #   if errors:
  #     raise StructBlockValidationError(errors)

  #   return super().clean(value)

