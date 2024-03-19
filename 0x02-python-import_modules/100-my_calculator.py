#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1.py as calc
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./{} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    if sys.argv[2] not in "+-*/":
        print("Unknown operators. Available operators: +, -, * and /")
        sys.exit(1)
    elif (sys.argv[2]) == "+":
        print("{}".format(calc.add(int(sys.argv[1]), int(sys.argv[3]))))
    elif (sys.argv[2]) == "-":
        print("{}".format(calc.sub(int(sys.argv[1]), int(sys.argv[3]))))
    elif (sys.argv[2]) == "*":
        print("{}".format(calc.mul(int(sys.argv[1]), int(sys.argv[3]))))
    else:
        print("{}".format(calc.div(int(sys.argv[1]), int(sys.argv[3]))))