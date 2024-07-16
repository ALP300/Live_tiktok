#Escribe un programa en Python 
# que pida al usuario un número 
# entero y calcule su factorial. 
# El programa debe imprimir 
# "El factorial de X es Y."

#5!= 5x4x3x2x1


numero=int(input("Introduce el número: "))#10
factorial= 1
for i in range(1, numero+1):
    factorial *= i

print("El factorial de", numero, "es", factorial)