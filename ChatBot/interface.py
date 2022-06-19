import random

import vk_api
import urllib.request
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
import const

from ChatBot.keyboards import *
from ChatBot.common_methods import *
from ChatBot.poster_parser import get_posters
from ChatBot.query import *
from ChatBot.expert_system import genre_calculate

vk_session = vk_api.VkApi(token=const.token)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk_session)
longPoll = VkBotLongPoll(vk_session, group_id=const.group_id)
count_for_answer = 0
list_for_answer = []

flag_for_es = False


# Создание простого ответа чат-бота на сообщение пользователя
def create_event_message(message, chat_bot_responce, keyboard):
    if event.obj.text.lower() == message.lower():
        if event.from_user:
            vk.messages.send(
                user_id=event.obj.from_id,
                random_id=get_random_id(),
                message=chat_bot_responce,
                keyboard=keyboard)


for event in longPoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text.lower() == 'начать' or event.obj.text.lower() == 'привет':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Здраствуй',
                    keyboard=encode_keyboard_for_vk(main_menu_keyboard))

        if event.obj.text.lower() == 'посоветуй фильм':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message="Выбери жанр",
                    keyboard=encode_keyboard_for_vk(keyboard_for_films))

        if event.obj.text.lower() == 'афиша':

            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Подождите, Афиша уже готовится))',
                    keyboard=encode_keyboard_for_vk(keyboard_for_back),
                )

            films = get_posters('https://krsk.kinoluch.ru/poster')

            for film in films:
                if film.data is None:
                    if event.from_user:
                        vk.messages.send(
                            user_id=event.obj.from_id,
                            random_id=get_random_id(),
                            message=f'Название: {film.name[0]}\n\n{film.description}',
                            attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'вернуться в главное меню':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Ок',
                    keyboard=encode_keyboard_for_vk(main_menu_keyboard))

        if event.obj.text.lower() == 'комедия':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'мультфильм':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'триллер':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'фантастика':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'аниме':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'боевик':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'вестерн':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'военный':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'детектив':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'драма':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'криминал':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'мелодрама':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'мюзикл':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'фэнтези':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'ужасы':
            film = select_film_by_genre_name(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'давай подберём мне фильм':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Пройди опрос, чтобы узнать какие фильмы тебе по душе, со временем, я  буду '
                            f'тебе предлагать фильмы, на своё усмотрение',
                    keyboard=encode_keyboard_for_vk(keyboard_for_expert_system), )

        if event.obj.text.lower() == 'выбери на своё усмотрение':
            list_genres = automatically_select(event.obj.from_id)
            film_genre = select_film_by_genre_name(select_genre_by_id(list_genres[0][0]))
            _genre_f = film_genre.genre
            count = 0
            list_genres = set()
            finally_genre_film = _genre_f
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Сейчас попробую!\n'
                            f'\nНазвание: {film_genre.name}\nЖанр:{film_genre.genre}\n{film_genre.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_choice_film),
                    attachment=load_photo(film_genre, upload=upload))

            for _event in longPoll.listen():
                if _event.obj.text.lower() == 'выбери другой' and count < 3:
                    count += 1
                    film = select_film_by_genre_name(_genre_f)
                    if _event.from_user:
                        vk.messages.send(
                            user_id=_event.obj.from_id,
                            random_id=get_random_id(),
                            message=f'\nНазвание: {film.name}\nЖанр:{film.genre}\n{film.description}',
                            keyboard=encode_keyboard_for_vk(keyboard_for_choice_film),
                            attachment=load_photo(film, upload=upload))

                if _event.obj.text.lower() == 'выбери другой' and count >= 3:
                    count += 1
                    ids_genre = select_sim_film(_genre_f)
                    for _id in ids_genre:
                        list_genres.add(select_genre_by_id(_id))
                    name_genre = random.choice(list(list_genres))
                    film = select_film_by_genre_name(name_genre)
                    finally_genre_film = name_genre

                    if _event.from_user:
                        vk.messages.send(
                            user_id=_event.obj.from_id,
                            random_id=get_random_id(),
                            message=f'\nНазвание: {film.name}\nЖанр:{film.genre}\n{film.description}',
                            keyboard=encode_keyboard_for_vk(keyboard_for_choice_film),
                            attachment=load_photo(film, upload=upload))

                if _event.obj.text.lower() == 'мне этот подойдет':
                    finally_genre_film = select_genre_by_name(finally_genre_film)
                    insert_user_info(finally_genre_film, event.obj.from_id)
                    if _event.from_user:
                        vk.messages.send(
                            user_id=_event.obj.from_id,
                            random_id=get_random_id(),
                            message=f'Отлично!',
                            keyboard=encode_keyboard_for_vk(main_menu_keyboard), )
                        break

                if _event.obj.text.lower() == 'вернуться в главное меню':
                    if _event.from_user:
                        vk.messages.send(
                            user_id=_event.obj.from_id,
                            random_id=get_random_id(),
                            message=f'Хорошо',
                            keyboard=encode_keyboard_for_vk(main_menu_keyboard), )
                        break

        if event.obj.text.lower() == 'пройти опрос':
            flag_for_es = True
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Давай подберём!\nОтветь на следующие вопросы либо "Да", либо "Нет"\n'
                            '1. Ты любишь картины, во время просмотра которых необходимо поразмыслить?\n'
                            '2. Ты любишь веселые, ненапряжные, смешные фильмы?\n'
                            '3. По твоему мнению любовные линии в фильме - это его основа?\n'
                            '4. Любишь понервничать во время просмотра?\n'
                            '5. А драконов ты любишь? Или любых других вымышленых персонажей?\n'
                            '6. Хочешь насладиться драйвом, погонями и драками?',
                    keyboard=encode_keyboard_for_vk(keyboard_for_polls))

            for _event in longPoll.listen():
                if _event.type == VkBotEventType.MESSAGE_NEW:
                    flag_for_es = False
                    list_for_answer.append(_event.obj.text.lower())

                    if _event.obj.text.lower() == 'продолжить':
                        finally_genre_film = ''
                        list_genres = set()
                        count = 0
                        _answer = list_for_answer[0].split(',')
                        _genre = genre_calculate(_answer)
                        list_genres.add(_genre)
                        finally_genre_film = _genre
                        film = select_film_by_genre_name(_genre)

                        if _event.from_user:
                            vk.messages.send(
                                user_id=_event.obj.from_id,
                                random_id=get_random_id(),
                                message=f'\nНазвание: {film.name}\nЖанр:{film.genre}\n{film.description}',
                                keyboard=encode_keyboard_for_vk(keyboard_for_choice_film),
                                attachment=load_photo(film, upload=upload))

                    if _event.obj.text.lower() == 'выбери другой' and count < 3:
                        count += 1
                        film = select_film_by_genre_name(_genre)
                        if _event.from_user:
                            vk.messages.send(
                                user_id=_event.obj.from_id,
                                random_id=get_random_id(),
                                message=f'\nНазвание: {film.name}\nЖанр:{film.genre}\n{film.description}',
                                keyboard=encode_keyboard_for_vk(keyboard_for_choice_film),
                                attachment=load_photo(film, upload=upload))

                    if _event.obj.text.lower() == 'выбери другой' and count >= 3:
                        count += 1
                        ids_genre = select_sim_film(_genre)
                        for _id in ids_genre:
                            list_genres.add(select_genre_by_id(_id))
                        name_genre = random.choice(list(list_genres))
                        film = select_film_by_genre_name(name_genre)
                        finally_genre_film = name_genre

                        if _event.from_user:
                            vk.messages.send(
                                user_id=_event.obj.from_id,
                                random_id=get_random_id(),
                                message=f'\nНазвание: {film.name}\nЖанр:{film.genre}\n{film.description}',
                                keyboard=encode_keyboard_for_vk(keyboard_for_choice_film),
                                attachment=load_photo(film, upload=upload))

                    if _event.obj.text.lower() == 'мне этот подойдет':
                        finally_genre_film = select_genre_by_name(finally_genre_film)
                        insert_user_info(finally_genre_film, event.obj.from_id)
                        if _event.from_user:
                            vk.messages.send(
                                user_id=_event.obj.from_id,
                                random_id=get_random_id(),
                                message=f'Отлично!',
                                keyboard=encode_keyboard_for_vk(main_menu_keyboard), )
                            break

                    if _event.obj.text.lower() == 'вернуться в главное меню':
                        if _event.from_user:
                            vk.messages.send(
                                user_id=_event.obj.from_id,
                                random_id=get_random_id(),
                                message=f'Хорошо',
                                keyboard=encode_keyboard_for_vk(main_menu_keyboard), )
                            break
