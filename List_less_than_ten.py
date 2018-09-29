#List Less Than Number



def List_less_than(num):
	list1=[]
	n=int(input("number of elements in the list"))
	for i in range(0,n):
		list1.append(int(input("Enter element into the list ")))
	print(list1)
	num = int(input("Enter the number less then which we want to print elements"))

	list2=[]
	for j in list1:
		print(j)
		if j<num:
			list2.append(j)
	print(list2)


List_less_than(None)

