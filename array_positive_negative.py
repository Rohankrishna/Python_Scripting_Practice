arr=int(input())
arr=list(map(int,input().split()))
total_elements=len(arr)
pos, neg, neu= 0, 0, 0
for i in arr:
    if i>0:
        pos+=1
    elif i==0:
        neu+=1
    else:
        neg+=1

print(pos/total_elements)
print(neg/total_elements)
print(neu/total_elements)