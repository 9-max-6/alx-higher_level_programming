#!/bin/python3
"""A script that fetches a URL using requests package"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as resp:
        print("Body response:")
        print(f"    - type: {type(resp.text)}")
        print(f"    - content: {resp.text}")
