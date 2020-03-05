DevOps Lab 2020: Python Task5
***
## Description of the pr-stats application:

This python application which lists files of the specified directory with the following options:

- Output files only from the parent directory by default or specified it with -d argument
- list files recursively if starts with -r argument
- Filter by file extension if specified it with -f argument
- Order output by filename (by default) by date of creation if starts with -s argument

Full description you can see if you write
>./pr-stats --help

or just

>  pr-stats -h

# How to use it:

Download explorer.py file. You can run this file in the directory where it is located.

  Simple run: type "explorer.py" in the command prompt. Default <path> is ".." (parent directory), default sorting is by filename.
  To change it use -d <path> and -s arguments corresponding.

  You can choose next argument options:

  - --recurse (or -r) for recursive listening (make sure that you have all necessary rights)
  - --created (or -c)
  - --filter <extension or end of files> input filter extension
  - --sort (or -s) for sorting files by last modified date

   For get more information use:
   - --help (or -h)
   - --version (or -V)

  Application was developed for CentOS.

## Examples of use script:

>./explorer.py --version

You will see the version of the script

> ./explorer.py -d ~ -r -s -f .py

List all *.py files recursively sorted by last modified date from the user home directory. 
