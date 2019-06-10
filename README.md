# Git-create
Simple script meant to automate the creation of a git repository on github by simply typing: `git-create name-of-project`
In order to use, clone this repository.

Create an OAuth token on github

Create a file in the repository called `.env`.

In the `.env` file, add the token using the following layout:

`token: OAUTH_TOKEN`

Ensure that the .py file is executable, if not run the command `chmod +x git-create.py` to fix it.


In the `git-create` file, make sure to modify the `project_path` and `git_path` variables to suit your own needs!

Optional:

Add repository to your PATH variable or copy the file to /usr/local/bin by either adding the following to your .bashrc or similar:

`export PATH=$PATH:/path/to/script`

or

`cp /path/to/file.py /usr/local/bin`. Note, `sudo` may need to be invoked to move the file
