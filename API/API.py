import sqlite3
class dbconn:
    # def crear_conexion():
    #     try:
    #         conn = sqlite3.connect('./mydatabase.db')
    #         return conn
    #     except Exception as e:
    #         print(e)

    def crear_tabla(conn):
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS Peques( NOMBRE varchar(60) 
                PRIMARY KEY, 
                HORAS int(10), 
                PRIVADO int(200), 
                cita date(100), 
                Progenitor1 VARCHAR(255), 
                Progenitor2 VARCHAR(255)) '''
            )
            conn.commit()
            print('TAbla creada')
        except Exception as e:
            print(e)

    def insertar_registro(conn, Peque):
        try:
            cursor = conn.cursor()
            sql = '''INSERT into Peques (NOMBRE,HORAS,PRIVADO,CITA, Progenitor1, Progenitor2)
                    values(?,?,?,?,?,?)
            '''
            parametro = (Peque.nombre, Peque.horas, Peque.privado, Peque.cita, Peque.Progenitor1, Peque.Progenitor2)
            cursor.execute(sql, parametro)
            conn.commit()
            print('Registro insertado')
        except Exception as e:
            print(e)
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



#insertar_registro(conn)

# insertar_registro_tabla_x2(conn)
# mostrar_registro(conn)
# actualizar_registro(conn)
# mostrar_registro(conn)
# eliminar_registro(conn)
# mostrar_registro(conn)