#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            with requests.get(url) as resp:
                resp.raise_for_status()
                print(resp.text)
        except requests.exceptions.HTTPError as errh:
            if errh.response.status_code > 400:
                print("Error code: {}".format(errh.response.status_code))
