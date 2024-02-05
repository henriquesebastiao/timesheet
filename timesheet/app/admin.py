"""Timesheet app admin configuration."""

from django.contrib import admin
from django.contrib.auth import get_user_model
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

    def get_form(self, request, obj=None, change=False, **kwargs):
        """Return a custom form for the admin."""
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['user'].queryset = get_user_model().objects.filter(
            id=request.user.id
        )
        return form

    def get_queryset(self, request):
        """Return a QuerySet of only the logged-in user's point records."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
