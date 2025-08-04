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
    categoria = cargar_categoria()
    for cat in categoria:
        print(f'{cat["nombre"]} - {cat["descripcion"]}')
        
def actualizar_categoria():
    categorias = cargar_categoria()  
    nombre = input("Nombre de la categoría a actualizar: ")
    for cat in categorias: 
        if cat["nombre"].lower() == nombre.lower():
            cat["descripcion"] = input("Nueva descripción: ")
            guardar_categoria(categorias)
            print("Categoría actualizada")
            return
    print("Categoría no encontrada.")  
def eliminar_categoria():
    categorias = cargar_categoria()
    nombre = input("Nombre de la categoría a eliminar: ")
    categorias = [cat for cat in categorias if cat["nombre"].lower() != nombre.lower()]
    guardar_categoria(categorias)
    print("Categoría eliminada")
