#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   3.0             2020            Final version
# --------------------------------------------------------------------

import re

a = input()
b = list(map(int, re.split('[^0-9]', a)))
c = re.split('[0-9]', a)
d = list(filter(None, c))

if len(b) != 3:
    print("ERROR")
elif d[1] != "=":
    print("ERROR")
elif d[0] == "+":
    if (b[0] + b[1]) == b[2]:
        print("YES")
    else:
        print("NO")
elif d[0] == "-":
    if (b[0] - b[1]) == b[2]:
        print("YES")
    else:
        print("NO")
elif d[0] == "*":
    if (b[0] * b[1]) == b[2]:
        print("YES")
    else:
        print("NO")
elif d[0] == "/":
    if (b[0] / b[1]) == b[2]:
        print("YES")
    else:
        print("NO")
else:
    print("ERROR")
