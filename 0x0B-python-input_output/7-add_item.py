#!/usr/bin/python3
"""
a script that adds all arguments to a
Python list, and then save them to a file
"""
import sys
to_file = __import__('5-save_to_json_file').save_to_json_file
from_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    args_list = from_file("add_item.json")
    for i in range(1, len(sys.argv)):
        args_list.append(sys.argv[i])

    json_list = to_file(args_list, "add_item.json")
