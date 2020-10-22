diccionario= {}
datos = int(input("Cantidas de datos a ingresar: "))
x=0
while x<datos:
  llaves=int(input("ingrese la llave: "))
  valores=str(input("ingrese los valores: "))
  diccionario.update({llaves:valores})
  x +=1

llaves1=int(input("ingrese la llave1: "))
valores1=str(input("ingrese los valores1: "))

diccionario.setdefault(llaves1,valores1)
print(diccionario)

'''if llaves1 in diccionario:
  print("si esta")
else:
  valores1=str(input("ingrese los valores: "))
  diccionario.update({llaves1:valores1})
  #diccionario[llaves]=valores
  print(diccionario)'''

#Consultar un par clave en el diccionario, si esta eliminelo
if diccionario.get(20, False)==False:
   print("No esta")
else:
  diccionario.pop(20)
  print(diccionario)

#Mostrarme las llaves del diccionario y convertirlas en una lista
for r,u in diccionario.items():
  print(r," ",u)

diccionario = list(diccionario.values())
print(diccionario)