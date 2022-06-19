import sqlite3
from ChatBot.ClassFilm import Film
import random

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()


def select_film_by_genre_name(genre):
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


def select_sim_film(genre):
    list_films = list()
    select_films_sql = cursor.execute(
        'SELECT CinemaApp_similargenre.sim_genre_id '
        'FROM CinemaApp_similargenre '
        'JOIN CinemaApp_genre ON CinemaApp_similargenre.genre_id = CinemaApp_genre.id'
        f' WHERE CinemaApp_genre.name = "{genre}"', )

    for _id in select_films_sql:
        list_films.append(_id[0])

    return list_films


def select_genre_by_id(id_genre):
    name_genre = ''
    select_genre = cursor.execute(
        'SELECT CinemaApp_genre.name FROM CinemaApp_genre '
        f'WHERE CinemaApp_genre.id = {id_genre}'
    )

    for _name in select_genre:
        name_genre = _name[0]

    return name_genre


def select_genre_by_name(name_genre):
    id_genre = ''
    select_genre = cursor.execute(
        'SELECT CinemaApp_genre.id FROM CinemaApp_genre '
        f'WHERE CinemaApp_genre.name = "{name_genre}"'
    )

    for _id in select_genre:
        id_genre = _id[0]

    return id_genre


def insert_user_info(genre, user_id):
    select_films_sql = cursor.execute(
        'INSERT into CinemaApp_user values (NULL,?,?,?,?)', (user_id, 'name', 'surname', genre)
    )

    conn.commit()


def automatically_select(id_user):
    list_genres = list()

    select_users_info = cursor.execute(
        'SELECT CinemaApp_user.chosen_genre_id, COUNT(CinemaApp_user.chosen_genre_id)  FROM CinemaApp_user '
        f'WHERE CinemaApp_user.vk_id = {id_user} '
        f'GROUP BY CinemaApp_user.chosen_genre_id'
    )

    for id_genre, count in select_users_info:
        list_genres.append([id_genre, count])

    return list_genres

