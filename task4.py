#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   2.0             2020           Initial version
# --------------------------------------------------------------------


mas = []
a = int(input())
for i in range(a):
    b = input().split(" ")
    if b[0] == "insert":
        mas.insert(int(b[1]), int(b[2]))
    elif b[0] == "print":
        print(mas)
    elif b[0] == "remove":
        mas.remove(int(b[1]))
    elif b[0] == "append":
        mas.append(int(b[1]))
    elif b[0] == "sort":
        mas.sort()
    elif b[0] == "pop":
        mas.pop()
    elif b[0] == "reverse":
        mas.reverse()
    else:
        print("Enter correct command")
