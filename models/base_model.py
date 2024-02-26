#!/usr/bin/python3
"""
This is a 'base_model' module and contains BaseModel class
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This class defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Initializes object with public instance attributes:

         - id: string - assigns with an uuid when an instance is created
         (unique id for each BaseModel)

         - created_at: datetime - assigns with the current datetime when
         an instance is created
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.save()

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Prints: [<class name>] (<self.id>) <self.__dict__>
        """
        stmt = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return stmt

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        instance_dict = {'__class__': self.__class__.__name__}

        for k, v in self.__dict__.items():
            instance_dict[k] = v

        instance_dict['created_at'] = instance_dict['created_at'].isoformat()
        instance_dict['updated_at'] = instance_dict['updated_at'].isoformat()
        return instance_dict
