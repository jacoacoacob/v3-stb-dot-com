# Generated by Django 4.1.1 on 2022-09-14 02:08

from django.db import migrations, models
import django_extensions.db.fields
import wagtail.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0005_menusectionitem_rename_menulinklist_menusection_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('sections', wagtail.fields.StreamField([('section', wagtail.snippets.blocks.SnippetChooserBlock('MenuSection'))], use_json_field=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]