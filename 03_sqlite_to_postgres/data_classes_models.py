import datetime
import uuid
from dataclasses import dataclass, field


@dataclass
class Genre(object):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    name: str
    description: str
    created: datetime.datetime
    modified: datetime.datetime


@dataclass
class Filmwork(object):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    title: str
    descriptions: str
    creation_date: datetime.date
    rating: float = field(dafault=0)
    type: str
    created: datetime.datetime
    modified: datetime.datetime


@dataclass
class Person(object):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    fill_name: str
    created: datetime.datetime
    modified: datetime.datetime


@dataclass
class GenreFilmwork(object):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    genre: uuid.UUID
    film_work: uuid.UUID
    created: datetime.datetime


@dataclass
class PersonFilmWork(object):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    person: uuid.UUID
    film_work: uuid.UUID
    role: str
    created: datetime.datetime
