from final_battle import Unit
import random
__author__ = 'Pro'


class Skypro(Unit):
    name = 'skypro1111'
    def update(self):
        e = filter(lambda enemy: (enemy.is_alive and enemy.name != self.name), self.enemies)
        mn = min([enm.hp for enm in e])
        for enm in self.enemies:
            if enm.hp == mn:
                enemy = enm
        if self.hp <= sum([(7.5 + 7.5*enm.st/100) for enm in e])*1.5:
            getattr(self, "_heal")(self)
            # print "heal"
        else:
            getattr(self, "_hit")(enemy)
            # print "hit"
