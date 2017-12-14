
from src.geom import Point

class Wall:
    def __init__(self, x, y):
        self.loc = Point(x, y)

    @classmethod
    def render(cls):
        return '###'

class Hazard:
    def __init__(self, x, y):
        self.loc = Point(x, y)

    @classmethod
    def render(cls):
        return ' T '

class DonutSpawner:
    def __init__(self, x, y):
        self.loc = Point(x, y)

    @classmethod
    def render(cls):
        return ' D '

class Empty:
    def __init__(self, x, y):
        self.loc = Point(x, y)

    @classmethod
    def render(cls):
        return '   '

class Agent:
    def __init__(self, x, y):
        self.loc = Point(x, y)

    @classmethod
    def render(cls):
        return '<O>'

