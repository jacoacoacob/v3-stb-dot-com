from django import template

from home.models import HomePage
from ..models import Menu

register = template.Library()

def get_main_pages():
  try:
    home_page: HomePage = HomePage.objects.first()
    return [home_page, *home_page.get_children().live().in_menu()]
  except HomePage.DoesNotExist:
    return HomePage.objects.none()
  

def is_page_active(context, page):
  req_path = context["request"].path
  if page.url == "/":
    return req_path == page.url
  return req_path.startswith(page.url)


@register.inclusion_tag("footer.html")
def footer():
  return {
    "pages": get_main_pages()
  }

@register.inclusion_tag("navbar.html", takes_context=True)
def navbar(context):
  return {
    "pages": [(is_page_active(context, page), page) for page in get_main_pages()]
  }
  