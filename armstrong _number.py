


# num=int(input("Enter the number :"))
# if num%10!=0:
#     print("the number is  armstrong")
# else:
#     print("the number is not armstrong")





# num=int(input("Enter the number :"))
# if num%10!=0:
    
#     print("the number is  armstrong")
# else:
#     print("the number is not armstrong")
# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

