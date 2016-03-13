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

    def update_1(self):

        close_enemies = []
        print close_enemies

    def update(self):
        weak_enemy = None
        close_enemies = []
        for en in self.enemies:
            if en != self and en.hp > 0:
                x_dist = math.fabs(en.x - self.x)
                y_dist = math.fabs(en.y - self.y)
                if x_dist <= 1 and y_dist <= 1:
                    close_enemies.append(en)
        if close_enemies:
            weak_enemy = min(close_enemies, key=lambda x: x.hp)

        if len(close_enemies) == 0 and self.hp == 100:
            direction = self.find_perfect_direction()
            getattr(self, "_move")(*direction)
            return
        elif len(close_enemies) >= 2:
            direction = self.find_perfect_direction()
            getattr(self, "_move")(*direction)
            return

        if weak_enemy:
            if self.st >= 25: #and self.hp >= weak_enemy.hp:
                getattr(self, "_bighit")(weak_enemy)
                return
            #elif self.hp < weak_enemy.hp:
            #    direction = self.find_perfect_direction()
            #    getattr(self, "_move")(*direction)
            #    return
            if self.st < 25 and self.hp > weak_enemy.hp:
                getattr(self, "_hit")(weak_enemy)
                return
            if self.st < 25 and self.hp < weak_enemy.hp:
                direction = self.find_perfect_direction()
                getattr(self, "_move")(*direction)
                return



        if self.hp < 100:
            getattr(self, "_heal")(self)
            return
        if self.hp == 100:
            direction = self.find_perfect_direction()
            getattr(self, "_move")(*direction)
            return



n4k = Nikolaychik()
n4k.update_1()






