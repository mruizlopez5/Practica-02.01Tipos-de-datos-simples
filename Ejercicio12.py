"""Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de 
barras vendidas que no son del día. Después el programa 
debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca 
y la ganancia final total."""


barras = int(input("introduce el numero de barras vendidas que no sean del dia\n"))

plata = round(3.49*0.6*barras,2)

print("la barra de pan del dia vale 3.49, la que no es del dia se descuenta el 60%\nLo que hace una ganancia hoy de: "+str(plata) + " lereles")