"""This module contains the models of the app."""

import datetime

from django.contrib.auth import get_user_model
from django.db import models


class PointRecord(models.Model):
    """Model that represents a point record."""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    register_date = models.DateField(default=datetime.date.today)
    clock_in_morning = models.TimeField(null=True, blank=True)
    clock_out_morning = models.TimeField(null=True, blank=True)
    clock_in_afternoon = models.TimeField(null=True, blank=True)
    clock_out_afternoon = models.TimeField(null=True, blank=True)
    is_saturday = models.BooleanField(default=False)
    is_sunday = models.BooleanField(default=False)
    is_holiday = models.BooleanField(default=False)
    is_vacation = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'register_date')

    def __str__(self):
        return f'{self.register_date.day}-{self.register_date.month}-{self.register_date.year}'
