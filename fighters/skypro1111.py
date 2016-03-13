#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'skypro1111'

from final_battle import Unit, Environment

class Skypro(Unit):
    dmg_coef = 1

    def __init__(self, name='Sky'):
        Unit.__init__(self)
        self.name = name
        self.filtered_enemies = []
        self.nearest_enemies = []

    def goto(self, enemies):
        enemy = self.choose_enemy(enemies)
        if enemy != None:
            if abs(self.position[0] - enemy.position[0]) > 1:
                if self.position[0] > enemy.position[0]:
                    x1 = self.position[0]-1
                else:
                    x1 = self.position[0]+1
            else:
                x1 = self.position[0]

            if abs(self.position[1] - enemy.position[1]) > 1:
                if self.position[1] > enemy.position[1]:
                    y1 = self.position[1]-1
                else:
                    y1 = self.position[1]+1
            else:
                y1 = self.position[1]

        self._move(y1, x1)


    def action(self, enemies):
        enemy = self.choose_enemy(enemies)
        if self.st >= 50:
            self._bighit(enemy)
            return
        elif self.hp <= sum([(7.5 + 7.5*enm.st/100) for enm in enemies])*self.dmg_coef and self.mp >= 10:
            self._heal(self)
            return
        else:
            self._hit(enemy)
            return

    def get_all_enemies(self, enemies):
        return filter(lambda enemy: (enemy.is_alive and enemy != self), enemies)

    def get_nearest_enemies(self, enemies):
        return filter(lambda enemy: (abs(abs(enemy.position[0])-abs(self.position[0]))<2
                                     and abs(abs(enemy.position[1])-abs(self.position[1]))<2
        ), enemies)

    def choose_enemy(self, enemies):
        if enemies != []:
            min_hp_list = [enm.hp for enm in self.filtered_enemies]
        else:
            min_hp_list = [0]
        if min_hp_list != []:
            mn = min(min_hp_list)
        else:
            mn = 0
        for enm in enemies:
            if enm.name == 'BigDaddy':
                return enm
            elif enm.hp == mn:
                return enm

    def update(self):
        self.filtered_enemies = self.get_all_enemies(self.enemies)
        self.nearest_enemies = self.get_nearest_enemies(self.filtered_enemies)

        if self.nearest_enemies == []:
            self.goto(self.filtered_enemies)
        else:
            self.action(self.nearest_enemies)