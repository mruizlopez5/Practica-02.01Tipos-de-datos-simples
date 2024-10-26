"""Escribir un programa que pregunte al usuario 
una cantidad a invertir, el interés anual y el 
número de años, y muestre por pantalla el capital
obtenido en la inversión"""

print("welcome to la calculadora de inversiones\n")

inversion = float(input("Introduzca la cantidad a invertir\n"))
interes = float(input("introduce el valor del interés anual\n"))
años = int(input("introduce el numero de años que estrá en inversion\n"))

total = inversion*pow((1+interes),años)

print("has capitalizado un capital total de: ",str(total)," capitales slu2")