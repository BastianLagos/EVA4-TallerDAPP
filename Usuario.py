class Usuario():
    __rut = ""
    __nombre = ""
    __apellido = ""
    __password = ""
    __email = ""
    __veri =""

    def __init__(self):
        pass

    def setRut(self,rut):
        self.__rut = rut

    def setNombre(self,nom):
        self.__nombre = nom

    def setApellido(self,ape):
        self.__apellido = ape
    
    def setPassword(self,pas):
        self.__password = pas

    def setEmail(self,ema):
        self.__email = ema
        
    def setVer(self,ver):
        self.__veri = ver

    def getRut(self):
        return self.__rut

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido
    
    def getPassword(self):
        return self.__password
    
    def getEmail(self):
        return self.__email
    
    def getVer(self):
        return self.__veri