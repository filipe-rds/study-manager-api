from study_manager.domain.validators.user_validators import (
    validate_name,
    validate_email,
)
from study_manager.domain.validators.identity_validators import resolve_id
from uuid import UUID


class User:
    def __init__(self, name: str, email: str, user_id: UUID | None = None) -> None:
        self._id = resolve_id(user_id)
        self._name = validate_name(name)
        self._email = validate_email(email)

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email
