from final_battle import Unit
import random

class ITymoshenko(Unit):
    name = "Tim"

    @property
    def update(self):

        def chose_enemy(self):
            for enemy in self.enemies:
                if enemy != self and enemy.hp > 0:
                    return enemy

        opponent = chose_enemy(self)
        print opponent

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
            back_position = random.randint(2, 2)
            self._move(*back_position)
