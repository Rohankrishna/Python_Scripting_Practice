num = int(input("Enter the number for which we want divisors : "))
n = num/2 +1
divisors=[num,]
for i in range(1,n):
	if num%i==0:
		divisors.append(i)
divisors.sort()
print(divisors)	
