#!/usr/bin/python3
"""
A script to list the last 10 commits on a repo
"""
from sys import argv
import requests


if __name__ == '__main__':
    if len(argv) > 2:
        user_name = argv[1]
        repo_name = argv[2]

        url = f"https://api.github.com/repos/{user_name}/{repo_name}/commits"
        headers = {"Accept": "application/vnd.github.v3+json"}
        all_commits = []
        with requests.get(url, headers=headers) as resp:
            marker = 1
            for item in resp.json():
                name = item.get("commit")["committer"]["name"]
                sha = item.get("sha")
                print(f"{sha}: {name}")
                if marker == 10:
                    break
                else:
                    marker+=1
