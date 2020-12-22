import os, subprocess


os.system("git add .")
user_commit_message = input("Commit message.. ")
os.system(f"git commit -m {user_commit_message}")
user_branch = input("Branch? ")
cmd = f"git branch -r --contains {user_branch}"
output = os.popen(cmd)
output = str(output)
while output.__contains__("error"):
    user_branch = input("What branch do you want to push to? ")
    cmd = f"git branch -r --contains {user_branch}"
    output = os.popen(cmd)
    output = str(output)
    
# os.system(f"git push origin {user_branch}")