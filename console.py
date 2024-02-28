#!/usr/bin/python3
"""
This is a 'console' module and contains the entry point of the
command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program
        """
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
