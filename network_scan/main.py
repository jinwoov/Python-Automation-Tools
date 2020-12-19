from tools.nm import *


user_dictionary ={
    "1": scan_network,
    "2": scan_ip,
    "3": exit
}


def interface():
    print("""
    1) Scan network
    2) Scan specific IP
    3) exit
    """)

    user_input = input("What do you want to accomplish? ")
    user_dictionary[user_input]()

def main():
    interface()

if __name__ == "__main__":
    main()

## https://pypi.org/project/python3-nmap/