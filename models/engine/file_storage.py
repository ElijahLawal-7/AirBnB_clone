#!/usr/bin/python3
"""A class that inherence from BaseModel"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return a dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """save in __objects an object"""
        stri = obj.__class__.__name__
        stri = stri + "." + obj.id
        self.__objects.setdefault(stri, obj)

    def save(self):
        """Save in json file a serialized dictionary"""
        otro = {}
        for key in self.__objects:
            otro.setdefault(key, self.__objects[key].to_dict())
        jdic = json.dumps(otro)
        with open(self.__file_path, "w") as f:
            f.write(jdic)

    def reload(self):
        """load from json file gets a dictionary of
        dictionary and change to a dictionary of objects"""
        class_list = [BaseModel, User, Place, State, City, Amenity, Review]
        try:
            otro = {}
            otro2 = {}
            with open(self.__file_path, "r") as f:
                otro = json.load(f)
            for key in otro:
                y = otro[key]["__class__"]
                for idx, item in enumerate(class_list):
                    if y in str(item):
                        a = class_list[idx](**otro[key])
                otro2.setdefault(key, a)
            self.__objects = otro2
        except:
            pass
