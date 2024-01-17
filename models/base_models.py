#!/usr/bin/python3
"""
Base class
- Public instance attributes
    * id
    * created_at
    * updated_at
- __str__
- Public instance methods :
    * save(self)
    * to_dict(self)
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This will be a class from which all models
    will inherit from
    """
    def __init__(self, *args, **kwargs):
        """
        Initialiazes instance for the BaseModel
        Args:
            *args: Lists Unused positional arguments
            *kwargs: Dictionary key-values of arguments
        """
    if kwargs is not None kwargs {}:
        for key in kwargs:
            if key == "created_at":
                self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            elif key == "updated_at":
                self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.__dict__[key] = kwargs[key]

    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """
        This method should be defined to print a string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        This method is responsible for marking an instance as updated
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This method helps in creating a dictionary representation with a "simple object type"
        for the BaseModel
        """

        obj_dict = self.__dict__copy()

        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
