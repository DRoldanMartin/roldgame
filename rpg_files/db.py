import mysql.connector
from rpg_files.msg import *


def connect_to_db():
        return mysql.connector.connect(
        host='localhost',
        user='',
        password='',
        database='roldgame',
    )
        
def insert_values_into_db(email,contrasena): 

    db = connect_to_db()

    cursorObject = db.cursor()
    mySql_insert_query = "INSERT INTO login (email, contrasena) VALUES (%s,%s)"
    record = (email, contrasena)
    cursorObject.execute(mySql_insert_query,record)
    db.commit()
    cursorObject.close()
    db.close()

def select_user(email,contrasena): 

    db = connect_to_db()
    
    cursorObject = db.cursor()
    mySql_select_query = "SELECT email FROM login WHERE email = %s AND contrasena = %s"
    record = (email, contrasena)
    cursorObject.execute(mySql_select_query,record)
    result = cursorObject.fetchall()

    if result:
        value = 1
        credenciales_correctas()
    
    else:
        value = 0
        credenciales_incorrectas()

    cursorObject.close()
    db.close()
    return value

def insert__equipo_into_db(email,nombre_equipo,clase_personaje_1,nombre_personaje_1,clase_personaje_2,nombre_personaje_2,clase_personaje_3,nombre_personaje_3,clase_personaje_4,nombre_personaje_4):

    db = connect_to_db()
    
    cursorObject = db.cursor()
    mySql_insert_query = "INSERT INTO equipos (email,nombre_equipo,clase_personaje_1,nombre_personaje_1,clase_personaje_2,nombre_personaje_2,clase_personaje_3,nombre_personaje_3,clase_personaje_4,nombre_personaje_4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    record = (email,nombre_equipo,clase_personaje_1,nombre_personaje_1,clase_personaje_2,nombre_personaje_2,clase_personaje_3,nombre_personaje_3,clase_personaje_4,nombre_personaje_4)
    cursorObject.execute(mySql_insert_query,record)
    db.commit()
    cursorObject.close()
    db.close()

def insert_personajes_into_db(nombre_equipo,nombre_personaje,clase_personaje,nivel,vida,resistencia,dano_condicion,fuerza,curacion,resistencia_condicion,experiencia,max_experiencia):

    db = connect_to_db()
    
    cursorObject = db.cursor()
    mySql_insert_query = "INSERT INTO personajes (nombre_equipo,nombre_personaje,clase_personaje,nivel,vida,resistencia,dano_condicion,fuerza,curacion,resistencia_condicion,experiencia,max_experiencia) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    record = (nombre_equipo,nombre_personaje,clase_personaje,nivel,vida,resistencia,dano_condicion,fuerza,curacion,resistencia_condicion,experiencia,max_experiencia)
    cursorObject.execute(mySql_insert_query,record)
    db.commit()
    cursorObject.close()
    db.close()

def insert_into_personaje(clase_personaje,nombre_personaje):

    db = connect_to_db()
    
    cursorObject = db.cursor()
    mySql_insert_query = "INSERT INTO personaje (id_clase,nombre_personaje) VALUES (%s,%s)"
    record = (clase_personaje,nombre_personaje)
    cursorObject.execute(mySql_insert_query,record)
    db.commit()
    cursorObject.close()
    db.close()

def listar_personajes_equipo(nombre_equipo):

    db = connect_to_db()

    cursorObject = db.cursor()
    mySql_select_query = """
        SELECT p.nombre_equipo, p.nombre_personaje, p.clase_personaje, p.nivel, p.vida, p.resistencia, p.dano_condicion, p.fuerza, p.curacion, p.resistencia_condicion, p.experiencia, p.max_experiencia
        FROM personajes p
        JOIN equipos e ON p.nombre_equipo = e.nombre_equipo
        WHERE p.nombre_equipo = %s
    """
    record = (nombre_equipo,)
    cursorObject.execute(mySql_select_query,record)
    result = cursorObject.fetchall()
    cursorObject.close()
    db.close()

    return result

def listar_personajes_totales():

    db = connect_to_db()

    cursorObject = db.cursor()
    mySql_select_query = """
        SELECT p.nombre_equipo, p.nombre_personaje, p.clase_personaje, p.nivel, p.vida, p.resistencia, p.dano_condicion, p.fuerza, p.curacion, p.resistencia_condicion, p.experiencia, p.max_experiencia
        FROM personajes p
        JOIN equipos e ON p.nombre_equipo = e.nombre_equipo
        ORDER BY p.nombre_equipo
    """

    cursorObject.execute(mySql_select_query)
    result = cursorObject.fetchall()
    cursorObject.close()
    db.close()

    return result

