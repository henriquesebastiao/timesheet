"""Module for configuration of the app."""

from django.apps import AppConfig


class TimesheetAppConfig(AppConfig):
    """Timesheet app configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'timesheet.app'
