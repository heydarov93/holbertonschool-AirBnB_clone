#!/usr/bin/python3
"""
This is a 'file_storage' module and contains FileStorage class
"""

from json import dump, load
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary '__objects'
        """
        return self.__class__.__objects

    def new(self, obj):
        """
        Sets in '__objects' the 'obj' with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj

    def save(self):
        """
        Serializes '__objects' to the JSON file (path: __file_path)
        """
        filename = self.__class__.__file_path
        objects = self.__class__.__objects.items()
        objs_dicts = {k: v.to_dict() for (k, v) in objects}

        with open(filename, "w", encoding="utf-8") as afile:
            dump(objs_dicts, afile)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, does nothing. If the file
        doesn’t exist, no exception raised)
        """

        filename = self.__class__.__file_path
        try:
            with open(filename, "r", encoding="utf-8") as afile:
                objs_dicts = load(afile)
            objects = self.__class__.__objects
            for k, v in objs_dicts.items():
                stmt = "{}(**{})".format(v["__class__"], v)
                objects[k] = eval(stmt)
        except FileNotFoundError:
            pass
