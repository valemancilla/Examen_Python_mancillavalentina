import json

HAMBURGUESAS_FILE = "hamburguesas.json"

def cargar_hamburguesas():
    try:
        with open(HAMBURGUESAS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def hamburguesas_por_categoria():
    categoria = input("Ingrese la categoría: ")
    hamburguesas = cargar_hamburguesas()
    encontradas = [h for h in hamburguesas if h["categoria"].lower() == categoria.lower()]
    if encontradas:
        print(f"Hamburguesas en la categoría '{categoria}':")
        for h in encontradas:
            print(f" - {h['nombre']} (${h['precio']})")
    else:
        print("No se encontraron hamburguesas para esa categoría.")

def hamburguesas_por_chef():
    chef = input("Ingrese el nombre del chef: ")
    hamburguesas = cargar_hamburguesas()
    encontradas = [h for h in hamburguesas if h["chef"].lower() == chef.lower()]
    if encontradas:
        print(f"Hamburguesas hechas por el chef '{chef}':")
        for h in encontradas:
            print(f" - {h['nombre']} (${h['precio']})")
    else:
        print("No se encontraron hamburguesas para ese chef.")

def hamburguesa_mas_cara():
    hamburguesas = cargar_hamburguesas()
    if hamburguesas:
        mas_cara = max(hamburguesas, key=lambda h: h["precio"])
        print(f"La hamburguesa más cara es '{mas_cara['nombre']}' (${mas_cara['precio']})")
    else:
        print("No hay hamburguesas registradas.")