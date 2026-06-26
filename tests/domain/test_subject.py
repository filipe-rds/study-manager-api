from uuid import UUID

import pytest

from study_manager.domain.exceptions.topic_errors import (
    TopicAlreadyExistsError,
    TopicNotFoundError,
)
from study_manager.domain.models.subject import Subject
from study_manager.domain.models.topic import Topic


class TestId:
    def test_should_generate_uuid_v7_when_id_is_not_provided(self) -> None:
        subject = Subject(name="Test Subject")

        assert type(subject.id) is UUID
        assert subject.id.version == 7

    def test_should_reject_non_uuid_id(self) -> None:
        with pytest.raises(TypeError, match="Id must be a UUID"):
            Subject(
                name="Test Subject",
                subject_id="INVALID ID",  # ty:ignore[invalid-argument-type]
            )

    def test_should_reject_invalid_uuid_version(self) -> None:
        subject_id = UUID("550e8400-e29b-41d4-a716-446655440000")
        with pytest.raises(ValueError, match="Id must be a UUIDv7"):
            Subject(name="Test Subject", subject_id=subject_id)

    def test_should_preserve_given_valid_id(self) -> None:
        subject_id = UUID("01943f7e-7c2b-7c0e-9f7b-2d5fd7a7a9d1")
        subject = Subject(name="Test Subject", subject_id=subject_id)

        assert type(subject.id) is UUID
        assert subject.id.version == 7
        assert subject.id == subject_id

    def test_should_generate_different_ids_when_id_is_not_provided(self) -> None:
        subject_oop = Subject(name="OOP")
        subject_database = Subject(name="DATABASE")

        assert type(subject_oop.id) is UUID
        assert type(subject_database.id) is UUID
        assert subject_oop.id.version == 7
        assert subject_database.id.version == 7
        assert subject_oop.id != subject_database.id


class TestName:
    def test_should_store_expected_value(self) -> None:
        subject = Subject(name="Test Subject")

        assert subject.name == "Test Subject"

    def test_should_strip_name_surrounding_whitespace(self) -> None:
        subject = Subject(name="        Test Subject        ")

        assert subject.name == "Test Subject"

    def test_should_reject_empty_name(self) -> None:
        with pytest.raises(ValueError, match="Name is required"):
            Subject(name="")

    def test_should_reject_blank_name(self) -> None:
        with pytest.raises(ValueError, match="Name is required"):
            Subject(name="                       ")

    def test_should_reject_non_string_name(self) -> None:
        with pytest.raises(TypeError, match="Name must be a string"):
            Subject(name=123)  # ty:ignore[invalid-argument-type]


