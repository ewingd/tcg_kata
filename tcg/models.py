from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class Player:
    health: int = 30
    mana: int = 0


@dataclass(frozen=True)
class Card:
    cost: int


def make_default_deck():
    costs = (0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8)
    return tuple([Card(cost) for cost in costs])


@dataclass(frozen=True)
class Deck:
    cards: Tuple[Card] = field(default_factory=make_default_deck)
