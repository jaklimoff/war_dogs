from items import Item, HeadArmor, BodyArmor, BootsArmor

__author__ = 'jaklimoff'


class Bag:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)
        return self

    def remove_item(self, item):
        self.items.remove(item)
        return item


class Unit:
    name = "anon"

    hp = 100
    strength = 1
    agility = 1

    @property
    def defense(self):
        defense = 0
        for slot in self.slots:
            item = self.slots[slot]["item"]
            defense += item.defense
        return defense

    @property
    def attack(self):
        attack = 0
        for slot in self.slots:
            item = self.slots[slot]["item"]
            attack += item.attack
        return attack

    def __init__(self, name):
        self.name = name
        self.bag = Bag()
        self.slots = {
            "hd": {
                "item": HeadArmor("Head", visible_in_bag=False),
                "name": "Head",
                "allow": HeadArmor,
            },
            "bd": {
                "item": BodyArmor("Head", visible_in_bag=False),
                "name": "Body",
                "allow": BodyArmor,
            },
            "bt": {
                "item": BootsArmor("Head", visible_in_bag=False),
                "name": "Left Hand",
                "allow": BootsArmor,
            },
            "rh": {
                "item": Item("Fist", visible_in_bag=False),
                "name": "Right Hand",
                "allow": Item,
            },
            "lh": {
                "item": Item("Fist", visible_in_bag=False),
                "name": "Left Hand",
                "allow": Item,
            }
        }

    def wear(self, item, slot):
        if slot in self.slots:
            item_slot = self.slots[slot]
            prev_item = item_slot["item"]
            allow_class = item_slot["allow"]
            if isinstance(item, allow_class):
                item_slot["item"] = item
                self.bag.add_item(prev_item)
                if item in self.bag.items:
                    self.bag.remove_item(item)
                return prev_item
        return False


class Knight(Unit):
    pass