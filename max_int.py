# get two inputs to start checking to see which num is higher
num1 = int(input("please enter a number: "))
num2 = int(input("please enter a another number: "))
# set a variables to change to the highest number
highest_num = 0
new_num = 0

# see which number is higher
if num1 > num2:
    highest_int = num1
else:
    highest_num = num2
# go into an enless loop of questions untill the user enter 0 > 
while 0 <= highest_num:
    new_num = int(input("please enter a new number: "))
    if new_num < 0:
        break
    elif new_num > highest_num:
        highest_int = new_num
    else:
        print("previus number was higher.")