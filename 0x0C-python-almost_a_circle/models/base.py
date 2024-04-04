#!/usr/bin/python3
"""
Module - class Base
"""
import json


class Base:
    """
    base class of all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries:"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        new_list = []
        file_name = str(cls.__name__) + ".json"
        with open(file_name, 'w', encoding='utf-8') as f:
            if len(list_objs) == 0 or not list_objs:
                f.write(cls.to_json_string(None))
            else:
                for item in list_objs:
                    new_list.append(cls.to_json_string(item.to_dictionary()))
                f.write(str(new_list))
