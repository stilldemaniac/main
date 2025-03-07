print("Calculadora de masa")
nombre=input("favor de introducir su nombre: ")

try:
    peso=float(input("ingrese su peso en Kg con valor mayor a 0 y menor a 180: "))
except ValueError:
    print("valor no reconocido, finalizando el programa...")

try:
    altura=float(input("ingrese su estatura en metros: "))
except ValueError:
    print("valor no reconocido, finalizando el programa...")

print("calculando su indice de masa...")
imc=str((peso/(altura**2)))
str(imc)
print(f"{nombre} su indice de masa es de: {imc} basado en su altura de: {altura} y su peso de: {peso}")