
from itertools import chain

from src.geom import Point, Grid
from src.config.base_config import BaseConfig
from src.map.objects import Wall, Hazard, DonutSpawner, Empty, Agent

class Map(BaseConfig):
    _fields_ = [
        ('grid',         lambda d: Grid(**d)),
        ('walls',        lambda els: [Wall(*el) for el in els]),
        ('hazards',      lambda els: [Hazard(*el) for el in els]),
        ('donut_spawns', lambda els: [DonutSpawner(*el) for el in els]),
    ]

    def objects(self):
        for wall in self.walls:
            yield wall

        for hazard in self.hazards:
            yield hazard

        for donut_spawn in self.donut_spawns:
            yield donut_spawn

    def obj_grid(self):
        objs = {}
        for x in range(self.grid.num_cols):
            for y in range(self.grid.num_rows):
                loc = Point(x, y)
                objs[loc] = Empty(*loc)

        for obj in self.objects():
            objs[obj.loc] = obj

        return objs

    def empty_spaces(self):
        objs = self.obj_grid()
        return [obj for obj in objs.values() if isinstance(obj, Empty)]

    def render_objs(self, objs):
        render_els = []
        render_els.append([Wall for _ in range(self.grid.num_cols + 2)])
        for row_num in sorted(range(self.grid.num_rows), reverse=True):
            row_els = list(chain([Wall], [objs[(col_num, row_num)] for col_num in range(self.grid.num_cols)], [Wall]))
            render_els.append(row_els)
        render_els.append([Wall for _ in range(self.grid.num_cols + 2)])

        return '\n'.join(map(lambda r: ''.join(map(lambda el: el.render(), r)), render_els))

    def render_agent(self, agent_loc):
        objs = self.obj_grid()
        objs[agent_loc] = Agent(*agent_loc)
        return self.render_objs(objs)

    def __repr__(self):
        objs = self.obj_grid()
        return self.render_objs(objs)

