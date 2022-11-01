import requests

payload = {"slackUsername": "greatchudim", "backend": True, "age": 29,
           "bio": "An Enthusiast Python Programmer looking at making more waves and growing better"}

r = requests.get("https://httpbin.org/get", params=payload)

print(r.url)
