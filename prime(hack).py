N=int(input("enter the number upto which you want to find primes: "))
#n=N/2
fact=0
for i in range(1,N):
    I=(i//2)+1
    for j in range(2,I):
        if i%j==0:
            fact=fact+1
        if fact==0:
             print(i)

# for check_number in range(2, (number / 2)+1):
#             if number % check_number == 0: