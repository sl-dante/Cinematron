from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
import requests



def parse_cinema_info(url):
    html = urlopen(f'https://www.kinonews.ru/{url}')
    soup = BeautifulSoup(html, 'html.parser')
    film_list = list()

    names_of_films = soup.find_all('a', attrs={'class': 'titlefilm'})

    for i in names_of_films:
        film = Film(name=i.text, href=i['href'])
        film_list.append(film)

    choice_film = random.choice(film_list)
    html = urlopen(f'https://www.kinonews.ru/{choice_film.href}')
    soup = BeautifulSoup(html, 'html.parser')
    choice_film.description = soup.find_all('div', {'itemprop': 'description'})[0].text
    choice_film.photo = soup.find('img', attrs={'class': 'newsimg'})['src']

    return choice_film
