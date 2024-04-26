#!/usr/bin/python3
"""
that takes in a URL, sends a request to the URL and displays th
body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.parse
from urllib.error import HTTPError, URLError


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]

    try:
        resp = urllib.request.urlopen(url)
        content_body = resp.read()
        print(content_body.decode("utf-8"))

    except HTTPError as e:
        print("Error code: {}".format(e.__dict__.get("code")))
    except URLError as e:
        print("Error code: {}".format(e.__dict__.get("code")))
