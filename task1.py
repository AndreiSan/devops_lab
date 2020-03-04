#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   2.0             2020           Initial version
# --------------------------------------------------------------------


def leap(y):
    """function to check if the year is leap or not"""
    print(not(0 != y % 4 or (y % 400 != 0 and y % 100 == 0)))


year = int(input())
leap(year)
