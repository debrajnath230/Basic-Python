import requests

url= 'http://127.0.0.1:8000/post/'

username= 'admin'
password ='12345'

payload = {
     'Title' :'Greetings',
    'Content' : 'Welcome to python',
    'created_on' : '01/01/2023 09:45 PM',
    'updated_on' : '01/01/2023 09:45 PM'
}

response = requests.post(url =url,data=payload,auth=(username,password))

print(response.text)