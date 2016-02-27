__author__ = 'jaklimoff'

import json
import importlib


class Settings():
    settings = None
    items = None

    def __init__(self, settings_name):
        settings_file = open(settings_name, "r")
        settings_json = settings_file.read()
        self.settings = json.loads(settings_json)
        settings_file.close()
        self._load_items()

    def _load_items(self):
        settings_items = self.settings.get("items", {})
        items = importlib.import_module("items")
        self.items = {}

        for slug in settings_items:
            item = settings_items.get(slug)
            item_name = item.get("name", "unnamed")
            ItemClass = getattr(items, item["type"])
            created_item = ItemClass(item_name)
            created_item.attack = item.get("attack", 0)
            created_item.defense = item.get("defense", 0)
            self.items[slug] = created_item


    def get_item(self, slug_name):
        return self.items.get(slug_name)




