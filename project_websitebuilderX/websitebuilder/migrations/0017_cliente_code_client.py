# Generated by Django 5.0.4 on 2024-05-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0016_rename_name_cliente_nom_cliente_prenom'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='code_client',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
