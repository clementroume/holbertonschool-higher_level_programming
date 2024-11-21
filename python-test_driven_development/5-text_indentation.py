#!/usr/bin/python3
"""4. Text indentation"""


def text_indentation(text):
    """text_indentation function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # fmt: off
    print(
        text.replace(". ", ".\n\n")
            .replace("? ", "?\n\n")
            .replace(": ", ":\n\n"),
        end="",
    )
    # fmt: on
