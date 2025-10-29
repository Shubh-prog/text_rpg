from utils import slow_print

class Shop:
    def __init__(self, inventory=None):
        """Inventory is a list of items available in the shop"""
        if inventory is None:
            self.inventory = [
                {"name": "Small Health Potion", "type": "heal", "value": 30, "price": 10},
                {"name": "Large Health Potion", "type": "heal", "value": 70, "price": 25},
                {"name": "Attack Elixir", "type": "buff", "stat": "attack", "value": 5, "duration": 3, "price": 20},
                {"name": "Defense Tonic", "type": "buff", "stat": "defense", "value": 3, "duration": 3, "price": 15},
                {"name": "Magic Scroll", "type": "buff", "stat": "magic_attack", "value": 5, "duration": 3, "price": 20}
            ]
        else:
            self.inventory = inventory

    def display_items(self):
        slow_print("\nWelcome to the shop! Here's what's available:")
        for i, item in enumerate(self.inventory, 1):
            desc = f"{item['name']} - Price: {item['price']} Gold"
            if item['type'] == 'heal':
                desc += f" (Heals {item['value']} HP)"
            elif item['type'] == 'buff':
                desc += f" (+{item['value']} {item['stat']} for {item['duration']} battles)"
            slow_print(f"{i}. {desc}")

    def buy_item(self, player):
        self.display_items()
        slow_print(f"\nYou have {player.gold} gold.")
        try:
            choice = int(input("Enter the number of the item you want to buy (0 to exit): "))
            if choice == 0:
                slow_print("Leaving the shop...")
                return
            if 1 <= choice <= len(self.inventory):
                item = self.inventory[choice - 1]
                if player.gold >= item['price']:
                    player.gold -= item['price']
                    player.add_item(item)
                    slow_print(f"You bought {item['name']}!")
                else:
                    slow_print("You don't have enough gold for that item.")
            else:
                slow_print("Invalid choice. Try again.")
        except ValueError:
            slow_print("Invalid input. Please enter a number.")

    def enter_shop(self, player):
        slow_print("\nYou enter the shop.")
        while True:
            slow_print("\n1. Buy Item\n2. Exit Shop")
            try:
                choice = int(input("Choose an option: "))
                if choice == 1:
                    self.buy_item(player)
                elif choice == 2:
                    slow_print("You leave the shop.")
                    break
                else:
                    slow_print("Invalid option. Choose 1 or 2.")
            except ValueError:
                slow_print("Invalid input. Please enter a number.")
