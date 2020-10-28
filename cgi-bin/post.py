#!/usr/bin/env python
# The line above ^ is important. Don't leave it out. It should be at the
# top of the file.

import cgi, cgitb # Not used, but will be needed later.

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()
'''if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")'''
# Output to stdout, CGIHttpServer will take this as response to the client
print("<p>Hello world!</p>")         # Start of content
print ("<p>" +  form['firstname'].value + "</p>")