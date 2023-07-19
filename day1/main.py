# print("hello")
# a = 10
# b = 5

# print(a + b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a ** b)
# print("*" * 100)

# happy_face = '☺'
# print(happy_face)

# s = "256"
# print(int(s), type(int(s)))
# print(float(s), type(float(s)))

# random_list  = [3, 3.9, "python", False, True]
# print(random_list)

# for element in random_list:
#   print(type(element))
  
# aa = "Hello world"
# bb = "ESG"
# my_list = [1, 2, 3, 4]
# print(len(aa))
# print(len(bb))
# print(len(my_list))

# print(aa[0:1])
# print(aa[0:2])
# print(aa[0:3])
# print(aa[0:6])

# find_str = "python!"
# print(find_str.find("y"))

# title = "       PytHon ClasS      "
# print(title.lower())
# print(title.upper())
# print(title.strip().lower())

# find_love = "I love lyou"
# print(find_love.find("love"))

# quote = "Life if too short"
# print(quote.replace("too", "very"))
# print(quote.replace("o", "0"))
# print(quote.split())

# split_str = "a:b:c:d"
# print(split_str.split(":"))
# split_a = "Iaknowasplit"
# print(split_a.split("a"))

# a = [1, 2, 3, 4, 5]
# a[2] = 6
# print(a)

# del a[2]
# print(a)

# del a[2:]
# print(a)

# a.extend(['3', '4', '5'])
# print(a)

# a.append(6)
# print(a)

# b = [1, 4, 3, 2, 5]
# b.sort()
# print(b)

# b.reverse()
# print(b)

# b.insert(0, 0)
# print(b)

# c = [4, 5, 6, 4, 5, 6]
# c.remove(6)
# print(c)

# print(c.pop())
# print(c)

# print(c.count(6))

# a = ["A", "B", "c", "D", "e"]
# print(sorted(a))

# d = {'name': 'bin', 'birth':'0601'}
# print(d['name'])
# print(d.get('name'))
# print(d.get('phone'))
# print(d.get('phone', 'value is not'))
# for k in d.keys():
#   print(k)

# print('name' in d)
# print('phone' in d)

# # d.clear()
# # print(d)

# print(d.keys())
# print(d.values())
# print(d.items())
# for key, value in d.items():
#   print("key:", key)
#   print("value:", value)
  
s1 = set([1, 2, 3, 1, 2, 3])
s2 = set([3, 4, 5, 3, 4, 5])
# 교집합
print(s1 & s2, s1.intersection(s2))
# 합집합
print(s1 | s2, s1.union(s2))
# 차집합
print(s1 - s2, s1.difference(s2))
s1.add(4)
print(s1)