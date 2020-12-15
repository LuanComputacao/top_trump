import pytest

from src.models.card import Card


def test_must_initialize_a_card_with_name_and_extra_info():
    name = 'Test'
    extra_info = 'This is a test extra info'

    result = Card(name, extra_info)

    assert isinstance(result, Card) is True
    assert name == result.name
    assert extra_info == result.extra_info


def test_must_initialize_a_card_with_name_only():
    name = 'Test'

    result = Card(name)

    assert isinstance(result, Card) is True
    assert name == result.name, 'Must be possible to initialize without an extra info'


def test_must_not_initialize_a_card_with_type_number_in_the_name():
    with pytest.raises(TypeError):
        Card(3.1415)


def test_must_initialize_a_card_with_numbers_in_the_name_with_str_type():
    name = str(3.1415)
    result = Card(name)

    assert isinstance(result, Card) is True
    assert name == result.name, 'Must be possible to initialize a card with number in the name'
