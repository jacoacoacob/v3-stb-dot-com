# Generated by Django 4.1.1 on 2022-09-17 17:28

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0009_remove_menu_sections_menu_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=140, unique=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='variant',
            field=wagtail.fields.StreamField([('footer', wagtail.blocks.StructBlock([('sections', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(blank=True, label='Section Title', max_length=64, null=True)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('_text', wagtail.blocks.CharBlock(label='Text', max_length=240, required=False)), ('_kind', wagtail.blocks.ChoiceBlock(choices=[('URL', 'URL'), ('PAGE', 'Page')], help_text='If you want to link to a page on some other website (e.g. twitter.com) chose "URL". If you want to link to a page on this site, choose "Page"', label='Kind')), ('_page', wagtail.blocks.PageChooserBlock(label='Page', required=False)), ('_url', wagtail.blocks.URLBlock(label='URL', required=False))])))]))), ('include_social_media', wagtail.blocks.BooleanBlock(required=False))])), ('mobile_menu', wagtail.blocks.StructBlock([('brand', wagtail.blocks.CharBlock(max_length=32)), ('pages', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock())), ('call_to_action', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('_text', wagtail.blocks.CharBlock(label='Text', max_length=240, required=False)), ('_kind', wagtail.blocks.ChoiceBlock(choices=[('URL', 'URL'), ('PAGE', 'Page')], help_text='If you want to link to a page on some other website (e.g. twitter.com) chose "URL". If you want to link to a page on this site, choose "Page"', label='Kind')), ('_page', wagtail.blocks.PageChooserBlock(label='Page', required=False)), ('_url', wagtail.blocks.URLBlock(label='URL', required=False))]), max_num=2)), ('include_social_media', wagtail.blocks.BooleanBlock(required=False))])), ('navbar', wagtail.blocks.StructBlock([('brand', wagtail.blocks.CharBlock(max_length=32)), ('pages', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock())), ('call_to_action', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('_text', wagtail.blocks.CharBlock(label='Text', max_length=240, required=False)), ('_kind', wagtail.blocks.ChoiceBlock(choices=[('URL', 'URL'), ('PAGE', 'Page')], help_text='If you want to link to a page on some other website (e.g. twitter.com) chose "URL". If you want to link to a page on this site, choose "Page"', label='Kind')), ('_page', wagtail.blocks.PageChooserBlock(label='Page', required=False)), ('_url', wagtail.blocks.URLBlock(label='URL', required=False))]), max_num=2))]))], null=True, use_json_field=True),
        ),
    ]
