from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Vacancy:
    title: str
    company: str
    location: str
    description: str
    url: str
    technologies: List[str] = field(default_factory=list)
    salary: Optional[float] = None


def __repr__(self):
        return f"<Job {self.title} at {self.company}>"