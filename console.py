#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
import shlex

classes_dict = {
    'BaseModel': BaseModel,
    'User': User,
    'City': City,
    'Place': Place,
    'State': State,
    'Amenity': Amenity,
    'Review': Review,
}

class HBNBCommand(cmd.Cmd):

    collection_keys = classes_dict.keys()

    prompt = '(hbnb) '

    def do_quit(self, _input):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, _input):
        'Exits command console'
        return True

    def emptyline(self):
        """An empty line + ENTER should not execute anything"""
        return False

    def do_create(self, _input_class_name):
        """Creates a new instance of BaseModel in JSON"""

        if not _input_class_name:
            print('** class name missing **')
            return

        if _input_class_name not in self.collection_keys:
            print("** class doesn't exist **")
            return

        new_record = classes_dict[_input_class_name]()
        new_record.save()
        print(new_record.id)


    def do_show(self, _input):

        if len(_input.split(' ')[0]) is 0:
            print("** class name missing **")
            return

        if _input.split(' ')[0] not in self.collection_keys:
            print("** class doesn't exist **")
            return

        if len(_input.split()) is 1:
            print("** instance id missing **")
            return

        class_name, class_id = (_input.split(' ')[0], _input.split(' ')[1])
        query_key = class_name + '.' + class_id

        if query_key not in models.storage.all().keys():
            print("** no instance found **")
            return

        print(models.storage.all()[query_key])

    def do_destroy(self, _input):

        if len(_input.split(' ')[0]) is 0:
            print("** class name missing **")
            return

        if _input.split(' ')[0] not in self.collection_keys:
            print("** class doesn't exist **")
            return

        if len(_input.split()) is 1:
            print("** instance id missing **")
            return

        class_name, class_id = (_input.split(' ')[0], _input.split(' ')[1])
        query_key = class_name + '.' + class_id

        if query_key not in models.storage.all().keys():
            print("** no instance found **")
            return

        del models.storage.all()[query_key]
        models.storage.save()

    def do_all(self, _input_class_name):
        if _input_class_name:
            if _input_class_name not in self.collection_keys:
                print("** class doesn't exist **")
                return

        for item_id in models.storage.all().keys():
            item_id = models.storage.all()[item_id]
            print(item_id)
        return

    def do_update(self, _input):
        _input = shlex.split(_input)
        query_key = ''

        if len(_input) is 0:
            print("** class name missing **")
            return

        if _input[0] not in self.collection_keys:
            print("** class doesn't exist **")
            return

        if len(_input) is 1:
            print("** instance id missing **")
            return

        if len(_input) > 1:
            query_key = _input[0] + '.' + _input[1]

        if query_key not in models.storage.all().keys():
            print("** no instance found **")
            return

        if len(_input) is 2:
            print('** attribute name missing **')
            return

        if len(_input) is 3:
            print('** value missing **')
            return
        
        key_name = _input[2]
        input_value = _input[3]
        setattr(models.storage.all()[query_key], key_name, input_value)

        models.storage.all()[query_key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
