from django import template

from home.models import HomePage
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
    home_page: HomePage = HomePage.objects.first()
    return {
      "pages": [home_page, *home_page.get_children().live().in_menu()]
    }
  except HomePage.DoesNotExist:
    return {
      "pages": HomePage.objects.none()
    }