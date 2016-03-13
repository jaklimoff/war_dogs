import math
from final_battle import Unit
import random

class ITymoshenko(Unit):
    name = "Tim"


    def update(self):

        def chose_enemy(self):
            for enemy in self.enemies:
                if enemy != self and enemy.hp > 0:
                    return enemy

        opponent = chose_enemy(self)

        distance = self.distance(self.position, opponent.position)

        if distance == 1:
            if self.hp > 50 and self.st > 40:
                self._hit(opponent)
            elif self.hp > 50 and self.st > 60:
                self._bighit(opponent)
            elif self.hp < 40 and self.st > 60:
                self._hit(opponent)
            elif self.hp < 50 and self.st < 40:
                self._heal(self)
            elif self.hp < 40:
                self._heal(self)
            else:
                back_position = random.randint(2, 2), random.randint(2, 2)
                self._move(*back_position)
        else:   # need to update.
            if self.x > opponent.x and self.y > opponent.y:
                self._move(self.x + 1, self.y + 1)
            elif self.x > opponent.x + 1 and self.y > opponent.y + 1:
                self._move(2, 2)
            elif self.x > opponent.x + 2 and self.y > opponent.y + 2:
                self._move(3, 3)
            else:
                pass

    def distance(self, pos1, pos2):
        """

        :return: Number of cells between the units
        """
        e_x, e_y = pos1
        u_x, u_y = pos2
        x_range = math.fabs(e_x - u_x)
        y_range = math.fabs(e_y - u_y)
        distance = math.sqrt((x_range ** 2) + (y_range ** 2))
        return int(distance)