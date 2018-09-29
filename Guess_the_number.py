from random import randint

number=randint(1,99)
user_guess=0
count=0

while user_guess != "exit" and user_guess!= number:
	user_guess=input("Guess the number between 1 and 9 : ")

	if user_guess=="exit":
		print("You entered exit so stopping the game")
		break
	user_guess=int(user_guess)
	if(user_guess==number):
		count+=1
		print("That's right your guess is correct : ")
		
	elif(user_guess > number):
		count+=1
		print("Your guess is higher than the number : ")
		
	elif(user_guess < number):
		count+=1
		print("Your guess is lesser than the number : ")
		


print("you took %s attempts to guess the correct number "%count)

