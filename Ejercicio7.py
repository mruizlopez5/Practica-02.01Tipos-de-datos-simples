"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
es el índice de masa corporal calculado redondeado con dos decimales."""

kg = float(input("introduce tu peso en kg\n"))
m = float(input("introduce tu altura en metros\n"))
imc = kg/(m*m)
print("Tu índice de masa corporal es "+ str(round(imc,2)))