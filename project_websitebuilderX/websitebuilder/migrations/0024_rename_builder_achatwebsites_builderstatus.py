# Generated by Django 5.0.4 on 2024-05-07 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0023_alter_achatwebsites_builder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achatwebsites',
            old_name='Builder',
            new_name='BuilderStatus',
        ),
    ]
