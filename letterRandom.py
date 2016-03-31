#Quinton Dean
#this program prints a random letter

import random
letterOrd = random.randint(ord("A"), ord("Z"))
letter = chr(letterOrd)
print("Random letter generated is", letter)
