import vk_api
import urllib.request
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
import const

from ChatBot.keyboards import *
from ChatBot.common_methods import *
from ChatBot.poster_parser import get_posters
from ChatBot.query import select_film

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
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'мультфильм':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'триллер':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'фантастика':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'аниме':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'боевик':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'вестерн':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'военный':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'детектив':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'драма':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'криминал':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'мелодрама':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'мюзикл':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'фэнтези':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

        if event.obj.text.lower() == 'ужасы':
            film = select_film(event.obj.text.capitalize())
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=f'Название: {film.name}\n\n{film.description}',
                    keyboard=encode_keyboard_for_vk(keyboard_for_films),
                    attachment=load_photo(film, upload=upload))

                if event.obj.text.lower() == 'давай подберём мне фильм':
                    flag_for_es = True
                    if event.from_user:
                        vk.messages.send(
                            user_id=event.obj.from_id,
                            random_id=get_random_id(),
                            message='Давай подберём!\nОтветь на следующие вопросы либо "Да", либо "Нет"\n'
                                    '1. Ты хочешь посмотреть кино со смыслом?\n'
                                    '2. Может тебе хочется посмеяться?\n'
                                    '3. Ты хочешь посмотреть фильмы про любовные отношения?\n'
                                    '4. Как ты относишься к фильмам, от которых очень страшно?\n'
                                    '5. Хочешь во время фильма немного поразмыслить?\n'
                                    '6. Или хочешь посмотреть кино про брутальных парней?',
                            keyboard=encode_keyboard_for_vk(keyboard_for_expert_system))

                if flag_for_es is True:
                    list_for_answer.append(event.obj.text.lower())

                if event.obj.text.lower() == 'продолжить':
                    flag_for_es = False
                    _info = list_for_answer[1].split(',')

                    if event.from_user:
                        vk.messages.send(
                            user_id=event.obj.from_id,
                            random_id=get_random_id(),
                            message=f'\nНазвание: {film.name[0]}\n\n{film.description}',
                            keyboard=encode_keyboard_for_vk(keyboard_for_expert_system),
                            attachment=load_photo(film, upload=upload))
