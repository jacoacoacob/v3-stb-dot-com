from wagtail.hooks import register
from wagtail.rich_text import LinkHandler

class NoOpenerExternalLinkHandler(LinkHandler):
  identifier = "external"

  @classmethod
  def expand_db_attributes(cls, attrs):
    return f'<a href={attrs.get("href")} target="_blank" rel="noopener noreferrer">'


@register("register_rich_text_features")
def register_external_link(features):
  features.register_link_type(NoOpenerExternalLinkHandler)
