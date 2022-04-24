import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Genre(object):
    name: str
    description: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(frozen=True)
class Filmwork(object):
    title: str
    description: str
    creation_date: str
    type: str
    rating: float = field(default=0)
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(frozen=True)
class Person(object):
    full_name: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(frozen=True)
class GenreFilmwork(object):
    genre_id: uuid.UUID
    film_work_id: uuid.UUID
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(frozen=True)
class PersonFilmWork(object):
    person_id: uuid.UUID
    film_work_id: uuid.UUID
    role: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
