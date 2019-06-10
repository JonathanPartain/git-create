#!/usr/bin/env bash

## Options for creating a github repo:
# name : string, required
# description : string,
# homepage : string,
# private : boolean, F
# has_issues : boolean, T
# has_projects : boolean, T
# has_wiki : boolean, T
# team_id : integer, only in organization
# auto_init : boolean, F, true to create initial commit with empty readme
# gitignore_template : string, https://github.com/github/gitignore for examples
# license_template : string, https://help.github.com/en/articles/licensing-a-repository#searching-github-by-license-type for extensions, choosealicence.com for options
# allow_squash_merge : boolean, T
# allow_merge_commit : boolean, T
# allow_rebase_merge : boolean, T

# Options to start with:
# name
# description
# gitignore_template
# licence_template
help="Help text goes here"

if [[ $# -eq 0 ]]; then
    echo $help
    exit 0
fi


POSITIONAL=()
while [[ $# -gt 0 ]]; do
    key="$1"

    case $key in
        -n|--name)
        NAME="$2"
        shift # past argument
        shift # past value
        ;;
        -d|--description)
        DESCRIPTION="$2"
        shift
        shift
        ;;
        -gi|--gitignore)
        GITIGNORE="$2"
        shift
        shift
        ;;
        -l|--licence)
        LICENCE="$2"
        shift
        shift
        ;;
        -h|--help)
        echo "$help"
        shift
        ;;
        *)
        echo "$2 is not a known option"
        POSITIONAL+=("$1")
        shift
        ;;
    esac
done

set -- "${POSITIONAL[@]}" # restore positional params

env="./.env"
token=""
# Read env token
while IFS= read -r line; do
    text=$line

    echo "text read from line: $line"
done < "$env"
# check licence and gitignore against wordlist?
echo NAME = $NAME
echo DESCRIPTION = $DESCRIPTION


