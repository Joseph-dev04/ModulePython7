from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        self._attack = attack
        self._health = health
        super().__init__(name, cost, rarity)

    def play(sekf, game_state):
        return super().play(game_state)

    def attack_target():
        pass
