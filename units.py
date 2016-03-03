import random
from items import Item, HeadArmor, BodyArmor, BootsArmor
from controller import RestController

__author__ = 'jaklimoff'


class Bag:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def add_item(self, item):
        if item.multiple:
            created_item = None
            for it in self.items:
                if it.name == item.name:
                    it.amount += 1
                    created_item = 1
                    break
            if not created_item:
                    self.items.append(item)
        else:
            self.items.append(item)
        return True

    def remove_item(self, item, count=1):
        if item.multiple:
            removed_item = None
            for i in self.items:
                if i.name == item.name:
                    if i.amount > count:
                        i.amount -= count
                        item.amount += count
                        removed_item = True
                        break
                    elif i.amount == count:
                        item.amount = count
                        self.items.remove(item)
                        removed_item = True
                        break
                    else:
                        print"You don't have so much %s" % item.name
                        return False
            if not removed_item:
                    print"You don't have such item: %s" % item.name
                    return False
            return item
        else:
            self.items.remove(item)
            return item


class Unit:
    name = "anon"
    enemies = None
    choosen_enemy = None
    hp = 100
    strength = 1
    agility = 1
    exp = 0
    exp_map = [100, 200, 400, 500]


    def use(self, potion):
        potion.uses -= 1
        self.hp += potion.restored_hp
        if potion.uses <= 0:
            self.bag.remove_item(potion)


    def __str__(self):
        return self.name

    @property
    def is_alive(self):
        return self.hp > 0

    @property
    def defense(self):
        defense = 0
        for slot in self.slots:
            item = self.slots[slot]["item"]
            defense += item.defense
        return defense

    @property
    def attack(self):
        def percentage(part, whole):
            return 20 * float(part)/float(whole)

        def pervalue(percent, whole):
            return (percent * whole) / 100.0

        attack = 0
        for slot in self.slots:
            item = self.slots[slot]["item"]
            attack += item.attack

        attack_bonus_percents = percentage(self.strength, 10)
        attack += pervalue(attack_bonus_percents, attack)  # add attack bonus percents
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
                "item": BodyArmor("Body", visible_in_bag=False),
                "name": "Body",
                "allow": BodyArmor,
            },
            "bt": {
                "item": BootsArmor("Boots", visible_in_bag=False),
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

    def battle_begin(self, enemies):
        if not isinstance(enemies, list):
            enemies = [enemies]

        self.enemies = enemies

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

    def hit(self, unit, point):
        self.choosen_enemy = unit
        self.hit_point = point

    def block(self, point):
        self.block_point = point

    _lastlevel=1
    @property
    def level(self):
      for l in self.exp_map:
        if self.exp<self.exp_map[l]:
            currentlevel=l+1
            if currentlevel>self._lastlevel:
                self._lastlevel=currentlevel
                self.level_up()
        return currentlevel

    def level_up(self):
        self.agility += 1*self.level
        self.strength += 1*self.level


class Knight(Unit):
    map = None
    pass


class Enemy(Unit):
    def next_turn(self):
        self.hit(self.enemies[0], random.randint(0, 2))
        self.block(random.randint(0, 2))
