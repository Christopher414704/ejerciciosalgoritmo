
print ("Introduce tú número de teléfono en el formato +34-XXXXXX-XX: ")

num_telefono = input(": ")

parts = num_telefono.split("-")
num_prefijo = parts[1]

print( " Tú Número de teléfono sin prefijo y extensión: ", num_prefijo)
