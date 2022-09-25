import re
from datetime import datetime, date

from django.utils import timezone


class DateTimeSegments:
  def __init__(self, dt: datetime, time_override: str | None) -> None:
    # dt_str = timezone.localtime(dt).strftime("%A__%B %d__%Y__%I:%M__%p__%Z")
    ### Use the abbreviated datetime format to allow for display in one line
    ### in event_page and event_listing_page template
    dt_str = timezone.localtime(dt).strftime("%a__%b %d__%Y__%I:%M__%p__%Z")
    day_of_week, month_and_date, year, hours_minutes, am_pm, tz_name = [
      x.strip() for x in dt_str.split("__")
    ]
    self.time_override = time_override
    self.day_of_week = day_of_week
    self.month_and_date = re.sub(
      r"0\d$",
      lambda m: m.group()[1:],
      month_and_date
    )
    self.year = year
    self.hours_minutes = re.sub(r"^0\d", lambda m: m.group()[1:], hours_minutes)
    self.am_pm = am_pm
    self.tz_name = tz_name

  def get_time_of_day(self):
    """
    Returns string containing `hours_minutes`, `am` or `pm`, and `time_zone_name`
    OR the truthy value of `self.time_override`
    """
    if self.time_override:
      return self.time_override
    return f"{self.hours_minutes}{self.am_pm} {self.tz_name}"
  
  def get_date(self):
    """
    Returns string containing `day_of_week`
    """
    return f"{self.day_of_week}, {self.month_and_date}, {self.year}"

  def __str__(self) -> str:
    return f"{self.get_date()} @ {self.get_time_of_day()}"
  

def merge_sameday_time(start: DateTimeSegments, end: DateTimeSegments):
  """
  Returns string containing merged `start` and `end` `DateTimeSegments` 
  instances and returns string which includes: `hours_minutes`, `am` or 
  `pm`, and `time_zone_name`
  """
  if start.hours_minutes == end.hours_minutes and start.am_pm == end.am_pm:
    return f"{start.hours_minutes}{start.am_pm} {start.tz_name}"
  return f"{start.hours_minutes}{start.am_pm}-{end.hours_minutes}{end.am_pm} {start.tz_name}"


def message_parts(
  start_date_time: datetime | None,
  start_date_time_override: str | None,
  start_time_override: str | None,
  end_date_time: datetime | None,
  end_date_time_override: str | None,
  end_time_override: str | None,
):
  if start_date_time and end_date_time:
    start = DateTimeSegments(start_date_time, start_time_override)
    end = DateTimeSegments(end_date_time, end_time_override)
    if start.year == end.year:
      if start.month_and_date == end.month_and_date:
        return f"{start.get_date()} @ {merge_sameday_time(start, end)}"
    return {
      'start': str(start),
      'end': str(end),
    }
  elif start_date_time:
    return {
      'start': str(DateTimeSegments(start_date_time, start_time_override)),
      'end': end_date_time_override,
    }
  elif end_date_time:
    return {
      'start': start_date_time_override,
      'end': str(DateTimeSegments(end_date_time, end_time_override)),
    }
  elif start_date_time_override or end_date_time_override:
    return {
      'start': start_date_time_override,
      'end': end_date_time_override
    }


def complex_date_time_range_message(
  start_date_time: datetime | None,
  start_date_time_override: str | None,
  start_time_override: str | None,
  end_date_time: datetime | None,
  end_date_time_override: str | None,
  end_time_override: str | None,
):
  parts = message_parts(
    start_date_time,
    start_date_time_override,
    start_time_override,
    end_date_time,
    end_date_time_override,
    end_time_override,
  )
  if type(parts) == dict:
    start = parts.get("start")
    end = parts.get("end")
    if start and end:
      return f"{start} - {end}"
    return start or end
  elif type(parts) == str:
    return parts
  return "TBD"
