from Classes.Progenitor import Progenitor_class
from API.API import *
class Peque_class:
    try:
        def __init__(self,
        id=int,
        nombre=str,
        horas=int,
        privado=bool,
        progenitor=Progenitor_class,
        progenitor2= Progenitor_class,
    ) -> None:
            self.id = id
            self.nombre = nombre
            self.horas = horas
            self.privado = privado
            self.progenitor = Progenitor_class
            self.progenitor2 = Progenitor_class
    except Exception as e:
        print(e)
    
    def get_peque(self):
        return self.nombre
    def set_peque(self):
        pass

    def crear_niño():
        pass
    def eliminar_niño():
        pass
    
# print('Peque')
# progenitor1 = Progenitor('papá', '6623923i408'),
# progenitor2 = Progenitor('Mamá', '798719123'),
# peque1 = Peque(1,'Juan Mari',3, 0, progenitor1, progenitor2)
# print(peque1)