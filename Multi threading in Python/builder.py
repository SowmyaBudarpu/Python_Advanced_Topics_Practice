"""
	builder
	- Builder is a creational design pattern that lets you construct complex objects step by step.
	The pattern allows you to produce different types and representations of an object using the same
	construction code.
"""
from abc import ABC, abstractmethod

class Car:  # Product
    def __init__(self):
        self._wheel = None
        self._engine = None
        self._body = None

    def set_wheel(self, wheel: 'Wheel'):
        self._wheel = wheel

    def set_body(self, body: 'Body'):
        self._body = body

    def set_engine(self, engine: 'Engine'):
        self._engine = engine

    def detail(self) -> str:
        return (f'Body: {self._body.shape}\n'
                f'Engine: {self._engine.hp}\n'
                f'Wheel: {self._wheel.size}')

class AbstractBuilder(ABC):  # Abstract Builder
    @abstractmethod
    def get_engine(self): pass

    @abstractmethod
    def get_wheel(self): pass

    @abstractmethod
    def get_body(self): pass

class Benz(AbstractBuilder):  # Concrete Builder 1
    def get_body(self):
        body = Body()
        body.shape = 'Suv'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

class Bmw(AbstractBuilder):  # Concrete Builder 2
    def get_body(self):
        body = Body()
        body.shape = 'Sedan'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 340
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20
        return wheel

class Director:
    def __init__(self):
        self._builder = None

    def set_builder(self, builder: AbstractBuilder):
        self._builder = builder

    def construct(self) -> Car:
        car = Car()
        car.set_body(self._builder.get_body())
        car.set_wheel(self._builder.get_wheel())
        car.set_engine(self._builder.get_engine())
        return car

class Wheel:
    def __init__(self):
        self.size = None

class Body:
    def __init__(self):
        self.shape = None

class Engine:
    def __init__(self):
        self.hp = None

def client_builder(builder_key: str) -> str:
    builders = {
        'bmw': Bmw,
        'benz': Benz
    }

    builder_class = builders.get(builder_key)
    if not builder_class:
        return f"No builder found for {builder_key}"

    builder = builder_class()
    director = Director()
    director.set_builder(builder)
    car = director.construct()
    return car.detail()

# Example usage:
print(client_builder('bmw'))  # Expected to return car details as a string
