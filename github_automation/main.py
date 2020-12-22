import os


os.system("git add .")
user_commit_message = input("Commit message.. ")
os.system(f"git commit -m {user_commit_message}")
user_branch = input("Brnach? ")
os.system(f"git push origin {user_branch}")
