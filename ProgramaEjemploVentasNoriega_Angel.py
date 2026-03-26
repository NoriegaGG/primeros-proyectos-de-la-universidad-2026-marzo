#ejemplo programa de venta con descuento 
#calculamos el monto de pago, etc

import datetime 

print ("========= Programa de ventas hecho por tu terror del codigo Gabito =========")

nombreProducto = input("Ingrese el nombre del producto: ")
precioProducto = float(input("Ingrese el precio del producto: "))
cantidadProducto = int(input("Ingrese la cantidad del producto: "))
descuento = float(input("Ingrese el descuento: "))

montobruto = precioProducto * cantidadProducto
montodescuento = montobruto * descuento / 100
montopagar = montobruto - montodescuento

print ("========= Resumen de la compra =========")
print ("        ========= Boleta =========      ")
print(f"El monto bruto de la compra es: {montobruto} soles")
print(f"El monto del descuento es: {montodescuento} soles")
print(f"El monto a pagar es: {montopagar} soles")

fecha_actual = datetime.datetime.now()
print(f"Fecha de la compra: {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")
print("Gracias por su compra, vuelva pronto")

print ("=" * 50)