import random
import time
c=random.randint(1, 2)
z=random.randint(1, 3)
a=random.randint(1, 9)
def programacion1():
  b=int(input('Escribe un número del 1 al 9'))
programacion1()
if b==a:
  print('Que mala suerte')
else:
  for i in range(7):
    time.sleep(c)
    print('intent de nuevo')
    time.sleep(z)
    programacion1()
  print('uf, que buena suerte tienes')
