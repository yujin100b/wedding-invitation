
import random, string

def randomword(length):
   letters = string.ascii_lowercase
   code= ''.join(random.choice(letters) for i in range(length))
   return code