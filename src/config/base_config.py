
import shlex
from json import loads

'''
Base Class
'''

class BaseConfig:
    _fields_ = []
    def __init__(self, **kwargs):
        for label, value_constructor, *options in self._fields_:
            if options:
                default, = options
                if label not in kwargs:
                    kwargs[label] = default

            try:
                attr_val = value_constructor(kwargs[label])
            except TypeError:
                attr_val = kwargs[label]
            setattr(self, label, attr_val)

    @classmethod
    def from_json_text(cls, json_text):
        json_dict = loads(json_text)
        return cls.from_dict(json_dict)

    @classmethod
    def from_dict(cls, dct):
        return cls(**dct)

    def to_dict(self):
        data = {}
        for label, *_ in self._fields_:
            value = getattr(self, label)
            if isinstance(value, BaseConfig):
                value = value.to_dict()
            elif isinstance(value, list):
                value = [v.to_dict() if isinstance(v, BaseConfig) else v for v in value]
            data[label] = value
        
        return data

