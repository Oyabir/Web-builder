# Generated by Django 5.0.4 on 2024-06-19 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0085_websitebuilder_date_build'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationwebsitebuilder',
            name='Statu_du_website_action',
        ),
    ]
