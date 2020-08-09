class Player:
    def __init__(self):
        self._health = 30

    @property
    def health(self):
        return self._health