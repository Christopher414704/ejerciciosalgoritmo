correo = input("Ingrese un correo electronico: ")
caracter1 = "gmail"
remplazo1 = "ceu"
caracter2 = ".com"
remplazo2 = ".es"

nuevocorreo = correo.replace(caracter1, remplazo1)
nuevocorreo2 = nuevocorreo.replace(caracter2, remplazo2)

print(nuevocorreo2)
