# Generated by Django 5.0.4 on 2024-05-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0025_alter_achatwebsites_builderstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Disponible', 'Disponible'), ('No Disponible', 'No Disponible')], default='Disponible', max_length=50, null=True)),
                ('prix', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('slugSupports', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
