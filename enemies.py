import random
from utils import fibonacci
import player
class Enemy:
    def __init__(self, name, max_hp, attack, defense, xp_reward, gold_reward, player_level):
        self.name = name
        self.max_hp = max_hp + (15 * player_level)
        self.hp = self.max_hp
        self.attack = attack + (2 * player_level)
        self.defense = defense + int(1.5 * player_level)
        self.xp_reward = int(xp_reward * (1 + 0.25 * player_level))
        self.gold_reward = int(gold_reward * (1 + 0.15 * player_level))
    def is_alive(self):
        return self.hp > 0
    def take_damage(self, amount):
        damage = max(1, amount - self.defense)
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return damage
    def attack_player(self, player):
        damage = random.randint(self.attack - 2, self.attack + 2)
        player.take_damage(damage)
    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp})"
class Bandit(Enemy):
    def __init__(self, player_level):
        super().__init__(
            name="Bandit",
            max_hp=20,
            attack=8,
            defense=0,
            xp_reward=5,
            gold_reward=5,
            player_level=player_level
        )
class Outlaw(Enemy):
    def __init__(self, player_level):
        super().__init__(
            name="Outlaw",
            max_hp=25,
            attack=10,
            defense=1,
            xp_reward=10,
            gold_reward=10,
            player_level=player_level
        )
class Goblin(Enemy):
    def __init__(self, player_level):
        super().__init__(
            name="Goblin",
            max_hp=30,
            attack=10,
            defense=2,
            xp_reward=15,
            gold_reward=15,
            player_level=player_level
        )
class GoblinWarrior(Enemy):
    def __init__(self, player_level):
        super().__init__(
            name="Goblin Warrior",
            max_hp=40,
            attack=12,
            defense=4,
            xp_reward=20,
            gold_reward=20,
            player_level=player_level
        )
class Skeleton(Enemy):
    def __init__(self, player_level):
        super().__init__(
            name="Skeleton",
            max_hp=50,
            attack=15,
            defense=5,
            xp_reward=25,
            gold_reward=25,
            player_level=player_level
        )
class Necromancer(Enemy):
    def __init__(self, player_level):
        super().__init__(
            name="Necromancer",
            max_hp=60,
            attack=18,
            defense=6,
            xp_reward=30,
            gold_reward=30,
            player_level=player_level
        )