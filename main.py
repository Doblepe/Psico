from Classes.Peque import *
import tkinter as tk
from API.API import *
import _sqlite3
from datetime import datetime
class Prueba:
    def __init__(self, nombre, horas, privado, cita, Progenitor1, Progenitor2) -> None:
       self.nombre = nombre
       self.horas = horas
       self.privado = privado
       self.cita = cita
       self.progenitor1 = Progenitor1
       self.progenitor2 = Progenitor2


fecha_actual = datetime.now()
fecha_actual = datetime.strftime(fecha_actual, '%H:%M:%S --> %d/%B/%Y')

progenitor1 = Progenitor_class('papá', '6623923i408'),
progenitor2 = Progenitor_class('Mamá', '798719123'),

prueba1 = Prueba('Juan', 3, 1, fecha_actual, progenitor1, progenitor2)


# peque1 = Peque_class(1, 'Juan Mari', 3, 0, progenitor1, progenitor2)
con = None
try:
    con = sqlite3.connect('mydatabase.db')
    dbconn.crear_tabla(con)
    dbconn.insertar_registro(con, prueba1)

except Exception as e:
    print(e)


# print(peque1)












########### ----------- > Tkinter CODE

# root = tk.Tk()
# root.title('Agenda')

# root.resizable(0,0)
# root.geometry("1200x700")
# click = 0
# def funcion_click():
#     global click
#     click += 1
#     print('Pulsado', click, "veces")

# button = tk.Button(root, fg= 'White', bg = 'blue', text = 'Haga click', width = 20, 
# height = 10, command = funcion_click )
# button.pack()
# root.mainloop()




