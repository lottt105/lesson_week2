#구구단
def gugudan(num):
  for i in range(1, 10): 
    print(f'{num} * {i} = {num * i}')

for n in range(2, 10):
  gugudan(n)
  print('-'*15)

#커피자판기
coffee_machine = {'latte' : 2500, 'americano' : 2000}
money, coffee = input().split(', ')
money = int(money)

if coffee in coffee_machine: 
  print(f'커피 나왔습니다! 거스름돈은 {money - coffee_machine[coffee]}원 입니다.')
  
#BMI
weight, height = map(int, input().split(', '))
bmi = weight / ((height/100) ** 2)
if bmi < 18.5: print('저체중입니다.')
elif bmi <= 24.9: print('정상입니다.')
elif bmi <= 29.9: print('과체중입니다.')
else: print('비만입니다.')
print(bmi)
