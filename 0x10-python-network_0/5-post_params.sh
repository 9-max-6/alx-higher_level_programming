#!/bin/bash
# sends a POST req to the passed URL, and disp the body of the 
curl -X POST "$1" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
