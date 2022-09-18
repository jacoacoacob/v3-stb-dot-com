from django.templatetags.static import static
from django.utils.html import format_html

def global_admin_css():
  """Load /static/css/custom_admin.css on admin pages"""
  return format_html(
    '<link rel="stylesheet" href="{}">',
    static("css/custom_admin.css")
  )