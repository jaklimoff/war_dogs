#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time



class Unit():
    _hp = 100
    _mp = 100
    _st = 100

    attack = 50
    decision = ""
    # enemies = None
    choosen_unit = None
    name = "Default"

    def __init__(self, name=None):
        if name is not None:
            self.name = name
            self.enemies = []

    def update(self):
        if self.is_alive:
            enemy = random.choice(self.enemies)
            getattr(self, random.choice(["_hit", "_heal"]))(enemy)

    @property
    def is_alive(self):
        return self.hp > 0

    @property
    def hp(self):
        return self._hp
    def set_hp(self, value):
        self._hp = max(min(value, 100), 0)

    @property
    def mp(self):
        return self._mp
    def set_mp(self, value):
        self._mp = max(min(value, 100), 0)

    @property
    def st(self):
        return self._st
    def set_st(self, value):
        self._st = max(min(value, 100), 0)

    def _hit(self, unit):
        self.choosen_unit = unit
        self.decision = "hit"

    def _heal(self, unit):
        self.choosen_unit = unit
        self.decision = "heal"

class Environment:
    """ Battle environment """
    def __init__(self, units):
        self.units = units
        for unit in self.units:
            unit.health = 100
            unit.attack = 10
            unit.enemies = self.units

        print "-" * 20
        print "Battle begin!"
        print "-" * 20

        while True:
            random.shuffle(self.units)
            for unit in self.units:
                if unit.is_alive:
                    unit.update()
                    amount = random.randint(-5,5) + unit.attack
                    if unit.decision == "hit" and unit.st > 10:
                        damage = amount / 2 + (amount / 2 * unit.st / 100)
                        unit.set_st(unit.st - 5)
                        unit.choosen_unit.set_hp(unit.choosen_unit.hp - damage)
                    elif unit.decision == "heal" and unit.mp > 10:
                        unit.set_mp(unit.mp - 10)
                        unit.choosen_unit.set_hp(unit.choosen_unit.hp + amount)

            self.units = filter(lambda unit: unit.is_alive, self.units)

            time.sleep(1)
            for unit in self.units:
                if unit.is_alive:
                    unit.set_mp(unit.mp+random.randint(0,2))
                    unit.set_st(unit.st+random.randint(0,2))

            prnt = {unit.name:{'hp':unit.hp, 'mp':unit.mp, 'st':unit.st} for unit in self.units}
            print "-"*35
            print '{0:19}{1:6}{2:6}{3:6}'.format('', 'HP:', 'MP:', 'ST:')
            for key in sorted(prnt):
                print '{0:15}{hp:6}{mp:6}{st:6}'.format(key, **prnt[key])

            if len(self.units) <= 1:
                break

if __name__ == "__main__":

    from fighters.skypro1111 import Skypro

    u1 = Skypro('sky')

    u2 = Unit('COCA')
    u3 = Unit('TSOI')
    u4 = Unit('Kaligula')

    units = [u1, u2, u3, u4]

    Environment(units)
