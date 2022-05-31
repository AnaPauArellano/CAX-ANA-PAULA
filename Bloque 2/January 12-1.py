x=int(input('Ingrese primera calificación: '))
z=int(input('Ingrese segunada calificación: '))
v=int(input('Ingrese tercera calificación: '))

suma=x+z+v
div=suma/3
a=div
print('El promedio es: ',a)

if(a>=9):
  print('Felicidades aprobó, premio ')

if(a>=6):
  print('Paso la materia')

if(a<6):
  print('Reprobó ')