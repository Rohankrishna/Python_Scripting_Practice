def rev_string(sentence):
	print(sentence)
	words=sentence.split(" ")
	print(words)
	#li=words
	#print(li)
	rev=[]
	rev=list(reversed(words))
	print(rev)
	rev_str=" ".join(rev)
	print(rev_str)


if __name__=="__main__":
	sentence=input("Enter a sentence that you want to reverse: ")
	print(sentence)
	rev_string(sentence)
