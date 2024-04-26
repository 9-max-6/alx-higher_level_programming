#!/usr/bin/python3
"""
A script to take in a URL, send a request and disaplay
the value ofthe variable X-Request-Id in response header.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]

        with requests.get(url) as resp:
            req_id = resp.headers.get("X-Request-Id")
            print(req_id)
