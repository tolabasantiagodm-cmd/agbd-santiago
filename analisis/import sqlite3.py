#                                 SIN ORM

#import sqlite3
#
#conn = sqlite3.connect("mi_app.db")
#cursor = conn.cursor()
#cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios ( 
#id INTEGER PRIMARY KEY, 
#nombre TEXT, 
#email TEXT, 
#activo INTEGER ) """) 
#cursor.execute("INSERT INTO usuarios VALUES (1, 'Ana García', 'ana@mail.com', 1)") 
#conn.commit();
#
## Escribimos el SQL nosotros
#cursor.execute("""
#    SELECT id, nombre, email
#    FROM usuarios
#    WHERE activo = 1
#""")
#
#rows = cursor.fetchall()
#
## Convertimos filas a diccionarios a mano
#usuarios = [
#    {'id': row[0], 'nombre': row[1], 'email': row[2]}
#    for row in rows
#]
#
#conn.close()
#

#----------------------------------------------------------------------
#----------------------------------------------------------------------

#                                CON ORM

#from sqlalchemy import Column, Integer, String, Boolean, create_engine
#from sqlalchemy.orm import DeclarativeBase, Session
#
## 1. Definimos la clase (una sola vez)
#class Base(DeclarativeBase):
#    pass
#
#class Usuario(Base):
#    __tablename__ = "usuarios"
#
#    id      = Column(Integer, primary_key=True)
#    nombre  = Column(String)
#    email   = Column(String)
#    activo  = Column(Boolean)
#
## 2. Consultamos como si fueran objetos Python
#engine = create_engine("sqlite:///mi_app.db")
#
#with Session(engine) as session:
#    usuarios = session.query(Usuario) \
#                      .filter(Usuario.activo == True) \
#                      .all()
#
#    for u in usuarios:
#        print(u.nombre, u.email)  # ← atributos reales, no índices

from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Float)
    stock = Column(Integer)
    categoria = Column(String)

engine = create_engine("sqlite:///mi_app.db", echo = True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    productos = [
        Producto(nombre="Teclado", precio=350, stock=10, categoria="Periféricos"),
        Producto(nombre="Mouse", precio=250, stock=15, categoria="Periféricos"),
        Producto(nombre="Monitor", precio=750, stock=5, categoria="Pantallas"),
        Producto(nombre="Auriculares", precio=450, stock=8, categoria="Audio"),
        Producto(nombre="Webcam", precio=400, stock=12, categoria="Cámaras")
    ]

    session.add_all(productos)
    session.commit()

    productos = session.query(Producto).filter(Producto.precio < 500).all()

    for p in productos:
        print(p.nombre, p.precio, p.stock, p.categoria)

