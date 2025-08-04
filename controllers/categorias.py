import json
categorias_file = "categorias.json"

def cargar_categoria():
    try:
        with open(categorias_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_categoria(data):
    with open(categorias_file, "w") as file:
        json.dump(data, file, indent=4)

def agregar_categoria():
    categorias = cargar_categoria()
    nombre = input("Nombre de la categoria: ")
    descripcion = input("Descripción: ")
    categorias.append({
        "nombre": nombre,
        "descripcion": descripcion
    })

    guardar_categoria(categorias)
    print("Categoría guardada")

def ver_categoria():
    categorias = cargar_categoria()
    if not categorias:
        print("No hay categorías para mostrar.")
        return

    for cat in categorias:
        print(f'{cat["nombre"]} - {cat["descripcion"]}')
        
def actualizar_categoria():
    categorias = cargar_categoria()  
    nombre = input("Nombre de la categoría a actualizar: ")

    categoria_encontrada = False
    for cat in categorias: 
        if cat["nombre"].lower() == nombre.lower():
            categoria_encontrada = True
            cat["descripcion"] = input("Nueva descripción: ")
            guardar_categoria(categorias)
            print("Categoría actualizada")
            break

    if not categoria_encontrada:
        print("Categoría no encontrada.")  

def eliminar_categoria():
    categorias = cargar_categoria()
    nombre = input("Nombre de la categoría a eliminar: ")

    categorias_filtradas = [cat for cat in categorias if cat["nombre"].lower() != nombre.lower()]

    if len(categorias_filtradas) == len(categorias):
        print("Categoría no encontrada.")
    else:
        guardar_categoria(categorias_filtradas)
        print("Categoría eliminada")
