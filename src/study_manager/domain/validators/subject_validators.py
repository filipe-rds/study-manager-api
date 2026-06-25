from study_manager.domain.exceptions.topic_errors import TopicAlreadyExists
from study_manager.domain.models.topic import Topic


def validate_name(name: str) -> str:
    if type(name) is not str:
        raise TypeError("Name must be a string")

    if name.strip() == "":
        raise ValueError("Name is required")

    return name.strip()


def resolve_topics(topics: list[Topic] | tuple[Topic, ...] | None) -> dict[str, Topic]:
    if topics is None:
        return {}

    if type(topics) is not list and type(topics) is not tuple:
        raise TypeError("Topics must be a list or tuple")

    topics_dict = {}

    for topic in topics:
        if type(topic) is not Topic:
            raise TypeError("Topics must contain only Topic instances")

        if topic.title in topics_dict:
            raise TopicAlreadyExists(topic.title)

        topics_dict[topic.title] = topic

    return topics_dict
