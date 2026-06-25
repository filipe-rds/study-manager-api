from uuid import UUID

from study_manager.domain.exceptions.topic_errors import (
    TopicAlreadyExistsError,
    TopicNotFoundError,
)
from study_manager.domain.models.topic import Topic
from study_manager.domain.validators.identity_validators import resolve_id
from study_manager.domain.validators.subject_validators import (
    resolve_topics,
    validate_name,
)


class Subject:
    def __init__(
        self,
        name: str,
        topics: list[Topic] | tuple[Topic, ...] | None = None,
        subject_id: UUID | None = None,
    ) -> None:
        self._id = resolve_id(subject_id)
        self._name = validate_name(name)
        self._topics = resolve_topics(topics)

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def completed(self) -> bool:
        if self.count_topics() == 0:
            return False

        if all(topic.completed for topic in self._topics.values()):
            return True

        return False

    def _has_topic(self, title: str) -> bool:
        if title not in self._topics:
            return False

        return True

    def add_topic(self, topic: Topic) -> None:
        if self._has_topic(topic.title):
            raise TopicAlreadyExistsError(topic.title)

        self._topics[topic.title] = topic

    def get_topic_by_title(self, title: str) -> Topic:
        if not self._has_topic(title):
            raise TopicNotFoundError(title)

        return self._topics[title]

    def count_topics(self) -> int:
        return len(self._topics)

    def list_topics(self) -> tuple[Topic, ...]:
        return tuple(self._topics.values())
