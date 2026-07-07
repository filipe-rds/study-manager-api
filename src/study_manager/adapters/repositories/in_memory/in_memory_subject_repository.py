from uuid import UUID

from study_manager.domain.models.subject import Subject
from study_manager.ports.repositories.subject_repository import SubjectRepository


class InMemorySubjectRepository(SubjectRepository):
    def __init__(self) -> None:
        self._subjects: dict[UUID, Subject] = {}

    def save(self, subject: Subject) -> None:
        self._subjects[subject.id] = subject

    def find_by_id(self, subject_id: UUID) -> Subject | None:
        return self._subjects.get(subject_id)

    def list_all(self) -> tuple[Subject, ...]:
        return tuple(self._subjects.values())

    def remove(self, subject_id: UUID) -> None:
        self._subjects.pop(subject_id)
