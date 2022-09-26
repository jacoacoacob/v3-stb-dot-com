from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import UsefulLink

@modeladmin_register
class UsefulLinkAdmin(ModelAdmin):
  model = UsefulLink
  menu_label = "Link Library"
  menu_icon = "link"
  menu_order = 200
  add_to_settings_menu = False
  exclude_from_explorer = False
  list_display = ("link_text", "is_live", "ts_created", "ts_updated")
  list_filter = ("is_live", "categories", "tags", "ts_created", "ts_updated")
  search_fields = ("link_url", "link_text", "description")