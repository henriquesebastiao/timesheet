# Generated by Django 5.0 on 2023-12-27 03:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_pointrecord_is_saturday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointrecord',
            name='register_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]