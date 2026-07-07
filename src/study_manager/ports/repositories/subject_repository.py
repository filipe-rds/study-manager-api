from uuid import UUID
from typing import Protocol

from study_manager.domain.models.subject import Subject


class SubjectRepository(Protocol):
    def save(self, subject: Subject) -> None: ...

    def find_by_id(self, subject_id: UUID) -> Subject | None: ...

    def list_all(self) -> tuple[Subject, ...]: ...

    def remove(self, subject_id: UUID) -> None: ...
