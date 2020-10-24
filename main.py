import string
import random as rnd

let = int(input("Quante lettere vuoi: \n"))
nums = ["0123456789"]
chars = string.ascii_letters + "0123456789" + "!?£$%&=+#@"
list = []
loop = True
while loop == True:
  list.append(rnd.choice(chars))
  if len(list) == let:
    loop = False
  else:
    loop = True

print(list)
