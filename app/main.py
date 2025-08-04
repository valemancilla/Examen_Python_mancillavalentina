"""
Autor:  valentina mancilla
Fecha: 28/07/2025
Descripción: La cafetería de Campuslands proporcionará a los campistas la conveniencia de adquirir hamburguesas
"""

import controllers.ingredientes as gr
import sys
import utils.screencontroller as sc


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main_menu():
    while True:
            
        print('========================================')
        print('Menu ingredientes')
        print('========================================')
        print('1. ver ingredientes')
        print('2. agregar ingredientes')
        print('3. actualizar ingredientes')
        print('4. eliminar ingredientes')
        print('5. Salir')
        print('========================================')

        try:
            op = int(input("\nElige una opción (1-7): "))
            if 1 <= op <= 5:
                return op
        except ValueError:
            pass  

        print("\nOpción no válida. Intenta nuevamente.")
        sc.pausar()


if __name__ == "__main__":
    while True:
        opcion = main_menu()

        if opcion == 1:
            gr.ver_ingredientes()
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            break
