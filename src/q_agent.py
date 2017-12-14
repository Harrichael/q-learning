
import random

from src.action import Action, ActionComponent
from src.map.objects import Wall

class QAgent:
    def __init__(self, state_locs, alpha, gamma):
        self.policy = {}
        for loc in state_locs:
            self.policy[loc] = dict([(a, 0) for a in Action])

        self.alpha = alpha
        self.gamma = gamma

    def step(self, loc):
        return max(self.policy[loc].items(), key=lambda kv: kv[1])[0]

    def update(self, start, dest, action, reward):
        unscaled_delta = reward - self.policy[start][action] + self.gamma * max(self.policy[dest].values())
        self.policy[start][action] += self.alpha * unscaled_delta

    def render_policy(self, env_map):
        objs = env_map.obj_grid()
        for loc, pol_acts in self.policy.items():
            if not isinstance(objs[loc], Wall):
                best_action, action_val = max(pol_acts.items(), key=lambda kv: kv[1])
                objs[loc] = ActionComponent(best_action)

        return env_map.render_objs(objs)

