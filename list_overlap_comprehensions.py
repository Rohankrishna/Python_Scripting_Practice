import random
from random import randint
j=randint(range(9))
k=randint(range(9))
a=random.sample(range(1,30),j)
b=random.sample(range(1,30),k)
result=[i for i in set(a) if i in b]
print(result)
