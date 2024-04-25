#!/bin/bash
# sends a POST req to the passed URL, and disp the body of the 
curl -X POST "$com/route_6" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
