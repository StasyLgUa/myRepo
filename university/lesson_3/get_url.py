import requests


# headers = {"user-agent": "my-app/0.0.1"}
# parameters = {"name": "Gfgg", "somth": "test"}
# req = requests.get("http://httpbin.org/get", headers=headers, params=parameters)
# body = req.json()
# print(req.text)
# print(body["headers"]["User-Agent"])
# print(req.url)
# print(req.headers["content-type"])
# print(req.text)
# print(req.text)



# f = urllib.request.urlopen("https://chrome.google.com")
# f.read()
# print(f)

books_data = {

    "title": "test_title2",
    "author": "test_author2"
}

#r = requests.get("http://pulse-rest-testing.herokuapp.com/roles/")
r = requests.post("http://pulse-rest-testing.herokuapp.com/books/", data=books_data)
book = r.json()
print(book)

r_d = requests.delete("http://pulse-rest-testing.herokuapp.com/books/" + str(book['id']))
print(r_d.status_code)