# Generated by Django 5.0.4 on 2024-05-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0052_alter_websitebuilder_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achatwebsites',
            name='BuilderStatus',
            field=models.CharField(choices=[('Builder', 'Builder'), ('in progress', 'in progress'), ('Not yet', 'Not yet')], default='Not yet', max_length=50, null=True),
        ),
    ]