import os
import sys

def pausar():
    if sys.platform in ["linux", "darwin"]:
        input("Presiona ENTER para continuar...")
    else:
        os.system("pause")

def limpiarpantalla ():
    if sys.platform in ["linux", "darwin"]:
        os.system("clear")
    else:
        os.system("cls")