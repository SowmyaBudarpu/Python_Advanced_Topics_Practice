import csv

class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} must be non-negative."
        assert quantity >= 0, f"Quantity {quantity} must be non-negative."

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open(r'file path', 'r') as f:
                reader = csv.DictReader(f)
                for item in reader:
                    cls(
                        name=item['name'],
                        price=float(item['price']),
                        quantity=int(item['quantity'])
                    )
        except FileNotFoundError:
            print("Error: 'items.csv' file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        return isinstance(num, int)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, "Broken phones count must be non-negative."
        self.broken_phones = broken_phones

    def __repr__(self):
        return super().__repr__() + f", {self.broken_phones} broken phones"

# Example usage
phone1 = Phone("jscPhonev10", 500, 5, 1)
Item.instantiate_from_csv()  # Make sure the CSV is formatted correctly and the file exists
print(Item.all)
