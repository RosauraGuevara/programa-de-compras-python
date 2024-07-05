# user.py
from wallet import Wallet

class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)

    def pick_items(self, number, quantity):
        # Implementación para seleccionar items
        pass

    def show_items(self):
        # Implementación para mostrar los items del usuario
        pass
