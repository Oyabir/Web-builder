# Generated by Django 5.0.4 on 2024-05-22 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0057_remove_mergedwebsitebuilder_namewebsite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mergedwebsitebuilder',
            name='app_port',
        ),
        migrations.RemoveField(
            model_name='mergedwebsitebuilder',
            name='db_port',
        ),
    ]
