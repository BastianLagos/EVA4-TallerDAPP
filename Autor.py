class Autor():
    __idaut= 0
    __nomaut = ""
    __apeaut = ""

    def __init__(self):
        pass

    def setIdAut(self,id):
        self.__idaut = id

    def setNomAut(self,nomaut):
        self.__nomaut = nomaut

    def setApeAut(self,apeaut):
        self.__apeaut = apeaut
    
    def getIdAut(self):
        return self.__idaut

    def getNomAut(self):
        return self.__nomaut
    
    def getApeAut(self):
        return self.__apeaut