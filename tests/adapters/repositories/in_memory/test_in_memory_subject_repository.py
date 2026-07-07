from uuid import UUID

from study_manager.domain.models.subject import Subject
import pytest

from study_manager.adapters.repositories.in_memory.in_memory_subject_repository import (
    InMemorySubjectRepository,
)


@pytest.fixture
def repository() -> InMemorySubjectRepository:
    return InMemorySubjectRepository()


class TestSave:
    def test_should_save_valid_subject(
        self, repository: InMemorySubjectRepository
    ) -> None:
        subject = Subject(name="Test")
        repository.save(subject)
        assert repository.find_by_id(subject.id) == subject


class TestFindById:
    def test_should_return_when_subject_exists(
        self, repository: InMemorySubjectRepository
    ) -> None:
        subject = Subject(name="Test")

        repository.save(subject)

        assert repository.find_by_id(subject.id) == subject

    def test_should_return_none_when_subject_does_not_exist(
        self, repository: InMemorySubjectRepository
    ) -> None:
        subject_id = UUID("01943f7e-7c2b-7c0e-9f7b-2d5fd7a7a9d1")

        assert repository.find_by_id(subject_id) is None


class TestListAll:
    def test_should_return_empty_list_when_repository_is_empty(
        self, repository: InMemorySubjectRepository
    ) -> None:
        subject_list = repository.list_all()

        assert len(subject_list) == 0
        assert type(subject_list) is tuple

    def test_should_return_list_of_subjects(
        self, repository: InMemorySubjectRepository
    ) -> None:
        subject_oop = Subject(name="OOP")
        subject_database = Subject(name="DATABASE")

        repository.save(subject_oop)
        repository.save(subject_database)

        subject_list = repository.list_all()

        assert len(subject_list) == 2
        assert type(subject_list) is tuple


class TestRemove:
    def test_should_remove_subject_from_repository(
        self, repository: InMemorySubjectRepository
    ) -> None:
        subject_oop = Subject(name="OOP")
        subject_database = Subject(name="DATABASE")

        repository.save(subject_oop)
        repository.save(subject_database)

        repository.remove(subject_oop.id)

        subject_list = repository.list_all()

        assert repository.find_by_id(subject_oop.id) is None
        assert len(subject_list) == 1
        assert type(subject_list) is tuple
