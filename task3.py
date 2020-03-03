#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   2.0             2020           Initial version
# --------------------------------------------------------------------

import re

a = str(input())
b = re.split('[^0-9]', a)
c = re.split('[0-9]', a)
d = list(filter(None, c))

if len(b) != 3:
    print("ERROR")
elif d[1] != "=":
    print("ERROR")
elif d[0] == "+":
    if (int(b[0]) + int(b[1])) == int(b[2]):
        print("YES")
    else:
        print("NO")
elif d[0] == "-":
    if (int(b[0]) - int(b[1])) == int(b[2]):
        print("YES")
    else:
        print("NO")
elif d[0] == "*":
    if (int(b[0]) * int(b[1])) == int(b[2]):
        print("YES")
    else:
        print("NO")
elif d[0] == "/":
    if (int(b[0]) / int(b[1])) == int(b[2]):
        print("YES")
    else:
        print("NO")
else:
    print("ERROR")
