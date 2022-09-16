from django import template

from ..models import Menu

register = template.Library()

@register.inclusion_tag("footer.html")
def footer():
  try:
    return dict(menu=Menu.objects.get(slug="footer"))
  except Menu.DoesNotExist:
    return dict(menu=Menu.objects.none())

@register.inclusion_tag("navbar.html")
def navbar():
  try:
    return dict(menu=Menu.objects.get(slug="navbar"))
  except Menu.DoesNotExist:
    return dict(menu=Menu.objects.none())