from django import template

register = template.Library()

@register.inclusion_tag("icons.html")
def icon(icon_name, **kwargs):
  return {
    "icon_name": icon_name,
    "class": kwargs.get("class"),
    "title": kwargs.get("title"),
    "description": kwargs.get("description"),
  }