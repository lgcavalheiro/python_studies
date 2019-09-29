import requests

mydata = {"name": "Juberto", "email": "juberto@jubertomail.com"}
r = requests.post("https://tryphp.w3schools.com/demo/welcome.php", data=mydata)
print(r.status_code)

f = open("response.html", "w+")
f.write(r.text)
