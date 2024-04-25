#!/bin/bash
# takes in a URL, lists allowed methods
curl -s -X OPTIONS "$1"
