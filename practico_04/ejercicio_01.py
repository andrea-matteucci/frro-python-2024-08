"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    db = sqlite3.connect('Personas.db')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Persona(IdPersona INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, fecNac DATE, DNI INTEGER, altura INTEGER)')
    db.commit()
    db.close()
    pass # Completar
    

def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    db = sqlite3.connect('Personas.db')
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS Persona')
    db.commit()
    db.close()
    pass # Completar
    

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
