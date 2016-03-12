from final_battle import Unit, Environment
import math, copy

class Terminator(Unit):
    def __init__(self, name = 'Mar`_Ivanovna'):
        Unit.__init__(self)
        self.name = name
        self.near_enemies = None
        self.enemies_sw = None
        self.lh_enemy = Unit()


    def enemy(self):
        self.near_enemies = []
        for i in self.enemies:
            if i == self:
                continue
            elif self.distance(i.position[0], i.position[1]) < 1.5 \
                 and i.is_alive:
                self.near_enemies.append(i)
        return self.near_enemies


    def distance(self, e_x, e_y):
        kat1 = math.fabs(e_x - self.position[0])
        kat2 = math.fabs(e_y - self.position[1])
        dist = math.hypot(kat1, kat2)
        return dist


    def dist(self, e_x, e_y, m_x, m_y):
        kat1 = math.fabs(e_x - m_x)
        kat2 = math.fabs(e_y - m_y)
        dist = math.hypot(kat1, kat2)
        return dist


    def second_wave(self):
        self.enemies_sw = []
        for i in self.enemies:
            if i == self:
                continue
            elif self.distance(i.position[0], i.position[1]) < 2.9 \
                 and i.is_alive:
                self.enemies_sw.append(i)
        return self.enemies_sw


    def en_coord(self, enemy):
        dx = [0, 1, -1]
        dy = [-1, 0, 1]
        dist = 999
        way = []
        for ex in dx:
            for ey in dy:
                go = []
                dist_x = self.position[0]
                dist_x += ex
                dist_y = self.position[1]
                dist_y += ey
                if dist_x < 0 or dist_x > 3 \
                       or 0 > dist_y or dist_y > 3 \
                       or (dist_x == self.position[0] and dist_y == self.position[1]) \
                       or self.map.cell_is_empty(dist_x, dist_y) == False:
                    continue
                if self.dist(enemy.position[0], enemy.position[1], dist_x, dist_y) < dist:
                    dist = self.dist(enemy.position[0], enemy.position[1], dist_x, dist_y)
                    go = [ex, ey]
                    way.append(go)
        return way


    def astar(self, enemy):
        a_map = copy.deepcopy(self.map.ring)
        dx = [-1, 0, 1]
        dy = [-1, 0, 1]
        for i, line in enumerate(a_map):
            for j, value in enumerate(line):
                if value == 0:
                    a_map[i][j] = -1
        sx = self.position[0]
        sy = self.position[1]
        a_map[sx][sy] = 0
        step = 0
        flag = True
        while flag == True:
            for i, line in enumerate(a_map):
                for j, value in enumerate(line):
                    if value == step:
                        for x in dx:
                            for y in dy:
                                xe = i + x
                                ye = j + y
                                if xe < 0 or xe > 3 \
                                   or 0 > ye or ye > 3 \
                                   or (xe == self.position[0] and ye == self.position[1]):
                                    continue
                                elif xe == enemy.position[0] and ye == enemy.position[1]:
                                    flag = False
                                elif a_map[xe][ye] != -1:
                                    continue
                                else:
                                    a_map[xe][ye] = step+1
                    elif value == step - 1:
                        continue
            step += 1
        sflag = True
        way = []
        enx = enemy.position[0]
        eny = enemy.position[1]
        while sflag == True:
            point_way = []
            for x in dx:
                for y in dy:
                    if step == 1:
                        sflag = False
                    xs = enx + x
                    xy = eny + y
                    if xs < 0 or xs > 3 \
                        or 0 > xy or xy > 3 \
                        or (xs == enx and xy == eny):
                        continue
                    elif a_map[xs][xy] == step:
                        enx = xs
                        eny = xy
                        step -= 1
                        point_way = [-x, -y]
                        way.append(point_way)
                        break
                    else:
                        continue
        return way


    def update(self):
        real_en = self.enemy()
        sec_wave = self.second_wave()
        if self.hp <= len(real_en) * 30:
            self._heal(self)
        elif real_en != []:
            self.lh_enemy = real_en[0]
            for i in real_en:
                if i.hp <= 100 and i.hp <= self.lh_enemy:
                    self.lh_enemy = i
            self._hit(self.lh_enemy)
        elif real_en == []:
            if sec_wave != []:
                self._move(0, 0)
            if self.hp < 100:
                self._heal(self)
            else:
                self.way_enemy = self.enemies[0]
                for i in self.enemies:
                    if i.hp <= 100 and i.hp < self.way_enemy.hp:
                        self.way_enemy = i
                way = self.astar(self.way_enemy)
                way.reverse()
                x = way[0][0]
                y = way[0][1]
                self._move(x, y)
