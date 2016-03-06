from final_battle import Unit


class ITymoshenko(Unit):
    name = "Tim"

    def update(self):
        if self.hp > 0:
            self._hit(self.enemies[0])
        else :
            self._heal(self)



