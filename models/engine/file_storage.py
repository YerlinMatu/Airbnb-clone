#!/usr/bin/python3
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity

classes_dict = {
    'BaseModel': BaseModel,
    'User': User,
    'City': City,
    'Place': Place,
    'State': State,
    'Amenity': Amenity,
    'Review': Review,
}

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
                self.__objects[key] = classes_list[data[key]['__class__']](**data[key])
        except:
            pass