#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel

classes_list = {
    'BaseModel': BaseModel,
}


class HBNBCommand(cmd.Cmd):

    collection_keys = classes_list.keys()

    prompt = '(hbnb) '

    def do_quit(self, input):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, input):
        'Exits command console'
        return True

    def emptyline(self):
        """An empty line + ENTER should not execute anything"""
        return False

    def do_create(self, input_type_model):
        """Creates a new instance of BaseModel in JSON"""

        if not input_type_model:
            print('** class name missing **')
            return

        class_name = input_type_model.split(' ', 1)[0]
        model_list = HBNBCommand.collection_keys

        if any(model != class_name for model in model_list):
            print("** class doesn't exist **")
            return
        else:
            new_record = classes_list[class_name]()
            new_record.save()
            print(new_record.id)

    def do_show(self, input):
        class_name, id = (input.split(' ')[0], input.split(' ')[1])
        query_key = class_name + '.' + id
        print(models.storage.all()[query_key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
