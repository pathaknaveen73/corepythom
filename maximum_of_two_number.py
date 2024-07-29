# a=15
# b=12
# if a>b:
#     print(a)
# else:
#     print(b)
# a=[2,3,4,5,53,232,6452]

# for i in range(0,len(a)):
#     if a[i]>a[i+1]:
#         print(a[i]," is greater")
#     else:
#         print(a[i+1])
a = int(input('Enter first number :'))
b = int(input('Enter second number :'))
c = a>b
d = {'True':a,
      'False':b
      }
print(f'for {a}>{b} result is {c} and greater number is {d[str(c)]}')