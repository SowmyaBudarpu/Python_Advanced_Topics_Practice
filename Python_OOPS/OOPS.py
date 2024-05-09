class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        # Ensure the price and quantity are not negative
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative")
    
    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def __str__(self) -> str:
        return f"Item({self.name}, {self.price}, {self.quantity})"

# Create instances of the class with attributes initialized
item1 = Item("Phone", 100, 5)
print(item1)  # Printing the object now shows its string representation
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000, 3)
print(item2)
print(item2.calculate_total_price())
