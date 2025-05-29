class Orden:
    def __init__(self, id_orden, cliente, fecha, fecha_entrega, descripcion, medidas, 
                    cantidad, diseñador, impresora, observaciones, precio):
        self.id_orden = id_orden
        self.cliente = cliente
        self.fecha = fecha
        self.fecha_entrega = fecha_entrega
        self.descripcion = descripcion
        self.medidas = medidas
        self.cantidad = cantidad
        self.diseñador = diseñador
        self.impresora = impresora
        self.observaciones = observaciones
        self.precio = precio
        self.estado = "pendiente"

        