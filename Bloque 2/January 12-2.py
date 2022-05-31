x=int(input('Ingrese el número a adivinar: '))
while True:
  a=int(input('Adivina el número: '))
  if(x<a):
    print('Lo siento te sobra')
  if(x>a):
    print('Lo siento te falta')
  if(x==a):
    print('Correcto adivinaste')
    print('Felicidades')
   

