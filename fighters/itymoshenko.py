from final_battle import Unit


class ITymoshenko(Unit):
    name = "Tim"

#    def chose_enemy(self):
#       for enemy in self.enemies:
#           if self.position != self.enemies.position: # how?
#              return enemy
#           else:
#               return None


    def update(self):
        if self.hp > 50 and self.st > 50:
            self._hit(self.chose_enemy())
        elif self.hp < 40 and self.st > 60:
            self._hit(self.enemies[0])
        elif self.hp < 50 and self.st < 40:
            self._heal(self)
        elif self.hp < 40:
            self._heal(self)
        else:
            self._move(2, 2)
