
import os
import json

NOMBRE_ARCHIVO_CLIENTES = "clientes.json"

def ingresar_valor(prompt, esTexto = True, esFlotante=False):
    while True:
        try:
            if esTexto:
                texto = input(prompt)
                if len(texto.strip()) == 0:
                    raise Exception()
                else: 
                    return texto 
            else:
                texto = int(input(prompt)) if esFlotante == False else float(input(prompt))  
                return texto  
        except Exception:
            print("Ingrese un texto valido")
        except ValueError:      
            print("Ingrese un numero valido")

def existe_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        return True
    else:
        return False

def crear_archivo(nombre_archivo, data):
    with open(nombre_archivo, "w") as json_file:
        json.dump(data, json_file)
    print(f"El archivo '{nombre_archivo}' ha sido creado correctamente.")

def leer_archivo_cliente(nombre_archivo):
    with open(nombre_archivo, "r") as file:
        data = json.load(file)  

    return formatear_clientes(data)    

def formatear_clientes(datos_clientes):
    clientes = []
    for cl in datos_clientes:
        cliente = {
            "cedula": cl["cedula"],
            "nombre_completo": cl["nombre_completo"],
            "telefono": cl["telefono"],
            "correo": cl["correo"],
            "direccion": cl["direccion"],
        }
        clientes.append(cliente)

    return clientes        

def formatear_text(texto):
    print(f"*********{texto}*********")

def limpiar_pantalla():
    input("Presione Enter para continuar...")
    # Limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')    