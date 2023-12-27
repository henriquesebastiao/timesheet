"""This module contains the models of the app."""

from django.contrib.auth import get_user_model
from django.db import models


class PointRecord(models.Model):
    """Model that represents a point record."""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    register_date = models.DateField(auto_now_add=True)
    clock_in_morning = models.TimeField(null=True, blank=True)
    clock_out_morning = models.TimeField(null=True, blank=True)
    clock_in_afternoon = models.TimeField(null=True, blank=True)
    clock_out_afternoon = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.register_date}'
