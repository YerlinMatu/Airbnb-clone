#!/usr/bin/python3
import json
import models
from models.base_model import BaseModel

classes = {'BaseModel': BaseModel}

class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        main_key = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({
            main_key : obj
        })

    def save(self):
        new_dict = {}

        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            for key in data:
                self.__objects[key] = classes[data[key]['__class__']](**data[key])
        except:
            pass