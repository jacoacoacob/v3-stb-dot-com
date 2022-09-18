from typing import List, Literal
from django import template

register = template.Library()

class Icon:
  _name = ""
  _fill = "currentColor"
  _stroke = "none"
  _viewBox = "0 0 24 24"
  _classname = "h-6 w-6"
  _title = None
  _description = None
  _paths = []

  def __init__(self, name: str, **kwargs) -> None:
    self._name = name
    # self.

  def fill(self, fill: Literal["none", "currentColor"] | None):
    if fill:
      self.fill = fill
    return self

  def stroke(self, stroke: Literal["none", "currentColor"] | None):
    if stroke:
      self.stroke = stroke
    return self

  def viewbox(self, viewbox: str | None):
    if viewbox:
      self.viewbox = viewbox
    return self

  def classname(self, classname: str | None):
    if classname:
      self.classname = classname
    return self

  def title(self, title: str | None):
    if title:
      self.title = title
    return self

  def description(self, description: str | None):
    if description:
      self.description = description
    return self
  
  def paths(self, paths: List[str] | None):
    if paths:
      self.paths = paths
    return self
  

# ICON_CONFIG = {
#   "external-link": {
#     "paths": [
#       "M13.5 6H5.25A2.25 2.25 0 003 8.25v10.5A2.25 2.25 0 005.25 21h10.5A2.25 2.25 0 0018 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"
#     ],

#   }
# }


# @register.inclusion_tag("template_tags/icon.html")
# def icon(name, **kwargs):
