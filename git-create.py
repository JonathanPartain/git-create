#!/usr/bin/env python3
import os
import argparse
import json
import requests


def create_repository(args):
    # URL to create repo
    URL = "https://api.github.com/user/repos"

    # Build json object to be POSTed to github
    post = {}
    post["name"] = args.name
    # description argument
    if args.description:
        post["description"] = args.description
    # gitignore template
    if args.gitignore:
        post["gitignore_template"] = args.gitignore
    # license template
    if args.license:
        post["license_template"] = args.license

    # get authorization token
    env = open(".env", "r")
    line = env.read()
    data = line.strip().split(" ")
    if data[0] == "token:":
        token = data[1]

    # create header for auth
    header = {}
    # add token to post
    tokenstr = "token " + token
    header["Authorization"] = tokenstr
    header["Accept"] = "application/vnd.github.v3+json"
    json_body = json.dumps(post)
    print(header)
    print(json.dumps(post))

    # request to create repository
    r = requests.post(URL, headers=header, data=json_body)
    # print(r.text)



## Options for creating a github repo
# name : string, required
# description : string,
# homepage : string,
# private : boolean, F
# has_issues : boolean, T
# has_projects : boolean, T
# has_wiki : boolean, T
# team_id : integer, only in organization
# auto_init : boolean, F, True to create inital commit with empty README.md
# gitignore_template : string, https://github.com/github/gitignore for examples
# license_template : string, https://help.github.com/en/articles/licensing-a-repository#searching-     github-by-license-type for extensions, choosealicense.com for options
# allow_squash_merge : boolean, T
# allow_merge_commit : boolean, T
# allow_rebase_merge : boolean, T

# Options to start with:
# name
# description
# gitignore_template
# license_template

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Name of the github repo to be created, may not contain spaces")
parser.add_argument("--description", help="description of the repo")
parser.add_argument("--gitignore", help="Name of a gitignore template. Names available at https://github.com/github/gitignore")
parser.add_argument("--license", help="Name of a license. Names available at https://help.github.com/en/articles/licensing-a-repository#searching-github-by-license-type. Popular ones are: gpl-2.0/3.0, mit and apache-2.0")
args = parser.parse_args()

# URL to create repo
URL = "https://api.github.com/user/repos"

# Documents folder
# create folder with args.name
os.system("mkdir ~/Documents/github-projects/" + args.name)
# create repository
create_repository(args)
# clone repository into folder
clone = "git@github.com:JonathanPartain/" + args.name
os.system("git clone " + clone + " ~/Documents/github-projects/" + args.name)

