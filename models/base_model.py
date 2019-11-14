#!/usr/bin/python3
from datetime import datetime
import models
import uuid

format_time = '%Y-%m-%dT%H:%M:%S.%f'
class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__ = kwargs
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], format_time)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], format_time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        if 'created_at' in new_dict:
            new_dict.update({'created_at': 
                new_dict['created_at'].strftime(format_time)})
        if 'updated_at' in new_dict:
            new_dict.update({'updated_at':
                new_dict['updated_at'].strftime(format_time)})
        new_dict.update({'__class__': self.__class__.__name__})
        return new_dict