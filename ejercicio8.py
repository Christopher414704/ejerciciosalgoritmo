precio_producto = float(input("Ingrese el precio de un producto: "))

euros = int(precio_producto)
centimos = int((precio_producto - euros) * 100)

print("El precio es de " , euros ,  " euros y " , centimos , "centavos")
