
import readline
from seller import Seller
from customer import Customer
from item import Item
from tabulate import tabulate

def initialize_products(seller):
    products = [
        ("CPU", 40830),
        ("Memoria RAM", 13880),
        ("Placa madre", 28980),
        ("Unidad de fuente de alimentación", 8980),
        ("Carcasa de PC", 8727),
        ("Disco duro de 3.5 pulgadas", 10980),
        ("SSD de 2.5 pulgadas", 13370),
        ("SSD M.2", 12980),
        ("Refrigeración para CPU", 13400),
        ("Tarjeta gráfica", 23800)
    ]

    for idx, (product_name, price) in enumerate(products):
        item = Item(product_name, price, seller)
        seller.stock.append({
            "number": idx,
            "label": item.label(),
            "items": [item] * 10  # Inicialmente 10 unidades de cada producto
        })

seller = Seller("DIC Store")
initialize_products(seller)

print("🤖 Por favor, introduce tu nombre")
customer = Customer(input())

amount_to_deposit = None
while amount_to_deposit is None:
    try:
        print("🏧 Por favor, introduce la cantidad que deseas cargar en tu billetera")
        amount_input = input().strip()
        
        # Limpiar la entrada de caracteres no deseados antes de convertir a entero
        amount_cleaned = ''.join(filter(str.isdigit, amount_input))
        
        amount_to_deposit = int(amount_cleaned)
    except ValueError:
        print("Cantidad inválida. Introduce un número entero válido.")

customer.wallet.deposit(amount_to_deposit)

print("🛍️ Comienza la compra")
end_shopping = False
while not end_shopping:
    seller.show_items()  # Mostrar los productos disponibles del vendedor

    print("️️⛏ Por favor, introduce el número del producto")
    number = None
    while number is None:
        try:
            number_input = input().strip()
            number_cleaned = ''.join(filter(str.isdigit, number_input))
            number = int(number_cleaned)
        except ValueError:
            print("Número de producto inválido. Introduce un número entero válido.")

    print("⛏ Introduce la cantidad que deseas")
    quantity = None
    while quantity is None:
        try:
            quantity_input = input().strip()
            quantity_cleaned = ''.join(filter(str.isdigit, quantity_input))
            quantity = int(quantity_cleaned)
        except ValueError:
            print("Cantidad inválida. Introduce un número entero válido.")

    # Obtener los artículos del vendedor
    items = seller.pick_items(number, quantity)

    if items is None:
        print("Lo sentimos, no hay suficientes existencias de este producto.")
        continue

    # Agregar los artículos al carrito del cliente
    for item in items:
        item.quantity = quantity  # Establecer la cantidad seleccionada en el artículo
        customer.cart.add(item)

    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Total a pagar: {customer.cart.total_amount()}")

    print("😭 ¿Deseas finalizar la compra? (sí/no)")
    end_shopping = input() == "sí"

    if end_shopping:
        print("💸 ¿Deseas confirmar la compra? (sí/no)")
        if input() == "sí":
            if customer.cart.check_out():
                print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultado ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
                print(f"️🛍️ Propiedad de {customer.name}")
                customer.show_items()
                print(f"😱👛 Saldo en la billetera de {customer.name}: {customer.wallet.balance}")

                print(f"📦 Disponibilidad de la tienda {seller.name}")
                seller.show_items()

                print("🛒 Contenido del carrito")
                customer.cart.show_items()
                print(f"🌚 Total a pagar: {customer.cart.total_amount()}")

                customer.cart.empty_cart()  # Vaciar el carrito después de confirmar la compra

                print("😭 Gracias por tu compra!")
                break  # Salir del bucle principal después de confirmar la compra
            else:
                print("No se pudo completar la compra. Saldo insuficiente.")

print("🎉 Fin del programa")
