import random
import time
a=random.randint(1, 9)
def programacion1():
  b=int(input('Escribe un número del 1 al 9'))
programacion1()
if b==a:
  print('Que mala suerte')
else:
  for i in range(7):
    print('intent de nuevo')
    programacion1()
  print('uf, que buena suerte tienes')
