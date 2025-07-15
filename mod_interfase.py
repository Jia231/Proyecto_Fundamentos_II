import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import utils as u

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
    def crear():
        cliente = simpledialog.askstring("Cliente", "Ingrese el nombre del cliente:")
        fecha = simpledialog.askstring("Fecha", "Ingrese la fecha de creación (DD-MM-AAAA):")
        fecha_entrega = simpledialog.askstring("Fecha Entrega", "Ingrese la fecha de entrega (DD-MM-AAAA):")
        descripcion = simpledialog.askstring("Descripción", "Tipo de Producto:")
        medidas = simpledialog.askstring("Medidas", "Medidas:")
        cantidad = simpledialog.askstring("Cantidad", "Cantidad:")
        diseñador = simpledialog.askstring("Diseñador", "Nombre del diseñador:")
        impresora = simpledialog.askstring("Impresora", "Nombre de la impresora:")
        obcervaciones = simpledialog.askstring("Observaciones", "Observaciones:")
        precio = simpledialog.askstring("Precio", "Precio:")
        estado = simpledialog.askstring("Estado", "Estado (Pendiente/Completada/Entregada):")
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
        criterio = simpledialog.askstring("Buscar", "Buscar por cliente (1) o fecha (2):")
        if criterio == "1":
            cliente = simpledialog.askstring("Cliente", "Ingrese el nombre del cliente:")
            ordenes = [o for o in guardar_orden if o["cliente"].lower() == cliente.lower()]
        elif criterio == "2":
            fecha = simpledialog.askstring("Fecha", "Ingrese la fecha (DD-MM-AAAA):")
            ordenes = [o for o in guardar_orden if o["fecha"] == fecha]
        else:
            ordenes = []
        if ordenes:
            resultado = "\n".join([str(o) for o in ordenes])
            messagebox.showinfo("Resultados", resultado)
        else:
            messagebox.showinfo("Resultados", "No se encontraron órdenes.")

    def modificar():
        id_orden = simpledialog.askstring("Modificar", "Ingrese el ID de la orden:")
        orden = next((o for o in guardar_orden if o["id_orden"] == id_orden), None)
        if orden:
            cliente = simpledialog.askstring("Cliente", f"Cliente ({orden['cliente']}):") or orden["cliente"]
            descripcion = simpledialog.askstring("Descripción", f"Descripción ({orden['descripcion']}):") or orden["descripcion"]
            fecha_entrega = simpledialog.askstring("Fecha Entrega", f"Fecha de entrega ({orden['fecha de entrega']}):") or orden["fecha de entrega"]
            cantidad = simpledialog.askstring("Cantidad", f"Cantidad ({orden['cantidad']}):") or orden["cantidad"]
            obcervaciones = simpledialog.askstring("Observaciones", f"Observaciones ({orden['obcervaciones']}):") or orden["obcervaciones"]
            estado = simpledialog.askstring("Estado", f"Estado ({orden['estado']}):") or orden["estado"]
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
        id_orden = simpledialog.askstring("Eliminar", "Ingrese el ID de la orden:")
        orden = next((o for o in guardar_orden if o["id_orden"] == id_orden), None)
        if orden:
            guardar_orden.remove(orden)
            guardar_ordenes_json()
            messagebox.showinfo("Éxito", f"Orden {id_orden} eliminada.")
        else:
            messagebox.showwarning("Error", "No se encontró la orden.")

    def reporte_dia():
        fecha = simpledialog.askstring("Reporte Día", "Ingrese la fecha (DD-MM-AAAA):")
        ordenes_dia = [o for o in guardar_orden if o["fecha"] == fecha]
        if ordenes_dia:
            resultado = "\n".join([f"ID: {o['id_orden']}, Cliente: {o['cliente']}, Desc: {o['descripcion']}, Estado: {o['estado']}" for o in ordenes_dia])
            messagebox.showinfo("Reporte", resultado)
        else:
            messagebox.showinfo("Reporte", "No hay órdenes para esa fecha.")

    def reporte_mes():
        mes = simpledialog.askstring("Reporte Mes", "Ingrese el mes (MM-AAAA):")
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
            cedula = simpledialog.askstring("Agregar Cliente", "Ingrese la cédula del cliente:")
            if not cedula or not cedula.strip():
                messagebox.showwarning("Error", "Debe ingresar una cédula válida.")
                continue
            if cedula in cedulas:
                messagebox.showwarning("Error", f"Ya hay un cliente con la cédula {cedula}")
                continue
            break

        # Solicitar nombre completo válido
        while True:
            nombre_completo = simpledialog.askstring("Agregar Cliente", "Ingrese el nombre completo:") or ""
            if not nombre_completo.strip():
                messagebox.showwarning("Error", "Debe ingresar un nombre completo válido.")
                continue
            break

        # Solicitar teléfono válido
        while True:
            telefono = simpledialog.askstring("Agregar Cliente", "Ingrese un teléfono (8 dígitos):") or ""
            if not (telefono.isdigit() and len(telefono) == 8):
                messagebox.showwarning("Error", "Debe ingresar un teléfono válido de 8 dígitos.")
                continue
            break

        # Solicitar correo válido
        while True:
            correo = simpledialog.askstring("Agregar Cliente", "Ingrese un correo:") or ""
            if not correo.strip():
                messagebox.showwarning("Error", "Debe ingresar un correo válido.")
                continue
            break

        # Solicitar dirección válida
        while True:
            direccion = simpledialog.askstring("Agregar Cliente", "Ingrese una dirección:") or ""
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
        cedula = simpledialog.askstring("Editar Cliente", "Ingrese la cédula del cliente a editar:")
        clientes = u.leer_archivo_cliente(u.NOMBRE_ARCHIVO_CLIENTES)
        cliente = next((c for c in clientes if c.get("cedula") == int(cedula)), None)
        if not cliente:
            messagebox.showwarning("Error", "No se encontró el cliente.")
            return

        nombre_completo = simpledialog.askstring("Editar Cliente", f"Nombre completo ({cliente['nombre_completo']}):") or cliente["nombre_completo"]
        telefono = simpledialog.askstring("Editar Cliente", f"Teléfono ({cliente['telefono']}):") or cliente["telefono"]
        correo = simpledialog.askstring("Editar Cliente", f"Correo ({cliente['correo']}):") or cliente["correo"]
        direccion = simpledialog.askstring("Editar Cliente", f"Dirección ({cliente['direccion']}):") or cliente["direccion"]

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
        cedula = simpledialog.askstring("Eliminar Cliente", "Ingrese la cédula del cliente a eliminar:")
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
    tk

    root.mainloop()
    




