# Файл по заполнению базы данных с помощью парсинга

import sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
import requests
from ChatBot.ClassFilm import Film

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()


def fill_db_with_parser(url_data_films):
    html = urlopen(f'https://www.kinonews.ru/{url_data_films}')
    soup = BeautifulSoup(html, 'html.parser')
    film_list = list()
    flag_year = False
    flag_main_actor = False
    flag_directed = False
    flag_county = False
    name_films = soup.find_all('a', attrs={'class': 'titlefilm'})

    for name_film in name_films:
        name = name_film.text
        href = name_film['href']

        html_film = urlopen(f'https://www.kinonews.ru/{href}')

        soup = BeautifulSoup(html_film, 'html.parser')

        # В фильме может не указываться режиссёр
        try:
            directed = soup.find('table', attrs={'class': 'tab-film'}).find(text='Режиссеры:').parent.parent.text \
                .split(':')[1].split(',')[0].replace('\n', '')
        except AttributeError:
            flag_directed = True

        if flag_directed is True:
            flag_directed = False
            directed = ''

        # Не у всех фильмов есть актёры
        try:
            main_actor = soup.find('table', attrs={'class': 'tab-film'}).find(text='Актеры:').parent.parent.text \
                .split(':')[1].split(',')[0].replace('\n', '')
        except AttributeError:
            flag_main_actor = True

        if flag_main_actor is True:
            flag_main_actor = False
            main_actor = ''

        try:
            country = soup.find('table', attrs={'class': 'tab-film'}).find(text='Страна:').parent.parent.text \
                .split(':')[1].split(',')[0].replace('\n', '')
        except AttributeError:
            flag_county = True

        if flag_county is True:
            flag_county = False
            main_actor = ''

        # Некоторые жанры идут сериалами у них нет этого поля
        try:
            year = soup.find('table', attrs={'class': 'tab-film'}).find(text='Год выпуска:').parent.parent.text \
                .split(':')[1].split(',')[0].replace('\n', '')
        except AttributeError:
            flag_year = True

        if flag_year is True:
            flag_year = False
            year = soup.find('table', attrs={'class': 'tab-film'}).find(text='Год начала:').parent.parent.text \
                .split(':')[1].split(',')[0].replace('\n', '')

        description = soup.find('div', {'itemprop': 'description'}).text
        photo = soup.find('img', attrs={'class': 'newsimg'})['src']
        genre = soup.find_all('span', {'itemprop': 'genre'})[0].text

        list_genre = cursor.execute('select * from CinemaApp_genre')
        for genre_by_db in list_genre:
            if str(genre).lower() == str(genre_by_db[1]).lower():
                genre = genre_by_db[0]
                break

        film = Film(_name=name,
                    _description=description,
                    _photo=photo,
                    _href=href,
                    _main_actor=main_actor,
                    _year=year,
                    _country=country,
                    _genre=genre,
                    _directed=directed)

        film = (name, description, photo, href, main_actor, directed, year, country, genre)
        film_list.append(film)

    query = "INSERT into CinemaApp_film values (NULL,?,?,?,?,?,?,?,?,?)"

    cursor.executemany(query, film_list)
    conn.commit()


if __name__ == '__main__':
    # Невошедшие жанры
    urls_genre_film = ['top100-anime/', ]
