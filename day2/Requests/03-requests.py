
import requests

response = requests.get('http://127.0.0.1:8081/api/books/3')
print(response.status_code)
print(response.headers['Content-Type'])
print(response.text)