import requests

url ='http://127.0.0.1:8000/Hello%20World'

user ={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

response =requests.get(url = url, headers = user)
print(response.request.headers)

