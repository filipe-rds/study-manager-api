from study_manager.domain.exceptions.base import StudyManagerError


class UserNotFoundError(StudyManagerError):
    def __init__(self, email: str) -> None:
        super().__init__(f"No such user with email '{email}'")


class UserAlreadyExistsError(StudyManagerError):
    def __init__(self, email: str) -> None:
        super().__init__(f"User with email '{email}' already exists")
