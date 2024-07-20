# Generated by Django 5.0.4 on 2024-06-05 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0072_remove_website_need_suspendre_website'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Website_need_reprendre',
            new_name='Website_resiliation_reprendre',
        ),
        migrations.CreateModel(
            name='Website_reprendre_suspendre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Statu_du_website', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websitebuilder.cliente')),
                ('location_website_builder', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='websitebuilder.locationwebsitebuilder')),
                ('website_builder', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='websitebuilder.websitebuilder')),
            ],
        ),
    ]