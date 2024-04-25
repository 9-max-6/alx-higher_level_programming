#!/bin/bash
# takes in a URL, sends a GET req, disp body
curl -s "$1" | grep "HTTP" | grep "200" >/dev/null && curl -s 0.0.0.0:5000
