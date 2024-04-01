#!/usr/bin/python3
"""
Python script that lists 10 commits (from the most recent to oldest) of the
repository specified by the owner name and repository name.
"""

import requests
import sys

if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = requests.get(url)

    commits = response.json()[:10]  # Get the first 10 commits

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
