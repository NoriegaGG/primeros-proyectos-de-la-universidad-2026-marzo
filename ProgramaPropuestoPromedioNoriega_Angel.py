#calculadora para sacar el promedio final de un almuno

print ("========= Programa para calcular el promedio final de un alumno hecho por tu terror del codigo Gabito =========")
nombreAlumno = input("Ingrese el nombre del alumno: ")
c1 = float(input("Ingrese el consolidado 1: \t"))
c1f = c1 * 0.20

ep = float(input("Ingrese el examen parcial: \t"))
epf = ep * 0.25

c2 = float(input("Ingrese el consolidado 2: \t"))
c2f = c2 * 0.20

ef = float(input("Ingrese el examen final: \t"))
eff = ef * 0.35

promedioFinal = c1f + epf + c2f + eff

print ("========= Resumen del alumno =========")
print(f"El promedio final de {nombreAlumno} es: {promedioFinal}")
print("==========================================")
