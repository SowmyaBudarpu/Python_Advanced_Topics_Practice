"""Abstract Factory pattern, where abstract and concrete factories create related products without specifying their concrete classes. 
"""


from abc import ABC, abstractmethod

class Car(ABC):  # Abstract Factory
    @abstractmethod
    def call_suv(self):
        """Create and return an SUV object."""
        pass

    @abstractmethod
    def call_coupe(self):
        """Create and return a Coupe object."""
        pass


class Benz(Car):  # Concrete Factory1
    def call_suv(self):
        return Gla()

    def call_coupe(self):
        return Cls()


class Bmw(Car):  # Concrete Factory2
    def call_suv(self):
        return X1()

    def call_coupe(self):
        return M2()


class Suv(ABC):  # Abstract Product A
    @abstractmethod
    def create_suv(self):
        """Return a description of the SUV."""
        pass


class Coupe(ABC):  # Abstract Product B
    @abstractmethod
    def create_coupe(self):
        """Return a description of the Coupe."""
        pass


class Gla(Suv):  # Concrete Product A1
    def create_suv(self):
        return 'This is your suv benz gla...'


class X1(Suv):  # Concrete Product A2
    def create_suv(self):
        return 'This is your suv bmw x1...'


class Cls(Coupe):  # Concrete Product B1
    def create_coupe(self):
        return 'This is your coupe benz cls...'


class M2(Coupe):  # Concrete Product B2
    def create_coupe(self):
        return 'This is your coupe bmw m2...'


def client_vehicle(order, vehicle_type):  # Client
    brands = {
        'benz': Benz,
        'bmw': Bmw
    }
    if order in brands and vehicle_type in ['suv', 'coupe']:
        factory = brands[order]()
        vehicle = factory.call_suv() if vehicle_type == 'suv' else factory.call_coupe()
        return vehicle.create_suv() if vehicle_type == 'suv' else vehicle.create_coupe()
    else:
        return f"Error: Unsupported brand '{order}' or vehicle type '{vehicle_type}'."


# Example usage:
print(client_vehicle('benz', 'coupe'))  # Expected output: "This is your coupe benz cls..."
print(client_vehicle('audi', 'suv'))    # Expected error handling
