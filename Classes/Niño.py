import Progenitor
class Niño:
    def __init__(self, 
    id=int, 
    nombre=str,
    horas=int,
    privado=bool,
    progenitor=Progenitor, 
    progenitor2= Progenitor,
    informes = [{}] ) -> None:
        self.id = id
        self.nombre = nombre
        self.horas = horas
        self.privado = privado
        self.progenitor = Progenitor
        self.progenitor2 = Progenitor
        self.informes = None