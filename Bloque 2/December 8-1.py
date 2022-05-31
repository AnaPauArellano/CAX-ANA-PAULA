a=9

while True:
  print('adivina el numero ')
  n=int(input('escribe un numero:'))
  if(a<n):
    print('te sobra')
  if(a>n):
    print('te falta')
  if(n==a):
    print('felicidades')
  