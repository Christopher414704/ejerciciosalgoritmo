print("Introduce los productos de la cesta de compra separados por comas: ")
lista_productos = input(": ").split(',')

if lista_productos:
    print("Productos en la cesta de compra:")
    for producto in lista_productos:
        
        producto_limpio = producto.strip()  
        print(producto_limpio)
