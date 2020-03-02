#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   1.0             2020           Initial version
# --------------------------------------------------------------------


def leap(y):
    """function to check if the year is leap or not"""
    if (0 != y % 4) or (y % 400 != 0 and y % 100 == 0):
        print("False")
    else:
        print("True")


year = int(input("Input year to check: "))
leap(year)
