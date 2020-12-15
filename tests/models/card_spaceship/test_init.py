from src.models.card_spaceship import CardSpaceship


def test_must_initialize_a_card_with_name_and_extra_info():
    name = 'Test'
    extra_info = 'This is a test extra info'
    size = 1
    speed = 1
    fire_power = 1
    maneuvering = 1
    force_factor = 1

    result = CardSpaceship(name, extra_info, size, speed, fire_power, maneuvering, force_factor)

    assert isinstance(result, CardSpaceship) is True
    assert name == result.name
    assert extra_info == result.extra_info
    assert size == result.size
    assert speed == result.speed
    assert fire_power == result.fire_power
    assert maneuvering == result.maneuvering
    assert force_factor == result.force_factor
