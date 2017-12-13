
from collections import defaultdict
from itertools import chain

from src.geom import Point, Grid
from src.config.base_config import BaseConfig
from src.map.objects import Wall, Hazard, DonutSpawner, Empty

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

    def __repr__(self):
        objs = defaultdict(Empty)
        for obj in self.objects():
            objs[obj.loc] = obj

        render_els = []
        render_els.append([Wall for _ in range(self.grid.num_cols + 2)])
        for row_num in range(self.grid.num_rows):
            row_els = list(chain([Wall], [objs[(col_num, row_num)] for col_num in range(self.grid.num_cols)], [Wall]))
            render_els.append(row_els)
        render_els.append([Wall for _ in range(self.grid.num_cols + 2)])

        return '\n'.join(map(lambda r: ''.join(map(lambda el: el.render(), r)), render_els))

