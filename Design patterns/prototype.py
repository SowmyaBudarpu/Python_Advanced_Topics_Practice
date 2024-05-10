"""
	Prototype
	- Prototype is a creational design pattern that lets you copy existing objects
	without making your code dependent on their classes.
"""
import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        if name in self._objects:
            del self._objects[name]
        else:
            print(f"No object named {name} is registered.")

    def clone(self, name, **kwargs):
        if name in self._objects:
            cloned_obj = copy.deepcopy(self._objects[name])
            cloned_obj.__dict__.update(kwargs)
            return cloned_obj
        else:
            raise ValueError(f"No object named {name} available for cloning.")

prototype_manager = Prototype()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def client_prototype(prototype, name, obj, **kwargs):
    prototype.register(name, obj)
    return prototype.clone(name, **kwargs)

p = Person('amir', 34)
prototype_manager.register('p1', p)

p_clone = client_prototype(prototype_manager, 'p2', p, age=20)
p_clone2 = client_prototype(prototype_manager, 'p3', p_clone, age=19)

print(p_clone2.__dict__)  # Output: {'name': 'amir', 'age': 19}
