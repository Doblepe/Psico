from Classes.Peque import *
import tkinter as tk
from API.API import *
from API.BBDD import *
from datetime import datetime
from tkinter import *

# class Prueba:
#     def __init__(self, nombre, horas, privado, cita) -> None:
#        self.nombre = nombre
#        self.horas = horas
#        self.privado = privado
#        self.cita = cita


# fecha_actual = datetime.now()
# fecha_actual = datetime.strftime(fecha_actual, '%H:%M:%S --> %d/%B/%Y')

# progenitor1 = Progenitor_class('papá', '6623923i408'),
# progenitor2 = Progenitor_class('Mamá', '798719123'),

# prueba1 = Prueba('Juan', 3, 1, fecha_actual)

# progenitor1 = str(progenitor1)

# # peque1 = Peque_class(1, 'Juan Mari', 3, 0, progenitor1, progenitor2)
# con = None
# try:
#     #BBDD.peques.insert_one({"nombre": "Marcelo", "Privado": True, "Número de horas": 10, "Padre": progenitor1})
#     BBDD.agenda.insert_one({"fecha Actual" :fecha_actual}) 

# # {"Nombre padre": "Felipe", "Teléfono": "62910231089"}, {"Nombre Madre": "Felipona", "Teléfono": "1231289"}
#     print('Añadido')
# except Exception as e:
#     print(e)

# print('----------')
# for x in BBDD.peques.find().limit(5):
#   print(x)
# for x in BBDD.agenda.find().limit(5):
#   print(x)

# # print(peque1)



# ########### ----------- > Tkinter CODE

# root = tk.Tk()
# root.title('Agenda')

# root.resizable(0,0)
# root.geometry("1200x700")
# click = 0
# def funcion_click():
#   for x in BBDD.agenda.find().limit(5):
#     print(x)

# button = tk.Button(root, fg= 'White', bg = 'blue', text = 'show', width = 20, 
# height = 10, command = funcion_click )
# button.pack()
# root.mainloop()




