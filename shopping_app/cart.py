from ownable import set_owner

class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        # Verificar si el artículo ya está en el carrito y solo incrementar la cantidad
        found_item = next((x for x in self.items if x.name == item.name), None)
        if found_item:
            found_item.quantity += item.quantity
        else:
            self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            return False
        
        for item in self.items:
            item.owner.wallet.deposit(item.price)
            set_owner(item, self.owner)  # Establecer propietario del artículo al propietario del carrito
        
        self.items.clear()  # Vaciar el carrito después de la compra
        return True

    def show_items(self):
        if not self.items:
            print("El carrito está vacío.")
        else:
            for item in self.items:
                print(f"{item.quantity} {item.name} precio: {item.price}")

    def empty_cart(self):
        self.items.clear()