from wagtail.blocks import StructBlock, URLBlock, PageChooserBlock, ChoiceBlock, CharBlock

class LinkBlock(StructBlock):
  kind = ChoiceBlock(
    default="url",
    choices=[
      ("page", "Page"),
      ("url", "URL"),
    ]
  )
  text = CharBlock(max_length=240)
  page = PageChooserBlock(required=False)
  url = URLBlock(required=False)
