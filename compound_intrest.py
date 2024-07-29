from __future__ import division
p=float(input("Principle or original value :"))
r=float(input("rate of intrest per annum :"))
n=float(input("number of years the money invested :"))
A=p*(1+r/100)
#print(A)
x=pow(A,n)
print(x)