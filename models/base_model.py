#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
      return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict.update(
            {
              'created_at': datetime.isoformat(self.created_at),
              'updated_at': datetime.isoformat(self.created_at),
              '__class__': self.__class__.__name__
            }
        )
        return new_dict
