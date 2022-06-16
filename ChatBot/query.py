import sqlite3
from ChatBot.ClassFilm import Film
import random

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()


def select_film(genre):
    list_films = list()
    select_films_sql = cursor.execute(
        'SELECT CinemaApp_film.name,CinemaApp_film.description, CinemaApp_film.photo, CinemaApp_film.href,'
        'CinemaApp_film.main_actor, CinemaApp_film.directed,CinemaApp_film.year, CinemaApp_film.country,'
        'CinemaApp_genre.name FROM CinemaApp_film '
        'INNER JOIN CinemaApp_genre ON CinemaApp_film.genre_id = CinemaApp_genre.id '
        f'WHERE CinemaApp_genre.name="{genre}"', )

    for name, description, photo, href, main_actor, directed, year, country, genre in select_films_sql:
        film = Film(_name=name,
                    _description=description,
                    _photo=photo,
                    _href=href,
                    _main_actor=main_actor,
                    _year=year,
                    _country=country,
                    _genre=genre,
                    _directed=directed)

        list_films.append(film)

    return random.choice(list_films)