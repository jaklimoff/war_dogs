#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'skypro1111'

from final_battle import Unit


class Skypro(Unit):
    dmg_coef = 1.5

    def __init__(self, name='Sky'):
        Unit.__init__(self)
        self.name = name
        self.filtered_enemies = []

    def update(self):
        if self.filtered_enemies == []:
            self.filtered_enemies = filter(lambda enemy: (enemy.is_alive and enemy.name != self.name), self.enemies)
        else:
            self.filtered_enemies = filter(lambda enemy: (enemy.is_alive and enemy.name != self.name), self.filtered_enemies)
        min_hp_tup = (enm.hp for enm in self.filtered_enemies)
        if min_hp_tup != []:
            mn = min(min_hp_tup)
        else:
            mn = 0
        enemy = None
        for enm in self.filtered_enemies:
            if enm.hp == mn:
                enemy = enm
        if self.hp <= sum([(7.5 + 7.5*enm.st/100) for enm in self.filtered_enemies])*self.dmg_coef:
            getattr(self, "_heal")(self)
            print "heal"
        else:
            getattr(self, "_hit")(enemy)
            print [(e.name, e.hp) for e in self.filtered_enemies]
            print "{0} hit {1}".format(self.name, enemy.name)