"""Module that contains the function that generates the PDF file."""

import calendar
from datetime import date, datetime
from io import BytesIO

from django.db.models import QuerySet
from django.http import FileResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle
from workalendar.america import Brazil

from .pdf_stylesheet import style


def generate_pdf(queryset: QuerySet):
    """
    Function that generates a PDF file with the registers of the queryset.
    Args:
        queryset: Queryset with the registers to be included in the PDF.

    Returns:
        A FileResponse object with the PDF file.
    """
    buffer = BytesIO()
    kalendar = Brazil()

    _, last_day = calendar.monthrange(
        datetime.now().year, datetime.now().month
    )

    month_name = {
        1: 'janeiro',
        2: 'fevereiro',
        3: 'março',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro',
    }

    records = [
        [
            'DIA DO MÊS',
            'ENTRADA MANHÃ',
            'SAÍDA MANHÃ',
            'RETORNO',
            'SAÍDA TARDE',
        ],
    ]

    def format_time(time) -> str:
        """
        Function that formats a time object to a string.
        Args:
            time: Time object to be formatted.

        Returns:
            A string with the time formatted.
        """

        if time is not None and (
            kalendar.is_working_day(d) or d.weekday() == 5 or d.weekday() == 6
        ):
            formatted_time = time.strftime('%H:%M')
        elif time is None and kalendar.is_working_day(d):
            formatted_time = '-'
        else:
            formatted_time = '*'

        return formatted_time

    for record in queryset:
        d = date(
            record.register_date.year,
            record.register_date.month,
            record.register_date.day,
        )

        day = str(record.register_date.day)

        if d.weekday() == 6:
            day += '(domingo)'
        elif kalendar.is_holiday(d):
            day += '(feriado)'
        elif d.weekday() == 5:
            day += '(sábado)'

        records.append(
            [
                day,
                format_time(record.clock_in_morning),
                format_time(record.clock_out_morning),
                format_time(record.clock_in_afternoon),
                format_time(record.clock_out_afternoon),
            ]
        )

        if d.weekday() == 5 and record.register_date.day < last_day:
            records.append(
                [
                    str(record.register_date.day + 1),
                    [None] * 4,
                ]
            )

    elements = []

    table = Table(data=records)
    table.setStyle(
        TableStyle(
            [
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ]
        )
    )

    for item in (
        Paragraph(
            f'Folha de Ponto - {str(datetime.now().month)}/{str(datetime.now().year)}',
            style('Title'),
        ),
        Paragraph('Henrique Sebastião da Silva Rosa', style('Name')),
        Paragraph('Técnico de Redes', style('Function')),
        Paragraph('Horários aos sábados: 07:30 às 12:00', style('Saturday')),
        table,
        Paragraph(
            'PDF gerado por Timesheet - Desenvolvido com Python por Henrique Sebastião.',
            style('Footer'),
        ),
    ):
        elements.append(item)

    pdf = SimpleDocTemplate(buffer, pagesize=A4)

    pdf.build(elements)
    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename=f'folha_de_ponto_{month_name[datetime.now().month]}.pdf',
    )