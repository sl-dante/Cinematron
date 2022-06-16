from django.db import models


# Класс с жанрами фильмов
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Класс похожих жанров
class SimilarGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre')
    sim_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='sim_genre')


# Класс пользователя
class User(models.Model):
    vk_id = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    chosen_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


# Класс в БД, где будут храниться фильмы
class Film(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.TextField()
    href = models.TextField()
    main_actor = models.CharField(max_length=50)
    directed = models.CharField(max_length=50)
    year = models.IntegerField()
    country = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


# Класс для локаторов, по которым будет парситься информация с кинотеатров
class ParserPosterProperty(models.Model):
    name_of_cinema = models.CharField(max_length=100)
    list_of_films_arg_1 = models.CharField(max_length=100)
    list_of_films_arg_2 = models.CharField(max_length=100)
    name_of_film_arg_1 = models.CharField(max_length=100)
    name_of_film_arg_2 = models.CharField(max_length=100)
    data_of_film_arg_1 = models.CharField(max_length=100)
    data_of_film_arg_2 = models.CharField(max_length=100)
    href_of_film_arg_1 = models.CharField(max_length=100)
    photo_of_film_arg_1 = models.CharField(max_length=100)
    photo_of_film_arg_2 = models.CharField(max_length=100)
    description_of_film_arg_1 = models.CharField(max_length=100)
    description_of_film_arg_2 = models.CharField(max_length=100)
    description_of_film_arg_3 = models.CharField(max_length=100)
