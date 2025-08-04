import utils.screencontroller as sc
import controllers.ingredientes as gr
import controllers.categorias as ca
import controllers.cheft as ch
import controllers.hamburgesas as ha
import controllers.reportes as re

def main_ingredientes():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('        MENU INGREDIENTES')
        print('===========================================')
        print('¿Qué tipo de elemento deseas añadir?')
        print('1. ver ingrediente')
        print('2. agregar ingrediente')
        print('3. actualizar ingrediente')
        print("4. eliminar ingrediente")
        print('5. Regresar al Menú Principal')
        print('===========================================')

        try:
            op = int(input('\nSelecciona una opción (1-5): '))
            if op == 1:
                gr.ver_ingredientes()
                
            elif op == 2:
                gr.guardar_ingredientes()
                
            elif op == 3:
                gr.actualizar_ingredientes()
                
            elif op == 4:
                gr.eliminar_ingredientes()

            elif op == 5:   
                print("\nRegresando al menú principal...")
                break
            else:
                print("\nOpción inválida. Por favor selecciona un número del 1 al 4.")
                sc.pausar()
        except ValueError:
            print('\nEntrada inválida. Por favor, introduce un número.')
            sc.pausar()


        

        
  

def main_menu_categorias():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('          MENU CATEGORIAS')
        print('===========================================')
        print('1. ver categorias')
        print('2. agregar categorias')
        print('3. actualizar categoria')
        print('4. eliminar categoria')
        print('5. Regresar al Menú Principal')
        print('===========================================')

        try:
            opcion = int(input('\nSelecciona una opción (1-4): '))
            if opcion == 1:
                ca.ver_categoria()
                

            elif opcion == 2:
                ca.agregar_categoria()
                

            elif opcion == 3:
                ca.actualizar_categoria()
                

            elif opcion == 4:
                ca.eliminar_categoria()

            elif opcion == 5:
                print("\nRegresando al menú principal...")
                break
            else:
                print("\nOpción inválida. Por favor selecciona un número del 1 al 4.")
                sc.pausar()

        except ValueError:
            print('\nEntrada no válida. Por favor, ingresa un número.')
            sc.pausar()

def main_menu_chefs():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('              MENU CHEFS')
        print('===========================================')
        print('1. ver chefs')
        print('2. agregar chefs')
        print('3. actualizar chefs')
        print('4. eliminar chefs')
        print('5. Regresar al Menú Principal')
        print('===========================================')

        try:
            op = int(input('\nSelecciona una opción (1-4): '))
            if op == 1:
                ch.ver_chefs()
                

            elif op == 2:
                ch.agregar_chef()

            elif op == 3:
                ch.actualizar_chef()

            elif op == 4:
                ch.eliminar_chef()

            elif op == 5:
                print("\nRegresando al menú principal...")
                break
            else:
                print('\nOpción no válida. Intenta de nuevo.')
                sc.pausar()
        except ValueError:
            print("\nEntrada no válida. Por favor, introduce un número.")
            sc.pausar()

def main_menu_hamburgesas():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('        MENU HAMBURGUESAS ')
        print('===========================================')
        print('1. ver hamburgesas')
        print('2. agregar hamburgesas')
        print('3. actualizar hambuergesas')
        print('4. eliminar hamburguesas')
        print('5. Regresar al Menú Principal')
        print('===========================================')

        try:
            op = int(input('\nSelecciona una opción (1-5): '))
            if op == 1:
                ha.ver_hamburguesas()
                
            elif op == 2:
                ha.agregar_hamburguesa()
                
            elif op == 3:
                ha.actualizar_hamburguesa()
                
            elif op == 4:
                ha.eliminar_hamburguesa()
                
            elif op == 5:
                print("\nRegresando al menú principal...")
                break
            else:
                print('\nOpción no válida. Intenta de nuevo.')
                sc.pausar()
        except ValueError:
            print('\nEntrada inválida. Por favor, introduce un número.')
            sc.pausar()






def main_menu_reportes():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('         MENU REPORTES')
        print('===========================================')
        print('1. ver hamburgesa por categoria')
        print('2. ver hamburgesa por chef')
        print('3. ver hamburgesa mas cara')
        print('3. Regresar al Menú Principal')
        print('===========================================')

        try:
            opcion = int(input('\nSelecciona una opción (1-3): '))
            
            if opcion == 1:
                re.hamburguesas_por_categoria()

            elif opcion == 2:
               re.hamburguesas_por_chef()

            elif opcion == 3:
                re.hamburguesa_mas_cara()

            elif opcion == 4:
                print("\nRegresando al menú principal...")
                break  

            else:
                print("\nOpción no válida. Por favor, ingresa un número del 1 al 3.")
                sc.pausar()

        except ValueError:
            print('\nEntrada no válida. Por favor, ingresa un número.')
            sc.pausar()

                       
    




                                
                

