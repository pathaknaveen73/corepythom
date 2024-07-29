# a=input("Enter the mark in english ")
# b=input("Enter the mark in hindi ")
# c=input("Enter the mark in math ")
# d=input("Enter the mark in physics ")
# e=input("Enter the mark in computer ")33333333
a=int(input("Enter Marks in English :")) 
b=int(input("Enter Marks in Maths: ")) 
c=int(input("Enter Marks in Physics: ")) 
d=int(input("Enter Marks in Chemistry: ")) 
e=int(input("Enter Marks in Computer Science: ")) 
avg=((a+b+c+d+e)/500)*100 
#print(avg)
if(avg>=90):
	print("Distinction ", avg) 
elif(avg>=70 and avg>80): 
	print("Excellent ", avg ) 
elif (avg>=60 and avg<70): 
	print("Good ", avg) 
elif (avg<60): 
	print( "Fail",avg)
else:
	print("you enter once")
# a=float(input("Enter Marks in English :\t")) 
# b=float(input("Enter Marks in Maths: \t")) 
# c=float(input("Enter Marks in Physics: \t")) 
# d=float(input("Enter Marks in Chemistry: \t")) 
# e=float(input("Enter Marks in Computer Science: \t")) 
# avg=((a+b+c+d+e)/500)*100 
# if(avg>=80): 
     
# 	print("Congratulations ! You have secured first Class, and your percentage is ", avg) 
# elif(avg>=60 and avg<80): 
# 	print("Congratulations ! You have secured Seecond Classand your percentage is ", avg ) 
# elif (avg>=40 and avg<60): 
# 	print("Congratulations ! You have secured Third Class, and your percentage is ", avg) 
# elif (avg<40): 
# 	print( "You are fail") 



