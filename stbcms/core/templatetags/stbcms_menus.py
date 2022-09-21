import re

from django.core.handlers.wsgi import WSGIRequest
from django.template import Library
from django.template.context import RequestContext

from wagtail.models import Page

from home.models import HomePage

register = Library()

def get_request(context: RequestContext) -> WSGIRequest | None:
  return context.get("request")

def get_main_site_pages():
  try:
    home_page: HomePage = HomePage.objects.first()
    return [home_page, *home_page.get_children().live().in_menu()]
  except HomePage.DoesNotExist:
    return HomePage.objects.none()

def is_page_active(context: RequestContext, page: Page):
  req_path = get_request(context).path
  page_url = page.url
  if page_url == "/":
    return req_path == page_url
  return req_path.startswith(page_url)

@register.inclusion_tag("template_tags/footer.html")
def footer():
  return {
    "pages": get_main_site_pages()
  }

@register.inclusion_tag("template_tags/navbar.html", takes_context=True)
def navbar(context: RequestContext):
  current_page: Page = context.get("self")
  if not current_page or current_page.depth <= 2:
    breadcrumbs = []
  elif current_page:
    breadcrumbs = Page.objects.ancestor_of(current_page, inclusive=True)
  breadcrumbs = breadcrumbs[1:]
  return {
    "pages": [(is_page_active(context, page), page) for page in get_main_site_pages()],
    "breadcrumbs": breadcrumbs,
    "is_breadcrumbs": len(breadcrumbs) > 0,
  }

