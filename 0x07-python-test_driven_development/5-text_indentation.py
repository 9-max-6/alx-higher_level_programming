#!/usr/bin/python3
"""
module: text_indentation
"""


def text_indentation(text):
    """
    Function: that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
    text - the text to be printed.

    Raises:
    TypeError - if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    spec = ".?:"
    new_line = True
    for item in text:
        if item == " " and new_line:
            continue
        print(item, end="")
        new_line = False
        if item in spec:
            print("\n\n", end="")
            new_line = True
