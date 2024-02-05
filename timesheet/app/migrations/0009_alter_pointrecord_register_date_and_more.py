# Generated by Django 5.0 on 2024-02-05 00:33

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_pointrecord_is_vacation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointrecord',
            name='register_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterUniqueTogether(
            name='pointrecord',
            unique_together={('user', 'register_date')},
        ),
    ]