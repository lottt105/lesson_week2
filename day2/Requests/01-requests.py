import requests
import secrets

def main():
  payload = {"access_key": secrets.API_KEY}
  response = requests.get("http://api.exchangeratesapi.io/v1/latest",
                          params=payload)
  
  
  # print(response.status_code)
  # print(response.headers['Content-Type'])
  response_json = response.json()

  # 받은 response를 dictionary화 해서 success, timestamp, base EUR 기준 달러는 얼마인지 출력
  print(response_json['success'])
  print(response_json['timestamp'])
  print(response_json['rates']['USD'])
  
  
if __name__ =="__main__":
  main()