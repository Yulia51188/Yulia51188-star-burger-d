# Generated by Django 3.2 on 2022-01-25 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0041_order_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='phone',
            new_name='phonenumber',
        ),
    ]
