# Write your code here
isbn=input("Mr.Potter, Enter the ISBN code to reveal the secrets : ")
#isbn=str(isbn)
ISBN=list(isbn)
print(ISBN, len(ISBN))
length_of_ISBN = len(ISBN)    
if length_of_ISBN==list(isbn):
    print("This is executing")
    sum=0
    for i in range(0,(len(ISBN))):
        sum+=(int(ISBN[i]))*(i+1)
        print(ISBN[i],sum)
    if sum%11==0:
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
else:
    print("Illegal ISBN")
        
    
