import datetime
import uuid
from dataclasses import dataclass, field

from dataclasses_mixin import (  # isort:skip
    UUIDMixin,
    TimeStampedMixin,
    CreatedMixin,
)


@dataclass
class Genre(UUIDMixin, TimeStampedMixin):
    name: str = field(default=None)
    description: str = field(default=None)


@dataclass
class Filmwork(UUIDMixin, TimeStampedMixin):
    title: str = field(default=None)
    descriptions: str = field(default=None)
    creation_date: datetime.date = field(default=None)
    type: str = field(default=None)
    rating: float = field(default=0)


@dataclass
class Person(UUIDMixin, TimeStampedMixin):
    fill_name: str = field(default=None)


@dataclass
class GenreFilmwork(UUIDMixin, CreatedMixin):
    genre: uuid.UUID = field(default=None)
    film_work: uuid.UUID = field(default=None)


@dataclass
class PersonFilmWork(UUIDMixin, CreatedMixin):
    person: uuid.UUID = field(default=None)
    film_work: uuid.UUID = field(default=None)
    role: str = field(default=None)
