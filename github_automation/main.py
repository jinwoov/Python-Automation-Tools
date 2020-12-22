import os


os.system("git add .")
user_commit_message = input("Commit message.. ")
os.system(f"git commit -m {user_commit_message}")
was_not_push = True
while was_not_push:
    try:
        user_branch = input("Brnach? ")
        os.system(f"git push origin {user_branch}")
        was_not_push = False
    except Exception:
        print("Please enter valid branch.. ")
        continue
