#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response.
"""
import sys
import requests
from requests.exceptions import HTTPError


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[0]
        try:
            with requests.get(url) as resp:
                print(resp.text)
        except HTTPError as errh:
            if errh.response.status_code > 400:
                print("Error code: {}".format(errh.response.status_code))
