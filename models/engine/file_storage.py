#!/usr/bin/python3
"""The file storage module"""

import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """File storage module"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets a new obj"""
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """saves a new obj"""
        objects = FileStorage.__objects
        file = FileStorage.__file_path
        content = {}

        for key, value in objects.items():
            content[key] = value.to_dict()

        with open(file, 'w', encoding="utf-8") as f:
            return f.write(json.dumps(content))

    def reload(self):
        """reloads from a json file"""

        file = FileStorage.__file_path
        # classes = models.classes

        if os.path.isfile(file):
            with open(file, 'r', encoding="utf-8") as f:
                content = f.read()
                formattedContent = json.loads(content)

                for value in formattedContent.values():
                    class_name = value["__class__"]
                    # self.new(classes[class_name](**value))
                    self.new(eval(class_name)(**value))

    def update(self, key, attr, value):
        """updates an instance"""
        model = FileStorage.__objects[key]
        setattr(model, attr, value)

    def delete(self, key):
        """deletes an instance"""
        del FileStorage.__objects[key]
