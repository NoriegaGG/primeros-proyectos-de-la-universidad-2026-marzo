#area de terreno de la empresa 
print("********** ====== Calculo de Area del terreno que se venderá ====== **********\n")
nombre = input("querido ingeniero/a por favor ingrese su nombre:\t")
TerrenoLadoA = float(input("ingrese el lado A del terreno:\t"))
terrenoLadoB = float(input("ingrese el lado B del terreno:\t"))
areaDelCuadrado = TerrenoLadoA * terrenoLadoB

print (f"el terreno es simetrico?, osea tiene una forma extra como triangular?)")
respuesta = input("responda con si o no:\t")

if respuesta.lower() == "si":
    altura = float(input("ingrese la altura del triangulo:\t"))
    base = float(input("ingrese la base del triangulo:\t"))
    areaDelTriangulo = (altura * base) / 2
    areaTotal = areaDelCuadrado + areaDelTriangulo
    print(f"{nombre} el area total del terreno es: {areaTotal:.2f} unidades cuadradas")
    
if respuesta.lower() == "no":
    print(f"ingeniero/a {nombre} el area total del terreno es: {areaDelCuadrado:.2f} unidades cuadradas")