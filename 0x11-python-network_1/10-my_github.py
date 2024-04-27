#!/usr/bin/python3
"""
Script to authenticate Github login
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 2:
        username = argv[1]
        password = argv[2]

        url = "https://api.github.com/user"
        try:
            with requests.get(url, auth=(username, password)) as resp:
                resp.raise_for_status()
                print(resp.json().get("id"))
        except requests.exceptions.Exception as err:
            pass
