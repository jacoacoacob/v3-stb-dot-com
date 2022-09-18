from wagtail import hooks

from .hooks import rich_text_features, global_admin_css

hooks.register("register_rich_text_features", rich_text_features)
hooks.register("insert_global_admin_css", global_admin_css, order=100)