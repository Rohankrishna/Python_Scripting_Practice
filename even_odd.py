from math import sqrt

n = int(input("enter a number "))
check = int(input("Enter the number with which we want to check "))
if n % 4 == 0:
	print("It is an even number and also a multiple of 4")
elif n%2==0:
	print("It is an even number")
else:
	print("It is an odd number")

if(n%check==0):
	print(n, " is evenly divisible by ",check)
else:
	print(n, "is not divisible by", check)
