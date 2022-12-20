import tkinter as tk
# ----------- > Tkinter CODE

# root = tk.Tk()
# root.title('Agenda')
ventana = tk.Tk()
ventana.title("Checkbutton y label")
ventana.resizable(0,0)
ventana.geometry("800x300")


def funcion_opcion():
    print("Variable1:", v1.get(), "- Varuiable2: ", v2.get(), "-Variable3:", v3.get())

tk.Label(ventana, text="Elija la opción que desee")

v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()

tk.Checkbutton(ventana, text= 'Opcion1', variable=v1).grid(row=0, column=0)
tk.Checkbutton(ventana, text='Opcion2', variable=v2).grid(row=0, column=1)
tk.Checkbutton(ventana, text='Opcion3', variable=v3).grid(row=0, column=2)

tk.Button(ventana, text="Mostrar opciones elegidas", fg="white", command= funcion_opcion).grid(row=0, column=3)

ventana.mainloop()
# root.resizable(0,0)
# root.geometry("1200x700")
# click = 0
# def funcion_click():
#     global click
#     click = click +1 
#     print(click)

# button = tk.Button(root, fg= 'White', bg = 'blue', text = 'show', width = 20,
# height = 10, command = funcion_click )
# button.pack()
# root.mainloop()
