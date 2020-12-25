import yara, os


def check_file_yara(file_name):
    user_path = input("What path is Yara rule in? ")
    path = os.path.abspath(user_path)
    rules = yara.compile(filepath = path)
    abspath = os.path.abspath(file_name)
    matches = rules.match(data = abspath)
    if(len(matches) > 0):
        print("[-] Did not passed the rule ❌")
    else:
        print("[+] Passed the Yara rule ✔")
