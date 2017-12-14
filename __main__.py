
import argparse

from src.map.map import Map
from src.sim import Simulator
from src.config.config import Config
from src.action import Action

def run_sim(config):
    with open(config.map_file) as f:
        basement = Map.from_json_text(f.read())

    class agent:
        def step(self, env_map, loc):
            import random
            return random.choice([Action.up, Action.down, Action.left, Action.right])

    sim = Simulator(basement, agent())

    for _ in range(config.sim_iterations):
        sim.step()

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Give me some args')
    parser.add_argument('config_file', help='Configuration parameters')
    args = parser.parse_args()

    with open(args.config_file) as cf:
        config = Config.from_json_text(cf.read())

    run_sim(config)

