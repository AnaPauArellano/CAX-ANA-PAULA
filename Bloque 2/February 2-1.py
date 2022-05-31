#nested conditions


mensaje=input("escribe hola")

if(mensaje!="hola"):
  if (mensaje =="HOLA"):
    print("que no sabe leer, era hola ............")
    mensaje=input("intentelo nuevamente")

    if(mensaje=="HOLA"):
      print("y con todo y eso no aprende a leer")
      
    elif(mensaje=="hOla"):
      print("la O era minuscula")
    
    elif (mensaje=="hoLA"):
      print("por favor lea bien")
    
    elif (mensaje=="holA"):
      print("perdí la fe en la humanidad")

  elif(mensaje=="Hola"):
    print("se agradece una persona muy letrada, ero aprenda a leer, dije hola")

  elif(mensaje=="hOLA"):
    print("desactive el bloq mayus")

  else:
    print("en serio............")

elif(mensaje=="hola"):
  print("que agradable sujeto")
