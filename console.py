import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    collection = ['BaseModel']
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
        model_list = HBNBCommand.collection

        if any(model != class_name for model in model_list):
            print("** class doesn't exist **")
            return
        else:
            new_record = BaseModel()
            print(new_record.id)

        def do_show(self, input_type_model):
            if not input_type_model:
                print('** class name missing **')
                return
            extract_class_name = input_type_model.split(" ", 1)[0]
            if extract_class_name != HBNBCommand.collection[0]:
                print("** class doesn't exist **")
                return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
