from wagtail.rich_text import LinkHandler
from wagtail.rich_text.feature_registry import FeatureRegistry

class NoOpenerExternalLinkHandler(LinkHandler):
  identifier = "external"

  @classmethod
  def expand_db_attributes(cls, attrs):
    return f'<a href={attrs.get("href")} target="_blank" rel="noopener noreferrer">'


def rich_text_features(features: FeatureRegistry):
  """Register with `"register_rich_text_features"`"""
  features.register_link_type(NoOpenerExternalLinkHandler)