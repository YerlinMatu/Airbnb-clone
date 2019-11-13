#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel

classes_dict = {
    'BaseModel': BaseModel,
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

        if _input_class_name not in HBNBCommand.collection_keys:
            print("** class doesn't exist **")
            return

        new_record = classes_dict[_input_class_name]()
        new_record.save()
        print(new_record.id)


    def do_show(self, _input):

        if len(_input.split(' ')[0]) == 0:
            print("** class name missing **")
            return

        if _input.split(' ')[0] not in HBNBCommand.collection_keys:
            print("** class doesn't exist **")
            return

        if len(_input.split()) == 1:
            print("** instance id missing **")
            return

        class_name, class_id = (_input.split(' ')[0], _input.split(' ')[1])
        query_key = class_name + '.' + class_id

        if query_key not in models.storage.all().keys():
            print("** no instance found **")
            return

        print(models.storage.all()[query_key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
