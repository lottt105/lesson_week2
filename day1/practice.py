# # 1. 특정 문자열 출력
# str_dog = "Dog is love"
# idx = str_dog.find("love")
# print(str_dog[idx:idx + 4])

# # 2. 특정 문자열 바꿔서 출력
# print(str_dog.replace("Dog", "Cat"))

# # 3. 문자열 길이 구하고, 특정 문자 개수 출력
# str_la = "lalalalalalalalalalala"
# print(len(str_la))
# print(str_la.count("a"))

# # 4. 특정 문자 제거하고 출력
# str_tel = "010-1234-5678"
# print(str_tel.replace("-", ""))

# # 5. 리스트 - 특정 문자 제거하고 출력
# colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]
# colors.remove("green")
# print(colors)

# # 6. 리스트 - 특정 문자 추가하고 출력
# colors.insert(1, "pink")
# print(colors)

# # 7. 딕셔너리 - 키에 해당하는 값 출력
# a = {'A': 90, 'B': 80, 'C': 70, 'D': 60}
# print(a['B'])

# # 8. 교집합과 차집합 출력
# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7 , 8, 9])
# print(s1 & s2, s1 - s2)

# # 9. 중복이 없는 리스트로 출력
# s = [1, 2, 3, 4, 4, 4, 9, 11, 11, 11, 14]
# print(list(set(s)))

# 입력한 점수가 60 이상이면 pass 아니면 fail 출력
score = int(input("점수가 몇 점인가요?"))
# if score >= 60: print('pass')
# else: print('fail')

if 0 <= score <=100 :
  if score >= 90: print('A')
  elif score >= 80: print('B') 
  elif score >= 70: print('C') 
  elif score >= 60: print('D') 
  elif score >= 50: print('E')
  else: print("F") 
else: print("0~100까지의 숫자만 입력 가능합니다.")