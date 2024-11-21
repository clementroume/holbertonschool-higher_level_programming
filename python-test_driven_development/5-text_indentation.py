#!/usr/bin/python3
"""4. Text indentation"""


def text_indentation(text):
    """text_indentation function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    temp = ""
    for char in text:
        temp += char
        if char in ".:?":
            result += temp.strip() + "\n\n"
            temp = ""

    if temp.strip():
        result += temp.strip()

    print(result, end="")
