import pytest

from study_manager.domain.models.topic import Topic


class TestTitle:

    def test_should_store_expected_value(self) -> None:
        topic = Topic("Test Topic", 5)

        assert topic.title == "Test Topic"

    def test_should_strip_title_surrounding_whitespace(self) -> None:
        topic = Topic("           Test Topic           ", 5)

        assert topic.title == "Test Topic"

    def test_should_reject_empty_title(self) -> None:
        with pytest.raises(ValueError, match="Title is required"):
            Topic("", 77)

    def test_should_reject_blank_title(self) -> None:
        with pytest.raises(ValueError, match="Title is required"):
            Topic("           ", 77)

    def test_should_reject_non_string_title(self) -> None:
        with pytest.raises(TypeError, match="Title must be a string"):
            Topic(True, 77)  # ty:ignore[invalid-argument-type]


class TestEstimatedHours:

    def test_should_store_expected_value(self) -> None:
        topic = Topic("Test Topic", 5)

        assert topic.estimated_hours == 5

    def test_should_reject_non_integer_estimated_hours(self) -> None:
        with pytest.raises(TypeError, match="Estimated hours must be an integer"):
            Topic("Test Topic", True)

    def test_should_reject_negative_estimated_hours(self) -> None:
        with pytest.raises(ValueError, match="Estimated hours must be a positive integer"):
            Topic("Test Topic", -15)

    def test_should_reject_zero_estimated_hours(self) -> None:
        with pytest.raises(ValueError, match="Estimated hours must be a positive integer"):
            Topic("Test Topic", 0)


class TestCompleted:

    def test_should_initialize_completed_as_false_by_default(self) -> None:
        topic = Topic("Test Topic", 5)

        assert topic.completed is False
