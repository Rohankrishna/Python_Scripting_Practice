#Python program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

def char_input(nam, age, year):
	nam = input("Enter your name: ")
	age = int(input("Enter your age: "))
	year = str((2018-age)+100)
	print(nam +", your age will be 100 years by the year "+ year)


char_input(None, None, None)


