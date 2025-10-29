from areas import Area
from enemies import Bandit, Outlaw, Goblin, GoblinWarrior, Skeleton, Necromancer
from bosses import GoblinKing, SkeletonKing, RogueWarrior, FinalBoss

# -------------------------
# Area Instances
# -------------------------

# Town area
town = Area(
    name="Town",
    description="The central hub of the realm. Bandits and Outlaws roam here.",
    enemy_types=[Bandit, Outlaw],
    boss_class=RogueWarrior,
    level_range=(1, 2),
    enemy_count=5
)

# Forest area
enchanted_forest = Area(
    name="Enchanted Forest",
    description="A mystical forest inhabited by Goblins and Goblin Warriors.",
    enemy_types=[Goblin, GoblinWarrior],
    boss_class=GoblinKing,
    level_range=(2, 4),
    enemy_count=6
)

# Cave area
skeleton_cave = Area(
    name="Skeleton Cave",
    description="A dark cave where Skeletons and Necromancers dwell.",
    enemy_types=[Skeleton, Necromancer],
    boss_class=SkeletonKing,
    level_range=(3, 6),
    enemy_count=7
)

# Final boss area
dark_castle = Area(
    name="Dark Castle",
    description="The lair of the Dark Overlord, an evil version of yourself.",
    enemy_types=[],
    boss_class=FinalBoss,
    level_range=(7, 10),
    enemy_count=0
)

# -------------------------
# List of all areas in order
# -------------------------
areas_list = [town, enchanted_forest, skeleton_cave, dark_castle]
