import random
import time




class Unit():
    _hp = 100
    mp = 100
    st = 100

    attack = 10
    decision = ""
    enemies = None
    choosen_unit = None
    name = "Default"

    def __init__(self, name=None):
        if name is not None:
            self.name = name

    def update(self):
        enemy = random.choice(self.enemies)
        getattr(self, random.choice(["_hit", "_heal"]))(enemy)

    @property
    def is_alive(self):
        return self.hp > 0

    @property
    def hp(self):
        return self._hp

    def set_hp(self, value):
        self._hp = min(value, 100)

    def _hit(self, unit):
        self.choosen_unit = unit
        self.decision = "hit"

    def _heal(self, unit):
        self.choosen_unit = unit
        self.decision = "heal"

class Environment:
    """ Battle environment """
    def __init__(self, units):
        self.units = units
        for unit in self.units:
            unit.health = 100
            unit.attack = 10
            unit.enemies = self.units

        print "-" * 20
        print "Battle begin!"
        print "-" * 20

        while True:
            random.shuffle(self.units)
            for unit in self.units:
                if unit.is_alive:
                    unit.update()
                    amount = random.randint(-5,5) + unit.attack
                    if unit.decision == "hit" and unit.st > 10:
                        damage = amount / 2 + (amount / 2 * unit.st / 100)
                        unit.st -= 5
                        unit.choosen_unit.set_hp(unit.choosen_unit.hp - damage)
                    elif unit.decision == "heal" and unit.mp > 10:
                        unit.mp -= 10
                        unit.choosen_unit.set_hp(unit.choosen_unit.hp + amount)


            time.sleep(1)
            for unit in self.units:
                unit.mp += random.randint(0,2)
                unit.st += random.randint(0,2)
                print "-- %s: HP:%s MP:%s ST:%s" % (unit.name, unit.hp, unit.mp, unit.st)

            self.units = filter(lambda unit: unit.is_alive, self.units)
            print "-" * 20

            if len(self.units) <= 1:
                break

if __name__ == "__main__":
    from fighters.itymoshenko import ITymoshenko
    units = [ITymoshenko(), Unit("Pepsi"), Unit("Buratino")]
    Environment(units)
