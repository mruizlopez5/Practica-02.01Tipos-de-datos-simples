"""Escribir un programa que comience leyendo la cantidad 
de dinero depositada en la cuenta de ahorros, introducida 
por el usuario. Después el programa debe calcular y mostrar 
por pantalla la cantidad de ahorros tras el primer, segundo 
y tercer años. Redondear cada cantidad a dos decimales."""

billets = float(input("cuanto dinero tienes pensado meter en la cuenta de ahorros, sinceramente\n"))

ano1 = billets + billets*0.4
ano2 = ano1 + ano1*0.4
ano3 = ano2 + ano2*0.4

print("El primer año habrias obtenido: "+str(ano1)+"\nEl segundo año habrias obtenido: "+str(ano2)+"\nEl tercero año habrias obtenido: "+str(ano3))