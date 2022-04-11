"""Объявление моделей приложения фильмы."""
import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

CONSTRAINT_RATING_MIN = 0
CONSTRAINT_RATING_MAX = 10.0

template_tablename = 'content\".\"{tablename}'


class UUIDMixin(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta(object):
        abstract = True


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(
        verbose_name=_('created'),
        auto_now_add=True,
        null=True,
    )
    modified = models.DateTimeField(
        verbose_name=_('modified'),
        auto_now=True,
        null=True,
    )

    class Meta(object):
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.TextField(
        verbose_name=_('name'),
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
        null=True,
    )

    class Meta(object):
        db_table = template_tablename.format(tablename='genre')
        verbose_name = _('genre')
        verbose_name_plural = _('genres')
        constraints = [
            models.UniqueConstraint(
                name='uneque_genre_name_idx',
                fields=['name'],
            ),
        ]
        indexes = [
            models.Index(fields=['name'], name='genre_name_idx'),
        ]

    def __str__(self):
        return self.name


class Filmwork(UUIDMixin, TimeStampedMixin):
    class Type(models.TextChoices):
        MOVIE = _('movie')
        TV_SHOW = _('tv_show')

    title = models.TextField(
        verbose_name=_('title'),
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
        null=True,
    )
    creation_date = models.DateField(
        verbose_name=_('creation date'),
        blank=True,
        null=True,
    )
    rating = models.FloatField(
        verbose_name=_('rating'),
        blank=True,
        null=True,
        validators=[
            MinValueValidator(CONSTRAINT_RATING_MIN),
            MaxValueValidator(CONSTRAINT_RATING_MAX),
        ],
    )
    type = models.TextField(
        verbose_name=_('type'),
        choices=Type.choices,
        default=Type.MOVIE,
    )
    genres = models.ManyToManyField(
        verbose_name=_('genres'),
        to='Genre',
        through='GenreFilmwork',
    )
    persons = models.ManyToManyField(
        verbose_name=_('persons'),
        to='Person',
        through='PersonFilmWork',
    )

    class Meta(object):
        db_table = template_tablename.format(tablename='film_work')
        verbose_name = _('movie')
        verbose_name_plural = _('movies')
        indexes = [
            models.Index(
                fields=['creation_date'],
                name='film_work_creation_date_idx',
            ),
            models.Index(
                fields=['title'],
                name='filmwork_title_idx',
            ),
            models.Index(
                fields=['type'],
                name='filmwork_type_idx',
            ),
        ]

    def __str__(self):
        return self.title


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.TextField(
        verbose_name=_('full name'),
    )

    class Meta(object):
        db_table = template_tablename.format(tablename='person')
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __str__(self):
        return self.full_name


class GenreFilmwork(UUIDMixin):
    genre = models.ForeignKey(
        to='Genre',
        verbose_name=_('genre'),
        on_delete=models.CASCADE,
    )
    film_work = models.ForeignKey(
        to='Filmwork',
        verbose_name=_('filmwork'),
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        verbose_name=_('created'),
        auto_now_add=True,
    )

    class Meta(object):
        db_table = template_tablename.format(tablename='genre_film_work')
        verbose_name = _('genre filmwork')
        verbose_name_plural = _('genres filmwork')
        constraints = [
            models.UniqueConstraint(
                name='unique_genre_film_work',
                fields=('genre_id', 'film_work_id'),
            ),
        ]

    def __str__(self):
        return 'Genre: {genre} in filmwork: {filmwork}'.format(
            genre=self.genre,
            filmwork=self.film_work,
        )


class PersonFilmWork(UUIDMixin):
    class Role(models.TextChoices):
        ACTOR = _('actor')
        DIRECTOR = _('director')
        PRODUCER = _('producer')

    person = models.ForeignKey(
        verbose_name=_('person'),
        to='Person',
        on_delete=models.CASCADE,
    )
    film_work = models.ForeignKey(
        verbose_name=_('filmwork'),
        to='Filmwork',
        on_delete=models.CASCADE,
    )
    role = models.TextField(
        verbose_name=_('role'),
        choices=Role.choices,
        default=Role.ACTOR,
    )
    created = models.DateTimeField(
        verbose_name=_('created'),
        auto_now_add=True,
    )

    class Meta(object):
        db_table = template_tablename.format(tablename='person_film_work')
        verbose_name = _('person filmwork')
        verbose_name_plural = _('persons filmwork')
        constraints = [
            models.UniqueConstraint(
                fields=('film_work_id', 'person_id', 'role'),
                name='unique_film_work_person_role_idx',
            ),
        ]
        indexes = [
            models.Index(
                fields=['film_work_id', 'person_id'],
                name='film_work_person_idx',
            ),
        ]

    def __str__(self):
        return 'Person: {person} in filmwork: {filmwork}'.format(
            person=self.person,
            filmwork=self.film_work,
        )
