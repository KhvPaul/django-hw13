from django.contrib import admin

from .models import Author, Quote

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth']
    fields = ['name', 'date_of_birth', 'bio']


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'author']
    fields = ['text', 'author']