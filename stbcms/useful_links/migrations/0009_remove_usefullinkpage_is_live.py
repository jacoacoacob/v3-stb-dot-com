# Generated by Django 4.1.1 on 2022-10-14 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useful_links', '0008_remove_usefullinkpage_link_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usefullinkpage',
            name='is_live',
        ),
    ]
