# Файл с расчетами ЭС

def genre_calculate(answers):
    _drama = 1
    _comedy = 1
    _melodrama = 1
    _scary = 1
    _detective = 1
    _war = 1
    _cartoon = 1
    _thriller = 1
    _western = 1
    _action = 1
    _crime = 1
    _music = 1
    _fantasy = 1
    _fantastic = 1

    # Ответ на первый вопрос
    answers[0].replace(' ', '')
    if answers[0].lower() == 'да':
        _drama *= 1.8
        _comedy *= 1.3
        _melodrama *= 1.4
        _scary *= 1.05
        _detective *= 1.7
        _war *= 1.5
        _fantastic *= 1.6
        _music *= 1.2
        _crime *= 1.05
        _cartoon *= 1.1
        _thriller *= 1.3
        _action *= 1.1
        _western *= 1.1
        _fantasy *= 1.3
    elif answers[0].lower() == 'нет':
        _drama *= 1.1
        _comedy *= 1.5
        _melodrama *= 1.5
        _scary *= 1.7
        _detective *= 1.3
        _war *= 1.5
        _cartoon *= 1.8
        _thriller *= 1.6
        _western *= 1.7
        _action *= 1.7
        _crime *= 1.5
        _music *= 1.5
        _fantasy *= 1.6
        _fantastic *= 1.4
    else:
        'Некоректный ответ'

    # Ответ на второй вопрос
    answers[1].replace(' ', '')
    if answers[1].lower() == 'да':
        _drama *= 1.3
        _comedy *= 1.8
        _melodrama *= 1.4
        _scary *= 1.1
        _detective *= 1.3
        _war *= 1.3
        _cartoon *= 1.8
        _thriller *= 1.1
        _western *= 1.2
        _action *= 1.2
        _crime *= 1.1
        _music *= 1.7
        _fantasy *= 1.5
        _fantastic *= 1.5
    elif answers[1].lower() == 'нет':
        _drama *= 1.5
        _comedy *= 1.3
        _melodrama *= 1.5
        _scary *= 1.8
        _detective *= 1.7
        _war *= 1.7
        _cartoon *= 1.2
        _thriller *= 1.7
        _western *= 1.5
        _action *= 1.5
        _crime *= 1.7
        _music *= 1.2
        _fantasy *= 1.6
        _fantastic *= 1.5

    else:
        'Некоректный ответ'

    # Ответ на третий вопрос
    answers[2].replace(' ', '')
    if answers[2].lower() == 'да':
        _drama *= 1.7
        _comedy *= 1.4
        _cartoon *= 1.5
        _melodrama *= 1.5
        _war *= 1.1
    elif answers[2].lower() == 'нет':
        _scary *= 1.3
        _thriller *= 1.5
        _detective *= 1.5
        _war *= 1.4
    else:
        'Некоректный ответ'

    # Ответ на четвёртый вопрос
    answers[3].replace(' ', '')
    if answers[3].lower() == 'да':
        _thriller *= 1.7
        _scary *= 1.9
        _detective *= 1.6
        _war *= 1.6
        _action *= 1.5
        _crime *= 1.7
    elif answers[3].lower() == 'нет':
        _drama *= 1.4
        _comedy *= 1.7
        _melodrama *= 1.5
        _cartoon *= 1.6
        _music *= 1.7
    else:
        'Некоректный ответ'

    # Ответ на пятый вопрос
    answers[4].replace(' ', '')
    if answers[4].lower() == 'да':
        _fantasy *= 1.9
        _fantastic *= 1.9
        _cartoon *= 1.8
        _scary *= 1.6
    elif answers[4].lower() == 'нет':
        _drama *= 1.4
        _comedy *= 1.5
        _melodrama *= 1.5
        _detective *= 1.3
        _war *= 1.5
        _action *= 1.3
        _music *= 1.7
        _action *= 1.6
        _crime *= 1.5
    else:
        'Некоректный ответ'

    # Ответ на шестой вопрос
    answers[5].replace(' ', '')
    if answers[5].lower() == 'да':
        _action *= 1.9
        _scary *= 1.4
        _detective *= 1.7
        _war *= 1.8
        _western *= 1.8
        _fantasy *= 1.8
        _fantastic *= 1.7
    elif answers[5].lower() == 'нет':
        _drama *= 1.7
        _comedy *= 1.5
        _melodrama *= 1.8
        _cartoon *= 1.7
        _music *= 1.6
    else:
        'Некоректный ответ'

    '''Комедия
        Мультфильм
        Триллер
        Ужасы
        Фантастика
        Боевик
        Вестерн
        Военный
        Детектив
        Драма
        Криминал
        Мелодрама
        Мюзикл
        Фэнтези'''

    list_of_index = [_comedy, _cartoon, _thriller, _scary, _fantastic, _action,
                     _western, _war, _detective, _drama, _crime, _melodrama, _music, _fantasy]

    list_for_film = ['Комедия', 'Мультфильм', 'Триллер', 'Ужасы', 'Фантастика', 'Боевик',
                     'Вестерн', 'Военный', 'Детектив', 'Драма', 'Криминал', 'Мелодрама', 'Мюзикл', 'Фэнтэзи']

    max_index = max(list_of_index)
    index_for_finally_genre = list_of_index.index(max_index)
    return list_for_film[index_for_finally_genre]
