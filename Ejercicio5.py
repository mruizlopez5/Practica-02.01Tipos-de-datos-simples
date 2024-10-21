"""Escribir un programa que pregunte al usuario por el número de horas trabajadas y
 el coste por hora. Después debe mostrar por pantalla la paga que le corresponde."""

horas = float(input("introduce el numero de horas trabajadas\n"))
coste = float(input("introduce el precio de la hora\n"))
print("deberias haberte embolsado: "+ str(horas*coste) + " eureles")
