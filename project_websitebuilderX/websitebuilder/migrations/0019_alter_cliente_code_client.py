# Generated by Django 5.0.4 on 2024-05-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0018_alter_cliente_code_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='code_client',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
