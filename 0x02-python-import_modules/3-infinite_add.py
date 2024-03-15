#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for i in range(len(sys.argv)):
        sum += int(sys.argv[i])
        i += 1
    
