#elaboracion de una pieza mecanica, Gabriel Noriega 
import math
print("=" * 50)
print("********** ====== Elaboracion de una pieza mecanica ====== **********\n")

nombre = input("Estimado Sr. mecanico, por favor ingrese su nombre: \t")
print (f"Bienvenido {nombre} a la elaboracion de una pieza mecanica y se tiene que calcular el area de la pieza mecanica mostrada")

#area dek cuadrado
ladoA = float(input("ingrese el lado A del cuadrado:\t"))
ladoB = float(input("ingrese el lado B del cuadrado:\t"))
areaCuadrado = ladoA * ladoB

#area del circulo 
radio = ladoA / 2
areaCirculo = math.pi * radio ** 2
print(f"El area del circulo (completo, equival. a dos semis) es: {areaCirculo:.2f}")

#area sombreada de la pieza mecanica
areaTotal = areaCuadrado - areaCirculo

print(f"{nombre} el area sombreada de la pieza mecanica es: {areaTotal:.5f} unidades cuadradas")

print("=" * 50)