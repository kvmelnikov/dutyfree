# Generated by Django 4.0 on 2021-12-24 07:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nomenclature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name shop', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Shop must be greater than 1 character')])),
                ('plu', models.CharField(help_text='plu', max_length=20)),
                ('barcode', models.IntegerField(help_text='Barcode')),
                ('inv_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('group', models.CharField(help_text='group', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Place spoiled', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Place must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name shop', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Shop must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Sub spoiled', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Sub must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Spoiled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(help_text='Name employee', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Employee must be greater than 1 character')])),
                ('nomenclature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spoiled.nomenclature')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spoiled.shop')),
            ],
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spoiled.shop'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name employee', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Employee must be greater than 1 character')])),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spoiled.shop')),
            ],
        ),
    ]