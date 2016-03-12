#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Map():
    def __init__(self):
        self.ring = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]

    def get_cell(self, x, y):
        return self.ring[y][x]

    def cell_is_empty(self, x, y):
        return self.get_cell(x, y) == 0


class Unit():
    ring = None

    _hp = 100
    _mp = 100
    _st = 100

    attack = 50
    decision = ""
    # enemies = None
    choosen_unit = None
    name = "Default"

    def __init__(self, name=None):
        self.position = (0, 0)
        self.direction = (0, 0)

        if name is not None:
            self.name = name
            self.enemies = []

    def update(self):
        self._move(random.randint(-1, 1), random.randint(-1, 1))
        # if self.is_alive:
        #     enemy = random.choice(self.enemies)
        #     getattr(self, random.choice(["_hit", "_heal"]))(enemy)

    @property
    def is_alive(self):
        return self.hp > 0

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(min(value, 100), 0)

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        self._mp = max(min(value, 100), 0)

    @property
    def st(self):
        return self._st

    @st.setter
    def st(self, value):
        self._st = max(min(value, 100), 0)

    def _move(self, x, y):
        self.decision = "move"
        self.direction = (x, y)

    def _hit(self, unit):
        self.choosen_unit = unit
        self.decision = "hit"

    def _heal(self, unit):
        self.choosen_unit = unit
        self.decision = "heal"

class Environment:
    """ Battle environment """
    def __init__(self, units):
        self.map = Map()
        self.units = units
        for unit in self.units:
            unit.health = 100
            unit.attack = 10
            unit.enemies = self.units
            unit.ring = self.map.ring

        print "-" * 20
        print "Battle begin!"
        print "-" * 20

        while True:
            random.shuffle(self.units)
            for unit in self.units:
                if unit.is_alive:
                    unit.update()
                    amount = random.randint(-5, 5) + unit.attack
                    if unit.decision == "hit" and unit.st > 10:
                        damage = amount / 2 + (amount / 2 * unit.st / 100)
                        unit.st -= 5
                        unit.choosen_unit.hp -= damage
                    elif unit.decision == "heal" and unit.mp > 10:
                        unit.mp -= 10
                        unit.choosen_unit.hp += amount
                    elif unit.decision == "move":
                        x, y = unit.position
                        self.map.ring[y][x] = 0

                        d_x, d_y = unit.direction
                        final_x = x + d_x
                        final_y = y + d_y
                        if final_x >= 4 or final_x < 0:
                            final_x = x
                        if final_y >= 4 or final_y < 0:
                            final_y = y
                        if not self.map.cell_is_empty(final_x, final_y):
                            final_x = x
                            final_y = y

                        unit.position = (final_x, final_y)

                    x, y = unit.position
                    self.map.ring[y][x] = unit


            self.units = filter(lambda unit: unit.is_alive, self.units)
            time.sleep(1)
            clear()
            for unit in self.units:
                if unit.is_alive:
                    unit.mp += random.randint(0, 2)
                    unit.st += random.randint(0, 2)

            h_line = " ".join([("-" * 4) for i in range(4)])

            ring_height = len(self.map.ring)
            ring_width = len(self.map.ring[0])

            def get_cell_content(x, y, field):
                cell = self.map.ring[y][x]
                if cell != 0:
                    value = getattr(cell, field)
                    if isinstance(value, str):
                        return value[:4]
                    else:
                        return value
                else:
                    return " "

            upper = {'u%s_%s' % (x, y): get_cell_content(x, y, "name") for y in range(ring_height) for x in range(ring_width)}
            footer = {'f%s_%s' % (x, y): (" %s " % get_cell_content(x, y, "hp"))[:4] for y in range(ring_height) for x in range(ring_width)}
            upper.update(footer)

            mapr = """
            {h_line}
           |{u0_0:4}|{u0_1:4}|{u0_2:4}|{u0_3:4}|
           |{f0_0:4}|{f0_1:4}|{f0_2:4}|{f0_3:4}|
            {h_line}
           |{u1_0:4}|{u1_1:4}|{u1_2:4}|{u1_3:4}|
           |{f1_0:4}|{f1_1:4}|{f1_2:4}|{f1_3:4}|
            {h_line}
           |{u2_0:4}|{u2_1:4}|{u2_2:4}|{u2_3:4}|
           |{f2_0:4}|{f2_1:4}|{f2_2:4}|{f2_3:4}|
            {h_line}
           |{u3_0:4}|{u3_1:4}|{u3_2:4}|{u3_3:4}|
           |{f3_0:4}|{f3_1:4}|{f3_2:4}|{f3_3:4}|
            {h_line}
            """.format(h_line=h_line, **upper)

            print mapr


            prnt = {unit.name:{'hp':unit.hp, 'mp':unit.mp, 'st':unit.st} for unit in self.units}
            print "-"*35
            print '{0:19}{1:6}{2:6}{3:6}'.format('', 'HP:', 'MP:', 'ST:')
            for key in sorted(prnt):
                print '{0:15}{hp:6}{mp:6}{st:6}'.format(key, **prnt[key])

            if len(self.units) <= 1:
                break

if __name__ == "__main__":

    from fighters.skypro1111 import Skypro
    from fighters.bodidze import Bodidze

    u1 = Skypro('sky')

    u2 = Unit('COCA')
    u3 = Unit('TSOI')
    u4 = Unit('Kaligula')
    u5 = Unit ('Bod')

    units = [u1, u2, u3, u4, u5]

    Environment(units)
