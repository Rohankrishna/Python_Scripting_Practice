import sys
def fibonacci(n):
	a, b, counter = 0, 1, 0
	while True:
		if(counter>n):
			return
		yield a
		a, b = b, a+b
		counter+=1

f=fibonacci(5)
print(f)

while True:
	try:
		print(next(f))
	except StopIteration:
		sys.exit()
	










