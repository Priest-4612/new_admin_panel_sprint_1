import datetime
import uuid
from dataclasses import dataclass, field


@dataclass
class Genre:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    name: str
    description: str
    created: datetime.datetime
    modified: datetime.datetime


@dataclass
class Filmwork:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    title: str
    descriptions: str
    creation_date: datetime.date
    rating: float = field(dafault=0.0)
    type: str


@dataclass
