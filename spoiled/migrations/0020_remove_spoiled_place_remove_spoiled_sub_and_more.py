# Generated by Django 4.0 on 2022-01-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoiled', '0019_rename_number_photo_spoiled_write_off'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spoiled',
            name='place',
        ),
        migrations.RemoveField(
            model_name='spoiled',
            name='sub',
        ),
        migrations.AddField(
            model_name='spoiled',
            name='sub_description',
            field=models.CharField(choices=[('WH', '1. Пропажа товара на складе / при разгрузке автомобиля.'), ('TF', '2. Пропажа, бой, брак, истекший срок годности товара в торговом зале.'), ('ST', '3. Бой товара в торговом зале или на складе сотрудником магазина.')], default='WH', max_length=2, verbose_name='Новый вид'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(help_text='Name group', max_length=200),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(help_text='Name shop', max_length=15),
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='Sub',
        ),
    ]
