from study_manager.domain.exceptions.base import StudyManagerError


class SubjectNotFoundError(StudyManagerError):
    def __init__(self, name: str) -> None:
        super().__init__(f"No such subject with name '{name}'")


class SubjectAlreadyExistsError(StudyManagerError):
    def __init__(self, name: str) -> None:
        super().__init__(f"Subject with name '{name}' already exists")
