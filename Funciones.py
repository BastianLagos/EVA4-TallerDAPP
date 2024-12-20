import os
from Autor import Autor
from Bodega import Bodega
from Editorial import Editorial
from Usuario import Usuario
from Libro import Libro
from Nub1 import Nub1
from DAO import DAO
from os import system
from beautifultable import BeautifulTable
import getpass



class Funciones():
    d = DAO()
    sesion=Usuario()

    def __init__(self):
        pass
    
    
    def menuInicial(self):
        while True:
            try:
                print("//---POLITICA DE TÉRMINOS Y CONDICIONES---//")
                print("Estos términos y condiciones describen las reglas y regulaciones para el uso de la aplicación Librería Virtual. Al acceder a la aplicación, asumimos que aceptas estos términos y condiciones en su totalidad. No continúes usando la aplicación, si no aceptas todos los términos y condiciones establecidos. La siguiente terminología se aplica a estos Términos y Condiciones, Declaración de Privacidad y Aviso legal y cualquiera o todos los Acuerdos: el Cliente, Usted y Su se refieren a usted, la persona que accede a esta aplicación y acepta los términos y condiciones de la Compañía. La Compañía, Nosotros mismos, Nosotros y Nuestro, se refiere a nuestra Compañía. Parte, Partes o Nosotros, se refiere en conjunto al Cliente y a nosotros mismos, o al Cliente o a nosotros mismos. Todos los términos se refieren a la oferta, aceptación y consideración del pago necesario para efectuar el proceso de nuestra asistencia al Cliente de la manera más adecuada, ya sea mediante reuniones formales de una duración fija, o por cualquier otro medio, con el propósito expreso de conocer las necesidades del Cliente con respecto a la provisión de los servicios/productos declarados de la Compañía, de acuerdo con y sujeto a la ley vigente. Cualquier uso de la terminología anterior u otras palabras en singular, plural, mayúsculas y/o, él/ella o ellos, se consideran intercambiables y, por lo tanto, se refieren a lo mismo.")
                print("//---LICENCIA---//")
                print("A menos que se indique lo contrario, (Nombre de la aplicación) y/o sus licenciatarios les pertenecen los derechos de propiedad intelectual de todo el material en (Nombre de la aplicación).Todos los derechos de propiedad intelectual están reservados.No debes:•	Vender, alquilar u otorgar una sub-licencia de cuentas de usuarios.•	Reproducir, duplicar o copiar material.•	Redistribuir contenido de Librería Virtual, a menos de que el contenido se haga específicamente para la redistribución.")
                print("//---AVISO LEGAL---//")
                print("En la medida máxima permitida por la ley aplicable, excluimos todas las representaciones, garantías y condiciones relacionadas con nuestra aplicación (incluyendo, sin limitación, cualquier garantía implícita por la ley con respecto a la calidad satisfactoria, idoneidad para el propósito y/o el uso de cuidado y habilidad razonables).Nada en este aviso legal:•	Limita o excluye nuestra o su responsabilidad por muerte o lesiones personales resultantes de negligencia.•	Limita o excluye nuestra o su responsabilidad por fraude o tergiversación fraudulenta.•	Limita cualquiera de nuestras o sus responsabilidades de cualquier manera que no esté permitida por la ley aplicable.•	Excluye cualquiera de nuestras o sus responsabilidades que no pueden ser excluidas bajo la ley aplicable.Las limitaciones y exclusiones de responsabilidad establecidas en esta Sección y en otras partes de este aviso legal:•	están sujetas al párrafo anterior; y•	rigen todas las responsabilidades que surjan bajo la exención de responsabilidad o en relación con el objeto de esta exención de responsabilidad, incluidas las responsabilidades que surjan en contrato, agravio (incluyendo negligencia) y por incumplimiento del deber legal.En la medida en que la aplicación y la información y los servicios de la aplicación se proporcionen de forma gratuita, no seremos responsables de ninguna pérdida o daño de ningún tipo.")
                print("///////////SI ACEPTA PORFAVOR TOCAR CUALQUIER LETRA///////////")
                system("pause")
                system("cls")
                print("--- MENU INICIAL ---")
                print("1.Iniciar Sesion")
                print("2.Salir")
                op = int(input("Digite Una Opcion : "))
                if op==1:
                    self.__login()
                elif op==2:
                    print("\n--- OK. ADIOS!! ---")
                    system("pause")
                    os._exit(1)
                else:
                    print("\n--- Error De Opcion De Menu!! ---")
                    system("pause")
            except:
                print("\n--- Error De Opcion Try!! 1---")
                system("pause")
                
