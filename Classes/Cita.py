from Peque import Peque_class
from Progenitor import Progenitor_class
from datetime import datetime

class Cita:
    def __init__(self, peque = Peque_class, responsable = Progenitor_class) -> None:
        self.peque = peque
        self.responsable = responsable
        self.fecha_actual = datetime.now()
        

fecha_actual = datetime.now()
fecha_actual = datetime.strftime(fecha_actual, '%H:%M:%S --> %d/%B/%Y')
print(fecha_actual)
