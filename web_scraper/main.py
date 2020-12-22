from tools.scraper import *
from time import sleep

def main():
    while True:
        print("""
                 _ _       __ _                       
                (_|_)_ _  / _| |_  _ ___ _ _  _____ _ 
                | | | ' \|  _| | || / -_) ' \|_ / _' |
               _/ |_|_||_|_| |_|\_,_\___|_||_/__\__,_|
              |__/                                     
                                        Web Scraper 
                                           v0.1
        """)
        scrape()
        user_choice = input("Do you want to quit? (y/n) ")
        if(user_choice == "y" or user_choice == "Y" or user_choice == "yes"):
            print("Thank you for using this application... ")
            sleep(2)
            exit(0)

if __name__ == "__main__":
    main()