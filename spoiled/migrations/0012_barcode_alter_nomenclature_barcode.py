# Generated by Django 4.0 on 2021-12-28 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spoiled', '0011_group_alter_nomenclature_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Barcode', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='nomenclature',
            name='barcode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spoiled.barcode'),
        ),
    ]