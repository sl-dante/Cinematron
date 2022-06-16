# Класс для удобной структуризации информации
class Film:
    def __init__(self, _name, _description, _photo, _href, _main_actor, _year, _country, _genre, _directed):
        self.name = _name
        self.description = _description
        self.photo = _photo
        self.href = _href
        self.main_actor = _main_actor
        self.year = _year
        self.country = _country
        self.genre = _genre
        self.directed = _directed
