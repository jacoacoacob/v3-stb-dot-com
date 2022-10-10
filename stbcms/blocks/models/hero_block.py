from wagtail.blocks import ListBlock, StructBlock, RichTextBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock

from blocks.models.link_block import LinkBlock

class HeroBlock(StructBlock):
  image = ImageChooserBlock(required=False)
  cta = StructBlock(
    [
      ("heading", CharBlock(max_length=140)),
      ("text", RichTextBlock(features=["h2", "h3", "h4", "bold", "italic", "ol", "ul", "link"])),
      ("links", ListBlock(LinkBlock(), min_num=0, max_num=1))
    ],
    label="Call To Action"
  )

  class Meta:
    template = "hero_block.html"