from areas_data import areas_list
from player import Warrior
player = Warrior("TestHero")
area = areas_list[0]
area.explore(player)