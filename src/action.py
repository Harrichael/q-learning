
from enum import Enum

class Action(Enum):
    up = 0
    down = 1
    left = 2
    right = 3

class ActionComponent:
    def __init__(self, action):
        self.action = action

    def render(self):
        if self.action == Action.up:
            return ' ^ '
        elif self.action == Action.down:
            return ' v '
        elif self.action == Action.left:
            return ' < '
        elif self.action == Action.right:
            return ' > '
        else:
            raise NotImplementedError('Action rendering not implemented: {}'.format(self.action))

