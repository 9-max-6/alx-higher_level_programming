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
        with requests.get(url, auth=(username, password)) as resp:
            if (resp.status_code == 401):
                print("None")
            else:
                print(resp.json().get("id", None))
