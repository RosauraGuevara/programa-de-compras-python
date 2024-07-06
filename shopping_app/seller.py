# seller.py

from user import User
from tabulate import tabulate

class Seller(User):
    def __init__(self, name):
        super().__init__(name)
        self.stock = []  # Inicializar una lista para el stock del vendedor



    def pick_items(self, number, quantity):
        items = self._find_items_by_number(number)
        if not items or len(items["items"]) < quantity:
            return None  # No hay suficientes existencias del producto
        else:
            picked_items = items["items"][:quantity]
            for item in picked_items:
                self.stock[number]["items"].remove(item)
            return picked_items



    def show_items(self):
       table_data = []  
       for stock_item in self.stock:  
         table_data.append([f"#{stock_item['number']}", stock_item['label']['name'], stock_item['label']['price'], len(stock_item['items'])])
       print(tabulate(table_data, headers=["Número", "Nombre del producto", "Precio", "Cantidad"], tablefmt="grid"))

    def items_list(self):
        return self.stock

    def _find_items_by_number(self, number):
        return next((item for item in self.stock if item["number"] == number), None)
