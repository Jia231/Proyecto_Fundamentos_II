import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import json
import os
import utils as u
import usuario as us



def resize_last_dialog(width=350, height=180):
    
    w = root.winfo_children()[-1]
    if isinstance(w, tk.Toplevel):
        w.geometry(f"{width}x{height}")
        

def my_askstring(title, prompt):
    root.after(20, resize_last_dialog, 400, 150)
    return askstring(title, f"{prompt}\t\t\t\t", parent=root)

root = tk.Tk()
root.withdraw()

ORDENES_FILE = "ordenes_trabajo.json"

def leer_clientes():
    
    return u.leer_archivo(u.NOMBRE_ARCHIVO_CLIENTES)

def cargar_ordenes():
    if os.path.exists(ORDENES_FILE):
        with open(ORDENES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

guardar_orden = cargar_ordenes()

def guardar_ordenes_json():
    with open(ORDENES_FILE, "w", encoding="utf-8") as f:
        json.dump(guardar_orden, f, ensure_ascii=False, indent=4)
    
def interfaz_ordenes_trabajo():
    def usuario_autenticado():
        usuario = my_askstring("Usuario", "Introduzca el usuario:")
        password = my_askstring("Contraseña", "Introduzca la contraseña:")
        return us.validar_usuario(usuario, password)
    if not usuario_autenticado():
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
        return
    
    def crear():
        cliente = my_askstring("Cliente", "Ingrese el nombre del cliente:")
        fecha = my_askstring("Fecha", "Ingrese la fecha de creación (DD-MM-AAAA):")
        fecha_entrega = my_askstring("Fecha Entrega", "Ingrese la fecha de entrega (DD-MM-AAAA):")
        descripcion = my_askstring("Descripción", "Tipo de Producto:")
        medidas = my_askstring("Medidas", "Medidas:")
        cantidad = my_askstring("Cantidad", "Cantidad:")
        diseñador = my_askstring("Diseñador", "Nombre del diseñador:")
        impresora = my_askstring("Impresora", "Nombre de la impresora:")
        obcervaciones = my_askstring("Observaciones", "Observaciones:")
        precio = my_askstring("Precio", "Precio:")
        estado = my_askstring("Estado", "Estado (Pendiente/Completada/Entregada):")
        if cliente and fecha:
            # Generar ID
            if guardar_orden:
                ultimo_id = max(int(o["id_orden"]) for o in guardar_orden)
                id_orden = str(ultimo_id + 1)
            else:
                id_orden = "1"
            nueva_orden = {
                "id_orden": id_orden,
                "cliente": cliente,
                "fecha": fecha,
                "fecha de entrega": fecha_entrega,
                "descripcion": descripcion,
                "medidas": medidas,
                "cantidad": cantidad,
                "diseñador": diseñador,
                "impresora": impresora,
                "obcervaciones": obcervaciones,
                "precio": precio,
                "estado": estado
            }
            guardar_orden.append(nueva_orden)
            guardar_ordenes_json()
            messagebox.showinfo("Éxito", f"Orden de trabajo {id_orden} creada con éxito.")
        else:
            messagebox.showwarning("Error", "Datos insuficientes.")

    def consultar():
        criterio = my_askstring("Buscar", "Buscar por cliente (1) o fecha (2):")
        if criterio == "1":
            cliente = my_askstring("Cliente", "Ingrese el nombre del cliente:")
            ordenes = [o for o in guardar_orden if o["cliente"].lower() == cliente.lower()]
        elif criterio == "2":
            fecha = my_askstring("Fecha", "Ingrese la fecha (DD-MM-AAAA):")
            ordenes = [o for o in guardar_orden if o["fecha"] == fecha]
        else:
            ordenes = []
        if ordenes:
            resultado = "\n".join([str(o) for o in ordenes])
            messagebox.showinfo("Resultados", resultado)
        else:
            messagebox.showinfo("Resultados", "No se encontraron órdenes.")

    def modificar():
        id_orden = my_askstring("Modificar", "Ingrese el ID de la orden:")
        orden = next((o for o in guardar_orden if int(o["id_orden"]) == int(id_orden)), None)
        if orden:
            cliente = my_askstring("Cliente", f"Cliente ({orden['cliente']}):") or orden["cliente"]
            descripcion = my_askstring("Descripción", f"Descripción ({orden['descripcion']}):") or orden["descripcion"]
            fecha_entrega = my_askstring("Fecha Entrega", f"Fecha de entrega ({orden['fecha de entrega']}):") or orden["fecha de entrega"]
            cantidad = my_askstring("Cantidad", f"Cantidad ({orden['cantidad']}):") or orden["cantidad"]
            obcervaciones = my_askstring("Observaciones", f"Observaciones ({orden['obcervaciones']}):") or orden["obcervaciones"]
            estado = my_askstring("Estado", f"Estado ({orden['estado']}):") or orden["estado"]
            orden["cliente"] = cliente
            orden["descripcion"] = descripcion
            orden["fecha de entrega"] = fecha_entrega
            orden["cantidad"] = cantidad
            orden["obcervaciones"] = obcervaciones
            orden["estado"] = estado
            guardar_ordenes_json()
            messagebox.showinfo("Éxito", f"Orden {id_orden} modificada.")
        else:
            messagebox.showwarning("Error", "No se encontró la orden.")

    def eliminar():
        id_orden = my_askstring("Eliminar", "Ingrese el ID de la orden:")
        orden = next((o for o in guardar_orden if o["id_orden"] == id_orden), None)
        if orden:
            guardar_orden.remove(orden)
            guardar_ordenes_json()
            messagebox.showinfo("Éxito", f"Orden {id_orden} eliminada.")
        else:
            messagebox.showwarning("Error", "No se encontró la orden.")

    def reporte_dia():
        fecha = my_askstring("Reporte Día", "Ingrese la fecha (DD-MM-AAAA):")
        ordenes_dia = [o for o in guardar_orden if o["fecha"] == fecha]
        if ordenes_dia:
            resultado = "\n".join([f"ID: {o['id_orden']}, Cliente: {o['cliente']}, Desc: {o['descripcion']}, Estado: {o['estado']}" for o in ordenes_dia])
            messagebox.showinfo("Reporte", resultado)
        else:
            messagebox.showinfo("Reporte", "No hay órdenes para esa fecha.")

    def reporte_mes():
        mes = my_askstring("Reporte Mes", "Ingrese el mes (MM-AAAA):")
        ingresos_mes = sum(float(o["precio"]) for o in guardar_orden if o["fecha"].endswith(mes))
        messagebox.showinfo("Ingresos", f"Ingresos totales del mes {mes}: ${ingresos_mes:.2f}")
        
    def reporte_uso_impresoras():
        impresoras = {}
        for orden in guardar_orden:
            impresora = orden["impresora"]
            if impresora not in impresoras:
                impresoras[impresora] = 0
            impresoras[impresora] += 1
        resultado = "\n".join([f"Impresora: {imp}, Órdenes: {count}" for imp, count in impresoras.items()])
        messagebox.showinfo("Uso Impresoras", resultado)
        
    def agregar_cliente():
        if not u.existe_archivo(u.NOMBRE_ARCHIVO_CLIENTES):
            u.crear_archivo(u.NOMBRE_ARCHIVO_CLIENTES, [])

        clientes = u.leer_archivo_cliente(u.NOMBRE_ARCHIVO_CLIENTES)
        cedulas = list(map(lambda x: x['cedula'], clientes))

        # Solicitar cédula válida 
        while True:
            cedula = my_askstring("Agregar Cliente", "Ingrese la cédula del cliente:")
            if not cedula or not cedula.strip():
                messagebox.showwarning("Error", "Debe ingresar una cédula válida.")
                continue
            if cedula in cedulas:
                messagebox.showwarning("Error", f"Ya hay un cliente con la cédula {cedula}")
                continue
            break

        # Solicitar nombre completo válido
        while True:
            nombre_completo = my_askstring("Agregar Cliente", "Ingrese el nombre completo:") or ""
            if not nombre_completo.strip():
                messagebox.showwarning("Error", "Debe ingresar un nombre completo válido.")
                continue
            break

        # Solicitar teléfono válido
        while True:
            telefono = my_askstring("Agregar Cliente", "Ingrese un teléfono (8 dígitos):") or ""
            if not (telefono.isdigit() and len(telefono) == 8):
                messagebox.showwarning("Error", "Debe ingresar un teléfono válido de 8 dígitos.")
                continue
            break

        # Solicitar correo válido
        while True:
            correo = my_askstring("Agregar Cliente", "Ingrese un correo:") or ""
            if not correo.strip():
                messagebox.showwarning("Error", "Debe ingresar un correo válido.")
                continue
            break

        # Solicitar dirección válida
        while True:
            direccion = my_askstring("Agregar Cliente", "Ingrese una dirección:") or ""
            if not direccion.strip():
                messagebox.showwarning("Error", "Debe ingresar una dirección válida.")
                continue
            break

        cliente = {
            "cedula": int(cedula),
            "nombre_completo": nombre_completo,
            "telefono": telefono,
            "correo": correo,
            "direccion": direccion,
        }
        clientes.append(cliente)
        u.crear_archivo(u.NOMBRE_ARCHIVO_CLIENTES, clientes)
        messagebox.showinfo("Éxito", "Cliente guardado con éxito")

    def editar_cliente():
        cedula = my_askstring("Editar Cliente", "Ingrese la cédula del cliente a editar:")
        clientes = u.leer_archivo_cliente(u.NOMBRE_ARCHIVO_CLIENTES)
        cliente = next((c for c in clientes if int(c.get("cedula")) == int(cedula)), None)
        if not cliente:
            messagebox.showwarning("Error", "No se encontró el cliente.")
            return

        nombre_completo = my_askstring("Editar Cliente", f"Nombre completo ({cliente['nombre_completo']}):") or cliente["nombre_completo"]
        telefono = my_askstring("Editar Cliente", f"Teléfono ({cliente['telefono']}):") or cliente["telefono"]
        correo = my_askstring("Editar Cliente", f"Correo ({cliente['correo']}):") or cliente["correo"]
        direccion = my_askstring("Editar Cliente", f"Dirección ({cliente['direccion']}):") or cliente["direccion"]

        cliente_editado = {
            "cedula": cedula,
            "nombre_completo": nombre_completo,
            "telefono": telefono,
            "correo": correo,
            "direccion": direccion,
        }
        # Reemplazar el cliente editado en la lista
        idx = clientes.index(cliente)
        clientes[idx] = cliente_editado
        u.crear_archivo(u.NOMBRE_ARCHIVO_CLIENTES, clientes)

        messagebox.showinfo("Éxito", "Cliente editado con éxito")

    def eliminar_cliente():
        cedula = my_askstring("Eliminar Cliente", "Ingrese la cédula del cliente a eliminar:")
        clientes = u.leer_archivo_cliente(u.NOMBRE_ARCHIVO_CLIENTES)
        cliente = next((c for c in clientes if c.get("cedula") == cedula), None)
        if not cliente:
            messagebox.showwarning("Error", "No se encontró el cliente.")
            return

        clientes.remove(cliente)
        u.crear_archivo(u.NOMBRE_ARCHIVO_CLIENTES, clientes)
        messagebox.showinfo("Éxito", "Cliente eliminado con éxito")

    

    root = tk.Tk()
    root.title("Gestión de Órdenes de Trabajo")
    root.geometry("400x600")
    root.configure(bg="#488226")

    # Frame para centrar los botones
    frame = tk.Frame(root, bg="#488226")
    frame.pack(expand=True)

    tk.Button(frame, text="Crear Orden", command=crear, width=30).pack(pady=5)
    tk.Button(frame, text="Consultar Orden", command=consultar, width=30).pack(pady=5)
    tk.Button(frame, text="Modificar Orden", command=modificar, width=30).pack(pady=5)
    tk.Button(frame, text="Eliminar Orden", command=eliminar, width=30).pack(pady=5)
    tk.Button(frame, text="Reporte Órdenes Día", command=reporte_dia, width=30).pack(pady=5)
    tk.Button(frame, text="Reporte Ingresos Mes", command=reporte_mes, width=30).pack(pady=5)
    tk.Button(frame, text="Reporte Uso Impresoras", command=reporte_uso_impresoras, width=30).pack(pady=5)
    tk.Button(frame, text="Agregar Cliente", command=agregar_cliente, width=30).pack(pady=5)
    tk.Button(frame, text="Editar Cliente", command=editar_cliente, width=30).pack(pady=5)
    tk.Button(frame, text="Eliminar Cliente", command=eliminar_cliente, width=30).pack(pady=5)    
    tk.Button(frame, text="Salir", command=root.destroy, width=30).pack(pady=5)
    

    root.mainloop()
    




