from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import UsefulLinkPage, UsefulLinkCategory


class UsefulLinkCategoryAdmin(ModelAdmin):
  model = UsefulLinkCategory
  menu_label = "Categories"
  menu_icon = "tag"
  list_display = ("name",)
  list_filter = ("name",)
  search_fields = ("name", "description")
  

class UsefulLinkPageAdmin(ModelAdmin):
  model = UsefulLinkPage
  menu_label = "Useful Links"
  menu_icon = "link"
  list_display = ("title", "ts_created", "ts_updated")
  list_filter = ("categories", "tags", "ts_created", "ts_updated")
  search_fields = ("link_url", "title", "description")


@modeladmin_register
class LinkLibrary(ModelAdminGroup):
  menu_label = "Link Library"
  menu_icon = "folder-open-inverse"
  menu_order = 200
  items = (UsefulLinkPageAdmin, UsefulLinkCategoryAdmin)
