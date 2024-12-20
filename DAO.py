from os import system
import pymysql
from Libro import Libro
from Usuario import Usuario

class DAO():
    
    def __init__(self):
        pass
    
    
#--------------------------------------------------------------------
    
    def conectar(self):
        self.con = pymysql.connect(
            host = "localhost", 
            user = "root",
            password = "",
            db = "eva4"
        )

        self.cursor = self.con.cursor()
        
#--------------------------------------------------------------------
        
        
    def desconectar(self):
        self.cursor = self.cursor.close()
        
#--------------------------------------------------------------------

    def iniciarSesion(self, rut, pas):
        try:
            self.conectar()
            sql = "select * from usuarios where rut_usu=%s and pas_usu=%s"
            val = (rut, pas)
            self.cursor.execute(sql, val)
            rs = self.cursor.fetchone()
            self.desconectar()   
            return rs 
        except:
            print("\n--- Error Al Obtener Usuario (LOGIN)!! d---")
            system("pause")
            
# ---------------------------------------------------------------------

    def comprobarNombreBod(self, nom):
        try:            
            self.conectar()
            sql = "select nom_bod from bodegas where nom_bod=%s"
            self.cursor.execute(sql, nom)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar Nombre de Bodega (DAO)!! ---")
            system("pause")
            
# ---------------------------------------------------------------------

    def agregarBod(self, b):
        try:
            nom = b.getNomBod()
            dir = b.getDirBod()
            self.conectar()
            sql = "insert into bodegas (nom_bod, dir_bod) values (%s, %s)"
            val = (nom, dir)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al agregarBodega (DAO)!! ---")
            system("pause")
# ---------------------------------------------------------------------

    def comprobarNombreAut(self, nom):
        try:            
            self.conectar()
            sql = "select nom_aut from autor where nom_aut=%s"
            self.cursor.execute(sql, nom)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al comprobarNombreaut (DAO)!! ---")
            system("pause")
            
    # ---------------------------------------------------------------------

    def agregarAutor(self, a):
        try:
            nom = a.getNomAut()
            ape = a.getApeAut()
            self.conectar()
            sql = "insert into autor (nom_aut, ape_aut) values (%s, %s)"
            val = (nom, ape)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al agregarAutor (DAO)!! ---")
            system("pause")
            
# ---------------------------------------------------------------------

    def comprobarNombreEdi(self, nom):
        try:            
            self.conectar()
            sql = "select nom_edi from editorial where nom_edi=%s"
            self.cursor.execute(sql, nom)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al comprobarNombreedi (DAO)!! ---")
            system("pause")
            
    # ---------------------------------------------------------------------

    def agregarEdi(self, nom):
        try:
            self.conectar()
            sql = "insert into editorial (nom_edi) values (%s)"
            self.cursor.execute(sql, nom)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al agregarEdi (DAO)!! ---")
            system("pause")
            
# ---------------------------------------------------------------------

    def obtenerAutor(self):
        try:
            self.conectar()
            sql = "select id_aut, nom_aut, ape_aut from autor"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()   
            return rs 
        except:
            print("\n--- Error Al Obtener autor (DAO)!! ---")
            system("pause")
            
# ---------------------------------------------------------------------

    def obtenerEdi(self):
        try:
            self.conectar()
            sql = "select id_edi, nom_edi from editorial"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()   
            return rs 
        except:
            print("\n--- Error Al Obtener Editorial (DAO)!! ---")
            system("pause")
            
# ---------------------------------------------------------------------

    def comprobarFKEdi(self, idEdi):
        try:
            self.conectar()
            sql = "select * from editorial where id_edi=%s"
            self.cursor.execute(sql, idEdi)
            rs = self.cursor.fetchone()
            if rs is None:
                self.desconectar()
                return False
            self.desconectar()   
            return True 
        except:
            print("\n--- Error Al Obtener Editorial (DAO)!! ---")
            system("pause")
            
    # ---------------------------------------------------------------------

    def comprobarFKAut(self, idAut):
        try:
            self.conectar()
            sql = "select * from autor where id_aut=%s"
            self.cursor.execute(sql, idAut)
            rs = self.cursor.fetchone()
            if rs is None:
                self.desconectar()
                return False
            self.desconectar()   
            return True 
        except:
            print("\n--- Error Al Obtener autorr (DAO)!! ---")
            system("pause")
            
    # ---------------------------------------------------------------------

    def agregarLib(self, l):
        try:
            idaut = l.getIdAutor()
            idedi = l.getIdEditorial()
            nom = l.getNomLib()
            self.conectar()
            sql = "insert into libro (id_aut, id_edi, nom_lib) values (%s, %s, %s)"
            val = (idaut, idedi, nom)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al agregarLibro (DAO)!! ---")
            system("pause")

