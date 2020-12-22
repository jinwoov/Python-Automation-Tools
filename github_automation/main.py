import os, subprocess


os.system("git add .")
user_commit_message = input("Commit message.. ")
os.system(f"git commit -m '{user_commit_message}'")
user_branch = input("Branch? ")
os.system(f"git push origin {user_branch}")