import string
import random as rnd

let = int(input("Quanti caratteri vuoi: \n"))
cosa = str(input("Che password vuoi creare? \n")) #facebook, instagram, ecc
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

finals = "".join(list)
file = open("passwords.txt", "a")
file.write(cosa +  ": " + finals + "\n")
file.close()
