
from src.action import Action

class QAgent:
    def step(self, env_map, loc):
        import random
        return random.choice([Action.up, Action.down, Action.left, Action.right])

