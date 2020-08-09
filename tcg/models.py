from dataclasses import dataclass

@dataclass(frozen=True)
class Player:
    health: int = 30
    mana: int = 0