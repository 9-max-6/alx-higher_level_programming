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
            if list_objs is None:
                f.write("[]")
                return
            if list_objs == [] or len(list_objs) > 0:
                if len(list_objs) == 0:
                    f.write(cls.to_json_string(None))
                else:
                    for item in list_objs:
                        new_list.append((item.to_dictionary()))
                    f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:"""
        file_name = str(cls.__name__) + ".json"
        try:
            f = open(file_name, "r", encoding="utf-8")
            json_string = f.read()
            new_list = cls.from_json_string(json_string)
            final_list = []
            for item in new_list:
                g = cls.create(**item)
                final_list.append(g)
        except FileNotFoundError:
            return []

        return final_list
