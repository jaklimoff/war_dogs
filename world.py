import random
from items import Item
from settings import Settings
from units import Knight, Unit, Enemy
from shop import Map

__author__ = 'jaklimoff'

import controller



class World:
    knight = None

    def __init__(self, knight):
        self.rest_controller = controller.RestController(knight)
        print "=" * 10
        print "Hello %s! Its a tough time. Be aware of monsters and step_mother!" % knight.name
        print "=" * 10

        self.knight = knight
        self.knight.hp = 67
        sword = Item("sword")
        sword.attack = 20
        sword.defense = 20
        self.knight.bag.add_item(sword)
        self.knight.bag.add_item(Item("shield"))
        self.knight.bag.add_item(Item("tourch"))
        self.knight.bag.add_item(Item("fri potato"))

        self.map = Map()
        self.knight.map = self.map


        while True:
            self.rest()
            self.fight()

    def rest(self):
        while True:
            command_line = raw_input("[REST] Command: ")
            result = self.rest_controller.command(command_line)
            if not result:
                break


    def fight(self):
        enemy = Enemy("Orc")
        item = Item("Brick")
        item.attack = 6
        enemy.wear(item, "lh")
        enemy.battle_begin(self.knight)
        knight.battle_begin(enemy)

        print "Enemy: %s" % enemy.hp
        print "Knight: %s" % self.knight.hp

        fight_controller = controller.FightController(self.knight)
        while True:
            command_line = raw_input("[FIGHT] Command: ")
            result = fight_controller.command(command_line)
            enemy.next_turn()

            def process(unit):
                enemy = unit.choosen_enemy
                damage = 0
                if unit.hit_point != enemy.block_point:
                    damage = unit.attack
                    enemy.hp -= damage
                fight_controller.show_battle_result(unit, damage, enemy)

            units = [self.knight, enemy]
            random.shuffle(units)
            for u in units:
                process(u)


            print "Enemy: %s" % enemy.hp
            print "Knight: %s" % self.knight.hp

            if not result:
                break

if __name__ == "__main__":
    settings = Settings("settings.json")
    name = raw_input("Enter your name:")
    knight = Knight(name)
    world = World(knight)
