#!/usr/bin/python3
"""
 takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user
 with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]

        pay_load = {"q": q}
        try:
            with requests.post(url, data=pay_load) as resp:
                resp.raise_for_status()
                req_id = resp.json().get("id", None)
                name = resp.json().get("name", None)
                if name and req_id:
                    print(f"[{req_id}] {name}")
                else:
                    print("No result")
        except requests.exceptions.Exception as err:
            print("Not a valid JSON")