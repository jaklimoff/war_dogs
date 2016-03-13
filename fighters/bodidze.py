from final_battle import Unit
import math

class Bodidze(Unit):
    name = "Bod"

    def update(self):
        if self.hp < 60:
            getattr(self, "_heal")(self)

        close_enemies = []
        for en in self.enemies:
            if en != self and en.hp > 0:
                x_dist = math.fabs(en.x - self.x)
                y_dist = math.fabs(en.y - self.y)
                if x_dist <= 1 or y_dist <= 1:
                    close_enemies.append(en)

        if close_enemies:
            weak_enemy = min(close_enemies, key=lambda x: x.hp)
            if self.st >= 50:
                getattr(self, "_bighit")(weak_enemy)
            self._hit(weak_enemy)
        else:
            dist=[]
            my_x=0
            my_y=0
            for en in self.enemies:
                if en != self and en.hp > 0:
                   dist.append((en.x,en.y))

            close_x,close_y=min(dist)
            if close_x>self.x:
                my_x=1
            if close_x<self.x:
                my_x=-1
            if close_y>self.y:
                my_x=1
            if close_y<self.y:
                my_x=-1
            self._move(my_x, my_y)
