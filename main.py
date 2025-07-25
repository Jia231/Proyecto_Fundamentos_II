"""Proyecto final Desarrollo de Software"""
#Autores: Jesús Villalobos Murillo, Jia Ming Liu
#Fecha: 2025
#Descripción: Boletas de Ordenes de Trabajo
#Version: 1.0
import os
from mod_menu import menu, crear_orden_trabajo, consultar_orden_trabajo, modificar_orden_trabajo, eliminar_orden_trabajo, generar_reporte_ordenes_dia, generar_reporte_ingresos_mes, generar_reporte_uso_impresoras
import mod_interfase as mi
import tkinter as tk
import cliente as cl 
import usuario as us
import utils as u
import maskpass as ma

# Definición de la función principal
if __name__ == "__main__":
    while True:
        u.limpiar_pantalla()
        usuario = input("Introduzca el usuario: ")
        password = ma.askpass(prompt="Introduzca la contraseña: ", mask="*")

        usuario_validado = us.validar_usuario(usuario, password)
        if usuario_validado:
            # Elige entre interfaz gráfica o menú de consola
            modo = input("Selecciona modo (1: Interfaz gráfica, 2: Consola): ")
            if modo == "1":
                mi.interfaz_ordenes_trabajo()
                
            elif modo == "2":
                menu_principal = True
                while menu_principal:
                    u.limpiar_pantalla()
                    # Mostrar el menú
                    opcion = menu()
                    
                    # Ejecutar la opción seleccionada
                    if opcion == "1":
                        crear_orden_trabajo()
                    elif opcion == "2":
                        consultar_orden_trabajo()
                    elif opcion == "3":
                        modificar_orden_trabajo()
                    elif opcion == "4":
                        eliminar_orden_trabajo()
                    elif opcion == "5":
                        generar_reporte_ordenes_dia()
                    elif opcion == "6":
                        generar_reporte_ingresos_mes()
                    elif opcion == "7":
                        generar_reporte_uso_impresoras()
                    elif opcion == "8":
                        cl.agregar_cliente()
                    elif opcion == "9":
                        cl.editar_cliente() 
                    elif opcion == "10":
                        cl.eliminar_cliente()
                    elif opcion == "11":
                        u.formatear_text("Cerrando sesión...\n")
                        menu_principal = False
                    else:
                        u.formatear_text("Opción no válida. Intente de nuevo.")
                # Al cerrar sesión, vuelve a solicitar usuario
                continue
            else:
                u.formatear_text("Modo no válido. Intente de nuevo.\n")
                continue
        else:
            u.formatear_text("Usuario o contrasena incorrecto\n")
            