class TestTopics:
    def test_should_initialize_with_empty_topics(self) -> None:
        subject = Subject(name="Test Subject")

        assert subject.count_topics() == 0
        assert subject.completed is False

    @pytest.mark.parametrize("collection_type", [list, tuple])
    def test_should_initialize_with_valid_topics(
        self, collection_type: type[list[Topic]] | type[tuple[Topic, ...]]
    ) -> None:
        topic_oop = Topic(title="POO", estimated_hours=5)
        topic_database = Topic(title="DB", estimated_hours=5)

        topics = collection_type([topic_oop, topic_database])

        subject = Subject(name="Test Subject", topics=topics)

        assert subject.count_topics() == 2
        assert {topic.title for topic in subject.list_topics()} == {"POO", "DB"}

    @pytest.mark.parametrize("collection_type", [list, tuple])
    def test_should_reject_initialize_duplicate_topics(
        self, collection_type: type[list[Topic]] | type[tuple[Topic, ...]]
    ) -> None:
        topic_database = Topic(title="DB", estimated_hours=5)
        topic_database_more_hours = Topic(title="DB", estimated_hours=80)

        topics = collection_type([topic_database, topic_database_more_hours])

        with pytest.raises(
            TopicAlreadyExistsError,
            match="Topic with title 'DB' already exists",
        ):
            Subject(name="Test Subject", topics=topics)

    @pytest.mark.parametrize(
        "invalid_topics",
        [
            "invalid",
            {"POO": Topic(title="POO", estimated_hours=5)},
            {"POO"},
            123,
        ],
    )
    def test_should_reject_invalid_topics_collection_type(
        self, invalid_topics: object
    ) -> None:
        with pytest.raises(TypeError, match="Topics must be a list or tuple"):
            Subject(name="Test Subject", topics=invalid_topics)  # ty:ignore[invalid-argument-type]

    @pytest.mark.parametrize(
        "invalid_topics",
        [
            ("not", "topics"),
            (True, False),
            (123, 456),
            ["not", "topics"],
            [True, False],
            [123, 456],
        ],
    )
    def test_should_reject_topics_collection_with_invalid_items(
        self, invalid_topics: object
    ) -> None:
        with pytest.raises(TypeError, match="Topics must contain only Topic instances"):
            Subject(name="Test Subject", topics=invalid_topics)  # ty:ignore[invalid-argument-type]

    def test_should_add_valid_topics(self) -> None:
        subject = Subject(name="Test Subject")

        topic_oop = Topic(title="POO", estimated_hours=5)
        topic_database = Topic(title="DB", estimated_hours=5)

        subject.add_topic(topic_oop)
        subject.add_topic(topic_database)

        assert subject.count_topics() == 2

    def test_should_list_all_topics(self) -> None:
        subject = Subject(name="Test Subject")

        topic_oop = Topic(title="POO", estimated_hours=5)
        topic_database = Topic(title="DB", estimated_hours=5)

        subject.add_topic(topic_oop)
        subject.add_topic(topic_database)

        topics = subject.list_topics()

        assert {topic.title for topic in topics} == {"POO", "DB"}
        assert len(topics) == 2
        assert subject.count_topics() == 2

    def test_should_not_expose_mutable_internal_collection(self):
        subject = Subject(name="Test Subject")

        topic_oop = Topic(title="POO", estimated_hours=5)
        topic_database = Topic(title="DB", estimated_hours=5)

        subject.add_topic(topic_oop)
        subject.add_topic(topic_database)

        topics = subject.list_topics()

        assert type(topics) is tuple
        assert len(topics) == 2

    def test_should_reject_duplicate_topics(self) -> None:
        subject = Subject(name="Test Subject")

        topic_database = Topic(title="DB", estimated_hours=5)
        topic_database_more_hours = Topic(title="DB", estimated_hours=80)

        subject.add_topic(topic_database)

        with pytest.raises(
            TopicAlreadyExistsError,
            match="Topic with title 'DB' already exists",
        ):
            subject.add_topic(topic_database_more_hours)

    def test_should_get_topic_by_title(self) -> None:
        subject = Subject(name="Test Subject")

        topic_oop = Topic(title="POO", estimated_hours=5)
        topic_database = Topic(title="DB", estimated_hours=5)

        subject.add_topic(topic_oop)
        subject.add_topic(topic_database)

        topic_found = subject.get_topic_by_title("DB")

        assert topic_found.id == topic_database.id

    def test_should_reject_search_topic_for_non_existing_title(self) -> None:
        subject = Subject(name="Test Subject")

        topic_oop = Topic(title="POO", estimated_hours=5)
        topic_database = Topic(title="DB", estimated_hours=5)

        subject.add_topic(topic_oop)
        subject.add_topic(topic_database)

        with pytest.raises(
            TopicNotFoundError,
            match="No such topic with title 'NON_EXISTING_TOPIC'",
        ):
            subject.get_topic_by_title("NON_EXISTING_TOPIC")


class TestCompleted:
    def test_should_return_true_when_all_topics_are_completed(self) -> None:
        subject = Subject(name="Test Subject")

        topic_oop = Topic(title="POO", estimated_hours=5)
        topic_database = Topic(title="DB", estimated_hours=5)

        subject.add_topic(topic_oop)
        subject.add_topic(topic_database)

        topic_oop.mark_as_completed()
        topic_database.mark_as_completed()

        assert subject.completed is True

    def test_should_return_false_when_are_topics_not_completed(self) -> None:
        subject = Subject(name="Test Subject")

        topic_oop = Topic(title="POO", estimated_hours=5)
        topic_database = Topic(title="DB", estimated_hours=5)

        subject.add_topic(topic_oop)
        subject.add_topic(topic_database)

        topic_oop.mark_as_completed()

        assert subject.completed is False

    def test_should_return_false_when_subject_has_no_topics(self) -> None:
        subject = Subject(name="Test Subject")

        assert subject.completed is False
