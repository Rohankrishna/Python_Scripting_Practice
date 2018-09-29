def prime(num):
	factors=0
	for i in range(2,num-1):
		if(num % i ==0):
			factors+=1
			break
	if(factors==0):
		print("It's a prime number")
	else:
		print("No, it's not a prime number")



if __name__ == "__main__":
	num=int(input("Enter the number which you want to check primality for:"))
	prime(num)
