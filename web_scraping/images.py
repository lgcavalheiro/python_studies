import os

from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO


def start_search():
    search = input("Search term: ")
    region = input("Select region:").lower()
    mkt = input("Select Market Code:")

    params = {"q": search, "cc": region, "safeSearch": "on"
               , "count": 10, "offset": 100, "mkt": mkt, "setLang": mkt}
    r = requests.get("https://wwww.bing.com/images/search", params=params)

    print("Status code is:", r.status_code)
    soup = BeautifulSoup(r.text, features="html.parser")
    links = soup.findAll("a", {"class": "thumb"})
    print("Links found: ", len(links))

    new_path = "./scrapped/" + search + "_" + region + "/"
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    ct = 1
    gotten = 0
    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            img = Image.open(BytesIO(img_obj.content))
            try:
                print("Getting: ", item.attrs["href"])
            except AttributeError:
                print("Couldn't get url from attrs")
            if os.path.isfile(new_path + title):
                img.save(new_path + title + "(" + str(ct) + ")", img.format)
                ct += 1
            else:
                img.save(new_path + title, img.format)
                gotten += 1
        except IOError:
            print("IOError")
        except requests.exceptions.SSLError:
            print("SSLError")

    print("\nScrapped images: ", gotten, "out of: ", len(links), "links")


end = False
opt = ""

while not end:
    try:
        start_search()
    except requests.exceptions.ConnectionError:
        print("Could establish a connection")
        continue

    print()
    opt = input("Another search? (Y/n)").lower()

    if opt == "y" or opt == "":
        continue
    else:
        end = True
