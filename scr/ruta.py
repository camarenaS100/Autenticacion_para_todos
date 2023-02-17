import os

def get_main_path():
    # Lista de directorios donde buscar el archivo "main.py"
    search_dirs = [
        os.getcwd(),             # Directorio actual
        os.path.expanduser("~")  # Directorio del usuario actual
    ]

    # Recorre los directorios en busca del archivo "main.py"
    for dir in search_dirs:
        main_path = os.path.join(dir, "Main.py")
        if os.path.exists(main_path):
            return main_path

    # Si no se encuentra el archivo, levanta una excepción
    raise FileNotFoundError("No se encontró el archivo main.py en ningún directorio.")
