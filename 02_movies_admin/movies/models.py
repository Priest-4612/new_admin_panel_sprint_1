"""Объявление моделей приложения фильмы."""
import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

CONSTRAINT_LENGTH = 255
CONSTRAINT_RATING_MIN = 0
CONSTRAINT_RATING_MAX = 100

template_tablename = 'content\".\"{tablename}'


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(object):
        abstract = True


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    class Meta(object):
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField('name', max_length=CONSTRAINT_LENGTH)
    description = models.TextField('description', blank=True)

    class Meta(object):
        db_table = template_tablename.format(tablename='genre')
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        constraints = [
            models.UniqueConstraint(
                name='uneque_genre_name',
                fields=['name'],
            ),
        ]

    def __str__(self):
        return self.name


class Filmwork(UUIDMixin, TimeStampedMixin):
    class Type(models.TextChoices):
        MOVIE = 'movie'
        TV_SHOW = 'tv_show'

    title = models.CharField(
        'title', max_length=CONSTRAINT_LENGTH, db_index=True,
    )
    description = models.TextField('description', blank=True, null=True)
    creation_date = models.DateField('creation date', db_index=True, null=True)
    rating = models.PositiveIntegerField(
        'rating',
        blank=True,
        null=True,
        validators=[
            MinValueValidator(CONSTRAINT_RATING_MIN),
            MaxValueValidator(CONSTRAINT_RATING_MAX),
        ],
    )
    type = models.CharField(
        'name',
        max_length=CONSTRAINT_LENGTH,
        choices=Type.choices,
        default=Type.MOVIE,
        db_index=True,
    )
    genres = models.ManyToManyField('Genre', through='GenreFilmwork')
    persons = models.ManyToManyField('Person', through='PersonFilmWork')

    class Meta(object):
        db_table = template_tablename.format(tablename='film_work')
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(
        'full name',
        max_length=CONSTRAINT_LENGTH,
    )

    class Meta(object):
        db_table = template_tablename.format(tablename='person')
        verbose_name = 'Персоны'
        verbose_name_plural = 'Персоны'

    def __str__(self):
        return self.full_name


class GenreFilmwork(UUIDMixin):
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        db_table = template_tablename.format(tablename='genre_film_work')
        verbose_name = 'Жанр в фильме'
        verbose_name_plural = 'Жанры в фильме'
        constraints = [
            models.UniqueConstraint(
                name='unique_genre_film_work',
                fields=('genre_id', 'film_work_id'),
            ),
        ]


class PersonFilmWork(UUIDMixin):
    class Role(models.TextChoices):
        ACTOR = 'actor'
        DIRECTOR = 'director'
        PRODUCER = 'producer'

    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    role = models.CharField(
        'role',
        max_length=CONSTRAINT_LENGTH,
        choices=Role.choices,
        default=Role.ACTOR,
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        db_table = template_tablename.format(tablename='person_film_work')
        verbose_name = 'Персоны в фильме'
        verbose_name_plural = 'Персоны в фильме'
        constraints = [
            models.UniqueConstraint(
                name='unique_film_work_person',
                fields=('film_work_id', 'person_id'),
            ),
        ]
