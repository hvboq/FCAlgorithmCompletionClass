#1번 문제
num1 = 1
flag = 0

while num1 <= 6:
    num2 = 1
    while num2 <= num1+flag:
        print("*", end='')
        num2 += 1
    print()
    if (num1%2==0):
        flag +=1
    num1 += 1

print()

#2번 문제
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = list(map(lambda x : str(int(x)+1), a))
print(a)

#4번 문제
print(0)
for i in range(11):
  num = 2**i
  print(min(num,256) , end=' ')