from atexit import register
import imp
from django import template

register = template.Library()

@register.inclusion_tag("icons.html")
def theme_icon(icon_name, **kwargs):
  return {
    "icon_name": icon_name,
    "class": kwargs.get("class"),
  }