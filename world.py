import random

from controller import VisualEffects
from items import Item
from settings import Settings
from units import Knight, Enemy


__author__ = 'jaklimoff'

import controller


class World:
    knight = None

    def __init__(self, knight):

# added it
        VisualEffects.hello(knight)

        self.knight = knight
        self.knight.hp = 67
        sword = Item("sword")
        sword.attack = 100
        sword.defense = 20
        self.knight.bag.add_item(sword)
        self.knight.wear(sword, 'rh')
        self.knight.bag.add_item(Item("shield"))
        self.knight.bag.add_item(Item("tourch"))
        self.knight.bag.add_item(Item("fri potato"))

        while True:
            self.rest()
            self.fight()

    def rest(self):
        rest_controller = controller.RestController(self.knight)
        while True:
            rest_controller.list_of_commands()
            rest_controller = controller.RestController(knight)
            if not self.knight.is_alive:
                self.knight.hit_point = 100
                print "Knight is alive now!"

            result = rest_controller.command()
            if not result:
                break


    def fight(self):
        enemy = Enemy("Orc")
        item = Item("Brick")
        item.attack = 6
        enemy.wear(item, "lh")
        enemy.battle_begin(self.knight)
        knight.battle_begin(enemy)

        print "Health of enemy" # added it
        print "Enemy: %s" % enemy.hp
        print "Health of hero" # added it
        print "Knight: %s" % self.knight.hp

        fight_controller = controller.FightController(self.knight)
        while True:
            fight_controller.list_of_commands()
            result = fight_controller.command()
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

            end = False
            for u in units:
                if not u.is_alive:
                    fight_controller.show_final_battle_result(u)
                    end = True

            if end:
                break

if __name__ == "__main__":
    settings = Settings("settings.json")

    name = raw_input("Enter your name:")
    knight = Knight(name)
    world = World(knight)