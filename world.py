from items import Item
from units import Knight

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
        self.knight.bag.add_item(Item("sword"))
        self.knight.bag.add_item(Item("shield"))
        self.knight.bag.add_item(Item("tourch"))
        self.knight.bag.add_item(Item("fri potato"))

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
        # enemy = Unit("Orc")
        # fight_controller = controller.FightController(self.knight, enemy)
        while True:
            command_line = raw_input("[FIGHT] Command: ")
            result = self.rest_controller.command(command_line)
            if not result:
                break

if __name__ == "__main__":
    name = raw_input("Enter your name:")
    knight = Knight(name)
    world = World(knight)