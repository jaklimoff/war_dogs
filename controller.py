import random, time

__author__ = 'jaklimoff'

class VisualEffects:
    @staticmethod
    def hello(knight):
        print "+" * 39
        print " Hello %s! Its a tough time." % knight.name
        print " Be aware of monsters and step_mother! "
        print " May the Force be with you! "
        print "+" * 39
        time.sleep(1)


class Controller:
    name = "DEFAULT"

    def __init__(self):
        self.commands = {
            "list": {
                "description": "List of available commands",
                "func": self.list_of_commands
            },
        }

    def command(self):
        command = raw_input("[%s] Command: " % self.name)
        arguments = command.split(" ")
        cmd = arguments[0]
        args = arguments[1:]
        a = self.commands.get(cmd, self.commands["list"])
        try:
            return a['func'](*args)
        except TypeError:
            print "Smth wrong... oO"

    def list_of_commands(self):
        print "=" * 39
        print "List of available commands"
        for key in self.commands:
            desc = self.commands[key]['description']
            print "[%s] : %s" % (key, desc)
        print "=" * 39
        return True


class FightController(Controller):
    name = "FIGHT"
    points = ["Head", "Body", "Legs"]

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

        self._show_list(self.points)
        hit_point = raw_input("What point to hit? ")
        self.hero.hit(enemy, int(hit_point))

        self._show_list(self.points)
        block_point = raw_input("What point to block? ")
        self.hero.block(int(block_point))

        # print "HIT! %s to %s and blocked %s" % (enemy, hit_point, block_point)

        return True

    # TODO: Add multiple phrazes for attack

    win_phrases = [
        "{unit} hit {enemy} to {point} with {damage} damage!"
    ]
    lose_phrases = [
        "{enemy} blocked the {unit} attack!"
    ]

    def show_battle_result(self, unit, damage, enemy):
        if damage > 0:
            print random.choice(self.win_phrases).format(unit=unit.name, enemy=enemy.name, damage=damage,
                                                         point=unit.hit_point)
        else:
            print random.choice(self.lose_phrases).format(unit=unit.name, enemy=enemy.name, damage=damage)

    def show_final_battle_result(self, unit):
        print "{name} is dead!"

class RestController(Controller):
    name = "REST"

    def __init__(self, hero):
        Controller.__init__(self)
        self.hero = hero
        cmd = {
            "ch": {
                "description": "Show hero stat ",
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
            "use": {
                "description": "Wanna drink some potions? [use {item_index}]",
                "func": self.use_a_potion
            },
            "map": {
                "description": "Return available places from Map",
                "func": self.get_places
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
        print "=" * 39
        print """
        Hero name: {name}
        HP: {health}
        Hero agility: {agility}
        Hero strength: {strength}
                --

        """.format(
            name=self.hero.name,
            health="[%s%s] %s%%" % ("#" * (self.hero.hp / 10), "_" * ((100 - self.hero.hp) / 10), self.hero.hp),
            agility=self.hero.agility,
            strength=self.hero.strength,
        )
        self.show_hero_slots()
        print "=" * 39

        return True

    def show_hero_inventory(self):
        print "=" * 39
        print """
        *** Inventory ***
        """
        items = self.hero.bag.get_items()
        index = 0
        for item in items:
            if item.visible_in_bag:
                print "     [%s] %s (%s)" % (index, item.name, item.amount)
            index += 1
        print "=" * 39
        return True

    def wear_to_hero(self):

        self.show_hero_inventory()
        item_index = raw_input("Choose your item [id]! :")
        self.show_hero_slots()
        slot = raw_input("Choose slot! :")
        if slot is None:
            return True

        items = self.hero.bag.get_items()
        item = items[int(item_index)]

        if self.hero.wear(item, slot):
            print "=" * 39
            self.show_hero_slots()
            print "=" * 39
        else:
            print "Error, while wearing!"
        return True

    def use_a_potion(self):
        self.show_hero_inventory()
        potion_index = raw_input("Choose your potion [id]! :")
        items = self.hero.bag.get_items()
        potion = items[int(potion_index)]
        self.hero.use(potion)

    def fight(self):

        print "+" * 39
        print "+ You entered in a fight mode.        +"
        print "+ Let's kill some monsters!           +"
        print "+ You can start the battle now.       +"
        print "+" * 39
        return False


    def get_places(self):
        return self.hero.map

    def go_to(self, place):
        print self.hero.name+" went to the "+place.name

