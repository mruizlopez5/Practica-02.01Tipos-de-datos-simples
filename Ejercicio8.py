"""Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto 
<r> donde <n> y <m> son los números introducidos por el usuario, y 
<c> y <r> son el cociente y el resto de la división entera respectivamente."""

num = int(input("introduce un numerador\n"))
den = int(input("introduce un denominador\n"))
 
resto = num%den
cocido = num//den

print("el número " + str(num) + " entre " + str(den) + " da un cociente "+ str(cocido) + " y un resto " + str(resto))