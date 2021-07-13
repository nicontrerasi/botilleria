import random

cont=0
tot=0

while True:
	try:
		ventas=int(input("Cantidad de ventas a ingresar: "))
		if ventas>0:
			break		
		else:
			print("El número de ventas debe ser mayor a 0")
	except ValueError:
		print("Debe ingresar un número entero")

while cont<ventas:
	print(f"\n\tVenta Nº {cont+1}")

	art=random.choice(["Verdulería", "Botillería", "Paquetería"])
	precio=random.randint(100,80000)

	while True:
			try:
				cant=int(input("Ingrese cantidad vendida: "))
				if cant>=1 and cant<=100:
					break		
				else:
					print("La cantidad vendida debe estar entre 1 y 100")
			except ValueError:
				print("Debe ingresar un número entero")

	while True:
			try:
				pago=input("Paga con efectivo o tarjeta? E/T: ").upper()
				if pago=="E" or pago=="T":
					break		
				else:
					print("Debe ingresar E si es en efectivo o T si es con tarjeta")
			except ValueError:
				print("Debe ingresar una letra válida")

	cont+=1

	print(f"Tipo de artículo: {art}")
	print(f"Precio unitario: ${precio}")
	print(f"Cantidad vendida: {cant}")


	if art=="Botillería":
		total=cant*precio
		

	if pago=="T" and precio > 5000:
		tot+=1
		


print(f"\n\tTotal recaudado por botillería: ${total}")
print(f"\n\tCantidad de ventas con tarjeta mayores a $5.000: {tot}\n\t")




