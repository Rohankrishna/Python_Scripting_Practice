from random import randrange
list_numbers=[]
list_even=[]
for i in range(0,10):
	list_numbers.append(randrange(0,100))
	if list_numbers[i]%2==0:
		list_even.append(list_numbers[i])
print(list_numbers)
print(list_even)

