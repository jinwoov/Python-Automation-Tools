from time import sleep
from functions.yara_app import *
import os

def main():
    while True:
        print("""
                 _ _       __ _                       
                (_|_)_ _  / _| |_  _ ___ _ _  _____ _ 
                | | | ' \|  _| | || / -_) ' \|_ / _' |
               _/ |_|_||_|_| |_|\_,_\___|_||_/__\__,_|
              |__/                                     
                                  Yara Rule Integration
                                           v0.1
        """)
        user_input = input("Which location do you want to scan? ") 
        abpath = os.path.abspath(user_input)
        check_file_yara(abpath)
        user_choice = input("Do you want to quit? (y/n) ")
        if(user_choice == "y" or user_choice == "Y" or user_choice == "yes"):
            print("Thank you for using this application... ")
            sleep(2)
            exit(0)

if __name__ == "__main__":
    main()