# Файл для создания клавиатур пользователя

import json


# Кодирование клавиатуры в JSON-формат
def encode_keyboard_for_vk(keyboard):
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))

    return keyboard


# Функция для создания кнопки
def get_button(label, color='primary', payload=''):
    return {
        'action': {
            'type': 'text',
            'payload': json.dumps(payload),
            'label': label
        },
        'color': color
    }


# Клавиатура главного меню
main_menu_keyboard = {
    'one_time': False,
    'buttons': [
        [
            get_button(label='Давай подберём мне фильм', color='primary'),
        ],
        [
            get_button(label='Посоветуй фильм', color='primary'),
        ],
        [
            get_button(label='Афиша', color='primary'),
        ]
    ]
}

# Клавиатура для возвращения назад
keyboard_for_back = {
    'one_time': False,
    'buttons': [
        [
            get_button(label='Вернуться в главное меню', color='primary')
        ],
    ]
}

# Клавиатура для ЭС
keyboard_for_expert_system = {
    'one_time': False,
    'buttons': [
        [
            get_button(label='Пройти опрос', color='primary'),
        ],
        [
            get_button(label='Выбери на своё усмотрение', color='primary')
        ],
        [
            get_button(label='Вернуться в главное меню', color='primary')
        ],
    ]
}

# Клавиатура для выбора фильмов
keyboard_for_choice_film = {
    'one_time': False,
    'buttons': [
        [
            get_button(label='Мне этот подойдет', color='primary'),
        ],
        [
            get_button(label='Выбери другой', color='primary')
        ],
        [
            get_button(label='Вернуться в главное меню', color='primary')
        ],
    ]
}

# Клавиатура для ЭС
keyboard_for_polls = {
    'one_time': False,
    'buttons': [
        [
            get_button(label='Продолжить', color='primary'),
        ],
        [
            get_button(label='Вернуться в главное меню', color='primary')
        ],
    ]
}

# Клавиатура для выбора фильмов по жанру
keyboard_for_films = {
    'one_time': False,
    'buttons': [
        [
            get_button(label='Комедия', color='primary'),
            get_button(label='Мультфильм', color='primary'),
            get_button(label='Триллер', color='primary'),
        ],
        [
            get_button(label='Ужасы', color='primary'),
            get_button(label='Фантастика', color='primary'),
            get_button(label='Аниме', color='primary'),
        ],
        [
            get_button(label='Боевик', color='primary'),
            get_button(label='Вестерн', color='primary'),
            get_button(label='Военный', color='primary'),
        ],
        [
            get_button(label='Детектив', color='primary'),
            get_button(label='Драма', color='primary'),
            get_button(label='Криминал', color='primary'),
        ],
        [
            get_button(label='Мелодрама', color='primary'),
            get_button(label='Мюзикл', color='primary'),
            get_button(label='Фэнтези', color='primary'),
        ],
        [
            get_button(label='Вернуться в главное меню', color='primary')
        ],
    ]
}
