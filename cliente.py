import utils as u

def leer_clientes():
    return u.leer_archivo(u.NOMBRE_ARCHIVO_CLIENTES)


def agregar_cliente(cedula, nombre_completo, telefono, correo, direccion = ""):
    if u.existe_archivo(u.NOMBRE_ARCHIVO_CLIENTES) == False:
        u.crear_archivo(u.NOMBRE_ARCHIVO_CLIENTES, [])

    clientes = u.leer_archivo_cliente(u.NOMBRE_ARCHIVO_CLIENTES)

    if cedula:
        cedulas = list(map(lambda x: x['cedula'], clientes))
        if cedula in cedulas:
            print(f"Ya hay un cliente con la cedula {cedula}")
            return 

    cliente = {
            "cedula": cedula,
            "nombre_completo": nombre_completo,
            "telefono": telefono,
            "correo": correo,
            "direccion": direccion,
        }
    clientes.append(cliente)
    u.crear_archivo(u.NOMBRE_ARCHIVO_CLIENTES, clientes)
    
    print("Cliente guardado con exito")


def editar_cliente(cedula):
    if u.existe_archivo(u.NOMBRE_ARCHIVO_CLIENTES) == False:
         print("No se ha encontrado el archivo de clientes")
         return
     
    clientes = u.leer_archivo_cliente(u.NOMBRE_ARCHIVO_CLIENTES) 
    cliente_encontrado = [cliente for cliente in clientes if cliente["cedula"] == cedula]
    if len(cliente_encontrado) == 0:
        print(f"No existe un cliente con la cedula {cedula}")
        return
    cliente_encontrado = cliente_encontrado[0]
    nombre_completo = input(f"Nombre {cliente_encontrado["nombre_completo"]}") or cliente_encontrado["nombre_completo"]
    telefono = input(f"Telefono {cliente_encontrado["telefono"]}") or cliente_encontrado["telefono"]
    direccion = input(f"Direccion {cliente_encontrado["direccion"]}") or cliente_encontrado["direccion"]
    correo = input(f"Correo {cliente_encontrado["correo"]}") or cliente_encontrado["correo"]

    otros_clientes = [cliente for cliente in clientes if cliente["cedula"] != cedula]
    cliente_editado = {
         "cedula": cedula,
         "nombre_completo": nombre_completo,
         "telefono": telefono,
         "correo": correo,
         "direccion": direccion,
    }
    otros_clientes.append(cliente_editado)
    u.crear_archivo(u.NOMBRE_ARCHIVO_CLIENTES, otros_clientes)
    print("Cliente editado con exito")