from .src.enums import Difficult

DIFFICULT_KEY = "difficult"
DIFFICULT_PREFIX = "difficult="


def get_difficult_from_request(response) -> str:
    raw_string = response[DIFFICULT_KEY].replace(DIFFICULT_PREFIX, "")
    difficult = validate_difficult(raw_string)

    return difficult


def validate_difficult(raw_string: str) -> str:
    """Validate raw string from html response."""

    if raw_string not in Difficult.legal_difficulties:
        return Difficult.default

    return raw_string
