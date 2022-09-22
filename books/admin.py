from django.contrib import admin
from django.db import models
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass