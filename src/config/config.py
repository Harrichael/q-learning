
from src.config.base_config import BaseConfig

class Config(BaseConfig):
    _fields_ = [
        ('map_file', str),
        ('sim_iterations', int),
    ]

