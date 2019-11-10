#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'update_at':
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def _str_(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict.update({
            'created_at': datetime.isoformat(self.created_at),
            'update_at': datetime.isoformat(self.updated_at),
            '__class__': self.__class__.__name__
        })
        return new_dict