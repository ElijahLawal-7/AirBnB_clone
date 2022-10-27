#!/usr/bin/python3
import models
"""
Base class
"""

import uuid
import datetime


class BaseModel:
    """Base class"""
    def __init__(self, *args, **kwargs):
        """Class constructor"""
        for key in kwargs:
            if key != "__class__":
                if key == 'created_at':
                    aux = datetime.datetime.strptime(kwargs['created_at'],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
                    self.created_at = aux
                elif key == 'updated_at':
                    aux = datetime.datetime.strptime(kwargs['updated_at'],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
                    self.updated_at = aux
                else:
                    setattr(self, key, kwargs[key])
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return specific string format"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Saves the object"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
