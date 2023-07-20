# print(abs(3))
# a = 3
# b = 3
# print(a is b)
# print(id(a), id(b))

# print(sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
# print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(sum({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))

# print(range(5))
# print(sum(range(11))) # 0~10

# c = [9, 2, 3, 0, -1, -2]
# print(sorted(c))

# def negative(x):
#   return x < 0
# print(list(filter(negative, c)))

# print(c)

# colors = ["white", "red", "brown", "blue"]
# names = ["Lukas", "Mike", "Yoon", "Lee"]

# for i, name in enumerate(names):
#   print(f"{name} likes color {colors[i]}")

# a = [1, 2, 2, 2, 3, 4, 5, 6, 6, 6, 7]
# print(list(set(a)))

# print(float(5))
# print(bool(1))
# print(list("python"))
# print(type(5.0))
# print(type(5))

# import os
# print(os.getcwd()) #get current working directory
# print(os.name)

# import time
# # from time import time
# print(time.time())
# print(time.gmtime())

import datetime
now = datetime.datetime.now()
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)