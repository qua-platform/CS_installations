import datetime
from enum import Enum
from dataclasses import dataclass


class InsertDirection(Enum):
    start = 1
    end = 2


@dataclass(frozen=True)
class PendingJobData:
    job_id: str
    position_in_queue: int
    time_added: datetime.datetime
    added_by: str
