class Player:
    def __init__(self):
        self._health = 30
        self._mana = 0

    @property
    def health(self):
        return self._health

    @property
    def mana(self):
        return self._mana