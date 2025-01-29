cocteles = [
    {
        "nombre": "Margarita",
        "cantidad": "6",
        "precio": 8.50
    },
    {
        "nombre": "Mojito",
        "cantidad": "10",
        "precio": 7.00
    },
    {
        "nombre": "Piña Colada",
        "cantidad": "9",
        "precio": 9.00
    },
    {
        "nombre": "Bloody Mary",
        "cantidad": "5",
        "precio": 8.00
    },
    {
        "nombre": "Daiquiri",
        "cantidad": "6",
        "precio": 8.75
    }
]

ancho_nombre = max(len(coctel['nombre']) for coctel in cocteles)
ancho_nombre = max(ancho_nombre, len("NOMBRE")) 

def imprimir_inventario():
    # Crear la línea separadora
    linea = "-" * (ancho_nombre + 30)
    
    # Imprimir el encabezado
    print(linea)
    print(f"{'NOMBRE':<{ancho_nombre}} | {'CANTIDAD':^10} | {'PRECIO':^10}")
    print(linea)
    
    # Imprimir cada coctel
    for coctel in cocteles:
        print(f"{coctel['nombre']:<{ancho_nombre}} | {coctel['cantidad']:^10} | {coctel['precio']:^10}€ ")
    
    print(linea)

def agregar_producto():
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Nombre del cóctel: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    if nombre == None or cantidad == None or precio == None:
        print("Por favor, rellene todos los campos")
    else:
        if cantidad < 0 or precio < 0:
            print("Por favor, introduzca un valor válido")
        else :
            if buscar_producto(nombre):
                print("El cóctel ya existe")
            else:
                nuevo_producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
                cocteles.append(nuevo_producto)
        print(f"El cóctel '{nombre}' ha sido agregado\n")
def buscar_producto(producto):
    encontrado=False
    i=0
    while i<len(cocteles) and not encontrado:
        if cocteles[i]['nombre'] == producto:
            ancho_nombre = len(cocteles[i]['nombre'])
            print(f"{cocteles[i]['nombre']:<{ancho_nombre}} | {cocteles[i]['cantidad']:^10} | {cocteles[i]['precio']:^10}€ ")
            encontrado= True
        i+=1
    
    if not encontrado:
        print("Lo sentimos, no tenemos ese coctel :(")

    return encontrado

def actualizar_producto(nombre_producto):
    encontrado=False
    if buscar_producto(nombre_producto) :
        eleccion = int(input("¿Qué deseas actualizar?\n1. Cantidad\n2. Precio\nElige : "))
        match eleccion:
            case 1:
                nueva_cantidad = int(input("Introduce la nueva cantidad: "))
                i=0
                while i<len(cocteles) and not encontrado:
                    if cocteles[i]['nombre'] == nombre_producto:
                        cocteles[i]['cantidad'] = nueva_cantidad
                        print("¡Cantidad actualizada!")
                        encontrado= True
                    i+=1
            case 2:
                nuevo_precio = float(input("Introduce el nuevo precio: "))
                encontrado=False
                i=0
                while i<len(cocteles) and not encontrado:
                    if cocteles[i]['nombre'] == nombre_producto:
                        cocteles[i]['precio'] = nuevo_precio
                        print("¡Precio actualizada!")
                        encontrado= True
                    i+=1
        return encontrado
    else :
        return encontrado

    
def menu():
    print("\n--- Menú ---")
    print("1. Mostrar Inventario")
    print("2. Añadir al Inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Salir")

def funcionalidades():
    menu() 
    opcion = int(input("Seleccione acción: "))
    while opcion != 5:
            match opcion:
                case 1:
                    imprimir_inventario()
                    opcion = int(input("Seleccione acción: "))
                case 2:
                    agregar_producto()
                    imprimir_inventario()
                    opcion = int(input("Seleccione acción: ")) 
                case 3:
                    producto = input("Introduce producto que quieres buscar: ")
                    buscar_producto(producto)
                    opcion = int(input("Seleccione acción: "))
                case 4:
                    print("Actualizar producto")
                    imprimir_inventario()
                    nombre_producto = input("Seleccione producto a actualizar: ")
                    if actualizar_producto(nombre_producto):
                        buscar_producto(nombre_producto)
                    else:
                        print("No se encontró el producto")
                    opcion = int(input("Seleccione acción: "))
                case _:
                    print("Opción no válida. Intente nuevamente.")
                    opcion = int(input("Seleccione acción: "))
    
    print("Saliendo... ¡Vuelva pronto!")

    #esto es una prueba para saber si se guardan las cosas


funcionalidades()