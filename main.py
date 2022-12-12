
from Classes.Progenitor import Progenitor_class
from Classes.Peque import Peque_class

progenitor1 = Progenitor_class('papá', '6623923i408'),
progenitor2 = Progenitor_class('Mamá', '798719123'),
peque1 = Peque_class(1,'Juan Mari',3, 0, progenitor1, progenitor2)
print(peque1)

Progenitor_class.saludar()
Peque_class.despedir()