#--------------------------------------------------------------------

    def menuAdmin(self):
        while True:
            try:
                system("cls")
                print("--- MENU DE JEFE DE BODEGA ---")
                print("1.Crear bodega")
                print("2.Registrar Libro")
                print("3.Registrar Autor") 
                print("4.Registrar Editorial")
                print("5.Ver inventario")
                print("6.Cerrar Sesion")
                op = int(input("Digite Una Opcion : "))
                if op==1:
                    self.__crearBodega()
                elif op==2:
                    self.__RegisLib()
                elif op==3:
                    self.__RegisAutor()
                elif op==4:
                    self.__RegisEdi()
                elif op==5:
                    self.__verInve()
                elif op==6:
                    self.menuInicial()
                else:
                    print("\n--- Error De Opcion De Menu!! ---")
                    system("pause")
            except:
                print("\n--- Error De Opcion Try!! 2---")
                system("pause")

#--------------------------------------------------------------------
                
    def menuUsuarios(self):
        while True:
            try:
                system("cls")
                print("--- MENU DE BODEGUERO ---")
                print("1.Mover Libro")
                print("2.Cerrar Sesion")
                op = int(input("Digite Una Opcion : "))
                if op==1:
                    self.__moverLibro()
                elif op==2:
                    self.menuInicial()
                else:
                    print("\n--- Error De Opcion De Menu Usuario!! ---")
                    system("pause")
            except:
                print("\n--- Error De Opcion Try!! 3---")
                system("pause")
                
#--------------------------------------------------------------------
                
    def __login(self):
        while True:
            try:
                system("cls")               
                print("--- LOGIN ---")
                rut = input("Digite El rut de Usuario : ")
                if len(rut)>12 or len(rut)<12:
                    print("\n--- EL RUT debe Tener 12 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar el rut De Usuario (LOGIN)!! ---")
                system("pause")

        while True:
            try:
                system("cls")               
                print("--- LOGIN ---")
                pas = getpass.getpass("Digite La Contraseña Del Usuario ("+rut.upper()+") : ")
                if len(pas)<1 or len(pas)>50:
                    print("\n--- La contraseña ebe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Ingresar Contraseña (LOGIN)!! ---")
                system("pause")
    
        system("cls")
        r = self.d.iniciarSesion(rut, pas)
        if r is None:
            print("\n--- Error De Usuario y/o Contraseña!! ---\n")
            system("pause")
        else:
            self.sesion.setRut(r[1])
            self.sesion.setNombre(r[2])
            self.sesion.setPassword(r[4])
            self.sesion.setVer(r[6])
            if self.sesion.getVer() == 1:
                print("\n--- Bienvenido Jefe de Bodega!! ---\n")
                system("pause")
                self.menuAdmin()
            else:
                print("\n--- Bienvenido Bodeguero!! ---\n")
                system("pause")
                self.menuUsuarios()
                
#--------------------------------------------------------------------

    def __crearBodega(self):
        while True:
            try:
                system("cls")
                print("--- CREAR BODEGA ---")
                nom = input("Digite El Nombre De Bodega a Registrar : ")
                if len(nom.strip())<1 or len(nom.strip())>20:
                    print("\n--- Debe Tener Entre 1 y 20 Caracteres!! ---")
                    system("pause")
                else:
                    r = self.d.comprobarNombreBod(nom)
                    if r is None:
                        break
                    else:
                        print("\n--- Nombre De Bodega Ya Existe!! ---")
                        system("pause")
            except:
                print("\n--- Error Al Intentar Almacenar El Nombre!! ---")
                system("pause")


        ####
        while True:
            try:
                system("cls")
                print("--- CREAR BODEGA ---")
                dir = input("Digite la DIRECCION de la Bodega a Registrar : ")
                if len(dir.strip())<1 or len(dir.strip())>100:
                    print("\n--- Debe Tener Entre 1 y 100 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Intentar Almacenar La Direccion!! ---")
                system("pause")

        ####
        b = Bodega()
        b.setNomBod(nom)
        b.setDirBod(dir)

        self.d.agregarBod(b)

        system("cls")
        print("--------------------------------------")
        print("--- Bodega Creado Correctamente!! ---")
        print("--------------------------------------")
        system("pause")
        self.menuAdmin()


