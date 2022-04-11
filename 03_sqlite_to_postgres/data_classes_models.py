from datetime import date
import uuid
from dataclasses import dataclass, field


@dataclass
class Genre:
    name: str
    description: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Filmwork:
    title: str
    descriptions: str
    creation_date: date
    rating: float = field(dafault=0.0)
    type: str
    genres
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
