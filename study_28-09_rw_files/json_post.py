import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

# payload is the data that is sent to the URL
payload = {"title": "foo",
           "body": "bar",
           "userId": 1}
# format the payload to json
headers = {"Content-Type": "application/json; charset=UTF-8"}

r = requests.post(url, json=payload, headers=headers)

print(r.text)
print(json.loads(r.text))
print(r.headers)

f = open("jsondata.json", "w+")
f.write(r.text)

