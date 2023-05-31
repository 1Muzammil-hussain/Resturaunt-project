# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:43:05 2023

@author: SHARJAH LAPTOPS
"""



#Group name:no 4
    #Bug Smashers🦗
    
#Group members:
    # Muzammil Hussain
    # Hafiz Muhammad Jahanzeb Ejaz
    # Ali Haider
    # Muhammad Asfand Kashif
    # Muhammad Furqan Javaid
    # Muhammad Abdullah
    # Muhammad Salman Manzoor

class MenuItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self._price = price
        self._ingredients = ingredients

    def display(self):
        print(f"{self.name} - ${self._price}")
        print("Ingredients:", ", ".join(self._ingredients))
                                      # Muzammil Hussain
    def get_price(self):
        return self._price
    def get_ingredients(self):
        return self._ingredients

    @staticmethod
    def file(name, price, ingredients):
        f = open("list.txt", "a")
        f.write(f"{name}, {price}, {', '.join(ingredients)}\n")
        f.close()


class Appetizer(MenuItem):
    def __init__(self, name, price, ingredients, serving_size):
        super().__init__(name, price, ingredients)
        self.serving_size = serving_size

    def display(self):              # Muhammad Abdullah
        super().display()
        print("Serving Size:", self.serving_size)


class Entree(MenuItem):
    def __init__(self, name, price, ingredients, spice_level):
        super().__init__(name, price, ingredients)
        self.spice_level = spice_level
                                            # Muhammad Asfand Kashif
    def display(self):
        super().display()
        print("Spice Level:", self.spice_level)


class Dessert(MenuItem):
    def __init__(self, name, price, ingredients, is_vegan):
        super().__init__(name, price, ingredients)
        self.is_vegan = is_vegan

    def display(self):       # Muhammad Salman Manzoor
        super().display()
        print("Vegan:", "Yes" if self.is_vegan else "No")


class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def display_menu(self):
        print("----- Menu -----")             # Hafiz Muhammad Jahanzeb Ejaz
        for item in self.menu_items:
            item.display()
            print()

    def find_item(self, name):
        for item in self.menu_items:
            if item.name.lower() == name.lower():
                return item
        return None


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
                                                   #Ali Haider
    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total


# Example usage
menu = Menu()

# Create menu items
appetizer1 = Appetizer("Spring Rolls", 5.99, ["Cabbage", "Carrots", "Mushrooms"], "4 pieces")
entree1 = Entree("Spicy Chicken", 12.99, ["Chicken", "Onions", "Peppers"], "Medium")
dessert1 = Dessert("Chocolate Cake", 7.99, ["Flour", "Sugar", "Cocoa Powder"], False)

# Add menu items to the menu
menu.add_item(appetizer1)
menu.add_item(entree1)
menu.add_item(dessert1)

# Call the file() function
MenuItem.file(appetizer1.name, appetizer1.get_price(), appetizer1.get_ingredients())
MenuItem.file(entree1.name, entree1.get_price(), entree1.get_ingredients())
MenuItem.file(dessert1.name, dessert1.get_price(), dessert1.get_ingredients())

# Display the menu
menu.display_menu()

# Create an order
order = Order()

while True:
    try:
        order_input = input("Enter the name of the item to add to the order (or 'q' to quit): ")
        if order_input.lower() == 'q':
            break

        menu_item = menu.find_item(order_input)
        if menu_item is None:
            raise ValueError("Item not found in the menu.")

        order.add_item(menu_item)          # Muhammad Furqan Javaid
        print(f"{menu_item.name} added to the order.")
    except ValueError as e:
        print(str(e))

# Calculate and display the total
total = order.calculate_total()
print(f"Total: ${total}")
