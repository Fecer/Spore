#!/usr/bin/env python3
# The line above ^ is important. Don't leave it out. It should be at the
# top of the file.

import cgi, cgitb # Not used, but will be needed later.

def judge_type(x):
    if(x=="+"):
        return str(int(form['a'].value)+int(form['b'].value))
    else:
        return str(int(form['a'].value)/int(form['b'].value))

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()
'''if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")'''
# Output to stdout, CGIHttpServer will take this as response to the client

print("<p>Hello world!</p>")         # Start of content

'''print("<p>Hello world!</p>")         # Start of content
print ("<p>" +  form['a'].value + "</p>")'''

print("<head>")
print("<title>WOW</title>")
print("</head>")
print("<html>")
print("<p>Wow, Python Server</p>")
print('<IMG src="../image/test.jpg"/>')
print('<form name="input" action="cgi-bin/post.py" method="post">')
print('a:<input type="text" name="a" value="')
try:
    print(form['a'].value)
except:
    print()
print('"><br>')


print('b:<input type="text" name="b" value="')
try:
    print(form['b'].value)
except:
    print()
print('"><br>')

print('    res:')
try:
    print(judge_type(form['type'].value))
except:
    print()
print('<br>')

print('<input type="submit" value="Submit">')
print('</form>')
print('</html>')
