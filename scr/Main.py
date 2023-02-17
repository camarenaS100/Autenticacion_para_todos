import os

def limpiar_pantalla():
    # En Unix/Linux
    if os.name == "posix":
        os.system("clear")
    # En Windows
    elif os.name == "nt":
        os.system("cls")

limpiar_pantalla()
print("\n\t**ASEGURESE DE QUE LAS RUTAS ESTEN CORRECTAS**\n")
print("\n¿Que programa desea probar?\n")
print("1. Seguimiento de oreja")
print("2. Captura de ojetos")
print("3. Cambio de escalas de colores")
print("0. EXIT")
opcion = input("\nOpcion: ")

if(opcion == '1'):
    # os.system("python siguiendoOreja.py")
    with open("siguiendoOreja.py", "r") as archivo:
        codigo = archivo.read()
    exec(codigo)
elif(opcion == '2'):
    with open("capturaObjetos.py", "r") as archivo:
        codigo1 = archivo.read()
    exec(codigo1)
elif(opcion == '3'):
    with open("figura_oreja.py", "r") as archivo:
        codigo2 = archivo.read()
    exec(codigo2)
elif(opcion == '0'):
    exit()
else:
    print("\nOpcion incorrecta\n")
