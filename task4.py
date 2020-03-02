#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   1.0             2020           Initial version
# --------------------------------------------------------------------


l = []
a = int(input())
for i in range(a):
    b = input().split(" ")
    if b[0] == "insert":
        l.insert(int(b[1]), int(b[2]))
    elif b[0] == "print":
        print(l)
    elif b[0] == "remove":
        l.remove(int(b[1]))
    elif b[0] == "append":
        l.append(int(b[1]))
    elif b[0] == "sort":
        l.sort()
    elif b[0] == "pop":
        l.pop()
    elif b[0] == "reverse":
        l.reverse()
    else:
        print("Enter correct command")
