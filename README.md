# DevOps Lab 2020: Python Task 3

***
## Description of the pr-stats application:

This python application that gets data from Github API:

You can obtain the following information about interesting pull requests:

- Status of the pull request
- Created date and time
- Number of comments for pull request
- Number of commits for pull requests
- User who opened

Full description you can see if you write
>./pr-stats --help

or just

>  pr-stats -h

# How to use it:

Download pr-stats file. You can run this file in the directory where it is located.

  Simple run: type "pr-stats -u <user>" in the command prompt. Where user is the owner of the Github repository. Default repository name is devops_lab, default pull request number is 31.
  To change it use -r (--repo) and -n (--number) arguments corresponding.

  You can choose next argument options:

  - --status (or -s) status of pull requests
  - --created (or -c)
  - --commits (or -cm)
  - --comments (or -ct)
  - --puller (or -p)


   For get more information use:
   - --help (or -h)
   - --version (or -V)


  Application was developed on CentOS.

## Examples of use script:

>./pr-stats --version

You will see the version of the script

> ./pr-stats -u alenaPy -r devops_lab -n 31 -c -ct -cm -p -s

You have to enter your github login/password and then you will see all parameters of the 31 pull request in the alenaPy user's devops_lab repo's and show all required parameters.

Note, there are not any distributions (*.whl, *.tar.gz, *.rpm and so on, only the project.
