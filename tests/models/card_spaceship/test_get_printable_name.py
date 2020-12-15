from src.models.card_spaceship import CardSpaceship


def test_the_name_must_be_in_uppercase():
    spaceship = CardSpaceship('Nave1', 'extra', 1, 1, 1, 1, 1)

    assert spaceship.get_printable_name() == 'NAVE1'
