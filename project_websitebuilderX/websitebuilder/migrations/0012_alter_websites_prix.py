# Generated by Django 5.0.4 on 2024-05-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0011_alter_achat_solde_alter_cliente_solde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websites',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
