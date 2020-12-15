from src.models.card import Card


class CardSpaceship(Card):
    _COLUMNS_NAMES = {
        'name': 'Individual',
        'extra_info': 'Owners',
        'size': 'Size',
        'speed': 'Speed',
        'fire_power': 'Fire Power',
        'maneuvering': 'Maneuvering',
        'force_factor': 'Force Factor'
    }

    def __init__(self,
                 name: str,
                 owners: str,
                 size: int,
                 speed: int,
                 fire_power: int,
                 maneuvering: int,
                 force_factor: int
                 ):
        super().__init__(name, extra_info=owners)

        self.size = size
        self.speed = speed
        self.fire_power = fire_power
        self.maneuvering = maneuvering
        self.force_factor = force_factor

    def get_printable_name(self):
        return self.name.upper()
