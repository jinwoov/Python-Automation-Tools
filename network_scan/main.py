from tools.nm import *
from time import sleep


def exit_app():
    print("exiting...")
    sleep(2)
    exit(0)

def interface():
    user_dictionary ={
    "1": scan_network,
    "2": scan_ip,
    "3": scan_os,
    "4": exit_app
    }
    print("""
       _ _       __ _                       
      (_|_)_ _  / _| |_  _ ___ _ _  _____ _ 
      | | | ' \|  _| | || / -_) ' \|_ / _' |
     _/ |_|_||_|_| |_|\_,_\___|_||_/__\__,_|
    |__/                                     
                                Nmap Scanner 
                                v0.1

    1) Scan network
    2) Scan specific IP
    3) Scan operating system
    4) exit
    """)

    user_input = input("What do you want to accomplish? ")
    user_dictionary[user_input]()

def main():
    while True:
        interface()

if __name__ == "__main__":
    main()

## https://pypi.org/project/python3-nmap/