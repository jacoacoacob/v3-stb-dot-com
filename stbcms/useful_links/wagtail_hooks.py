from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import UsefulLinkPage

@modeladmin_register
class UsefulLinkAdmin(ModelAdmin):
  model = UsefulLinkPage
  menu_label = "Link Library"
  menu_icon = "link"
  menu_order = 200
  add_to_settings_menu = False
  exclude_from_explorer = False
  list_display = ("link_text", "ts_created", "ts_updated")
  list_filter = ("categories", "tags", "ts_created", "ts_updated")
  search_fields = ("link_url", "link_text", "description")