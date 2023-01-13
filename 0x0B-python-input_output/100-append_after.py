#!/usr/bin/python3
"""
The '100-append_after' module
Inserts a line of text to a file, after
each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """function definition"""
    with open(filename, mode='r', encoding='utf-8') as fd:
        Text = ""
        for lines in fd:
            Text += lines
            if search_string in lines:
                Text += new_string
        fd.seek(0)
        fd.write(Text)
