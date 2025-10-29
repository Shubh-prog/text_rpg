# Text-Based RPG Game in Python

A text-based role-playing game (RPG) implemented in Python. Explore areas, battle enemies, level up your character, collect items, and face powerful bosses!

---

## Features

- **Character Classes**: Choose from Warrior, Mage, or Archer, each with unique stats and abilities.
- **Progression System**: Gain experience (XP) and level up. Leveling up allows you to improve your stats (HP, Attack, Magic, Defense, Range Attack).
- **Enemies and Bosses**: Fight a variety of enemies and area bosses. Each enemy scales based on your level.
- **Areas to Explore**: Adventure through multiple areas like towns, forests, and caves.
- **Random Encounters**: Random enemy encounters and occasional shop visits to buy items or heal.
- **Items and Buffs**: Collect healing items and buffs that temporarily enhance stats during battles.
- **Battle System**: Turn-based battles with choices for physical attack, magic attack, ranged attack, using items, or fleeing.
- **Storyline**: Follow a storyline with bosses and a final confrontation against the ultimate enemy.
- **Slow Text Printing**: Adds a better game feel by printing text gradually for a storytelling effect.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Terminal or Command Prompt to run the game

### Project Structure:

```bash
text-rpg/
│
├── main.py             # Main program to start the game
├── player.py           # Player character classes and methods
├── enemies.py          # Enemy classes and scaling
├── bosses.py           # Boss enemy classes
├── areas.py            # Area class and exploration mechanics
├── areas_data.py       # Predefined areas and their enemies/bosses
├── shop.py             # Shop system
├── items.py            # Items and buffs definitions
├── utils.py            # Utility functions (e.g., slow_print, fibonacci)
└── README.md           # Project documentation
```

### Installation:
```bash
git clone https://github.com/yourusername/text-rpg.git
cd text-rpg
python main.py
