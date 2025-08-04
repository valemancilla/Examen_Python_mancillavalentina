
import json

HAMBURGUESAS_FILE = "hamburguesas.json"

def cargar_hamburguesas():
    try:
        with open(HAMBURGUESAS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_hamburguesas(data):
    with open(HAMBURGUESAS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def agregar_hamburguesa():
    hamburguesas = cargar_hamburguesas()
    nombre = input("Nombre de la hamburguesa: ")
    ingredientes = input("Ingredientes (separados por comas): ").split(",")
    categoria = input("Categoría: ")
    chef = input("Nombre del chef: ")
    precio = float(input("Precio: "))
    hamburguesas.append({
        "nombre": nombre,
        "ingredientes": [i.strip() for i in ingredientes],
        "categoria": categoria,
        "chef": chef,
        "precio": precio
    })
    guardar_hamburguesas(hamburguesas)
    print("Hamburguesa agregada.")

def ver_hamburguesas():
    hamburguesas = cargar_hamburguesas()
    for h in hamburguesas:
        print(f"{h['nombre']} - ${h['precio']} | Cat: {h['categoria']} | Chef: {h['chef']}")
        print(f" Ingredientes: {', '.join(h['ingredientes'])}")
        print("-" * 40)

def actualizar_hamburguesa():
    hamburguesas = cargar_hamburguesas()
    nombre = input("Nombre de la hamburguesa a actualizar: ")
    for h in hamburguesas:
        if h["nombre"].lower() == nombre.lower():
            h["ingredientes"] = input("Nuevos ingredientes (separados por comas): ").split(",")
            h["categoria"] = input("Nueva categoría: ")
            h["chef"] = input("Nuevo chef: ")
            h["precio"] = float(input("Nuevo precio: "))
            guardar_hamburguesas(hamburguesas)
            print("Hamburguesa actualizada.")
            return
    print("Hamburguesa no encontrada.")

def eliminar_hamburguesa():
    hamburguesas = cargar_hamburguesas()
    nombre = input("Nombre de la hamburguesa a eliminar: ")
    hamburguesas = [h for h in hamburguesas if h["nombre"].lower() != nombre.lower()]
    guardar_hamburguesas(hamburguesas)
    print("Hamburguesa eliminada.")