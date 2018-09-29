from getpass import getpass

user1= input("Player 1, enter your name: ")
user2=input("Player2 enter your name: ")

#user1_choice=input("%s, select your choice: rock, paper or scissors: "% user1)
#user2_choice=input("%s, select your choice: rock, paper or scissors: "% user2)
#The above one is the normal way of taking input but the selection of the user depending on what he selected rock, paper or scissors would be known so we use the getpass method which hides the user selection.


user1_choice=getpass("%s, select your choice: rock, paper or scissors: "% user1)
user2_choice=getpass("%s, select your choice: rock, paper or scissors: "% user2)
#Above, 'getpass' function is imported from python class 'getpass' which is used for taking password as input. It hides the user input and wouldn't let us see what the user has selected

def compare(u1, u2, n1, n2):
	if u1==u2:	
		print("Its a tie")
	elif u1=='rock':
		if u2=='scissors':
			print("%s wins" % n1)
		else:
			print('%s wins'%n2)
	elif u1=='paper':
		if u2=='rock':
			print('%s wins'%n2)
		else:
			print('%s wins'%n1)
	elif u1=='scissors':
		if u2=='rock':
			print('%s wins'%n2)
		else:
			print('%s wins'%n1)
	else:
		return 'Invalid input'
		sys.exit()


compare(user1_choice, user2_choice, user1, user2)
