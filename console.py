#!/usr/bin/python3
"""
This is a 'console' module and contains the entry point of the
command interpreter
"""


import cmd
from json import load
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """
    prompt = '(hbnb) '
    __storage_filename = "file.json"
    __base_classname = "BaseModel"

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if args == "":
            print("** class name missing **")
        elif args != self.__base_classname:
            print("** class doesn't exist **")
        else:
            instance = eval(f"{args}()")
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        clargs = args.split()
        length = len(clargs)

        if length == 0:
            print("** class name missing **")
        elif clargs[0] != self.__base_classname:
            print("** class doesn't exist **")
        elif length == 1:
            print("** instance id missing **")
        else:
            classname = self.__base_classname
            key = f"{self.__base_classname}.{clargs[1]}"
            objs = storage.all()

            if not objs or not objs.get(key):
                print("** no instance found **")
            else:
                print(objs[key])

    def check_args(self, args):
        clargs = args.split()
        length = len(clargs)
        classname = self.__base_classname

        if length == 0:
            print("** class name missing **")
        elif clargs[0] != classname:
            print("** class doesn't exist **")
        elif length == 1:
            print("** instance id missing **")
        else:
            key = f"{self.__base_classname}.{clargs[1]}"
            objs = storage.all()

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Exits the program
        """
        return True

    def emptyline(self):
        pass

    """
    def __reload_instances(self):
        
        Reloads objects from file and returns dictionary
        
        filename = self.__storage_filename
        try:
            with open(filename, "r", encoding="utf-8") as afile:
                objs = load(afile)
                return objs
        except FileNotFoundError:
            return False
    """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
