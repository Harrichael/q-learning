
import random

from src.geom import Point
from src.action import Action
from src.map.objects import Wall, Hazard, Empty, DonutSpawner

class Simulator:
    def __init__(self, env_map, agent):
        self.map = env_map
        self.agent = agent
        self.agent_loc = random.choice(self.map.empty_spaces()).loc
        self.donut_loc = None
        self.reward = 0

    def step(self, logger):
        if self.donut_loc is None:
            if random.random() < 0.25:
                self.donut_loc = random.choice(self.map.donut_spawns).loc

        action = self.agent.step( self.agent_loc)

        if random.random() > 0.82:
            new_action = random.choice([a for a in Action if a != action])
            logger.write('You attempted to go {}. You fail and go {}.\n'.format(action.name, new_action.name))
            action = new_action
        else:
            logger.write('You go {}.\n'.format(action.name))

        if action == Action.up:
            new_agent_loc = Point(self.agent_loc.x, self.agent_loc.y + 1)
        elif action == Action.down:
            new_agent_loc = Point(self.agent_loc.x, self.agent_loc.y - 1)
        elif action == Action.left:
            new_agent_loc = Point(self.agent_loc.x - 1, self.agent_loc.y)
        elif action == Action.right:
            new_agent_loc = Point(self.agent_loc.x + 1, self.agent_loc.y)
        else:
            raise NotImplementedError('Action not implemented: {}'.format(action))

        objs = self.map.obj_grid()
        dest_obj = objs.get(new_agent_loc, Wall(*new_agent_loc))
        start_loc = self.agent_loc
        reward_delta = 0

        if isinstance(dest_obj, Wall):
            reward_delta -= 1

            if isinstance(objs[self.agent_loc], Hazard) and random.random() < 0.50:
                reward_delta -= 10
                logger.write('You walked into a wall and a tile fell on you. Minus eleven. Ouch.\n')

            else:
                logger.write('You walked into a wall. Minus one.\n')

        elif isinstance(dest_obj, Hazard):
            if random.random() < 0.50:
                reward_delta -= 10
                logger.write('A tile fell on you. Minus ten.\n')
            
            else:
                logger.write('The ceiling creaks, but nothing falls.\n')

            self.agent_loc = new_agent_loc

        elif isinstance(dest_obj, DonutSpawner):
            if self.donut_loc == new_agent_loc:
                reward_delta += 10
                self.donut_loc = None

                logger.write('Wow, a donut! Plus ten.\n')

            else:
                logger.write('Aww, no donut.\n')

            self.agent_loc = new_agent_loc

        elif isinstance(dest_obj, Empty):
            self.agent_loc = new_agent_loc
            logger.write('You walk on.\n')

        else:
            raise NotImplementedError('Object not implemented: {}'.format(dest_obj))
        
        self.reward += reward_delta
        self.agent.update(start_loc, self.agent_loc, action, reward_delta)
        
        logger.write(self.map.render_agent(self.agent_loc))
        logger.write('\n')

