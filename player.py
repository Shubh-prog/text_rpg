from utils import fibonacci
def choose_class(name):
    print("Choose your class:\n1: Warrior\n2: Mage\n3: Archer")
    choice = input("Enter number: ")
    if choice == "1":
        return Warrior(name)
    elif choice == "2":
        return Mage(name)
    elif choice == "3":
        return Archer(name)
    else:
        print("Invalid choice, defaulting to Warrior")
        return Warrior(name)
class Character:
    def __init__(self, name, class_name, level, xp, max_hp, attack,
                   defense, magic_attack, range_attack, gold=0):
        self.name = name
        self.class_name = class_name
        self.level = level
        self.xp = xp
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.attack = attack
        self.magic_attack = magic_attack
        self.defense = defense
        self.range_attack = range_attack
        self.gold = gold
        self.inventory = []
        self.active_buffs = []
    def take_damage(self, amount):
        self.hp = self.hp-(amount-(self.defense*amount//100))
    def is_alive(self):
        return self.hp>0
    def xp_to_nextLevel(self):
        return 10*fibonacci(self.level)
    def gain_xp(self, amount):
        self.xp +=amount
        while self.xp >= self.xp_to_nextLevel():
            self.xp-=self.xp_to_nextLevel()
            self.level_up()
    def level_up(self):
        self.level += 1
        print(f"\n{self.name} reached level {self.level}!")
        while True:
            try:
                stat = int(input(
                    "Which stat do you want to level up:\n"
                    "1: Max HP (+10)\n"
                    "2: Defense (+1)\n"
                    "3: Attack Power (+2)\n"
                    "4: Magic Attack (+2)\n"
                    "5: Range Attack (+2)\n"
                ))
                if stat == 1:
                    self.max_hp += 10
                    self.hp += 10  # optional: heal
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                    break
                elif stat == 2:
                    if self.defense<50:
                        self.defense += 1
                        break
                    else:
                        print("You have reached max level of Defense, level up some other stat")
                elif stat == 3:
                    if self.attack<99:
                        self.attack += 2
                        break
                    else:
                        print("You have reached max level of Attack, level up some other stat")
                elif stat == 4:
                    if self.magic_attack<99:
                        self.magic_attack += 2
                        break
                    else:
                        print("You have reached max level of Magic Attack, level up some other stat")
                elif stat == 5:
                    if self.range_attack<99:
                        self.range_attack += 2
                        break
                    else:
                        print("You have reached max level of Range attack, level up some other stat")
                else:
                    print("Invalid choice. Please choose a number from 1 to 5.")
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 5.")
    def add_gold(self, amount):
        self.gold+=amount
    def show_stats(self):
        print(f"\nYour Current stats are:\nHP:{self.hp}\nAttack Power:{self.attack}\nDefense:{self.defense}\nMagic Attack:{self.magic_attack}\nRange Attack:{self.range_attack}\nLevel:{self.level}")
    def add_item(self, item):
        """Add an item to inventory"""
        self.inventory.append(item)
        print(f"{item['name']} added to your inventory!")
    def show_inventory(self):
        """Display inventory items"""
        if not self.inventory:
            print("Your inventory is empty.")
            return
        print("\nYour Inventory:")
        for i, item in enumerate(self.inventory, 1):
            desc = f"{item['name']} (Type: {item['type']}"
            if item['type'] == 'heal':
                desc += f", Heals: {item['value']} HP"
            elif item['type'] == 'buff':
                desc += f", Buff: +{item['value']} {item['stat']} for {item['duration']} battles"
            desc += ")"
            print(f"{i}. {desc}")
    def use_item(self, item_index):
        """Use an item by index (1-based)"""
        if item_index < 1 or item_index > len(self.inventory):
            print("Invalid item selection.")
            return
        item = self.inventory.pop(item_index - 1)
        if item['type'] == 'heal':
            self.hp += item['value']
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f"You used {item['name']} and restored {item['value']} HP! Current HP: {self.hp}")
        elif item['type'] == 'buff':
            self.apply_buff(item)
        else:
            print(f"{item['name']} cannot be used right now.")
    def apply_buff(self, item):
        """Apply a buff item"""
        stat = item['stat']
        value = item['value']
        duration = item['duration']
        self.active_buffs.append({"stat": stat, "value": value, "turns_left": duration})
        print(f"{item['name']} used! +{value} {stat} for {duration} battles.")
    def apply_active_buffs(self):
        """Apply all active buffs before a battle (temporary stat boost)"""
        attack_boost = sum(buff['value'] for buff in self.active_buffs if buff['stat'] == 'attack')
        magic_boost = sum(buff['value'] for buff in self.active_buffs if buff['stat'] == 'magic_attack')
        defense_boost = sum(buff['value'] for buff in self.active_buffs if buff['stat'] == 'defense')
        range_boost = sum(buff['value'] for buff in self.active_buffs if buff['stat'] == 'range_attack')

        return {
            "attack": self.attack + attack_boost,
            "magic_attack": self.magic_attack + magic_boost,
            "defense": self.defense + defense_boost,
            "range_attack": self.range_attack + range_boost
        }
    def update_buffs(self):
        """Reduce buff durations after a battle and remove expired buffs"""
        expired = []
        for buff in self.active_buffs:
            buff['turns_left'] -= 1
            if buff['turns_left'] <= 0:
                expired.append(buff)
        for buff in expired:
            self.active_buffs.remove(buff)
            print(f"The effect of +{buff['value']} {buff['stat']} has worn off.")
    def show_active_buffs(self):
        """Show currently active buffs"""
        if not self.active_buffs:
            print("No active buffs.")
            return
        print("\nActive Buffs:")
        for buff in self.active_buffs:
            print(f"+{buff['value']} {buff['stat']} ({buff['turns_left']} battles left)")
    def __str__(self):
        return f"{self.name} the {self.class_name} (Level {self.level})"
class Warrior(Character):
    def __init__(self, name):
        super().__init__(
            name = name,
            class_name = "Warrior",
            max_hp = 120,
            attack = 10,
            defense = 5,
            magic_attack = 2,
            range_attack = 3,
            gold = 0,
            level = 1,
            xp = 0
        )
        self.inventory.append({"name": "Small Potion", "type": "heal", "value": 20})
        self.inventory.append({"name": "Attack Elixir", "type": "buff", "stat": "attack", "value": 5, "duration": 3})
class Mage(Character):
    def __init__(self, name):
        super().__init__(
            name = name,
            class_name = "Mage",
            max_hp = 80,
            attack = 3,
            defense = 3,
            magic_attack = 12,
            range_attack = 4,
            gold = 0,
            level = 1,
            xp = 0
        )
class Archer(Character):
    def __init__(self, name):
        super().__init__(
            name = name,
            class_name = "Archer",
            max_hp = 100,
            attack = 6,
            defense = 4,
            magic_attack = 4,
            range_attack = 10,
            gold = 0,
            level = 1,
            xp = 0
        )