"""Base de Datos SQL - Modificación"""

import datetime
import sqlite3
from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    """Implementar la funcion actualizar_persona, que actualiza un registro de
    una persona basado en su id. Devuelve un booleano en base a si encontro el
    registro y lo actualizo o no."""
    # Completar
    db = sqlite3.connect('Personas.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Persona WHERE IdPersona = "%s"' % (id_persona))
    persona = cursor.fetchone()
    if persona:
        cursor.execute('UPDATE persona SET nombre="%s", fecNac="%s", DNI="%s", altura="%s" WHERE IdPersona=%s' % (id_persona, nombre, nacimiento, dni, altura))
        db.commit()
        db.close()
        return True
    else: return False

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
