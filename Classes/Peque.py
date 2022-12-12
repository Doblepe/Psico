from Progenitor import Progenitor_class
class Peque_class:
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

    def despedir():
        print('Adios')

        
Progenitor_class.saludar()
# print('Peque')
# progenitor1 = Progenitor('papá', '6623923i408'),
# progenitor2 = Progenitor('Mamá', '798719123'),
# peque1 = Peque(1,'Juan Mari',3, 0, progenitor1, progenitor2)
# print(peque1)