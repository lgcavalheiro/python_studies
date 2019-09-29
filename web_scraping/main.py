from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")  # アニメ
params = {"q": search, "cc": "ca"}
r = requests.get("http://bing.com/search", params=params)

soup = BeautifulSoup(r.text, features="html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("Summary: ", item.find("a").parent.parent.find("p").text)

        children = item.children
        for child in children:
            print("    Child: ", child)
            sibling = child.next_sibling
            if sibling is not None:
                for si in sibling:
                    print("        Sibling: ", si)
