from Classes.Peque import *
import tkinter as tk


root = tk.Tk()
root.title('Agenda')

root.resizable(0,0)
root.geometry("1200x700")
click = 0
def funcion_click():
    global click
    click += 1
    print('Pulsado', click, "veces")

button = tk.Button(root, fg= 'White', bg = 'blue', text = 'Haga click', width = 20, 
height = 10, command = funcion_click )
button.pack()
root.mainloop()


progenitor1 = Progenitor_class('papá', '6623923i408'),
progenitor2 = Progenitor_class('Mamá', '798719123'),
peque1 = Peque_class(1,'Juan Mari',3, 0, progenitor1, progenitor2)
print(peque1)


