from mimetypes import init
from numpy import append
import pytest

class Fruit:
    def __init__(self, name) -> None:
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True

class FruitSalad:
    def __init__(self, *fruit_bowl) -> None:
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()

@pytest.fixture
def fruit_bowl():
    return [Fruit("Apple"), Fruit("Banana")]

def test_fruit_salad(fruit_bowl):
    fruit_salad = FruitSalad(*fruit_bowl)

    assert all(x.cubed for x in fruit_salad.fruit)

@pytest.fixture
def first_entry():
    return 'a'

@pytest.fixture
def order(first_entry):
    return [first_entry]

def test_string(order):
    order.append('b')
    assert order == ['a', 'b']