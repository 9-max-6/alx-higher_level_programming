#!/bin/bash
# takes in a URL, lists allowed methods
curl -s -X ALLOW "$1"
