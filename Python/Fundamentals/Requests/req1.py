#Api Calls
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/2')
data = response.json()
print(data)
print(response.status_code)