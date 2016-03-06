#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'skypro1111'

from final_battle import Unit



class Skypro(Unit):
    name = 'skypro1111'
    dmg_coef = 1.5
    def update(self):
        e = filter(lambda enemy: (enemy.is_alive and enemy.name != self.name), self.enemies)
        min_hp_tup = (enm.hp for enm in e)
        if min_hp_tup:
            mn = min(min_hp_tup)
        else:
            mn = 0

        for enm in self.enemies:
            if enm.hp == mn:
                enemy = enm
        if self.hp <= sum([(7.5 + 7.5*enm.st/100) for enm in e])*self.dmg_coef:
            getattr(self, "_heal")(self)
        else:
            getattr(self, "_hit")(enemy)
