# Generated by Django 3.2 on 2022-02-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0049_auto_20220203_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'Наличными при получении'), ('card_online', 'Банковской картой на сайте')], db_index=True, max_length=50, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('not_processed', 'Не обработан'), ('processed', 'Обработан'), ('done', 'Завершен')], db_index=True, default='not_processed', max_length=20, verbose_name='Статус заказа'),
        ),
    ]
