class Bodega():
    __id=0
    __nombod=""
    __dirbod=""
    
    def __init__(self):
        pass
    
    def setIdBod(self,id):
        self.__id=id
        
    def setNomBod(self,nombod):
        self.__nombod=nombod
        
    def setDirBod(self,dirbod):
        self.__dirbod=dirbod
        
    def getIdBod(self):
        return self.__id
    
    def getNomBod(self):
        return self.__nombod
    
    def getDirBod(self):
        return self.__dirbod