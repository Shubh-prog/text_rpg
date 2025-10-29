import random
import time
from player import Character
from enemies import Enemy

# Helper function: slow print text like a typewriter
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # newline

class Battle:
    def __init__(self, player: Character, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.turn_count = 0

    def start_battle(self):
        """Main battle loop"""
        while self.player.is_alive() and self.enemy.is_alive():
            self.turn_count += 1
            self.show_stats()

            # Player's turn
            if self.player_turn():
                slow_print("You fled the battle!", 0.05)
                break

            # Enemy's turn (if still alive)
            if self.enemy.is_alive():
                self.enemy_turn()

            # Check end conditions
            if self.player.is_alive() and not self.enemy.is_alive():
                self.handle_victory()
            elif not self.player.is_alive():
                self.handle_defeat()

    def show_stats(self):
        """Display player and enemy stats"""
        slow_print("="*30, 0.01)
        slow_print("\tPLAYER", 0.02)
        slow_print(f"Name: {self.player.name}\tClass: {self.player.class_name}\tLevel: {self.player.level}", 0.02)
        slow_print(f"HP: {self.player.hp}/{self.player.max_hp}\tAttack: {self.player.attack}\tDefense: {self.player.defense}", 0.02)
        slow_print(f"Magic: {self.player.magic_attack}\tRange: {self.player.range_attack}\tGold: {self.player.gold}", 0.02)
        self.player.show_active_buffs()
        slow_print("="*30, 0.01)
        slow_print("\tENEMY", 0.02)
        slow_print(f"Name: {self.enemy.name}\nHP: {self.enemy.hp}/{self.enemy.max_hp}", 0.02)
        slow_print(f"Attack: {self.enemy.attack}\tDefense: {self.enemy.defense}", 0.02)
        slow_print("="*30, 0.01)

    def player_turn(self):
        """Handle player's choice of action"""
        slow_print("\nYour turn! Choose an action:", 0.03)
        slow_print("1. Attack", 0.03)
        slow_print("2. Use Magic", 0.03)
        slow_print("3. Range Attack", 0.03)
        slow_print("4. Use Item", 0.03)
        slow_print("5. Flee", 0.03)

        try:
            action = int(input("Enter your action: "))
        except ValueError:
            slow_print("Invalid input! You lose your turn.", 0.03)
            return False

        # Apply active buffs to get temporary stats
        stats = self.player.apply_active_buffs()

        if action == 1:
            damage = self.calculate_damage(stats['attack'], self.enemy.defense)
            self.enemy.take_damage(damage)
            slow_print(f"You attacked {self.enemy.name} for {damage} damage!", 0.05)
        elif action == 2:
            damage = self.calculate_damage(stats['magic_attack'], self.enemy.defense)
            self.enemy.take_damage(damage)
            slow_print(f"You used magic on {self.enemy.name} for {damage} damage!", 0.05)
        elif action == 3:
            damage = self.calculate_damage(stats['range_attack'], self.enemy.defense)
            self.enemy.take_damage(damage)
            slow_print(f"You performed a range attack on {self.enemy.name} for {damage} damage!", 0.05)
        elif action == 4:
            self.player.show_inventory()
            try:
                item_index = int(input("Enter the item number to use: "))
                self.player.use_item(item_index)
            except (ValueError, IndexError):
                slow_print("Invalid item! You lose your turn.", 0.05)
        elif action == 5:
            flee_chance = random.random()
            if flee_chance < 0.5:
                return True
            else:
                slow_print("Flee attempt failed! Battle continues.", 0.05)
        else:
            slow_print("Invalid action! You lose your turn.", 0.05)

        return False

    def enemy_turn(self):
        """Enemy attacks the player"""
        damage = self.calculate_damage(self.enemy.attack, self.player.defense)
        self.player.take_damage(damage)
        slow_print(f"{self.enemy.name} attacked you for {damage} damage!", 0.05)

    def calculate_damage(self, attack, defense):
        """Calculate final damage after defense"""
        damage = attack - int(defense * attack / 100)
        return max(1, damage)

    def handle_victory(self):
        """Handle what happens when player wins"""
        slow_print(f"\nYou defeated {self.enemy.name}!", 0.05)
        self.player.gain_xp(self.enemy.xp_reward)
        self.player.add_gold(self.enemy.gold_reward)
        slow_print(f"You gained {self.enemy.xp_reward} XP and {self.enemy.gold_reward} gold!", 0.05)

    def handle_defeat(self):
        """Handle player defeat"""
        slow_print("\nYou have been defeated... Game Over.", 0.05)