#------------------------------------------------------------------------------------

    def agregarNub(self, n):
        try:
            idlib = n.getIdLib()
            idbod = n.getIdBod()
            self.conectar()
            sql = "insert into nub1 (id_lib, id_bod) values (%s, %s)"
            val = (idlib, idbod)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Añadir Libro en Bodega (DAO)!! ---")
            system("pause")


#-------------------------------------------------------------------------------------

    def obtenerInve(self):
        try:
            self.conectar()
            sql = "select nom_bod , nom_lib from nub1 inner JOIN bodegas on nub1.id_bod=bodegas.id_bod inner JOIN libro on nub1.id_lib=libro.id_lib group by nom_bod, nom_lib;"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()   
            return rs 
        except:
            print("\n--- Error Al Obtener Inventario (DAO)!! ---")
            system("pause")
            
# ---------------------------------------------------------------------

    def obtenerBod(self):
        try:
            self.conectar()
            sql = "select id_bod, nom_bod, dir_bod from bodegas"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()   
            return rs 
        except:
            print("\n--- Error Al Obtener Bodegas (DAO)!! ---")
            system("pause")

#-----------------------------------------------------------------------------

    def comprobarFKBod(self, idBod):
        try:
            self.conectar()
            sql = "select * from bodegas where id_bod=%s"
            self.cursor.execute(sql, idBod)
            rs = self.cursor.fetchone()
            if rs is None:
                self.desconectar()
                return False
            self.desconectar()   
            return True 
        except:
            print("\n--- Error Al Obtener Bodegas (DAO)!! ---")
            system("pause")

#---------------------------------------------------------------------------

    def comprobarLibro(self, idLib):
        try:
            self.conectar()
            sql = "select * from libro where id_lib=%s"
            self.cursor.execute(sql, idLib)
            rs = self.cursor.fetchone()
            if rs is None:
                self.desconectar()
                return False
            self.desconectar()   
            return True 
        except:
            print("\n--- Error Al Obtener Libro (DAO)!! ---")
            system("pause")

#---------------------------------------------------------------------------------------

    def obtenerLib(self):
        try:
            self.conectar()
            sql = "select id_lib, nom_aut, nom_edi, nom_lib from libro inner JOIN autor on libro.id_aut=autor.id_aut  inner JOIN editorial on libro.id_edi=editorial.id_edi group by id_lib;"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()   
            return rs 
        except:
            print("\n--- Error Al Obtener Libro (DAO)!! ---")
            system("pause")

#--------------------------------------------------------------------------------------------

    def moverLib(self, n):
        try:
            idbod = n.getIdBod()
            idlib = n.getIdLib()
            self.conectar()
            sql = "update nub1 set id_bod=%s where id_lib=%s"
            val = (idbod, idlib)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Mover Texto (DAO)!! ---")
            system("pause")

#---------------------------------------------------------------------------------------

    def obtenerNub(self):
        try:
            self.conectar()
            sql = "select nub1.id_bod, bodegas.nom_bod, nub1.id_lib, libro.nom_lib from nub1 inner JOIN bodegas on bodegas.id_bod=nub1.id_bod  inner JOIN libro on libro.id_lib=nub1.id_lib group by nom_bod, nom_lib"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()   
            return rs 
        except:
            print("\n--- Error Al Obtener Nub (DAO)!! ---")
            system("pause")

#---------------------------------------------------------------------------

    def comprobarNubLib(self, idLib):
        try:
            self.conectar()
            sql = "select * from nub1 where id_lib=%s"
            self.cursor.execute(sql, idLib)
            rs = self.cursor.fetchone()
            if rs is None:
                self.desconectar()
                return False
            self.desconectar()   
            return True 
        except:
            print("\n--- Error Al Obtener Id Libro de Nub (DAO)!! ---")
            system("pause")

#---------------------------------------------------------------------------

    def comprobarNubBod(self, idBod):
        try:
            self.conectar()
            sql = "select * from nub1 where id_bod=%s"
            self.cursor.execute(sql, idBod)
            rs = self.cursor.fetchone()
            if rs is None:
                self.desconectar()
                return False
            self.desconectar()   
            return True 
        except:
            print("\n--- Error Al Obtener Id Bodegas de Nub (DAO)!! ---")
            system("pause")