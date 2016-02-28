from units import Knight, Enemy
from shop import Shop, Map
from items import Weapon

hero = Knight("Dude")
shop = Shop()
map = Map()
map.add_place(shop)
hero.map = map
sword = Weapon('sword')

# print hero.map.places
shop.add_item_to_store(sword, 2, 100)
shop.add_item_to_store(sword, 22, 1100)
print shop.get_store_items()