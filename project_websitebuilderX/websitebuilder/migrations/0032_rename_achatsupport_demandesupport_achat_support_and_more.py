# Generated by Django 5.0.4 on 2024-05-08 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0031_remove_demandesupport_support_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demandesupport',
            old_name='achatSupport',
            new_name='achat_support',
        ),
        migrations.RenameField(
            model_name='demandesupport',
            old_name='Status',
            new_name='status',
        ),
    ]