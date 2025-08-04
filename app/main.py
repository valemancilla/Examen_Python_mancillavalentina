"""
Autor:  valentina mancilla
Fecha: 28/07/2025
Descripción: La cafetería de Campuslands proporcionará a los campistas la conveniencia de adquirir hamburguesas
"""

import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.screencontroller as sc
import controllers.menus as mn



def main_menu():
    while True:
        sc.limpiar_pantalla()
        print('==============================================================')
        print('El módulo de reportes debe realizar las siguientes consultas:')
        print('================================================================')
        print('1.Encontrar todos los ingredientes con stock menor a 400')
        print('2.encontrar todas las hamburguesas de la categoría “Vegetariana”.')
        print("3.Encontrar todos los chefs que se especializan en “Carnes”.")
        print("4.Aumentar en 1.5 el precio de todos los ingredientes.")
        print("5.Encontrar todas las hamburguesas preparadas por “ChefB”.")
        print('6.Encontrar el nombre y la descripción de todas las categorías.')
        print('7.Eliminar todos los ingredientes que tengan un stock de 0.')
        print('8.Agregar un nuevo ingrediente a la hamburguesa “Clásica”.')
        print('9.Encontrar todas las hamburguesas que contienen “Pan integral” como ingrediente.')
        print('10.Cambiar la especialidad del “ChefC” a “Cocina Internacional”.')
        print('Encontrar el ingrediente más caro.')
        print(' Encontrar las hamburguesas que no contienen “Queso cheddar” como ingrediente.')
        print('Incrementar el stock de “Pan” en 100 unidades.')
        print('Eliminar las hamburguesas que contienen menos de 5 ingredientes.')
        print('Agregar un nuevo chef a la colección con una especialidad en “Cocina Asiática”')
        print('Listar las hamburguesas en orden ascendente según su precio.')
        print('Encontrar todos los ingredientes cuyo precio sea entre $2 y $5.')
        print('Actualizar la descripción del “Pan” a “Pan fresco y crujiente”.')
        print('Encontrar la hamburguesa más cara que fue preparada por un chef especializado en “Gourmet”.')
        print('Listar todos los ingredientes junto con el número de hamburguesas que los contienen.')
        print('21. Salir')
        print('=====================================================================================')

        try:
            op = int(input("\nElige una opción (1-21): "))
            if 1 <= op <= 21:
                return op
        except ValueError:
            pass  

        print("\nOpción no válida. Intenta nuevamente.")
        sc.pausar()


if __name__ == "__main__":
    while True:
        opcion = main_menu()

        if opcion == 1:
            mn.main_ingredientes()
        elif opcion == 2:
            mn.main_menu_hamburgesas()
        elif opcion == 3:
            mn.main_menu_chefs()
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            break