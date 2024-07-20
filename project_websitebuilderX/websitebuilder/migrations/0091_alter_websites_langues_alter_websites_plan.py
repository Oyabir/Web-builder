# Generated by Django 5.0.4 on 2024-06-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0090_alter_websites_cms_alter_websites_catégorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websites',
            name='langues',
            field=models.CharField(choices=[('Français', 'Français'), ('Anglais', 'Anglais')], default='Français', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='websites',
            name='plan',
            field=models.CharField(choices=[('Free', 'Free'), ('Payant', 'Payant')], default='Free', max_length=50, null=True),
        ),
    ]