from enemies import Enemy
class RogueWarrior(Enemy):
    def __init__(self):
        super().__init__(
            name="Rogue Warrior",
            max_hp=130,
            hp=130,
            attack=15,
            defense=6,
            xp_reward=100,
            gold_reward=100
        )
class GoblinKing(Enemy):
    def __init__(self):
        super().__init__(
            name="Goblin King",
            max_hp=200,
            hp=200,
            attack=20,
            defense=10,
            xp_reward=200,
            gold_reward=200
        )
class SkeletonKing(Enemy):
    def __init__(self):
        super().__init__(
            name="Skeleton King",
            max_hp=300,
            hp=300,
            attack=25,
            defense=12,
            xp_reward=500,
            gold_reward=500
        )
class FinalBoss(Enemy):
    def __init__(self):
        super().__init__(
            name="Dark Overlord",
            max_hp=500,
            hp=500,
            attack=35,
            defense=15,
            xp_reward=1000,
            gold_reward=1000
        )