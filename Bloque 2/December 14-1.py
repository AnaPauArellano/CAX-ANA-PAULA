agua=1
galletas=2
leche=3
lechuga=4
jugo=5
carne=6
pan=7
pastillas=8
chocolate=9
pepinos=10
print('Producto 1: agua')
print('Producto 2: galletas')
print('Producto 3: leche')
print('Producto 4: lechuga')
print('Producto 5: jugo')
print('Producto 6: carne')
print('Producto 7: pan')
print('Producto 8: pastillas')
print('Producto 9: chocolate')
print('Producto 10: pepinos')
while True:
  
  numero=int(input('Ingrese el numero del producto uno: '))
  if(numero==1):
    print('El precio del agua es 10 pesos')
    precio1=10
    producto=precio1
  if(numero==2):
    print('El precio de las galletas es 12 pesos')
    precio2=12
    producto=precio2
  if(numero==3):
    print('El precio del leche es 12 pesos')
    precio3=12
    producto=precio3
  if(numero==4):
    print('El precio de la lechuga es 10 pesos')
    precio4=10
    producto=precio4
  if(numero==5):
    print('El precio del jugo es 12 pesos')
    precio5=12
    producto=precio5
  if(numero==6):
    print('El precio de la carne es 14 pesos')
    precio6=14
    producto=precio6
  if(numero==7):
    print('El precio del pan es 8 pesos')
    precio7=8
    producto=precio7
  if(numero==8):
    print('El precio de las pastillas es 16 pesos')
    precio8=16
    producto=precio8
  if(numero==9):
    print('El precio del chocolate es 8 pesos')
    precio9=8
    producto=precio9
  if(numero==10):
    print('El precio de los pepinos es 10 pesos')
    precio10=10
    producto=precio10
  numero2=int(input('Ingrese el numero del segundo artículo: '))
  if(numero2==1):
    print('El precio del agua es 10 pesos')
    precio1=10
    producto2=precio1
  if(numero2==2):
    print('El precio de las galletas es 12 pesos')
    precio2=12
    producto2=precio2
  if(numero2==3):
    print('El precio del leche es 12 pesos')
    precio3=12
    producto2=precio3
  if(numero2==4):
    print('El precio de la lechuga es 10 pesos')
    precio4=10
    producto2=precio4
  if(numero2==5):
    print('El precio del jugo es 12 pesos')
    precio5=12
    producto2=precio5
  if(numero2==6):
    print('El precio de la carne es 14 pesos')
    precio6=14
    producto2=precio6
  if(numero2==7):
    print('El precio del pan es 8 pesos')
    precio7=8
    producto2=precio7
  if(numero==8):
    print('El precio de las pastillas es 16 pesos')
    precio8=16
    producto2=precio8
  if(numero2==9):
    print('El precio del chocolate es 8 pesos')
    precio9=8
    producto2=precio9
  if(numero2==10):
    print('El precio de los pepinos es 10 pesos')
    precio10=10
    producto2=precio10
  print('Su total a pagar es: ', producto+producto2)