from uuid import UUID

import pytest

from study_manager.domain.models.topic import Topic


class TestId:
    def test_should_generate_uuid_v7_when_id_is_not_provided(self) -> None:
        topic = Topic(title="Test Topic", estimated_hours=5)

        assert type(topic.id) is UUID
        assert topic.id.version == 7

    def test_should_reject_non_uuid_id(self) -> None:
        with pytest.raises(TypeError, match="Id must be a UUID"):
            Topic(
                title="Test Topic",
                estimated_hours=5,
                topic_id="INVALID ID",  # ty:ignore[invalid-argument-type]
            )

    def test_should_reject_invalid_uuid_version(self) -> None:
        topic_id = UUID("550e8400-e29b-41d4-a716-446655440000")
        with pytest.raises(ValueError, match="Id must be a UUIDv7"):
            Topic(title="Test Topic", estimated_hours=5, topic_id=topic_id)

    def test_should_preserve_given_valid_id(self) -> None:
        topic_id = UUID("01943f7e-7c2b-7c0e-9f7b-2d5fd7a7a9d1")
        topic = Topic(title="Test Topic", estimated_hours=4, topic_id=topic_id)

        assert type(topic.id) is UUID
        assert topic.id.version == 7
        assert topic.id == topic_id

    def test_should_generate_different_ids_when_id_is_not_provided(self) -> None:
        topic_python = Topic(title="Python", estimated_hours=5)
        topic_java = Topic(title="Java", estimated_hours=5)

        assert type(topic_python.id) is UUID
        assert type(topic_java.id) is UUID
        assert topic_python.id.version == 7
        assert topic_java.id.version == 7
        assert topic_python.id != topic_java.id


class TestTitle:
    def test_should_store_expected_value(self) -> None:
        topic = Topic(title="Test Topic", estimated_hours=5)

        assert topic.title == "Test Topic"

    def test_should_strip_title_surrounding_whitespace(self) -> None:
        topic = Topic(title="           Test Topic           ", estimated_hours=5)

        assert topic.title == "Test Topic"

    def test_should_reject_empty_title(self) -> None:
        with pytest.raises(ValueError, match="Title is required"):
            Topic(title="", estimated_hours=77)

    def test_should_reject_blank_title(self) -> None:
        with pytest.raises(ValueError, match="Title is required"):
            Topic(title="           ", estimated_hours=77)

    def test_should_reject_non_string_title(self) -> None:
        with pytest.raises(TypeError, match="Title must be a string"):
            Topic(
                title=True,  # ty:ignore[invalid-argument-type]
                estimated_hours=77,
            )


class TestEstimatedHours:
    def test_should_store_expected_value(self) -> None:
        topic = Topic(title="Test Topic", estimated_hours=5)

        assert topic.estimated_hours == 5

    def test_should_reject_non_integer_estimated_hours(self) -> None:
        with pytest.raises(TypeError, match="Estimated hours must be an integer"):
            Topic(
                title="Test Topic",
                estimated_hours=True,
            )

    def test_should_reject_negative_estimated_hours(self) -> None:
        with pytest.raises(
            ValueError, match="Estimated hours must be a positive integer"
        ):
            Topic(title="Test Topic", estimated_hours=-15)

    def test_should_reject_zero_estimated_hours(self) -> None:
        with pytest.raises(
            ValueError, match="Estimated hours must be a positive integer"
        ):
            Topic(title="Test Topic", estimated_hours=0)


class TestCompleted:
    def test_should_initialize_completed_as_false_by_default(self) -> None:
        topic = Topic(title="Test Topic", estimated_hours=5)

        assert topic.completed is False

    def test_should_mark_topic_as_completed(self) -> None:
        topic = Topic(title="Test Topic", estimated_hours=5)

        topic.mark_as_completed()

        assert topic.completed is True
