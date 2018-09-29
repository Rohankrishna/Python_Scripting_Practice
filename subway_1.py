price=float(input("Enter the cost of subway: "))
money=float(input("Enter the amount customer has given: "))
if price!=0:
    if money==price:
        print("Money sufficient")
    elif money<price:
        print("Money not sufficient")
    else:
        change=money-price
        bills=[100,50,20,10,5,2,1,0.25,0.10,0.05,0.01]
        for a in bills:
            count=change//a
            if count>0:
                print(int(count),":", a, "coins" if a<1 else "dollar bills")
                
            change-=count*a
else:
    print("The cost of your subway is Zero dollars, you dont have to pay anything")