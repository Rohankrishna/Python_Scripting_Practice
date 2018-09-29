import random
import string

def pw_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

pw=int(input('How many characters in your password? : '))
print(pw_gen(pw))
