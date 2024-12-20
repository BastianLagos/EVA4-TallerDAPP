class Libro():
    __id = 0
    __idautor = 0
    __ideditorial = 0
    __nomlibro = ""

    def __init__(self):
        pass

    def setIdLib(self,id):
        self.__id = id

    def setIdAutor(self,idaut):
        self.__idautor = idaut

    def setIdEditorial(self,idedi):
        self.__ideditorial = idedi

    def setNomLib(self,nomlib):
        self.__nomlibro = nomlib
    
    def getIdLib(self):
        return self.__id

    def getIdAutor(self):
        return self.__idautor

    def getIdEditorial(self):
        return self.__ideditorial
    
    def getNomLib(self):
        return self.__nomlibro