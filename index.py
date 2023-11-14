class Producto:
    def __init__(self, id, nombre, precio, descripcion, cantidad, imagen):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.imagen = imagen

        class Carrito:
    def __init__(self, id, usuario_id, productos):
        self.id = id
        self.usuario_id = usuario_id
        self.productos = productos

        class Pedido:
    def __init__(self, id, usuario_id, direccion, fecha, productos, total):
        self.id = id
        self.usuario_id = usuario_id
        self.direccion = direccion
        self.fecha = fecha
        self.productos = productos
        self.total = total

        from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///tienda.db')
metadata = MetaData()

productos = Table('productos', metadata,
    Column('id', Integer, primary_key=True),
    Column('nombre', String),
    Column('precio', Float),
    Column('descripcion