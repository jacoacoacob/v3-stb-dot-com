# Generated by Django 4.1.1 on 2022-10-27 20:07

from django.db import migrations
import home.models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('cta', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=140)), ('text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link'])), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('_text', wagtail.blocks.CharBlock(label='Text', max_length=240, required=False)), ('_kind', wagtail.blocks.ChoiceBlock(choices=[('URL', 'URL'), ('PAGE', 'Page')], help_text='If you want to link to a page on some other website (e.g. twitter.com) chose "URL". If you want to link to a page on this site, choose "Page"', label='Kind')), ('_page', wagtail.blocks.PageChooserBlock(label='Page', required=False)), ('_url', wagtail.blocks.URLBlock(label='URL', required=False))]), max_num=1, min_num=0))], label='Call To Action'))])), ('article', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link'])), ('featured_pages', wagtail.blocks.StructBlock([('blog_post_page', home.models.PublishedPageChooserBlock(label='Featured Blog Post', page_type=['blog.BlogPostPage'], required=False)), ('event_page', home.models.PublishedPageChooserBlock(label='Featured Event', page_type=['events.EventPage'], required=False)), ('useful_link_pages', wagtail.blocks.ListBlock(home.models.PublishedPageChooserBlock(page_type=['useful_links.UsefulLinkPage'], required=True), collapsed=True, label='Featured Useful Link'))]))], blank=True, use_json_field=True),
        ),
    ]
