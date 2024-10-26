""" Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos 
y muñecas vendidos en el último pedido y calcule 
el peso total del paquete que será enviado. """

mu = int(input("introduce el número de muñecas incluidas en el último pedido\n"))
pa = int(input("introduce el número de payasos incluidos en el último pedido\n"))

peso = 112*pa + 75*mu

print("El paquete deberia contener: " + str(peso) + " gramos de puro pedido" )