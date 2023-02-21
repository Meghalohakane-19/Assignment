num = int(input("Enter the number : "))

num1 = 0
num2 = 1
num3 = 0

for i in range (num):
    print(num3 , end =" ")
    num1 = num2
    num2 = num3
    num3 = num1+num2