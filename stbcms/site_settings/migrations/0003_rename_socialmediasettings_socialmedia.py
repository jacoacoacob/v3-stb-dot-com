# Generated by Django 4.1.1 on 2022-09-17 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0076_modellogentry_revision'),
        ('site_settings', '0002_alter_socialmediasettings_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialMediaSettings',
            new_name='SocialMedia',
        ),
    ]