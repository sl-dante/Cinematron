# Файл с расчетами ЭС

def genre_calculate(answer):
    _drama = 0.1
    _comedy = 0.1
    _melodrama = 0.1
    _scary = 0.1
    _detective = 0.1
    _war = 0.1
    _cartoon = 0.1
    _thriller = 0.1
    _action = 0.1
    _crime = 0.1
    _music = 0.1
    _fantasy = 0.1
    _fantastic = 0.1

    # Ответ на первый вопрос
    answer[0].replace(' ', '')
    if answer[0].lower() == 'да':
        _drama *= 0.8
        _comedy *= 0.2
        _melodrama *= 0.5
        _scary *= 0.1
        _detective *= 0.5
        _war *= 0.5
        _fantastic *= 0.2
    elif answer[0].lower() == 'нет':
        _drama *= 0.1
        _comedy *= 0.7
        _melodrama *= 0.3
        _scary *= 0.5
        _detective *= 0.2
        _war *= 0.3
        _action *= 0.5
        _cartoon = 0.3
    else:
        'Некоректный ответ'

    # Ответ на второй вопрос
    answer[1].replace(' ', '')
    if answer[1].lower() == 'да':
        _drama *= 0.4
        _comedy *= 0.8
        _melodrama *= 0.2
        _scary *= 0.1
        _detective *= 0.2
        _war *= 0.1
        _cartoon = 0.5
        _music = 0.5
    elif answer[1].lower() == 'нет':
        _drama *= 0.4
        _comedy *= 0.2
        _melodrama *= 0.4
        _scary *= 0.7
        _detective *= 0.6
        _war *= 0.7

    else:
        'Некоректный ответ'

    answer[2].replace(' ', '')
    if answer[2].lower() == 'да':
        _drama *= 0.6
        _comedy *= 0.5
        _melodrama *= 0.4
        _scary *= 0.1
        _detective *= 0.3
        _war *= 0.3
    elif answer[2].lower() == 'нет':
        _drama *= 0.2
        _comedy *= 0.3
        _melodrama *= 0.3
        _scary *= 0.4
        _detective *= 0.3
        _war *= 0.3
    else:
        'Некоректный ответ'

    answer[3].replace(' ', '')
    if answer[3].lower() == 'да':
        _drama *= 0.1
        _comedy *= 0.1
        _melodrama *= 0.2
        _scary *= 0.9
        _detective *= 0.6
        _war *= 0.6
    elif answer[3].lower() == 'нет':
        _drama *= 0.4
        _comedy *= 0.4
        _melodrama *= 0.5
        _scary *= 0.1
        _detective *= 0.4
        _war *= 0.4
    else:
        'Некоректный ответ'

    answer[4].replace(' ', '')
    if answer[4].lower() == 'да':
        _drama *= 0.6
        _comedy *= 0.1
        _melodrama *= 0.2
        _scary *= 0.1
        _detective *= 0.9
        _war *= 0.3
    elif answer[4].lower() == 'нет':
        _drama *= 0.4
        _comedy *= 0.5
        _melodrama *= 0.5
        _scary *= 0.4
        _detective *= 0.1
        _war *= 0.7
    else:
        'Некоректный ответ'

    answer[5].replace(' ', '')
    if answer[5].lower() == 'да':
        _drama *= 0.7
        _comedy *= 0.3
        _melodrama *= 0.2
        _scary *= 0.6
        _detective *= 0.7
        _war *= 0.9
    elif answer[5].lower() == 'нет':
        _drama *= 0.3
        _comedy *= 0.6
        _melodrama *= 0.8
        _scary *= 0.4
        _detective *= 0.3
        _war *= 0.1
    else:
        'Некоректный ответ'

    '''Комедия
        Мультфильм
        Триллер
        Ужасы
        Фантастика
        Аниме
        Боевик
        Вестерн
        Военный
        Детектив
        Драма
        Криминал
        Мелодрама
        Мюзикл
        Фэнтези'''

    _list_of_index = [_drama, _comedy, _melodrama, _scary, _detective, _war]
    list_for_film = ['Драма', 'Комедия', 'Мелодрама', 'Ужасы', 'Детектив', 'Военный']

    a = max(_list_of_index)
    _index = _list_of_index.index(a)
    return list_for_film[_index]
