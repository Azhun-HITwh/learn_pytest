from mimetypes import init
import re
from numpy import append, record
import py
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

@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker("fixt_data")
    if marker is None:
        data = None
    else:
        data = marker.args[0]
    
    return data

@pytest.mark.fixt_data(42)
def test_fixt(fixt):
    assert fixt == 42

@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param


def test_a(a):
    pass


def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None


@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    return request.param


def test_b(b):
    pass