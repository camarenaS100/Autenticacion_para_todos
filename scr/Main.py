print("\n¿Que programa desea probar?\n")
print("1. Seguimiento de oreja")
print("2. Captura de ojetos")
print("3. Cambio de escalas de colores")
opcion = input("\nOpcion: ")

if(opcion == '1'):
    with open("siguiendoOreja.py", "r") as archivo:
        codigo = archivo.read()
    exec(codigo)
elif(opcion == '2'):
    with open("capturaObjetos.py", "r") as archivo:
        codigo = archivo.read()
    exec(codigo)
elif(opcion == '3'):
    with open("figura_oreja.py", "r") as archivo:
        codigo = archivo.read()
    exec(codigo)
else:
    print("\nOpcion incorrecta\n")
