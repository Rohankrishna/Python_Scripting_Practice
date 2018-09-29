def fib(n,a,b,c):
	for i in range(1,n):
		c=a+b;a=b;b=c
		print(c)

if __name__ == "__main__":
	n=int(input("Enter how many numbers you want to calculate fibonacci series for: "))
	a=int(input("Enter first number in the series: "))
	b=int(input("Enter second number in the series: "))
	print(fib(n,a,b,None))
