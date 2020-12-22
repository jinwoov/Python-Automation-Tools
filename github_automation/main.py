import os, subprocess

## Git adding
os.system("git add .")
## Commit message and committing
user_commit_message = input("Commit message.. ")
os.system(f"git commit -m '{user_commit_message}'")

# Listing the branches
os.system("git branch")

## Asking for which branch and pushing
user_branch = input("Branch? ")
os.system(f"git push origin {user_branch}")