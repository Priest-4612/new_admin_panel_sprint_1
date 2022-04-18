import datetime
import uuid
from dataclasses import dataclass, field


@dataclass
class UUIDMixin(object):
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class CreatedMixin(object):
    created: datetime.datetime = field(default=None)


@dataclass
class TimeStampedMixin(CreatedMixin):
    modified: datetime.datetime = field(default=None)
