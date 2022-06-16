from bs4 import BeautifulSoup
from urllib.request import urlopen
import sqlite3

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()

list_film = cursor.execute('select * from CinemaApp_parserposterproperty')

_new_item_film = list()
count = 0
for i in list_film:
    _new_item_film.append(i)


class Poster:
    def __init__(self, name, href, photo, description='', data='', ):
        self.name = name,
        self.description = description,
        self.photo = photo
        self.href = href
        self.data = data


# url = 'https://krsk.kinoluch.ru/poster'
# def choice_index():
#   pass
_index = 0


def get_posters(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    list_posters = list()

    names_of_films = soup.find_all(f'{_new_item_film[_index][2]}', class_=f'{_new_item_film[_index][3]}')

    for film in names_of_films:
        name = film.find(f'{_new_item_film[_index][4]}', class_=f'{_new_item_film[_index][5]}').text
        data = film.find(f'{_new_item_film[_index][6]}', class_=f'{_new_item_film[_index][13]}')
        href = film[f'{_new_item_film[_index][7]}']

        photo_ = film.find(f'{_new_item_film[_index][8]}')[f'{_new_item_film[_index][9]}']
        photo = f'https://krsk.kinoluch.ru{photo_}'

        film = Poster(name, href=href, photo=photo, data=data)
        list_posters.append(film)

    for film in list_posters:
        if film.data is None:
            html = urlopen(f'https://krsk.kinoluch.ru{film.href}')
            soup = BeautifulSoup(html, 'html.parser')
            description = soup.find(f'{_new_item_film[_index][10]}', class_=f'{_new_item_film[_index][11]}').find(
                f'{_new_item_film[_index][12]}').text
            film.description = description

    return list_posters
