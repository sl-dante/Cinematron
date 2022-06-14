import sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
import requests

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()

list_genre = cursor.execute('select * from CinemaApp_genre')


class Film:
    def __init__(self, name, href, year='', genre='', country='', description='', photo='', main_actor=''):
        self.name = name,
        self.description = description,
        self.photo = photo
        self.href = href
        self.main_actor = main_actor
        self.year = year
        self.country = country
        self.genre = genre


"""
data_film_comedy = list()

url = 'top100-comedy/'
html = urlopen(f'https://www.kinonews.ru/{url}')
soup = BeautifulSoup(html, 'html.parser')
film_list = list()

names_of_films = soup.find_all('a', attrs={'class': 'titlefilm'})

count = 1
for i in names_of_films:
    id = count
    name = i.text
    href = i['href']
    html_film = urlopen(f'https://www.kinonews.ru/{href}')
    soup = BeautifulSoup(html_film, 'html.parser')
    description = soup.find_all('div', {'itemprop': 'description'})[0].text
    photo = soup.find('img', attrs={'class': 'newsimg'})['src']
    genre = soup.find_all('span', {'itemprop': 'genre'})[0].text
    for i in list_genre:
        if genre == i[1]:
            print(i[1])
            genre = i[0]
    film_data = (id, name, description, photo, href, 'main_actor', 'year', 'country', genre)
    count += 1
    film_list.append(film_data)

print(film_list)"""

'''
query = "INSERT into CinemaApp_film values (?,?,?,?,?,?,?,?,?)"

cursor.executemany(query, film_list)
conn.commit()'''
url = 'top100-comedy/'
html = urlopen(f'https://www.kinonews.ru/{url}')
soup = BeautifulSoup(html, 'html.parser')
film_list = list()

name_film = soup.find('a', attrs={'class': 'titlefilm'})
directed = soup.find(text='Режиссер:').parent.parent
main_actor = soup.find(text='В главных ролях:').parent.parent
main_actor = main_actor.find('a').text
directed = directed.find('a').text
href = name_film['href']
html_film = urlopen(f'https://www.kinonews.ru/{href}')
soup = BeautifulSoup(html_film, 'html.parser')
description = soup.find_all('div', {'itemprop': 'description'})[0].text
photo = soup.find('img', attrs={'class': 'newsimg'})['src']
genre = soup.find_all('span', {'itemprop': 'genre'})[0].text

print(main_actor)

for i in list_genre:
    if str(genre).lower() == str(i[1]).lower():
        genre = i[0]

print(name_film, directed, href, description, photo, genre)
