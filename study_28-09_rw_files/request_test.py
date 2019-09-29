import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.gamewatcherstatic.com%2Fimage%2"
                 "Ffile%2F5%2F9f%2F94565%2Fspiderman_e3_2018_gs.jpg&f=1&nofb=1")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image." + str(image.format).lower()

try:
    image.save(path, image.format)
except IOError:
    print("Could not save image")

# end = False
#
# while not end:
#     params = {"q": input("Search for:")}
#
#     r = requests.get("http://google.com/search", params=params)
#     print("Status: ", r.status_code)
#     print(r.url)
#
#     f = open("./page.html", "w+")
#     f.write(r.text)
#
#     opt = input("another search? (Y/n").lower()
#     if opt == "y" or opt == "":
#         pass
#     else:
#         end = True