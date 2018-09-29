

# Complete the compareTriplets function below.
def compareTriplets():
    a,b=0,0
    # contestants=['alice','bob']
    # for i in contestants:
    #     print(i)
    alice=[]
    x,y,z=map(int, input("Enter 3 scores given by judges").split())
    alice.extend([x,y,z])
    print(alice)

    bob=[]
    x,y,z=map(int, input("Enter 3 scores given by judges").split())
    bob.extend([x,y,z])
    print(bob)
    for j in range(0,3):
        if alice[j]>bob[j]:
            a+=1
        elif alice[j]<bob[j]:
            b+=1
        else:
            pass
    print(a,b)
    if a>b:
        print("Alice wins")
    elif a<b:
        print("bob wins")
    else:
        print("Its a tie")

compareTriplets()
