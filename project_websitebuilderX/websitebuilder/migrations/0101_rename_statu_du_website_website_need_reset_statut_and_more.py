# Generated by Django 5.0.4 on 2024-07-15 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websitebuilder', '0100_alter_facturations_achat_website_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='website_need_reset',
            old_name='Statu_du_website',
            new_name='statut',
        ),
        migrations.RenameField(
            model_name='website_need_resiliation',
            old_name='Statu_du_website',
            new_name='statut',
        ),
        migrations.RenameField(
            model_name='website_need_suspendre',
            old_name='Statu_du_website',
            new_name='statut',
        ),
        migrations.RenameField(
            model_name='website_reprendre_resiliation',
            old_name='Statu_du_website',
            new_name='statut',
        ),
        migrations.RenameField(
            model_name='website_reprendre_suspendre',
            old_name='Statu_du_website',
            new_name='statut',
        ),
        migrations.RenameField(
            model_name='websites_hebergement_payment_delay',
            old_name='Statu_du_website',
            new_name='statut',
        ),
        migrations.RenameField(
            model_name='websites_location_payment_delay',
            old_name='Statu_du_website',
            new_name='statut',
        ),
        migrations.RenameField(
            model_name='websites_need_delete',
            old_name='Statu_du_website',
            new_name='statut',
        ),
    ]
