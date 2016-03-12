from final_battle import Unit
import random

class Bodidze(Unit):
    name = "Bod"

    def update(self):
        self._move(random.randint(0, 1), random.randint(0, 1))

        if self.is_alive:
          enemy = filter(lambda enemy: (enemy.is_alive and enemy.name != self.name), self.enemies)[0]
          getattr(self, random.choice(["_hit",]))(enemy)
          if self.hp <= sum([(7.5 + 7.5*enm.st/100) for enm in self.enemies])* 1.5:
            getattr(self, "_heal")(self)
