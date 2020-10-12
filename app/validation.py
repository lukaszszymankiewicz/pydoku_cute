from .src.enums import Difficult


def validate_difficult(form: dict) -> str:
    """Validated difficult form and return chosen option."""

    if not isinstance(form, dict):
        return Difficult.default

    if list(form.keys()) != ["difficult"]:
        return Difficult.default

    if len(list(form.values())) != 1:
        return Difficult.default

    if list(form.values())[0] not in Difficult.legal_difficulties:
        return Difficult.default

    return list(form.values())[0]
