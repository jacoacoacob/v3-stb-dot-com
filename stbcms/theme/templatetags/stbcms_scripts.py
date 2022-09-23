from django import template

register = template.Library()

@register.inclusion_tag("stbcms_scripts.html")
def stbcms_scripts():
  return {}