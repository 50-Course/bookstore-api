from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    """Object class for a Book

    Args:
        title (str): Name of a printed release
        subtitle (str): Sub-heading for a printed release
        author (str): Author(s) associated with the book
        isbn (str): 13-digit number associated to a book release
    """
    title = models.CharField(_('Title'), max_length=100, db_index=True, help_text='Book Title')
    subtitle = models.CharField(_('Subtitle'), max_length=120, null=True, blank=True, help_text='Tagline')
    author = models.CharField(_('Author'), max_length=80)
    isbn = models.CharField(_('ISBN'), max_length=13)

    def __str__(self) -> str:
        return f'{self.title} - {self.author}'