# Generated by Django 4.0 on 2022-01-04 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spoiled', '0018_spoiled_name_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spoiled',
            old_name='number_photo',
            new_name='write_off',
        ),
    ]
