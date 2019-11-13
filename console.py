import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    lista = ["BaseModel", ]
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

    def do_create(self, input):
        """Creates a new instance of BaseModel in JSON"""

        if not input:
            print("** class name missing **")
            return
        a = input.split(" ", 1)[0]
        if a != HBNBCommand.lista[0]:
            print("** class doesn't exist **")
            return
        else:
            #a == HBNBCommand.lista[0]:
            nueva = BaseModel()
            print(nueva.id)

        def do_show(self, input):
            if not input:
                print("** class name missing **")
                return
            a = input.split(" ", 1)[0]
            if a != HBNBCommand.lista[0]:
                print("** class doesn't exist **")
                return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
