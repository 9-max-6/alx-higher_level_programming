#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as resp:
        content_body = resp.read()
        type_resp = type(content_body)
        charset = content_body.decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type_resp}")
        print(f"\t- content: {content_body}")
        print(f"\t- utf8 content: {charset}")
