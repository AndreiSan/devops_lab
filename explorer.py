#!/usr/bin/env python3
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   1.0             2020           Initial version
# --------------------------------------------------------------------


import argparse
from os import scandir
from datetime import datetime
from os import path

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="Plz enter the dir path",
                    nargs="?", const=1, default="..")
parser.add_argument("-r", "--recurse", help="Choose this parameter for recursive listening",
                    action="store_true")
parser.add_argument("-f", "--filter", help="Plz input filter extension if needed"
                                           "( in format end of the file)",
                    nargs="?", const=1, default="")
parser.add_argument("-s", "--sort", help="Choose this option for sorting by date",
                    action="store_true")
parser.add_argument("-V", "--version", action="version", help="Number of version",
                    version="Initial v.1.0, created by Andrei Batura")
args = parser.parse_args()

f_list = []


def get_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    date = d.strftime("%Y %m %d")
    return date


def file_list(d):
    """lists files of the specified directory with options"""
    with scandir(d) as entries:
        for o in entries:
            if o.is_file() and o.name.endswith(args.filter):
                if args.sort:
                    info = o.stat()
                    f_list.append(f"Last modified: {get_date(info.st_mtime)}\t {o.name}")
                else:
                    f_list.append("\t" + o.name)
            elif o.is_dir() and args.recurse:
                # list files recursively
                file_list(o.path)


if path.isdir(args.directory and not path.exists(args.directory)):
    print("the directory does not exist")
    exit(-2)
else:
    if __name__ == "__main__":
        file_list(args.directory)
        f_list.sort()
        for e in f_list:
            print(e)
