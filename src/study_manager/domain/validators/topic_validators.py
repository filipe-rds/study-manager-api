def validate_estimated_hours(estimated_hours: int) -> int:
    if type(estimated_hours) is not int:
        raise TypeError("Estimated hours must be an integer")

    if estimated_hours <= 0:
        raise ValueError("Estimated hours must be a positive integer")

    return estimated_hours


def validate_title(title: str) -> str:
    if type(title) is not str:
        raise TypeError("Title must be a string")

    if title.strip() == "":
        raise ValueError("Title is required")

    return title.strip()
