from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

fecha_actual = datetime.today()
fecha_actual = datetime.strftime(fecha_actual, "%d/%m/%Y").split("/")

actual_day = int(fecha_actual[0])
actual_month = int(fecha_actual[1])
actual_year = int(fecha_actual[2])

# Create Object
root = Tk()
# Set geometry
root.geometry("400x400")
# Add Calendar
calendar = Calendar(root, selectmode='day',
               year=actual_year, month=actual_month,
               day=actual_day)

calendar.pack(pady=20)


def grad_date():
    date.config(text="Selected Date is: " + calendar.get_date())
    selected_day = calendar.get_date()
    
    return selected_day
    

# Add Button and Label
Button(root, text="Get Date",
       command=grad_date).pack(pady=20)

date = Label(root, text="")
date.pack(pady=20)

# Execute Tkinter
root.mainloop()
