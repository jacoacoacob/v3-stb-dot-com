# Generated by Django 4.1.1 on 2022-10-14 01:36

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('useful_links', '0006_usefullinkpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usefullinkcategories',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorized_items', to='useful_links.usefullinkpage'),
        ),
        migrations.AlterField(
            model_name='usefullinktag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='useful_links.usefullinkpage'),
        ),
        migrations.DeleteModel(
            name='UsefulLink',
        ),
    ]