class Card:
    def __init__(self, name: str, extra_info: str = None):

        if type(name) is not str:
            raise TypeError

        self.name = name
        self.extra_info = extra_info
