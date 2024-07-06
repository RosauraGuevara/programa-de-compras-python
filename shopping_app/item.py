# item.py

from ownable import set_owner

class Item:
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.quantity = 0  # Inicializa la cantidad en 0
        set_owner(self, owner)
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        return Item.instances

