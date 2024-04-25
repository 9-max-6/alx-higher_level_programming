#!/bin/bash
# takes in a URL, lists allowed methods
curl -s -X OPTIONS "$1" | grep "Allow" | cut -d -f 2-
