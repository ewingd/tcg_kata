from __future__ import annotations
from dataclasses import dataclass, field, replace
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
    max_mana: int = 0
    hand: Tuple = ()
    deck: Deck = field(default_factory=new_default_deck)

    def draw(self, count: int = 1) -> Player:
        hand, deck = self.deck.draw(count)
        return replace(self, hand=self.hand + hand)

    def increase_max_mana(self) -> Player:
        max_mana = min(self.max_mana + 1, 10)
        return replace(self, max_mana=max_mana)

    def fill_mana(self) -> Player:
        return replace(self, mana=self.max_mana)


def new_player():
    return Player()


class GameNotStartedException(Exception):
    pass


@dataclass(frozen=True)
class GameState:
    player: Player = field(default_factory=new_player)
    opponent: Player = field(default_factory=new_player)
    current_player: Optional[Player] = None

    def is_active(self, player: Player) -> bool:
        return self.current_player is player

    def start(self) -> GameState:
        current_player = random.choice((self.player, self.opponent))

        player = self.player.draw(3 if current_player is self.player else 4)
        opponent = self.opponent.draw(3 if current_player is self.opponent else 4)

        if len(player.hand) == 3:
            return GameState(player=player, opponent=opponent, current_player=player)
        else:
            return GameState(player=player, opponent=opponent, current_player=opponent)

    def start_new_turn(self) -> GameState:

        if self.current_player is None:
            raise GameNotStartedException()

        if self.is_active(self.player):
            player = "player"
        else:
            player = "opponent"

        current_player = self.current_player.increase_max_mana().fill_mana().draw()

        if player == "player":
            return GameState(
                player=current_player,
                opponent=self.opponent,
                current_player=current_player,
            )
        else:
            return GameState(
                player=self.player,
                opponent=current_player,
                current_player=current_player,
            )
