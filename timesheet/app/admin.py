"""Timesheet app admin configuration."""

from django.contrib import admin
from django.db.models import QuerySet

from .models import PointRecord
from .utils.pdf import generate_pdf


@admin.register(PointRecord)
class PointRecordAdmin(admin.ModelAdmin):
    """PointRecord admin configuration."""

    actions = ['get_pdf']

    list_display = [
        'register_date',
        'clock_in_morning',
        'clock_out_morning',
        'clock_in_afternoon',
        'clock_out_afternoon',
        'is_saturday',
        'is_sunday',
        'is_holiday',
        'is_vacation',
    ]

    list_display_links = ['register_date']
    search_fields = ['register_date']
    list_filter = ['register_date', 'is_saturday', 'is_sunday', 'is_holiday']
    list_per_page = 7

    # Ordena os registros por data em ordem decrescente para a visualização no painel de administração.
    ordering = ['-register_date']

    @admin.action(description='Generate PDF')
    def get_pdf(self, request, queryset: QuerySet):
        """Generate a PDF with the selected registers."""
        return generate_pdf(queryset)
