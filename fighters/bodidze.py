from final_battle import Unit
import random
import math

class Bodidze(Unit):
    name = "Bod"

    def update(self):
        self._move(random.randint(1, 1), random.randint(1, 1))

        close_enemies = []
        for en in self.enemies:
            if en != self and en.hp > 0:
                x_dist = math.fabs(en.x - self.x)
                y_dist = math.fabs(en.y - self.y)
                if x_dist <= 1 or y_dist <= 1:
                    close_enemies.append(en)

        if close_enemies:
            weak_enemy = min(close_enemies, key=lambda x: x.hp)
            self._hit(weak_enemy)

        if self.hp < 60:
            getattr(self, "_heal")(self)
