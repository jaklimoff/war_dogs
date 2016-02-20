__author__ = 'jaklimoff'


class Item:
    weight = 0
    defense = 0
    attack = 0

    def __init__(self, item_name="brick", visible_in_bag=True):
        self.visible_in_bag = visible_in_bag
        self.name = item_name


class Weapon(Item):
    pass


class Armor(Item):
    pass


class BootsArmor(Armor):
    pass


class HeadArmor(Armor):
    pass


class BodyArmor(Armor):
    pass
