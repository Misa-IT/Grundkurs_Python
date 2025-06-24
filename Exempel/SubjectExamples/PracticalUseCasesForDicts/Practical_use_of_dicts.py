# Det är värt att notera att om hastighet på programmet inte är ett problem kan
# detta lika lätt göras med klasser.

# Vi representerar menyn för ett kafé via ett dictionary:
# Menyn består av tre nivåer:
# Kategorier -> Typ -> Pris

cafe_menu = {
    "coffee": {
        "espresso": 25,
        "americano": 30,
        "latte": 35,
        "cappuccino": 35,
        "mocha": 40,
    },
    "tea": {
        "black": 20,
        "green": 25,
        "herbal": 25,
        "chai latte": 40,
    },
    "pastries": {
        "croissant": 25,
        "muffin": 30,
        "scone": 29,
        "cookie": 15,
    }
}

# Exempelorder
customer_order = [
    ("coffee", "latte"),
    ("pastries", "croissant"),
    ("tea", "chai latte"),
    ("pastries", "mudcake"),
]


# Funktion för att visa kaféets meny
def display_menu(menu):
    print("===== CAFÉ MENU =====")
    for category, items in menu.items():
        print(f"\n{category.upper()}:")
        for item, price in items.items():
            print(f"\t{item.title()}: {price}kr")
    wait()


# Funktion för att behandla en beställning
def process_order(menu, order_items):
    total = 0
    ordered_items = []

    for category, item in order_items:
        if category in menu and item in menu[category]:
            price = menu[category][item]
            total += price
            ordered_items.append((item, price))
        else:
            print(f"\nSorry, {item.title()} is not available. "
                  f"This item will be removed from your order.")

    return ordered_items, total

# Funktion för att invänta en förklaring
def wait():
    input("\nPress ENTER to continue...")



def main():
    # Visa menyn första gången
    display_menu(cafe_menu)

    # Hantera exempelordern. Egentligen borde detta brytas upp i fler funktioner.
    print("\n===== YOUR ORDER =====")
    items, total = process_order(cafe_menu, customer_order)
    for item, price in items:
        print(f"{item.title()}: {price}kr")
    print(f"\nTotal: {total}kr")
    wait()


    # Uppdatera menyn (lägg till nya produkter och ändra ett pris)
    cafe_menu["coffee"]["flat white"] = 38
    cafe_menu["pastries"]["brownie"] = 35
    cafe_menu["coffee"]["latte"] = 38  # Prisökning
    print("\n===== UPDATED MENU =====")
    wait()
    display_menu(cafe_menu)


if __name__ == '__main__':
    main()
