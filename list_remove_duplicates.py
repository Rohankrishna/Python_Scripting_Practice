import random
def List_input():
	li=[]
	for i in range(1,10):
		a=int(input("Enter element: "))
		li.append(a)
#	li=remove_duplicates(li)
	print("List before removing duplicates: ",li)
def remove_duplicates(li):
	li=set(li)
	print("Set after removing duplicates: ",li)
	li=list(li)
	return li

if __name__ == "__main__":
	print("Final list after removal of duplicates: ",List_input())
#	remove_duplicates(li)
