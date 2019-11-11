import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        'Exits command console'
        return True

    def emptyline(self):
        'An empty line + ENTER should not execute anything'
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
