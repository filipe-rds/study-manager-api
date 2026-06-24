from uuid import UUID, uuid7


def resolve_id(identifier: UUID | None = None) -> UUID:
    if identifier is None:
        return uuid7()

    if type(identifier) is not UUID:
        raise TypeError("Id must be a UUID")

    if identifier.version != 7:
        raise ValueError("Id must be a UUIDv7")

    return identifier
