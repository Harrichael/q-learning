
import argparse

from src.map.map import Map
from src.sim import Simulator
from src.config.config import Config
from src.q_agent import QAgent

def run_sim(config):
    with open(config.map_file) as f:
        basement = Map.from_json_text(f.read())

    agent = QAgent(basement.obj_grid().keys(), config.alpha, config.gamma)
    sim = Simulator(basement, agent)

    for _ in range(config.sim_iterations):
        sim.step()

    print('Final reward: {}'.format(sim.reward))
    print('Final policy network:')
    print(agent.render_policy(basement))

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Give me some args')
    parser.add_argument('config_file', help='Configuration parameters')
    args = parser.parse_args()

    with open(args.config_file) as cf:
        config = Config.from_json_text(cf.read())

    run_sim(config)