def listar_equipos(email):

    db = connect_to_db()

    cursorObject = db.cursor()
    mySql_select_query = """SELECT nombre_equipo FROM equipos WHERE email = %s"""

    record = (email,)
    cursorObject.execute(mySql_select_query, record)
    equipos = [e[0] for e in cursorObject.fetchall()]
    cursorObject.close()
    db.close()

    return equipos

def update_stats_in_db(nombre_equipo,clase_personaje,nombre_personaje,nivel,vida,resistencia,dano_condicion,fuerza,curacion,resistencia_condicion,experiencia,max_expericneica):

    db = connect_to_db()

    cursorObject = db.cursor()
    mySql_update_query = "UPDATE personajes SET nivel = %s, vida = %s, resistencia = %s, dano_condicion = %s, fuerza = %s, curacion = %s, resistencia_condicion = %s, experiencia = %s, max_experiencia = %s WHERE nombre_equipo = %s AND clase_personaje = %s AND nombre_personaje = %s"
    record = (nivel,vida,resistencia,dano_condicion,fuerza,curacion,resistencia_condicion,experiencia,max_expericneica,nombre_equipo,clase_personaje,nombre_personaje)
    cursorObject.execute(mySql_update_query, record)
    db.commit()
    cursorObject.close()
    db.close()

def insert_into_misiones(nombre_equipo,mision_name,valor_mision):

    db = connect_to_db()

    cursorObject = db.cursor()
    mySql_insert_query = "INSERT INTO misiones (nombre_equipo,mision,valor_mision) VALUES (%s,%s,%s)"
    record = (nombre_equipo,mision_name,valor_mision)
    cursorObject.execute(mySql_insert_query,record)
    db.commit()
    cursorObject.close()
    db.close()

def select_misiones(nombre_equipo):

    db = connect_to_db()

    cursorObject = db.cursor()
    mySql_select_query = "SELECT mision FROM misiones WHERE nombre_equipo = %s AND valor_mision = 1"
    record = (nombre_equipo,)
    cursorObject.execute(mySql_select_query, record)
    result = cursorObject.fetchall()
    cursorObject.close()
    db.close()

    return result

def update_misiones(nombre_equipo,mision_name,valor_mision):

    db = connect_to_db()

    cursorObject = db.cursor()
    mySql_insert_query = "UPDATE misiones SET valor_mision = %s WHERE nombre_equipo = %s AND mision = %s"
    record = (valor_mision,nombre_equipo,mision_name)
    cursorObject.execute(mySql_insert_query,record)
    db.commit()
    cursorObject.close()
    db.close()

def insert_weapon_into_db(nombre_personaje,nombre_arma,dano_base,prob_critico):

    db = connect_to_db()
    
    cursorObject = db.cursor()
    mySql_insert_query = "INSERT INTO armas (nombre_personaje,nombre_arma,dano_base,prob_critico) VALUES (%s,%s,%s,%s)"
    record = (nombre_personaje,nombre_arma,dano_base,prob_critico)
    cursorObject.execute(mySql_insert_query,record)
    db.commit()
    cursorObject.close()
    db.close()

def insert_items_into_db(nombre_equipo,tipo_item,nombre_item,cantidad_item):

    db = connect_to_db()

    cursorObject = db.cursor()
    mySql_insert_query = "INSERT INTO items (nombre_equipo,tipo_item,nombre_item,cantidad_item) VALUES (%s,%s,%s,%s)"
    record = (nombre_equipo,tipo_item,nombre_item,cantidad_item)
    cursorObject.execute(mySql_insert_query,record)
    db.commit()
    cursorObject.close()
    db.close()

def select_items_into_db(nombre_equipo):
    db = connect_to_db()
    cursorObject = db.cursor(dictionary=True)  # Utiliza el cursor en modo diccionario
    mySql_select_query = "SELECT nombre_item, tipo_item, cantidad_item FROM items WHERE nombre_equipo = %s"
    cursorObject.execute(mySql_select_query, (nombre_equipo,))
    items = cursorObject.fetchall()
    cursorObject.close()
    db.close()
    return items



def update_items(nombre_equipo,tipo_item,nombre_item,cantidad_item):

    db = connect_to_db()

    cursorObject = db.cursor()
    mySql_insert_query = "UPDATE items SET cantidad_item = %s WHERE nombre_equipo = %s AND tipo_item = %s AND nombre_item = %s"
    record = (cantidad_item,nombre_equipo,tipo_item,nombre_item)
    cursorObject.execute(mySql_insert_query,record)
    db.commit()
    cursorObject.close()
    db.close()