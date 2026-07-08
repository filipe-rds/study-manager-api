from study_manager.domain.exceptions.subject_errors import SubjectAlreadyExistsError
from study_manager.domain.models.subject import Subject
import re


def validate_name(name: str) -> str:
    if type(name) is not str:
        raise TypeError("Name must be a string")

    if name.strip() == "":
        raise ValueError("Name is required")

    return name.strip()


def validate_email(email: str) -> str:
    if type(email) is not str:
        raise TypeError("Email must be a string")

    if email.strip() == "":
        raise ValueError("Email is required")

    if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
        raise ValueError("Email must be a valid email address")

    return email.strip()


def resolve_subjects(
    subjects: list[Subject] | tuple[Subject, ...] | None,
) -> dict[str, Subject]:

    if subjects is None:
        return {}

    if type(subjects) is not list and type(subjects) is not tuple:
        raise TypeError("Subjects must be a list or tuple")

    subjects_dict = {}

    for subject in subjects:
        if type(subject) is not Subject:
            raise TypeError("Subjects must contains only Subject instances")

        if subject.name in subjects_dict:
            raise SubjectAlreadyExistsError(subject.name)

        subjects_dict[subject.name] = subject

    return subjects_dict
