import math


print("=============== Ecuaciones Ejemmplo ================")


x = eval(input("Ingrese x: "))

potencia1 = pow(x+3, 2)
raiz = math.sqrt(x+5)
potencia2 = pow(x, 2/3)
z = ( potencia1 + x + raiz) / potencia2+1

respuesta1 = input("responde si o no si quieres ver a detalle la ecuacion: \t")

if respuesta1.lower() == "si":
    print(f"la potencia 1 es: {potencia1}")
    print(f"la raiz es: {raiz}")
    print(f"la potencia 2 es: {potencia2}")
    print(f"el resultado de la ecuacion es: {z:.3f}")
    
if respuesta1.lower() == "no":
    print(f"el resultado de la ecuacion es: {z:.5f}")