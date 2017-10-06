"""
Updated this script so manually added css or js files (e.g. from CDN)
are not replaced with {% static '...' %} Django syntax
"""
import re

CONTENT = "{% load staticfiles %}"
PATH = "templates/index.html"
FILE = open(PATH, "r")
for line in FILE:
    CONTENT += re.sub(r'(href|src)=/generated/(css|js)/(app|manifest|vendor)\.(\w+)\.(css|js)',
                      r'\1="{% static "generated/\2/\3.\4.\5" %}"',
                      line)
FILE.close()

FILE = open(PATH, "w")
FILE.write(CONTENT)
FILE.close()
