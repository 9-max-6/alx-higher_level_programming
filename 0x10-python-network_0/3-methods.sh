#!/bin/bash
# A script to get allow: header
curl -sX OPTIONS -i "$1" | grep "Allow" | cut -d ' ' -f 2-
