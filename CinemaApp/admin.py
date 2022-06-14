from django.contrib import admin
from .models import *


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)


@admin.register(ParserPosterProperty)
class ParserProperty(admin.ModelAdmin):
    list_display = (
        'name_of_cinema', 'list_of_films_arg_1', 'list_of_films_arg_2', 'name_of_film_arg_1', 'name_of_film_arg_2',
        'data_of_film_arg_1', 'href_of_film_arg_1', 'photo_of_film_arg_1', 'photo_of_film_arg_2',
        'description_of_film_arg_1', 'description_of_film_arg_2', 'description_of_film_arg_3')


@admin.register(SimilarGenre)
class SimilarGenre(admin.ModelAdmin):
    list_display = ('id', 'genre', 'sim_genre')


@admin.register(Genre)
class Genre(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'vk_id', 'chosen_genre')
