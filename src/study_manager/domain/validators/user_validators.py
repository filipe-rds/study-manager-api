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
