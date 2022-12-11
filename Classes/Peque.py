import Progenitor
class Peque:
    def __init__(self,
    id=int,
    nombre=str,
    horas=int,
    privado=bool,
    progenitor=Progenitor,
    progenitor2= Progenitor,
   ) -> None:
        self.id = id
        self.nombre = nombre
        self.horas = horas
        self.privado = privado
        self.progenitor = Progenitor
        self.progenitor2 = Progenitor
def saludar():
    print('Hola')

# print('Peque')
# progenitor1 = Progenitor('papá', '6623923i408'),
# progenitor2 = Progenitor('Mamá', '798719123'),
# peque1 = Peque(1,'Juan Mari',3, 0, progenitor1, progenitor2)
# print(peque1)