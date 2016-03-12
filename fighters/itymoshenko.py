from final_battle import Unit
import random
import math


class ITymoshenko(Unit):
    name = "Tim"

    @property
    def update(self):

        def chose_enemy(self):
            global enemy
            for enemy in self.enemies:
                if enemy != self:
                    if enemy.hp > 0:
                        return enemy
                    else:
                        return None
                else:
                    return None

        enemy = 0
        opponent = chose_enemy(self)


        if self.hp > 50 and self.st > 50:
            self._hit(opponent)
        elif self.hp < 40 and self.st > 60:
            self._hit(opponent)
        elif self.hp < 50 and self.st < 40:
            self._heal(self)
        elif self.hp < 40:
            self._heal(self)
        else:
            self._move(2, 2)
