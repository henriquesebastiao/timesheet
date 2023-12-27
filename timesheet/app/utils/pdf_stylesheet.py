"""This module contains the stylesheet for the PDF report."""

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle, StyleSheet1


def stylesheet():
    """
    Function that returns the stylesheet for the PDF report.
    Returns:
        A StyleSheet1 object.
    """
    sheet = StyleSheet1()

    sheet.add(ParagraphStyle(name='Normal', fontSize=10, leading=12))

    sheet.add(
        ParagraphStyle(
            name='Title',
            parent=sheet['Normal'],
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
        ),
        alias='title',
    )

    sheet.add(
        ParagraphStyle(
            name='Name',
            parent=sheet['Normal'],
            fontSize=14,
            leading=18,
            spaceBefore=2,
        ),
        alias='h2',
    )

    sheet.add(
        ParagraphStyle(
            name='Function',
            parent=sheet['Normal'],
            fontSize=12,
            leading=14,
            spaceBefore=1,
        ),
        alias='h3',
    )

    sheet.add(
        ParagraphStyle(
            name='Saturday',
            parent=sheet['Normal'],
            fontSize=10,
            leading=12,
            spaceBefore=1,
            spaceAfter=12,
        ),
        alias='h4',
    )

    sheet.add(
        ParagraphStyle(
            name='Footer',
            parent=sheet['Normal'],
            fontSize=10,
            leading=12,
            spaceBefore=12,
        ),
    )

    return sheet


def style(heading):
    """
    Function that returns the style for a given heading.
    Args:
        heading: Heading to be styled.

    Returns:
        A ParagraphStyle object.
    """
    s = stylesheet()[heading]
    s.alignment = TA_CENTER
    return s
