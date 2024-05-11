"""
	Composite
	- a structural design pattern that lets you compose objects into tree structures
	and then work with these structures as if they were individual objects.
"""
import abc

class Being(abc.ABC):
    """
    Abstract base class for all beings, providing the interface for tree-like structures.
    """
    def add(self, child):
        pass

    def remove(self, child):
        pass

    def is_composite(self):
        return False

    @abc.abstractmethod
    def execute(self):
        pass


class Animal(Being):
    """
    Leaf: Represents individual animal entities in the structure.
    """
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f'Animal {self.name} doing something individually.')


class Human(Being):
    """
    Composite: Can contain other Beings and treats them uniformly.
    """
    def __init__(self):
        self._children = []

    def add(self, child):
        self._children.append(child)

    def remove(self, child):
        self._children.remove(child)

    def is_composite(self):
        return True

    def execute(self):
        print('Human group starting its activities:')
        for child in self._children:
            child.execute()


class Male(Being):
    """
    Leaf: Represents an individual male.
    """
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f'\tMale {self.name} doing something individually.')


class Female(Being):
    """
    Leaf: Represents an individual female.
    """
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f'\tFemale {self.name} doing something individually.')


def client_composite():
    # Creating leaf objects
    jane = Female('Jane')
    katty = Female('Katty')
    brad = Male('Brad')

    # Creating a composite object
    human_group = Human()
    human_group.add(jane)
    human_group.add(katty)
    human_group.add(brad)

    # Executing the composite's operation, which recursively calls its children's operations
    human_group.execute()

client_composite()
