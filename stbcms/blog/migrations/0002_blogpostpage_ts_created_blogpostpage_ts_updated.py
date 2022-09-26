# Generated by Django 4.1.1 on 2022-09-26 00:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostpage',
            name='ts_created',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpostpage',
            name='ts_updated',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
