# Generated by Django 5.0.4 on 2024-05-08 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0026_supports'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supports',
            old_name='slugSupports',
            new_name='slugSupport',
        ),
    ]
