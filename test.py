from units import Knight, Enemy

hero = Knight("Dude")
orc1 = Enemy("ORC")
ogr = Enemy("OGR")
hero.battle_begin([orc1, ogr])

count = 0
for value in hero.enemies:
    print "[%s] %s" % (count, value.name)
    count += 1
enemy_id = raw_input("Enter enemy ID: ")
enemy = hero.enemies[int(enemy_id)]

print enemy.name