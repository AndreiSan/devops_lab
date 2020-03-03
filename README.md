# DevOps Lab 2019 (September-December) Python Task 3

***
## Snaphot application description
This python application makes snapshot of the system:
1. Output is written to the plain text file or json file (you can choose it from the command prompt).

2. By default it creates snapshots of the state of the system each 5 minutes (configurable) with:
  - Overall CPU load
  - Overall disk memory usage
  - Overall virtual memory usage
  - Disk I/O information
  - Network I/O information

# How to use it:

  Simple run: type "snapshot" in the command prompt (notice, that results file will be created in current directory).
  You can change period of snapshots and export file type in command prompt. Only json and txt can be chosen. Default settings is txt and 300 sec (5min). For more information type snapshot --help
  Application was developed on CentOS.

# Installing/uninstalling:

  Before using this application please install psutil with pip (pip install psutil). Python version 3.6 requaried.

Created a distributive package of the script (to make wheel from source files):
> python3 setup.py bdist_wheel --universal

Package has to be located in the parent directory.
> pip install snapshot-1.0-py3-none-any.whl
> snapshot --help

Note, there are not any distributions (*.whl, *.tar.gz, *.rpm and so on, only the project, only
..setup.py
and
..snapshot
files

# Examples of use:

> snapshot 10 json

Run system monitoring with 10 sec interval, snapshots created in json format in current directory

> snapshot 600 txt

Run system monitoring with 600 sec (10 minutes) interval, snapshots created in simple txt format in current directory
