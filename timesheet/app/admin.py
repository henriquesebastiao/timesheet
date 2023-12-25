"""Timesheet app admin configuration."""

from django.contrib import admin

from .models import PointRecord


@admin.register(PointRecord)
class PointRecordAdmin(admin.ModelAdmin):
    """PointRecord admin configuration."""

    list_display = [
        'register_date',
        'clock_in_morning',
        'clock_out_morning',
        'clock_in_afternoon',
        'clock_out_afternoon',
        'is_saturday',
    ]

    list_display_links = ['register_date']
    search_fields = ['register_date']
    list_filter = ['is_saturday']
    list_per_page = 7
    ordering = ['id']
