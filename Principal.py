from mimetypes import init
from Funciones import Funciones

class Principal():
    
    f = Funciones()
    
    
    def __init__(self):
        pass

    def ejecutarPrograma(self):
        self.f.menuInicial()

p = Principal()
p.ejecutarPrograma()
