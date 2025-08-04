import json

chefs_file="chefs.json"
 
 
def cargar_chef():
    try:
        with open(chefs_file,"r")as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def guardar_chef(data):
    with open (chefs_file,"w") as file:
        json.dump(data,file,indent=4)

def agregar_chef():
    chefs=cargar_chef()
    nombre=input("nombre del chef:")
    especialidad=input("especialidad:")
    chefs.append({
        "nombre":nombre,
        "especialidad":especialidad
    })
    guardar_chef(chefs)
    print("chef agregado")

def ver_chefs():
    chefs=cargar_chef()
    for chef in chefs:
        print(f"{chef["nombre"]}-{chef["especialidad"]}")

def actualizar_chef():
    chefs=cargar_chef()
    nombre=input("nombre del chef a actualizar:")
    for chef in chefs:
        if chef["nombre"].lower()== nombre.lower():
            chef["especialidad"]=input("nueva especialidad:")
            guardar_chef(chefs)
            print("chef actualizado")
            return
        print("chef no encontrado")

def eliminar_chef():
    chefs=cargar_chef()
    nombre=input("nombre del chef a eliminar:")
    chefs=[c for c in chefs if c ["nombre"].lower()!=nombre.lower()]
    guardar_chef(chefs)
    print("chef eliminado")



        


 