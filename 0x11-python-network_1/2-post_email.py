#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]

        values = {"email": email}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as resp:
            content_body = resp.read()
            print(content_body.decode('ascii'))
