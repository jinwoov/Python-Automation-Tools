from bs4 import BeautifulSoup
import requests, lxml

def scrape():
    try:
        url = input("please enter url of your choice.. ")
        if not "http" in url:
            url = f"https://{url}"

        response = requests.get(url, timeout=5)
        response_content = response.text
        bs = BeautifulSoup(response_content, "lxml")
        print(response_content)
        user_search= input("what keyword do you want to search? ")
        output = bs(text=lambda t: user_search in t)
        query = output[0]
        if(query[0] == "."):
            query = query [2:]
        print(query)
    except IndexError as msg:
        print("There was no matching keyword.. Perhaps check your casing!")
        pass
    except Exception as msg:
        print(f"It was errorred out due to: {msg}")
        pass