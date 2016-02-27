__author__ = 'jaklimoff'


class Controller:
    def __init__(self):
        self.commands = {
            "list": {
                "description": "List of available commands",
                "func": self.list_of_commands
            },
        }

    def command(self, command):
        arguments = command.split(" ")
        cmd = arguments[0]
        args = arguments[1:]
        a = self.commands.get(cmd, self.commands["list"])
        return a['func'](*args)

    def list_of_commands(self):
        print "=" * 15
        print "List of available commands"
        for key in self.commands:
            desc = self.commands[key]['description']
            print "[%s] : %s" % (key, desc)
        print "=" * 15
        return True


class FightController(Controller):
    def __init__(self, hero):
        Controller.__init__(self)
        self.hero = hero

        cmd = {
            "hit": {
                "description": "Hit, MF, HIT!",
                "func": self.hit_the_enemy
            },
        }
        self.commands.update(cmd)

    def _show_list(self, iter):
        count = 0
        for value in iter:
            print "[%s] %s" % (count, value)
            count += 1

    def hit_the_enemy(self):
        self._show_list(self.hero.enemies)
        enemy_id = raw_input("Enter enemy ID: ")
        enemy = self.hero.enemies[int(enemy_id)]

        points = ["Head", "Body", "Legs"]
        self._show_list(points)
        hit_point = raw_input("What point to hit? ")
        self.hero.hit(enemy, int(hit_point))

        self._show_list(points)
        block_point = raw_input("What point to block? ")
        self.hero.block(int(block_point))

        # print "HIT! %s to %s and blocked %s" % (enemy, hit_point, block_point)

        return True

    def show_battle_result(self, unit, damage, enemy):
        if damage > 0:
            print "{unit} hit {enemy} with {damage} damage!".format(unit=unit.name, enemy=enemy.name, damage=damage)
        else:
            print "{enemy} blocked the {unit} attack".format(unit=unit.name, enemy=enemy.name, damage=damage)

class RestController(Controller):
    def __init__(self, hero):
        Controller.__init__(self)
        self.hero = hero
        cmd = {
            "ch": {
                "description": "Show hero stat",
                "func": self.show_hero_stat
            },
            "inv": {
                "description": "Show hero inventory",
                "func": self.show_hero_inventory
            },
            "wear": {
                "description": "Wear to hero [wear {item_index} {hero_slot}]",
                "func": self.wear_to_hero
            },
            "fight": {
                "description": "Get down to fight, MF!",
                "func": self.fight
            },
        }
        self.commands.update(cmd)

    def show_hero_slots(self):
        for slot in self.hero.slots:
            item_slot = self.hero.slots[slot]
            slot_name = item_slot['name']
            item = item_slot['item']
            print "        {name} ({slot}) :>> {item_name}".format(slot=slot, name=slot_name, item_name=item.name)

    def show_hero_stat(self):
        print "=" * 15
        print """
        Hero name: {name}
        HP: {health}
        Hero agility: {agility}
        Hero strength: {strength}
                --

        """.format(
            name=self.hero.name,
            health="[%s%s] %s%%" % ("#" * (self.hero.hp/10), "_" * ((100 - self.hero.hp)/10), self.hero.hp),
            agility=self.hero.agility,
            strength=self.hero.strength,
        )
        self.show_hero_slots()
        print "=" * 15

        return True

    def show_hero_inventory(self):
        print "=" * 15
        print """
        === Inventory ===
        """
        items = self.hero.bag.get_items()
        index = 0
        for item in items:
            if item.visible_in_bag:
                print "     [%s] %s" % (index, item.name)
            index += 1
        print "=" * 15
        return True

    def wear_to_hero(self, item_index=None, slot=None):
        if item_index is None:
            return True

        items = self.hero.bag.get_items()
        item = items[int(item_index)]

        if self.hero.wear(item, slot):
            print "=" * 15
            self.show_hero_slots()
            print "=" * 15
        else:
            print "Error, while wearing!"
        return True

    def fight(self):
        print "Lets the battle begin!"
        return False