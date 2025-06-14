import utils as u

def leer_clientes():
    """
        Esta funcion lee los clientes 
        Returns:
            lista: Lista de clientes en forma de diccionario
    """      
    return u.leer_archivo(u.NOMBRE_ARCHIVO_CLIENTES)


def agregar_cliente():
    """
        Esta funcion crear el archivo de cliente si no existe
            Si existe archivo lee archivo de clientes
            Recibe numero de cedula y valida si ya existe un usuario con esa cedula
            En caso de no existir recibe los valores faltantes del cliente y escribe sobre el archivo de cliente
    """        
    if u.existe_archivo(u.NOMBRE_ARCHIVO_CLIENTES) == False:
        u.crear_archivo(u.NOMBRE_ARCHIVO_CLIENTES, [])

    clientes = u.leer_archivo_cliente(u.NOMBRE_ARCHIVO_CLIENTES)
# cedula, nombre_completo, telefono, correo, direccion = ""
    cedula = u.ingresar_valor("Ingrese una cedula", False)
    if cedula:
        cedulas = list(map(lambda x: x['cedula'], clientes))
        if cedula in cedulas:
            print(f"Ya hay un cliente con la cedula {cedula}")
            return 
    nombre_completo = u.ingresar_valor("Ingrese el nombre completo")    
    telefono = u.ingresar_valor("Ingrese un telefono", False)  
    correo = u.ingresar_valor("Ingrese un correo")
    direccion = input("Ingrese una direccion")    
                   
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


def editar_cliente():
    """
        Esta funcion edita nombre, telefono, dirrecion y correo del cliente
            Si el archivo de clientes no existe se detiene el proceso
            Lee el archivo del cliente
            Filtra las cedulas existentes 
            Recibe los valores nuevos y despues los guarda en el archivo de clientes nuevamente
    """      
    cedula = u.ingresar_valor("Ingrese una cedula", False)
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

def eliminar_cliente():
    """
        Esta funcion borra el cliente con la cedula aportada
    """          
    cedula = u.ingresar_valor("Ingrese una cedula", False)
    if u.existe_archivo(u.NOMBRE_ARCHIVO_CLIENTES) == False:
         print("No se ha encontrado el archivo de clientes")
         
    clientes = u.leer_archivo_cliente(u.NOMBRE_ARCHIVO_CLIENTES)
    cliente_encontrado = [cliente for cliente in clientes if cliente["cedula"] == cedula] 
    if len(cliente_encontrado) == 0:
        print(f"Cliente con {cedula} no encontrado")
        return
    
    otros_clientes = [cliente for cliente in clientes if cliente["cedula"] != cedula]
    u.crear_archivo(u.NOMBRE_ARCHIVO_CLIENTES, otros_clientes)
    print(f"Cliente con {cedula}, removido con exito")
