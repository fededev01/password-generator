import string
import random as rnd

let = int(input("Quante lettere vuoi: \n"))
list = []
loop = True
while loop == True:
  list.append(rnd.choice(string.ascii_letters))
  list.append(rnd.randint(0,9))
  if len(list) >= let:
    loop = False
  else:
    loop = True

print(list)