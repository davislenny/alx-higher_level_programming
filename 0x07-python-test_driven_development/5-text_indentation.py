#!/usr/bin/python3
"""
The 'text_indentation module'
"""


def text_indentation(text):
    """
    This function prints 2 new lines every time 
    it encounters the '.?:' strings in
    the text 'text'
    The funtion also raises:
        TypeError if the text 'text' is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for chars in '.?:':
        text = text.replace(chars, chars + '\n\n')
        for i in range(len(text)):
            text = text.replace('\n ', '\n')
    print(text, end ="")
