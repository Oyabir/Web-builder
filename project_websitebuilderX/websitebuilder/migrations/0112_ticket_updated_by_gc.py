# Generated by Django 5.0.7 on 2024-07-23 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0111_ticket_description_updated_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='updated_by_gc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='websitebuilder.gestionnairecomptes'),
        ),
    ]
