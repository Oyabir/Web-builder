# Generated by Django 5.0.4 on 2024-05-08 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0029_alter_achatsupport_statusconsomé'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[('Consomé', 'Consomé'), ('Not Consomé', 'Not Consomé')], default='Not Consomé', max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('code_DemandeSupport', models.CharField(max_length=100, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websitebuilder.cliente')),
                ('support', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websitebuilder.supports')),
            ],
        ),
    ]
