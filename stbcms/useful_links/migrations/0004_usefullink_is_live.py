# Generated by Django 4.1.1 on 2022-09-25 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useful_links', '0003_alter_usefullink_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usefullink',
            name='is_live',
            field=models.BooleanField(default=False, help_text='This link will not appear to site visitors unless this box is checked'),
        ),
    ]
