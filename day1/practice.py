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

# 5. 리스트 - 특정 문자 제거하고 출력
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]
colors.remove("green")
print(colors)

# 6. 리스트 - 특정 문자 추가하고 출력
colors.insert(1, "pink")
print(colors)