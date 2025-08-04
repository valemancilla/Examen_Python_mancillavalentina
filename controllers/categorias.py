import json
categorias_file="categorias.json"

def cargar_categoria():
    try:
        with open (categorias_file,"r")as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def guardar_categoria(data):
    with open(categorias_file,"w") as file:
        json.dump(data,file,indent=4)


def agregar_categoria():
    categorias=cargar_categoria()
    nombre=input("nombre de la categoria")
    descripcion=input("descripcion:")
    categorias.append({
        "nombre":nombre,
        "descripcion":descripcion

    })

    guardar_categoria(categorias)
    print("categoria guardad")

def ver_categoria():
    categoria=cargar_categoria()
    for cat in categoria:
        print(f'{cat['nombre']}-{cat['descripcion']}')

def actualizar_categoria():
    categoria=categorias_file()
    nombre=input("nombre de la categoriaa actualizar:")
    for cat in categoria: 
        if cat ["nombre"].lower()== nombre.lower():
            cat["descripcion"]=input("nueva descripcion:")
            guardar_categoria(categoria)
            print("categoria actualizada")
            return
        
def eliminar_categoria():
    categorias=cargar_categoria()
    nombre=input("nombre de la categoria a eliminar:")
    categorias=[cat for cat in categorias if cat ["nombre"].lower()!=nombre.lower()]
    guardar_categoria(categorias)
    print("categoria eliminada")
