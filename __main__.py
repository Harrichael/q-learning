
import argparse
import tqdm

from src.map.map import Map
from src.sim import Simulator
from src.config.config import Config
from src.q_agent import QAgent

def run_sim(config):
    with open(config.map_file) as f:
        basement = Map.from_json_text(f.read())

    agent = QAgent(basement.obj_grid().keys(), config.alpha, config.gamma)
    sim = Simulator(basement, agent)

    progress_bar = lambda itr: tqdm.tqdm(itr, desc='Q Learning Sim', unit='steps')
    with open(config.log_file, 'w+') as log_file:
        for _ in progress_bar(range(config.sim_iterations)):
            sim.step(log_file)

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



