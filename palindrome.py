def palindrome(name):
	name = input("Enter a string :")
	print("The string you entered is",name,type(name))
	rev_str=name[::-1]
	print(rev_str)
	if name==rev_str:
		print("Given string is a palindrome")
	else:
		print("Not a palindrome :")



palindrome(None)
