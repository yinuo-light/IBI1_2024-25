# What does this piece of code do?
# Answer: count the whole number of the attempts until in an attempt the two numbers named first_n and second_n which randomly choose from 1 to 5 are the same

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress>=0:
	progress+=1
	
	first_n = randint(1,5)
	second_n = randint(1,5)
	if first_n == second_n:
		print(progress)
		break

