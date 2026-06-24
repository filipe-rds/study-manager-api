from uuid import UUID

from study_manager.domain.validators.identity_validators import resolve_id
from study_manager.domain.validators.topic_validators import (
    validate_estimated_hours,
    validate_title,
)


class Topic:
    def __init__(
        self, title: str, estimated_hours: int, topic_id: UUID | None = None
    ) -> None:
        self._id = resolve_id(topic_id)
        self._title = validate_title(title)
        self._estimated_hours = validate_estimated_hours(estimated_hours)
        self._completed = False

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def estimated_hours(self) -> int:
        return self._estimated_hours

    @property
    def completed(self) -> bool:
        return self._completed
