#!/usr/bin/python3
"""
module - to_json_string()
"""
import json


def to_json_string(my_obj):
    """
    a function to convert json to string
    """
    x = json.dumps(my_obj)

    return x
