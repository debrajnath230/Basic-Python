import requests

url ='http://127.0.0.1:8000/Hello%20World'
response =requests.get(url = url)
print(response)
print(dir(response))
print(response.status_code)
print(response.headers)
print(response.request.headers)
