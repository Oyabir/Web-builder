# Generated by Django 5.0.4 on 2024-05-08 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0032_rename_achatsupport_demandesupport_achat_support_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='achatsupport',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='websitebuilder.administrateur'),
        ),
    ]
