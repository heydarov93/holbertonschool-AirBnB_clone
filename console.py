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
    __classnames = ("BaseModel",)

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
            key = f"{clargs[0]}.{clargs[1]}"
            objs = storage.all()
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
            key = f"{clargs[0]}.{clargs[1]}"
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

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

        Usage:
        - update <class name> <id> <attribute name> "<attribute value>"
        """

        check_isok = self.check_args("update", args)
        if check_isok:
            clargs = args.split()
            objs = storage.all()
            key = clargs[0] + "." + clargs[1]

            instance = objs[key]
            setattr(instance, clargs[2], clargs[3])
            instance.save()

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

        For op_name = "create" valid args are:
        - <class name>

        For op_name = "all" valid args are:
        - ""
        - <class name>

        For op_name = "show" valid args are:
        - <class name> <id>

        For op_name = "update" valid args are:
        - <class name> <id> <attribute name> "<attribute value>"

        """
        clargs = args.split()
        length = len(clargs)
        classnames = self.__classnames

        if length == 0:
            if op_name != "all":
                print("** class name missing **")
            else:
                return True
        elif not clargs[0] in classnames:
            print("** class doesn't exist **")
        elif op_name in ("create", "all"):
            return True
        elif length == 1:
            print("** instance id missing **")
        else:
            key = f"{clargs[0]}.{clargs[1]}"
            objs = storage.all()

            if not objs or not objs.get(key):
                print("** no instance found **")
            elif op_name in ("show", "destroy"):
                return True
            elif not length > 2:
                print("** attribute name missing **")
            elif not length > 3:
                print("** value missing **")
            else:
                return True

        return False

    def do_test(self, args):
        print(args)

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
