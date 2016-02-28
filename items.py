__author__ = 'jaklimoff'


class Item:
    weight = 0
    defense = 0
    attack = 0

    def __init__(self, item_name="brick", visible_in_bag=True):
        self.visible_in_bag = visible_in_bag
        self.name = item_name


fist = Item
fist.name = "Fist"
fist.attack = 1
fist.defense = 1
fist.tough = 1000000000000000000

class Weapon(Item):
    pass


class Armor(Item):
    pass


class BootsArmor(Armor):
    pass

naked_boots = BootsArmor
naked_boots.name = "Naked"
naked_boots.attack = 1
naked_boots.defense = 1
naked_boots.tough = 1000000000000000000

class HeadArmor(Armor):
    pass

head = HeadArmor
head.name = "Head"
head.attack = 1
head.defense = 1
head.tough = 1000000000000000000

class BodyArmor(Armor):
    pass

naked_body = BodyArmor
naked_body.name = "Naked"
naked_body.attack = 1
naked_body.defense = 1
naked_body.tough = 1000000000000000000