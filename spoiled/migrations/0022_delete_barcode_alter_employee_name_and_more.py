# Generated by Django 4.0 on 2022-01-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoiled', '0021_spoiled_future_spoiled_alter_spoiled_sub_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Barcode',
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(help_text='Name employee', max_length=200),
        ),
        migrations.AlterField(
            model_name='nomenclature',
            name='characteristic',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='nomenclature',
            name='unit',
            field=models.CharField(default='', help_text='unit', max_length=10),
        ),
    ]
