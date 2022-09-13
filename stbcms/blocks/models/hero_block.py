from wagtail.blocks import StructBlock, RichTextBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock

from blocks.models.link_block import LinkBlock

class HeroBlock(StructBlock):
  image = ImageChooserBlock()
  cta = StructBlock(
    [
      ("heading", CharBlock(max_length=140)),
      ("text", RichTextBlock(features=["h2", "h3", "h4", "bold", "italic", "ol", "ul", "link"])),
      ("link", LinkBlock(features=["link"]))
    ],
    label_format="Call To Action"
  )

  class Meta:
    template = "hero_block.html"