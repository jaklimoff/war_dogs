import copy
import random

from controller import VisualEffects
from items import Item, Coins, HealingPotion
from settings import Settings
from shop import Map
from units import Knight

__author__ = 'jaklimoff'

import controller



class World:

    knight = None

    def __init__(self, knight, settings):

        self.settings = settings
        VisualEffects.hello(knight)


        self.knight = knight
        self.knight.hp = 67
        sword = Item("sword")
        sword.attack = 100
        sword.defense = 20
        self.knight.bag.add_item(sword)
        self.knight.wear(sword, 'rh')
        self.knight.bag.add_item(Item("shield"))
        coin = Coins()
        coin.amount = 21
        tax = Coins()
        self.knight.bag.add_item(coin)
        self.knight.bag.add_item(Item("tourch"))
        self.knight.bag.add_item(Item("fri potato"))
        big_healing_potion = HealingPotion("big healing potion")
        big_healing_potion.uses = 3
        big_healing_potion.restored_hp = 10
        self.knight.bag.add_item(big_healing_potion)
        self.knight.bag.remove_item(tax, 9)


        self.map = Map()
        self.knight.map = self.map


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

    def show_enemy_slots(self, *enemies):
        for i in enemies:
            for enemy in i:
                print "{:<7}   HP: {:>7}".format(enemy.name, enemy.hp)
                for slot in enemy.slots:
                    item_slot = enemy.slots[slot]
                    slot_name = item_slot['name']
                    item = item_slot['item']
                    print "{enemy:<7}   {name} :>> {item_name}".format(enemy=enemy.name, name=slot_name, item_name=item.name)
            if self.levelup:
                print "Knight is leveled up!"
                print "Type what you want to increase: agility or strength?"
                result = raw_input("Type what you want to increase: agility or strength?")
                if result =="agility":
                  self.agility += 1*self.level
                if result =="strength":
                  self.strength += 1*self.level

    def fight(self):
        #lvl = self.knight.level
        number_of_enemies = random.randint(1, 3)
        min_number_enemies = 1
        enemies = self.knight.enemies
        i = 1
        while min_number_enemies <= number_of_enemies:
            key_enemy = random.choice(settings.enemies.keys())
            list_enemies = settings.enemies
            enemy = copy.copy(list_enemies[key_enemy])
            for i_enemy in enemies:
                if enemy.name == i_enemy.name:
                    enemy.name = "{name} {i}".format(name=enemy.name, i=str(i))
                    i += 1
            enemies.append(enemy)
            min_number_enemies += 1

        #for every in enemies:
        #    every.battle_begin(self.knight)
        #knight.battle_begin(enemies)

        print "Health of enemy"
        print "-" * 14
        self.show_enemy_slots(enemies)
        print "-" * 14
        print "Health of hero" # added it
        print "Knight: %s" % self.knight.hp

        fight_controller = controller.FightController(self.knight)
        while True:
            fight_controller.list_of_commands()
            result = fight_controller.command()
            for enemy in enemies:
                enemy.next_turn(self.knight)

            def process(unit):
                enemy = unit.choosen_enemy
                damage = 0
                if unit.hit_point != enemy.block_point:
                    damage = unit.attack
                    enemy.hp -= damage
                fight_controller.show_battle_result(unit, damage, enemy)

            units = [self.knight]
         #   random.shuffle(units)
            for enemy in enemies:
                units.append(enemy)
            for u in units:
                process(u)

            for i in enemies:
                print "{:<7}{:>7}".format(i.name, i.hp)
            print "Knight: %s" % self.knight.hp

            end = False

            if not self.knight.is_alive:
                fight_controller.show_final_battle_result(self.knight)
                end = True
            else:
                self.knight.exp +=15



            for i, e in enumerate(enemies):
                if not e.is_alive:
                    fight_controller.show_final_battle_result(e)
                    enemies.remove(e)
                    if len(enemies) == 0:
                        end = True

            if end:
                break

if __name__ == "__main__":
    settings = Settings("settings.json")
    VisualEffects.invitation()
    VisualEffects.logo()
    VisualEffects.bar()
    name = raw_input("Enter your name:")
    knight = Knight(name)

    world = World(knight, settings)

