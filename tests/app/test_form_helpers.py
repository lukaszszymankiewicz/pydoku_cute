from app.form_helpers import validate_difficult
from app.src.enums import Difficult


def test_validate_difficult_returns_default_difficult_if_not_dict_is_inputted():
    # GIVEN
    wrong_form = ["a"]
    expected_difficult = Difficult.default

    # WHEN
    difficult = validate_difficult(wrong_form)

    # THEN
    assert difficult == expected_difficult


def test_validate_difficult_returns_default_difficult_if_form_has_wrong_keys():
    # GIVEN
    wrong_form = {"not_difficult": "easy"}
    expected_difficult = Difficult.default

    # WHEN
    difficult = validate_difficult(wrong_form)

    # THEN
    assert difficult == expected_difficult


def test_validate_difficult_returns_default_difficult_form_too_many_keys_or_values():
    # GIVEN
    wrong_form = {"difficult": "easy", "another_key": "another_value"}
    expected_difficult = Difficult.default

    # WHEN
    difficult = validate_difficult(wrong_form)

    # THEN
    assert difficult == expected_difficult


def test_validate_difficult_returns_default_difficult_form_if_not_proper_difficult_is_provided():
    # GIVEN
    wrong_form = {"difficult": "not_so_easy"}
    expected_difficult = Difficult.default

    # WHEN
    difficult = validate_difficult(wrong_form)

    # THEN
    assert difficult == expected_difficult