# ---------------------------------------------------------------------

    def __RegisLib(self):
        while True:
            try:
                r = self.d.obtenerAutor()
                tabla = BeautifulTable()
                for x in r:
                    tabla.rows.append([  x[0], x[1], x[2]  ])
                tabla.column_headers = ["ID", "NOMBRE", "APELLIDO"]
                system("cls")
                print(tabla)

                idAut = int(input("Digite El ID Del autor: "))
                
                r = self.d.comprobarFKAut(idAut)
                if r == False:
                    print("\n--- Error De Opcion De Autor!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar ID autor (try)!! ---")
                system("pause")

        ####

        while True:
            try:
                r = self.d.obtenerEdi()
                tabla = BeautifulTable()
                for x in r:
                    tabla.rows.append([  x[0], x[1] ])
                tabla.column_headers = ["ID", "NOMBRE"]
                system("cls")
                print(tabla)

                idEdi = int(input("Digite El ID Del Editorial: "))
                
                r = self.d.comprobarFKEdi(idEdi)
                if r == False:
                    print("\n--- Error De Opcion De Editorial!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar ID Editorial (try)!! ---")
                system("pause")


        ##
        while True:
            try:
                system("cls")
                print("Registrar LIBRO")
                nom = input("Digite El NOMBRE Del LIBRO : ")
                if len(nom.strip())<1 or len(nom.strip())>30:
                    print("\n--- El Nombre Debe Tener Entre 1 y 30 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar Nombre de Libro (try)!! ---")
                system("pause")

        #####
        l = Libro()
        l.setNomLib(nom)
        l.setIdAutor(idAut)
        l.setIdEditorial(idEdi)


        self.d.agregarLib(l)

        system("cls")
        print("\n-------------------------------------------")
        print("--- Libro Agregado Correctamente!! ---")
        print("-------------------------------------------")
        system("pause")
        self.__RegisLenB()
        self.menuAdmin()
        
 
# ---------------------------------------------------------------------

    def __RegisAutor(self):
        while True:
            try:
                system("cls")
                print("--- REGISTRAR NOMBRE DEL AUTOR ---")
                nomaut = input("Digite El Nombre del AUTOR del Libro a Registrar : ")
                if len(nomaut.strip())<1 or len(nomaut.strip())>30:
                    print("\n--- Debe Tener Entre 1 y 30 Caracteres!! ---")
                    system("pause")
                else:
                    r = self.d.comprobarNombreAut(nomaut)
                    if r is None:
                        break
                    else:
                        print("\n--- Nombre De AUTOR Ya Existe!! ---")
                        system("pause")
            except:
                print("\n--- Error Al Intentar Registrar El Nombre!! ---")
                system("pause")
                
        while True:
            try:
                system("cls")
                print("--- REGISTRAR APELLIDO DEL AUTOR ---")
                apeaut = input("Digite El Apellido del AUTOR del Libro a Registrar : ")
                if len(apeaut.strip())<1 or len(apeaut.strip())>30:
                    print("\n--- Debe Tener Entre 1 y 30 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Intentar REgistrar El Apellido!! ---")
                system("pause")
                
        a=Autor()
        a.setNomAut(nomaut)
        a.setApeAut(apeaut)
        self.d.agregarAutor(a)
        
        system("cls")
        print("--------------------------------------")
        print("--- Autor registrado Correctamente!! ---")
        print("--------------------------------------")
        system("pause")
        self.menuAdmin()
        
# ---------------------------------------------------------------------

    def __RegisEdi(self):
        while True:
            try:
                system("cls")
                print("--- REGISTRAR EDITORIAL ---")
                nom = input("Digite El Nombre de la EDITORIAL : ")
                if len(nom.strip())<1 or len(nom.strip())>30:
                    print("\n--- Debe Tener Entre 1 y 30 Caracteres!! ---")
                    system("pause")
                else:
                    r = self.d.comprobarNombreEdi(nom)
                    if r is None:
                        break
                    else:
                        print("\n--- Nombre De EDITORIAL Ya Existe!! ---")
                        system("pause")
            except:
                print("\n--- Error Al Intentar Almacenar El Nombre!! ---")
                system("pause")
                
        e=Editorial()
        self.d.agregarEdi(nom)
        
        system("cls")
        print("--------------------------------------")
        print("--- Editorial registrado Correctamente!! ---")
        print("--------------------------------------")
        system("pause")
        self.menuAdmin()
        
