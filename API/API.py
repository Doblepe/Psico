import sqlite3

def crear_conexion():
    try:
        conn = sqlite3.connect('./mydatabase.db')
        return conn
    except Exception as e:
        print(e)

def crear_tabla_x4(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Peques(id int(15) PRIMARY KEY, NOMBRE varchar(60), HORAS int(10), PRIVADO int(200), cita date(100)) '''
        )
        conn.commit()
        print('TAbla creada')
    except Exception as e:
        print(e)

# def insertar_registro_tabla_x2(conn):
#     cursor = conn.cursor()
#     cursor.execute("INSERT into alumnos (dni,nombre) values('xxx','paco')")
#     conn.commit()
# def actualizar_registro(conn):
#     cursor = conn.cursor()
#     cursor.execute('''
#     UPDATE alumnos SET dni = 'yyy',
#                         nombre = 'Lucia' 
#                     WHERE dni = 'xxx' ''')
# def mostrar_registro(conn):
#     try:
#         cursor = conn.cursor()
#         cursor.execute('SELECT * from alumnos')
#         rows = cursor.fetchall()
#         print(rows)
#     except: 
#         print('La tabla puede estar vacía')
# def eliminar_registro(conn):
#     cursor = conn.cursor()
#     cursor.execute('''DELETE FROM alumnos WHERE dni ='yyy' ''')
#     conn.commit()

conn = crear_conexion()
#crear_tabla_x2(conn)
crear_tabla_x4(conn)
# insertar_registro_tabla_x2(conn)
# mostrar_registro(conn)
# actualizar_registro(conn)
# mostrar_registro(conn)
# eliminar_registro(conn)
# mostrar_registro(conn)