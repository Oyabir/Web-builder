# Generated by Django 5.0.4 on 2024-05-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0063_mergedwebsitebuilder_statu_du_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='mergedwebsitebuilder',
            name='Website_Client_statu',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=50, null=True),
        ),
    ]
