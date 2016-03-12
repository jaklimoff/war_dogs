#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nikolaychik'

from final_battle import Unit
import random
import math

class Nikolaychik(Unit):
    name = "N4k"
    def find_perfect_direction(self):
        return random.randint(-1, 1), random.randint(-1, 1)

    def update(self):
        close_enemies = []
        for en in self.enemies:
            if en != self and en.hp > 0:
                x_dist = math.fabs(en.x - self.x)
                y_dist = math.fabs(en.y - self.y)
                if x_dist <= 1 or y_dist <= 1:
                    close_enemies.append(en)


        if self.hp <= sum([(7.5 + 7.5*enm.st/100) for enm in close_enemies])*1.5:
            getattr(self, "_heal")(self)
            return
        else:
            weak_enemy = min(close_enemies, key=lambda x: x.hp)
            self._hit(weak_enemy)

