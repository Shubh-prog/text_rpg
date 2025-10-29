import random
from player import Character
from battle import Battle
from enemies import Bandit, Outlaw, Goblin, GoblinWarrior, Skeleton, Necromancer
from shop import Shop
from utils import slow_print

class Area:
    def __init__(self, name, description, enemy_types, boss_class=None, level_range=(1, 1), enemy_count=5):
        self.name = name
        self.description = description
        self.enemy_types = enemy_types        # list of enemy classes
        self.boss_class = boss_class          # class of boss
        self.level_range = level_range
        self.enemy_count = enemy_count
        self.cleared = False
        self.enemies_defeated = 0

    def scale_enemy(self, enemy, player_level):
        """Scale enemy stats based on player level"""
        enemy.max_hp += 10 * (player_level - 1)
        enemy.hp = enemy.max_hp
        enemy.attack += 2 * (player_level - 1)
        enemy.defense += int(1.5 * (player_level - 1))
        enemy.xp_reward = int(enemy.xp_reward * (1 + 0.25 * (player_level - 1)))
        enemy.gold_reward = int(enemy.gold_reward * (1 + 0.15 * (player_level - 1)))
        return enemy

    def spawn_enemy(self, player: Character):
        """Create a new enemy instance and scale with player level"""
        if not self.enemy_types:
            return None
        enemy_class = random.choice(self.enemy_types)
        enemy = enemy_class(player.level)
        enemy = self.scale_enemy(enemy, player.level)
        return enemy

    def explore(self, player: Character):
        if self.cleared:
            slow_print(f"You have already cleared {self.name}.\n")
            return

        slow_print(f"Exploring {self.name}...\n")
        for i in range(self.enemy_count):
            # Random shop chance (1 in 20)
            if random.randint(1, 20) == 1:
                Shop.visit(player)

            enemy = self.spawn_enemy(player)
            slow_print(f"A wild {enemy.name} appears! (HP: {enemy.hp}, Attack: {enemy.attack})\n")

            player.apply_active_buffs()
            battle = Battle(player, enemy)
            battle.start_battle()
            player.update_buffs()

            if not player.is_alive():
                slow_print("You have been defeated! Game Over.\n")
                return

            self.enemies_defeated += 1
            slow_print(f"Enemies defeated in {self.name}: {self.enemies_defeated}/{self.enemy_count}\n")

        # Boss fight
        if self.boss_class:
            boss = self.boss_class(player.level)
            slow_print(f"The boss {boss.name} appears!\n")
            player.apply_active_buffs()
            battle = Battle(player, boss)
            battle.start_battle()
            player.update_buffs()

            if not player.is_alive():
                slow_print(f"You have been defeated by the boss {boss.name}! Game Over.\n")
                return
            slow_print(f"You have defeated the boss {boss.name}!\n")

        self.cleared = True
        slow_print(f"Congratulations! You have cleared {self.name}!\n")

    def describe(self):
        slow_print(f"Area: {self.name}\nDescription: {self.description}\n")
        slow_print(f"Enemy types: {', '.join([e.__name__ for e in self.enemy_types])}\n")
        if self.boss_class:
            slow_print(f"Boss: {self.boss_class.__name__}\n")
        else:
            slow_print("Boss: None\n")
        slow_print(f"Enemy count: {self.enemy_count}\nCleared: {'Yes' if self.cleared else 'No'}\n")
