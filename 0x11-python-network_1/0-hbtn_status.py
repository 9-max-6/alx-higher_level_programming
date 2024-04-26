#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as resp:
        content_body = resp.read()
        type_resp = type(content_body)
        if "utf-8" in str(resp.getheaders("Content-type")):
            charset = "OK"
        else:
            charset = ""
        formatted_output = f"Body response:\n\
            - type: {type_resp}\n\
            - content: {content_body}\n\
            - utf8 content: {charset}"
    print(formatted_output)
