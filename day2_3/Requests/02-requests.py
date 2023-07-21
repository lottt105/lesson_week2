import requests

response = requests.get("http://127.0.0.1:8000/api/books")

  # print(response.statu/_code)
  # print(response.headers['Content-Type'])
response_json = response.json() 