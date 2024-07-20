# Generated by Django 5.0.4 on 2024-06-28 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0091_alter_websites_langues_alter_websites_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Websites_hebergement_payment_delay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Statu_du_website', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websitebuilder.cliente')),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websitebuilder.websites')),
                ('website_builder', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='websitebuilder.websitebuilder')),
            ],
        ),
    ]
