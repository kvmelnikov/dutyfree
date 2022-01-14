# Generated by Django 4.0 on 2022-01-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoiled', '0025_spoiled_created_at_spoiled_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]