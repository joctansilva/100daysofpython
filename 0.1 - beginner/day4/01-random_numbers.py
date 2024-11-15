import random

#random integer
random_integer = random.randint(1, 10)
print(random_integer)

#random float: but here we never get a the top number
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

#random float: but here we can get a the top number
random_float = random.uniform(1, 10)
print(random_float)

