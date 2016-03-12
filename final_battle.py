#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
import os
import math


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


class Unit(object):
    ring = None

    _hp = 100
    _mp = 100
    _st = 100

    attack = 10
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
        def move():
            self._move(random.randint(-1, 1), random.randint(-1, 1))

        def attack():
            enemy = random.choice(self.enemies)
            getattr(self, random.choice(["_hit", "_heal"]))(enemy)

        choices = [move, attack]
        random.choice(choices)()

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

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

    def _bighit(self, unit):
        self.choosen_unit = unit
        self.decision = "bighit"

    def _heal(self, unit):
        self.choosen_unit = unit
        self.decision = "heal"


class Environment:
    """ Battle environment """

    def render_units(self):
        prnt = {unit.name: {'hp': unit.hp, 'mp': unit.mp, 'st': unit.st} for unit in self.units}
        output = ""
        output += "-" * 35 + "\n"
        output += '{0:19}{1:6}{2:6}{3:6}'.format('', 'HP:', 'MP:', 'ST:') + "\n"
        for key in sorted(prnt):
            output += '{0:15}{hp:6}{mp:6}{st:6}'.format(key, **prnt[key]) + "\n"
        output += "-" * 35 + "\n"
        return output

    def render_map(self):
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

        upper = {'u%s_%s' % (x, y): get_cell_content(x, y, "name") for y in range(ring_height) for x in
                 range(ring_width)}
        footer = {'f%s_%s' % (x, y): (" %s " % get_cell_content(x, y, "hp"))[:4] for y in range(ring_height) for x in
                  range(ring_width)}
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

        return mapr

    def distance(self, pos1, pos2):
        """

        :return: Number of cells between the units
        """
        e_x, e_y = pos1
        u_x, u_y = pos2
        x_range = math.fabs(e_x - u_x)
        y_range = math.fabs(e_y - u_y)
        distance = math.sqrt((x_range ** 2) + (y_range ** 2))
        # print "(UNIT1) X:%s Y:%s" % (e_x, e_y)
        # print "(UNIT2) X:%s Y:%s" % (u_x, u_y)
        # print "DISTANCE = %s" % int(distance)
        return int(distance)
        # if math.fabs(e_x - u_x) <= 1 or math.fabs(e_y - u_y) <= 1:


    def __init__(self, units):
        self.map = Map()
        self.units = units
        for unit in self.units:
            # unit.health = 100
            # unit.attack = 10
            unit.enemies = self.units
            unit.ring = self.map.ring

        clear()
        print "-" * 20
        print """
        _______  _______  _______  _______  ___      _______    _______  _______  _______  ___   __    _
        |  _    ||   _   ||       ||       ||   |    |       |  |  _    ||       ||       ||   | |  |  | |
        | |_|   ||  |_|  ||_     _||_     _||   |    |    ___|  | |_|   ||    ___||    ___||   | |   |_| |
        |       ||       |  |   |    |   |  |   |    |   |___   |       ||   |___ |   | __ |   | |       |
        |  _   | |       |  |   |    |   |  |   |___ |    ___|  |  _   | |    ___||   ||  ||   | |  _    |
        | |_|   ||   _   |  |   |    |   |  |       ||   |___   | |_|   ||   |___ |   |_| ||   | | | |   |
        |_______||__| |__|  |___|    |___|  |_______||_______|  |_______||_______||_______||___| |_|  |__|

            ______________________________________
          ,' -> May the force be with you!         `.
         /  ->   Lets start the battle              |
        |  ->       AND BEAT SOME ASS                 |
        |                                            |
         \  -> ...                                  /
          `._______  _____________________________,'
                  /,'
              O  /'
             /|-
             /|
        """
        print "-" * 20
        time.sleep(2)

        while True:
            r_message = ""
            random.shuffle(self.units)
            for unit in self.units:
                if unit.is_alive:
                    time.sleep(0.2)
                    clear()

                    unit.update()
                    amount = random.randint(-5, 5) + unit.attack
                    if unit.decision == "bighit" and unit.st > 25:
                        if self.distance(unit.choosen_unit.position, unit.position) <= 1:
                            damage = amount / 2 + (amount / 2 * unit.st / 100)
                            unit.st -= 25
                            unit.choosen_unit.hp -= damage * 5
                            kw = {
                                "unit": unit.name,
                                "enemy": unit.choosen_unit.name,
                                "damage": damage
                            }
                            r_message = "{unit} hit {enemy} with {damage} damage".format(**kw)
                    elif unit.decision == "hit" and unit.st > 10:
                        if self.distance(unit.choosen_unit.position, unit.position) <= 1:
                            damage = amount / 2 + (amount / 2 * unit.st / 100)
                            unit.st -= 5
                            unit.choosen_unit.hp -= damage
                            kw = {
                                "unit": unit.name,
                                "enemy": unit.choosen_unit.name,
                                "damage": damage
                            }
                            r_message = "{unit} hit {enemy} with {damage} damage".format(**kw)
                    elif unit.decision == "heal" and unit.mp > 10:
                        unit.mp -= 10
                        unit.choosen_unit.hp += amount
                        kw = {
                            "unit": unit.name,
                            "enemy": unit.choosen_unit.name,
                            "amount": amount
                        }
                        r_message = "{unit} heal {enemy} with {amount} HP".format(**kw)
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
                        kw = {
                            "unit": unit.name,
                            "amount": amount,
                            "final_x": final_x,
                            "final_y": final_y
                        }
                        r_message = "{unit} moved to X:{final_x} Y:{final_y}".format(**kw)

                    x, y = unit.position
                    self.map.ring[y][x] = unit

                    print self.render_map()

                    print ">> " + r_message + " <<"
                    print self.render_units()

            self.units = filter(lambda unit: unit.is_alive, self.units)

            for y, x_row in enumerate(self.map.ring):
                for x, value in enumerate(x_row):
                    if hasattr(value, "is_alive") and not value.is_alive:
                        self.map.ring[y][x] = 0


            for unit in self.units:
                if unit.is_alive:
                    unit.mp += random.randint(0, 2)
                    unit.st += random.randint(0, 2)



            if len(self.units) <= 1:
                break


if __name__ == "__main__":
    from fighters.skypro1111 import Skypro

    from fighters.itymoshenko import ITymoshenko

    u1 = Skypro('sky')
    u2 = ITymoshenko('Tim')
    u3 = Unit('TSOI')
    u4 = Unit('Kaligula')

    from fighters.bodidze import Bodidze


    u1 = Skypro('sky')

    u2 = Unit('COCA')
    u3 = Unit('TSOI')
    u4 = Unit('Kaligula')
    u5 = Unit ('Bod')

    from fighters.dummy_enemy import DummyEnemy, BigDaddy
    from fighters.nikolaychik import Nikolaychik


    u1 = Skypro()
    u1.position = (0, 0)
    u2 = ITymoshenko()
    u2.position = (0, 1)
    u3 = DummyEnemy('TSOI')
    u3.position = (1, 2)
    u3 = DummyEnemy('TSOI')
    u3.position = (2, 3)
    u4 = Bodidze()
    u4.position = (2, 2)
    u5 = BigDaddy()
    u5.position = (3, 3)


    units = [u1, u2, u3, u4]
    units = [u1, u2, u3, u4, u5]
    Environment(units)
