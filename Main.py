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

#Consultar productos con cantidad inferior a un umbral especificado.
def buscar_producto_cantidad(cantidad_menor):
    for coctel in cocteles:
        if int (coctel ['cantidad']) <= cantidad_menor:
          print(f"{coctel['nombre']:<{ancho_nombre}} | {coctel['cantidad']:^10} | {coctel['precio']:^10}€ ")


def estadisticas():
    total=0
    total_precio=0
    caro=cocteles[0]
    barato = cocteles[0]
    for coctel in cocteles:
        total += int(coctel['cantidad'])
        total_precio += int(coctel['precio']) * int(coctel['cantidad'])

        if coctel['precio'] >caro['precio'] :
            caro=coctel

        if coctel['precio'] <barato['precio']:
            barato = coctel
    
    print("\n=== ESTADÍSTICAS DEL INVENTARIO ===")
    print(f"Cantidad total de cocteles en inventario: {total} unidades")
    print(f"Valor total del inventario: {total_precio:,}€")
    print("\n--- Análisis de Precios ---")
    print(f"Coctel más caro: {caro['nombre']} ({caro['precio']:,}€)")
    print(f"Coctel más barato: {barato['nombre']} ({barato['precio']:,}€)")
    print("================================")
    
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
    print("4. Buscar producto por cantidad")
    print("5. Eliminar producto")
    print("6. Estadistica")
    print("7. Salir")

def funcionalidades():
    menu() 
    opcion = int(input("Seleccione acción: "))
    while opcion != 7:
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
                    cantidad =int(input("Introduce cantidad por la que quieres filtrar: ")) 
                    buscar_producto_cantidad(cantidad)
                    opcion = int(input("Seleccione acción: "))
                case 5:
                    producto = input("Introduce producto que quieres buscar: ")
                    buscar_producto(producto)
                    imprimir_inventario()
                    opcion = int(input("Seleccione acción: "))
                case 6:
                    estadisticas()
                    opcion = int(input("Seleccione acción: "))
                case _:
                    print("Opción no válida. Intente nuevamente.")
                    opcion = int(input("Seleccione acción: "))
    
    print("Saliendo... ¡Vuelva pronto!")

    #esto es una prueba para saber si se guardan las cosas


funcionalidades()