# ---------------------------------------------------------------------

    def __verInve(self):
        r = self.d.obtenerInve()
        if len(r)==0:
            system("cls")
            print("--------------------------------------")
            print("--- No Hay Registros Para Listar!! ---")
            print("--------------------------------------")
            system("pause")
            self.menuAdmin()
        else:
            tabla = BeautifulTable()
            for x in r:
                tabla.rows.append([  x[0], x[1] ])
            tabla.column_headers = ["BODEGA", "LIBRO"]
            system("cls")
            print("--- LISTADO DE BODEGAS ---")
            print(tabla)
            system("pause")
            self.menuAdmin()

#--------------------------------------------------------------------------------------

    def __RegisLenB(self):
        while True:
            try:
                r = self.d.obtenerLib()
                tabla = BeautifulTable()
                for x in r:
                    tabla.rows.append([  x[0], x[1], x[2], x[3]  ])
                tabla.column_headers = ["ID", "AUTOR", "EDITORIAL", "NOMBRE"]
                system("cls")
                print("--- AÑADA EL LIBRO A UNA BODEGA ---")
                print("------------ LIBROS ---------------")
                print(tabla)

                idLib = int(input("Digite El ID Del Libro: "))
                
                r = self.d.comprobarLibro(idLib)
                if r == False:
                    print("\n--- Error De Opcion De Id!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar ID Libro (try)!! ---")
                system("pause")

        while True:
            try:
                r = self.d.obtenerBod()
                tabla = BeautifulTable()
                for x in r:
                    tabla.rows.append([  x[0], x[1], x[2]  ])
                tabla.column_headers = ["ID", "NOMBRE", "DIRECCION"]
                system("cls")
                print("------ BODEGAS ------")
                print(tabla)

                idBod = int(input("Digite El ID De la Bodega: "))
                
                r = self.d.comprobarFKBod(idBod)
                if r == False:
                    print("\n--- Error De Opcion De Id!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar ID Bodega (try)!! ---")
                system("pause")

        n = Nub1()
        
        n.setIdLib(idLib)
        n.setIdBod(idBod)
        self.d.agregarNub(n)
        
        system("cls")
        print("------------------------------------------------------")
        print("--- El Libro se ha Añadido a la Bodega con Éxito!! ---")
        print("------------------------------------------------------")
        system("pause")
        self.menuAdmin()

#-------------------------------------------------------------------------------------------

    def __moverLibro(self):
        while True:
            try:
                r = self.d.obtenerNub()
                tabla = BeautifulTable()
                for x in r:
                    tabla.rows.append([  x[0], x[1], x[2], x[3]  ])
                tabla.column_headers = ["ID BODEGA", "NOMBRE BODEGA", "ID LIBRO", "NOMBRE LIBRO"]
                system("cls")
                print("------ INVENTARIO ------")
                print(tabla)

                idLib = int(input("Digite El ID Del Libro a Mover: "))
                
                r = self.d.comprobarNubLib(idLib)
                if r == False:
                    print("\n--- Error De Opcion De Nub Id!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar Nub ID Libro (try)!! ---")
                system("pause")

        while True:
            try:
                r = self.d.obtenerNub()
                tabla = BeautifulTable()
                for x in r:
                    tabla.rows.append([  x[0], x[1], x[2], x[3]  ])
                tabla.column_headers = ["ID BODEGA", "NOMBRE BODEGA", "ID LIBRO", "NOMBRE LIBRO"]
                system("cls")
                print("------ INVENTARIO ------")
                print(tabla)

                idBod = int(input("Digite El ID De la Bodega a la que Desea Mover el Libro: "))
                
                r = self.d.comprobarNubBod(idBod)
                if r == False:
                    print("\n--- Error De Opcion De Nub Bodega!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar Nub ID Bodega (try)!! ---")
                system("pause")

        n = Nub1()
        
        n.setIdLib(idLib)
        n.setIdBod(idBod)
        self.d.moverLib(n)

        
        system("cls")
        print("-----------------------------------------")
        print("--- El Texto se ha Movido con Éxito!! ---")
        print("------------------------------------------")
        system("pause")
        self.menuUsuarios()
