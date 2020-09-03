n = int(input("Enter the length of the sequence: ")) # Do not change this line
sum_int = 0

num1 = 1
num2 = 2
num3 = 3

for i in range(1,n+1):
    if i <= 3:
        print(i)
    else: 
        sum_int = num1 + num2 + num3       
        num1 = num2
        num2 = num3
        num3 = sum_int       
        
        print(sum_int)