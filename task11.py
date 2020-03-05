#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   2.0             2020             Final version
# --------------------------------------------------------------------


def leap(y):
    """function to check if the year is leap or not"""
    return (0 == y % 4 and (y % 400 == 0 or y % 100 != 0))


if __name__ == "__main__":
    print(leap(int(input())))
