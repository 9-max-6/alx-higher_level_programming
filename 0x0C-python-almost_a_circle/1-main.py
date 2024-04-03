#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

try:
    Rectangle(13, "12")
    print("1TypeError exception not raised")
 #   exit(1)
except TypeError as e:
    if str(e) != "height must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Rectangle(13, [13])
    print("2TypeError exception not raised")
except TypeError as e:
    if str(e) != "height must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))


try:
    Rectangle(13, 13.12)
    print("3TypeError exception not raised")

except TypeError as e:
    if str(e) != "height must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Rectangle(13, { 'id': 12 })
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "height must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

print("OK", end="")