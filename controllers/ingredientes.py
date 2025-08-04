import json
ingredientes_file="ingredientes.json"

def cargar_ingredientes():
    try:
        with open (ingredientes_file,"r")as file:
            return json.load(file)
    except FileNotFoundError:
        return[]


def guardar_ingredientes():
    ingredientes=cargar_ingredientes()
    nombre= input("nombre:")
    descripcion=input("descripcion:")
    precio=float(input("precio:"))
    stock=int(input("stock:"))
    ingredientes.append({
        "nombre":nombre,
        "descripcion":descripcion,
        "precio":precio,
        "stock":stock
    })
    guardar_ingredientes(ingredientes)
    print("ingredientes agregados")

def ver_ingredientes():
    ingredientes= cargar_ingredientes()
    for i in ingredientes:
        print("i")

def actualizar_ingredientes():
    ingredientes=cargar_ingredientes()
    nombre= input ("nombre del ingredientes a actualizar:")
    for ing in ingredientes:
        if ing ["nombre"].lower()== nombre.lower():
            ing["precio"]= float(input("nuevo precio:"))
            ing["stock"]=int(input("nuevo stock:"))
            guardar_ingredientes(ingredientes)
            print("ingredientes actualizados" )
            return
        print("ingredientes no encontrados")

def eliminar_ingredientes():
    ingredientes=cargar_ingredientes()
    nombre=input("nombre del ingrediente a eliminar:")
    ingredientes=[i for i in ingredientes if i ["nombre"].lower()!= nombre.lower()]
    guardar_ingredientes(ingredientes)
    print("ingrediente eliminado")





