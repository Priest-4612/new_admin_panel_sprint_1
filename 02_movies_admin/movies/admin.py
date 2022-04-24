"""Объявление admin моделей приложения фильмы."""
from django.contrib import admin

from movies import models  # isort:skip


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created', 'modified']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'created', 'modified']
    list_display_links = ['full_name']
    list_filter = ['full_name']
    search_fields = ['full_name']


class GenreFilmworkInline(admin.TabularInline):
    model = models.GenreFilmwork


class PersonFilmWorkInline(admin.TabularInline):
    model = models.PersonFilmwork
    autocomplete_fields = ['person']


@admin.register(models.Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'type', 'creation_date', 'rating', 'created', 'modified',
    ]
    list_filter = ['type']
    search_fields = ['title', 'description', 'id']
    inlines = (GenreFilmworkInline, PersonFilmWorkInline)
