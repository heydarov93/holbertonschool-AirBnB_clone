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
    __classname = "BaseModel"

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        check_isok = self.check_args("create", args)
        if check_isok:
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

        check_isok = self.check_args("show", args)

        if check_isok:
            key = f"{self.__classname}.{clargs[1]}"
            objs = storage.all()

            if not objs or not objs.get(key):
                print("** no instance found **")
            else:
                print(objs[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        check_isok = self.check_args("destroy", args)

        if check_isok:
            clargs = args.split()
            objs = storage.all()
            key = f"{self.__classname}.{clargs[1]}"
            del objs[key]
            storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name. Ex: $ all BaseModel or $ all

        If the class name doesn’t exist:
        print ** class doesn't exist ** (ex: $ all MyModel)
        """
        check_isok = self.check_args("all", args)

        if check_isok:
            clargs = args.split()
            objs = storage.all()

            if len(clargs):
                classname = clargs[0]

                def isin_key(classname, key):
                    """
                    checks if classname from args is in key
                    returns True if is in
                    otherwise False
                    """
                    if classname in key.split("."):
                        return True
                    return False

                objs_str_list = [str(obj) for k, obj in objs.items()
                                 if isin_key(classname, k)]
            else:
                objs_str_list = [str(obj) for obj in objs.values()]

            print(objs_str_list)

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

    def check_args(self, op_name, args):
        """
        Checks arguments based on operation name
        Returns True if all checks passed
        Otherwise returns False
        """
        clargs = args.split()
        length = len(clargs)
        classname = self.__classname

        if length == 0:
            if op_name != "all":
                print("** class name missing **")
            else:
                return True
        elif clargs[0] != classname:
            print("** class doesn't exist **")
        elif op_name in ("create", "all"):
            return True
        elif length == 1:
            print("** instance id missing **")
        else:
            return True

        return False

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
