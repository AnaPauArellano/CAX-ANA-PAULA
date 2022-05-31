numero=8

compara=int(input("numero? "))

if(compara<numero):
  print("te falta")

#elif necesita de un if para funcionar

elif(numero<(compara-numero)):
  print("tu numero esta sobrado mas no tanto")

elif(compara>numero):
  print("te sobra")

#es todo lo contrario del IF, no del elif

else:
  print("felicidades")