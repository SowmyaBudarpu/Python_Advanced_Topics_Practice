class Item:
    def __init__(self, name: str, price: float, quantity: int = 0):
        #Initialize a new instance of Item with name, price, and optional quantity.
        if price < 0:
            raise ValueError(f"Price {price} cannot be negative.")
        if quantity < 0:
            raise ValueError(f"Quantity {quantity} cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        #Calculate the total price based on the price and quantity.
        return self.price * self.quantity

    def __str__(self) -> str:
        #Return a string representation of the item.
        return f"{self.name}: ${self.price} x {self.quantity}"

    def __repr__(self) -> str:
       #return an unambiguous string representation of the item
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# Create instances of the class
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

# Print total prices using the calculate_total_price method
print(item1.calculate_total_price())  
print(item2.calculate_total_price())  

# Print item details
print(item1)  
print(item2)  
