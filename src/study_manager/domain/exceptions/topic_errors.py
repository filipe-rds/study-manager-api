from study_manager.domain.exceptions.base import StudyManagerError


class TopicNotFound(StudyManagerError):
    def __init__(self, title: str) -> None:
        super().__init__(f"No such topic with title '{title}'")


class TopicAlreadyExists(StudyManagerError):
    def __init__(self, title: str) -> None:
        super().__init__(f"Topic with title '{title}' already exists")
