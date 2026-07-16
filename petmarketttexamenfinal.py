#datos

productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
}

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
}


#validacion

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_marca(marca):
    return marca.strip() != ""

def validar_peso_kg(peso_kg):
    try:
        return float(peso_kg) > 0
    except ValueError:
        return False

def validar_es_importado(es_importado):
    return es_importado.lower() in ["s", "n"]

def validar_es_para_cachorro(es_para_cachorro):
    return es_para_cachorro.lower() in ["s", "n"]

def validar_precio(precio):
    return precio.isdigit() and int(precio) > 0

def validar_unidades(unidades):
    return unidades.isdigit()


#funciones de menu:

def unidades_categoria(categoria):
    total = 0
    categoria = categoria.lower()
    for codigo in productos:
        if productos[codigo][1].lower() == categoria:
            total += stock[codigo][1]
    print("El total de unidades disponibles es:", total)


def busqueda_precio(p_min, p_max):
    encontrados = []
    for codigo in stock:
        precio = stock[codigo][0]
        unidades = stock[codigo][1]
        if p_min <= precio <= p_max and unidades != 0:
            nombre = productos[codigo][0]
            encontrados.append(nombre + "--" + codigo)

    encontrados.sort()

    if len(encontrados) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        print("Los productos encontrados son:", encontrados)


def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.upper()
    if codigo in stock:
        stock[codigo][0] = nuevo_precio
        return True
    else:
        return False


def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    codigo = codigo.upper()
    if codigo in productos:
        return False

    productos[codigo] = [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
    stock[codigo] = [precio, unidades]
    return True


def eliminar_producto(codigo):
    codigo = codigo.upper()
    if codigo not in productos:
        return False

    productos.pop(codigo)
    stock.pop(codigo)
    return True


#MENU

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        opcion = input("Ingrese opción: ")
        if opcion in ["1", "2", "3", "4", "5", "6"]:
            return int(opcion)
        else:
            print("Debe seleccionar una opción válida")


#programa principal

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        categoria = input("Ingrese categoría a consultar: ")
        unidades_categoria(categoria)

    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        busqueda_precio(p_min, p_max)

    elif opcion == 3:
        continuar = "s"
        while continuar == "s":
            codigo = input("Ingrese código del producto: ")
            nuevo_precio = input("Ingrese nuevo precio: ")

            if not validar_precio(nuevo_precio):
                print("Debe ingresar un precio entero positivo")
            elif actualizar_precio(codigo, int(nuevo_precio)):
                print("Precio actualizado")
            else:
                print("El código no existe")

            continuar = input("¿Desea actualizar otro precio (s/n)?: ").lower()

    elif opcion == 4:
        codigo = input("Ingrese código del producto: ")
        nombre = input("Ingrese nombre: ")
        categoria = input("Ingrese categoría: ")
        marca = input("Ingrese marca: ")
        peso_kg = input("Ingrese peso (kg): ")
        importado = input("¿Es importado? (s/n): ")
        cachorro = input("¿Es para cachorro? (s/n): ")
        precio = input("Ingrese precio: ")
        unidades = input("Ingrese unidades: ")

        if codigo.strip() == "" or codigo.upper() in productos:
            print("El código ya existe")
        elif not validar_nombre(nombre):
            print("El nombre no es válido")
        elif not validar_categoria(categoria):
            print("La categoría no es válida")
        elif not validar_marca(marca):
            print("La marca no es válida")
        elif not validar_peso_kg(peso_kg):
            print("El peso no es válido")
        elif not validar_es_importado(importado):
            print("Debe ingresar 's' o 'n'")
        elif not validar_es_para_cachorro(cachorro):
            print("Debe ingresar 's' o 'n'")
        elif not validar_precio(precio):
            print("El precio no es válido")
        elif not validar_unidades(unidades):
            print("Las unidades no son válidas")
        else:
            es_importado = importado.lower() == "s"
            es_cachorro = cachorro.lower() == "s"
            agregar_producto(codigo, nombre, categoria, marca, float(peso_kg),
                              es_importado, es_cachorro, int(precio), int(unidades))
            print("Producto agregado")

    elif opcion == 5:
        codigo = input("Ingrese código del producto: ")
        if eliminar_producto(codigo):
            print("Producto eliminado")
        else:
            print("El código no existe")

    elif opcion == 6:
        print("Programa finalizado.")
        break