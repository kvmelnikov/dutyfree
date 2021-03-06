# Generated by Django 4.0 on 2022-01-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoiled', '0020_remove_spoiled_place_remove_spoiled_sub_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spoiled',
            name='future_spoiled',
            field=models.CharField(choices=[('NS', 'Нельзя Продать'), ('SD', 'Можно продать'), ('EB', 'Сотрудники')], default='NS', max_length=2, verbose_name='Что делать с браком'),
        ),
        migrations.AlterField(
            model_name='spoiled',
            name='sub_description',
            field=models.CharField(choices=[('WH', '1. Пропажа товара на складе / при разгрузке автомобиля.'), ('TF', '2. Пропажа, бой, брак, истекший срок годности товара в торговом зале.'), ('ST', '3. Бой товара в торговом зале или на складе сотрудником магазина.')], default='WH', max_length=2, verbose_name='Вид обстоятельств'),
        ),
    ]
