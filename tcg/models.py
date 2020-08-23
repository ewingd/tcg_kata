from __future__ import annotations
from dataclasses import dataclass, field
from typing import Tuple, Optional
import random


@dataclass(frozen=True)
class Card:
    cost: int


def make_default_deck() -> Tuple:
    costs = (0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8)
    return tuple([Card(cost) for cost in costs])


def new_default_deck() -> Deck:
    return Deck()


@dataclass(frozen=True)
class Deck:
    cards: Tuple[Card, ...] = field(default_factory=make_default_deck)

    def draw(self, count: int = 1) -> Tuple[Tuple[Card, ...], Deck]:
        return self.cards[:count], Deck(self.cards[count:])

    def shuffle(self) -> Deck:
        cards = list(self.cards)
        random.shuffle(cards)
        return Deck(tuple(cards))


@dataclass(frozen=True)
class Player:
    health: int = 30
    mana: int = 0
    hand: Tuple = ()
    is_active: bool = False
    deck: Deck = field(default_factory=new_default_deck)

    def draw(self, count: int = 1) -> Player:
        hand, deck = self.deck.draw(count)
        return Player(self.health, self.mana, self.hand + hand, self.is_active, deck)


def new_player():
    return Player()


@dataclass(frozen=True)
class GameState:
    player: Player = field(default_factory=new_player)
    opponent: Player = field(default_factory=new_player)
    current_player: Optional[Player] = None

    def start(self) -> GameState:
        current_player = random.choice((self.player, self.opponent))

        player = self.player.draw(3 if current_player is self.player else 4)
        opponent = self.opponent.draw(3 if current_player is self.opponent else 4)

        return GameState(player, opponent, current_player)
