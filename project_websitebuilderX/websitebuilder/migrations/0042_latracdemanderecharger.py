# Generated by Django 5.0.4 on 2024-05-14 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0041_demanderecharger_image_demanderecharger_solde'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaTracDemandeRecharger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('solde', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websitebuilder.cliente')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='websitebuilder.gestionnairecomptes')),
            ],
        ),
    ]
