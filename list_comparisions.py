from random import randrange
list1=[]
list2=[]
#list3=[]
for i in range(0,10):
	list1.append(randrange(0,10))
	list2.append(randrange(0,10))
#	for j in range(0,len(list1)):
#		if list1[i]==list2[j]:
#			list3.append(list1[i])


#print(list1,"\n",list2,"\n",list3)


a=set(list1)
b=set(list2)
c=(a & b)
print(a,b,c)


