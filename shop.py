#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'skypro1111'

# from items import Item, Weapon, Armor, BootsArmor, HeadArmor, BodyArmor

class Map():
    def __init__(self):
        self.places = []

    def add_place(self, place):
        self.places.append(place)

    def remove_place(self, place):
        if place in self.places:
            self.places.pop(place)

    def get_all_places(self):
        return self.places


class Shop():
    def __init__(self, name="NOWHERE"):
        self.name = name
        self.store_items = []

    def __str__(self):
        return self.name

    def by_item(self, money, item_id, items_count=1):
        if money.amount >= self.store_items[item_id]['price']:
            money.amount -= self.store_items[item_id]['price'] * items_count
            self.store_items[item_id]['count'] -= 1 * items_count
            i = 1
            sold_items = []
            while i <= items_count:
                sold_items.append(self.store_items[item_id]['item'])
            return sold_items

    def set_store_items(self, store_items={}):
        self.store_items.update(store_items)

    def get_store_items(self):
        return self.store_items

    def add_item_to_store(self, item, items_count, item_price):
        self.store_items.append({'item': item, 'items_count': items_count, 'item_price':item_price})









