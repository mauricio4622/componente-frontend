class Producto:
    def __init__(self, id, nombre, precio, descripcion, cantidad, imagen):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.imagen = imagen

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class Carrito:
    def __init__(self, id, usuario_id, productos):
        self.id = id
        self.usuario_id = usuario_id
        self.productos = productos

    def __str__(self):
        return f"Carrito: {self.id}, Usuario: {self.usuario_id}, Productos: {[str(producto) for producto in self.productos]}"


class Pedido:
    def __init__(self, id, usuario_id, direccion, fecha, productos, total):
        self.id = id
        self.usuario_id = usuario_id
        self.direccion = direccion
        self.fecha = fecha
        self.productos = productos
        self.total = total

    def __str__(self):
        return f"Pedido: {self.id}, Usuario: {self.usuario_id}, Dirección: {self.direccion}, Fecha: {self.fecha}, Productos: {[str(producto) for producto in self.productos]}, Total: {self.total}"