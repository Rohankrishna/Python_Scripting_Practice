import random

def List_ends():
	list=[]
	k=random.randrange(0,10)
	for i in range(0,k):
		list.append(random.randrange(0,100))
	print(list)
	list_new=[]
	list_new.extend((list[0],list[-1]))
	print(list_new)


if __name__ == "__main__":
	List_ends()
