#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 4.0                         #
# Fecha: 09/06/2024                     #
#***************************************#

#Este programa se encuentra diseñado par demostrar la funcionalidad que resulta 
# del correcto manejo del POP, mediante super clases, subclases y clases logramos
# crear y modificar los atributos y metodos de un objeto. Super clase producto, 
# subclases producto grabado, producto impreso,producto sofware, revista y libro


from random import randint 
from modules import functions as Fun
#---------------------PRODUCTO--------------------------------
class Producto: # Definicion de la superclase 


    def __init__(self, codigo, titulo, autor): # Definicion de la superclase  
        self.__codigo = codigo 
        self.__titulo = titulo     # Definicion self de los argumentos 
        self.__autor = autor


    def set_codigo(self, value):    
        self.__codigo = value   # Funcion que define el set del argumento codigo 
    

    def get_codigo(self):       # Funcion que define el get del argumento codigo 
        return self.__codigo
    

    def set_titulo(self, value): # Funcion que define el set del argumento titulo
        self.__titulo = value


    def get_titulo(self):        # Funcion que define el get del argumento titulo
        return self.__titulo


    def set_autor(self, value):  # Funcion que define el set del argumento autor
        self.__autor = value
        


    def get_autor(self):         # Funcion que define el get del argumento autor 
        return self.__autor


#---------------------PRODUCTO IMPRESO--------------------------------

class ProductoImpreso (Producto): # Definicion de la subclase 


    def __init__(self, codigo, titulo, autor, editorial, año, precio ):  # Creacion del constructor y sus argumentos 
        

        super ()
        def __init__ (self, codigo, titulo, autor): 
         # Definicion de los self de los argumentos que hereda de la super clase producto 
            self.__editorial = editorial    
            self.__año = año             


    def set_editorial(self, value):  # Funcion que define el set del argumento editorial 
        self.__editorial = value
    

    def get_editorial(self):         # Funcion que define el get del argumento editorial 
        return self.__editorial
    

    def set_año(self, value):       # Funcion que define el set del argumento año
        self.__año = value


    def get_año(self):              # Funcion que define el get del argumento año
        return self.__año


    def set_precio(self, value):    # Funcion que define el set del argumento precio
        self.__precio = value


    def get_precio(self):           # Funcion que define el get del argumento precio
        return self.__precio


  #---------------------REVISTA-----------------------------------------

class Revista (ProductoImpreso): # Definicio de la clase revista 


    def __init__(self, codigo = 0, titulo = "", autor = "", editorial = "", año = 0, precio = 0, volumen = "" ):
    # Defino argumentos heredados y nuevos  

        super ()
        def __init__ (self, codigo, titulo, autor, editorial, año, precio):
    # Defino argumentos heredados de las superclase y subclase 

            self.__volumen = volumen # Definicion self nuevos argumentos
            

    def set_volumen(self, value):  # Funcion que define el set del argumento volumen
        self.__volumen = value
    

    def get_volumen(self):         # Funcion que define el get del argumento volumen   
        return self.__volumen
    

    def leer_datos(self):
        self.set_codigo (Fun.control_numeros_letras("Digite el codigo de la revista: "))
        self.set_titulo (Fun.control_numeros_letras("Digite el titulo de la revista: "))
        self.set_autor (Fun.control_letras("Digite el autor de la revista: "))
        self.set_editorial (Fun.control_letras("Escriba el nombre de la editorial: "))
        self.set_año (Fun.control_numeros_letras("Digite el año de publicacion de la revista: "))
        self.set_precio (Fun.control_numeros("Digite el precio de la revista: "))
        self.set_volumen(Fun.control_numeros_letras("Digite el volumen de la revista: ")) 
    # Funcion para el ingreso de datos de la clase revista ( codigo/titulo/autor/editorial/año/precio/Volumen)

    def estado(self):
        estados = ["En revision", "En publicacion", "En impresion", "En diagramacion"]
        emi= randint(0,len(estados) -1)
        print("El estado de la revista: {0}".format(estados[emi]))

    # Funcion para definir el estado de la revista (publicaion/impresion/diagramacion)

    def informacion_revista(self):
        print("El codigo de la revista es : {0} El titulo de la revista es :  {1} El autor de la revista es : {2} La editorial de la revista es: {3}   El año de publicacion de la revista es : {4} ""El precio de la revista es:  {5} El volumen de la revista es:{6} " . format( self.get_codigo(), self.get_titulo(), self.get_autor (), self.get_editorial(), self.get_año(), self.get_precio(), self.get_volumen() ,end =""))
    
    # Funcion para imprimir los datos ingresados en la funcion leer datos 

#---------------------LIBRO-----------------------------------------

class Libro (ProductoImpreso): # Definicio de la clase libro

    def __init__(self, codigo = 0, titulo = "", autor = "", editorial = "", año = "", precio = 0, idioma = "" ):
    # Defino argumentos heredados y nuevos   

        super ()
        def __init__ (self, codigo, titulo, autor, editorial, año, precio):
     # Defino argumentos heredados de las superclase y subclase 
        
            self.__idioma = idioma # Definicion self nuevos argumentos 
            

    def set_idioma(self, value):  # Funcion que define el set del argumento idioma 
        self.__idioma = value
    

    def get_idioma(self):      # Funcion que define el get del argumento idioma      
        return self.__idioma


    def leer_datos(self):
        self.set_codigo (Fun.control_numeros_letras("Digite el codigo del libro: "))
        self.set_titulo (Fun.control_numeros_letras("Digite el titulo del libro: "))
        self.set_autor (Fun.control_letras("Digite el autor del libro: "))
        self.set_editorial (Fun.control_letras("Escriba el nombre de la editorial: "))
        self.set_año (Fun.control_numeros_letras("Digite el año de publicacion del libro: "))
        self.set_precio (Fun.control_numeros("Digite el precio del libro: "))
        self.set_idioma(Fun.control_letras("Digite el idioma en que esta publicado el libro: ")) 

 # Funcion para el ingreso de datos de la clase libro ( codigo/titulo/autor/editorial/año/precio/idioma )

    def estado(self):
        estados = ["En revision", "En publicacion", "En impresion", "En diagramacion"]
        emi= randint(0,len(estados) -1)
        print("El estado del libro es:  {0}".format(estados[emi]))
  # Funcion para definir el estado de la revista (publicaion/impresion/diagramacion)

    def informacion_libro(self):
        print("El codigo del libro es : {0} El titulo del libro es :  {1} El autor del libro es : {2} La editorial del libro es: {3}   El año de publicacion de publicacion del libro es : {4} ""El precio del libro es:  {5} El idioam en que viene publicado el libro es :{6} " . format( self.get_codigo(), self.get_titulo(), self.get_autor (), self.get_editorial(), self.get_año(), self.get_precio(), self.get_idioma() ,end =""))
    
      # Funcion para imprimir los datos ingresados en la funcion leer datos 

#---------------------PRODUCTO GRABADO--------------------------------
            
class ProductoGrabado (Producto): # Definicio de la clase producto grabado

    def __init__(self, codigo = 0, titulo = "", autor = "", tiempo_duracion = 0, medio_tecnologico = ""):
    # Defino argumentos heredados y nuevos   

        super ()
        def __init__ (self,codigo,titulo,autor):
        # Defino argumentos heredados de las superclase y subclase     

            self.__tiempo_duracion = tiempo_duracion     # Definicion self nuevos argumentos 
            self.__medio_tecnologico = medio_tecnologico
           

    def set_tiempo_duracion(self, value): # Funcion que define el set del argumento tiempo_duracion
        self.__tiempo_duracion = value
    

    def get_tiempo_duracion(self):   # Funcion que define el get del argumento tiempo_duracion       
        return self.__tiempo_duracion
    

    def set_medio_tecnologico(self, value):  # Funcion que define el set del argumento medio_tecnologico
        self.__medio_tecnologico = value


    def get_medio_tecnologico(self):  # Funcion que define el get del argumento medio_tecnologico
        return self.__medio_tecnologico


    def leer_datos(self):
        self.set_codigo (Fun.control_numeros_letras("Digite el codigo del producto grabado: "))
        self.set_titulo (Fun.control_numeros_letras("Digite el titulo del producto grabado : "))
        self.set_autor (Fun.control_letras("Digite el autor del producto grabado: "))
        self.set_tiempo_duracion (Fun.control_numeros_letras("Escriba el tiempo de duracion del producto: "))
        self.set_medio_tecnologico (Fun.control_letras("Digite el medio tecnologico del producto grabado: "))
    # Funcion para el ingreso de datos de la clase libro ( codigo/titulo/autor/tiempo_duracion/medio_tecnologico) 

    def informacion_producto_grabado(self):
        print("El codigo del producto grabado : {0} El titulo del producto grabado es :  {1} El autor del producto grabado es  : {2} El tiempo de duracion del producto es : {3} El medio tecnologico del producto grabado es : {4} " . format( self.get_codigo(), self.get_titulo(), self.get_autor (), self.get_tiempo_duracion(), self.get_medio_tecnologico() ,end =""))
    # Funcion para imprimir los datos ingresados en la funcion leer datos      

#---------------------PRODUCTO SOFWARE--------------------------------

class ProductoSofware (Producto): # Definicio de la clase producto grabado

    def __init__(self, codigo = 0, titulo = "", autor = "", version = 0, sistema_operativo = ""):
    # Defino argumentos heredados y nuevos      

        super ()
        def __init__ (self,codigo,titulo,autor):
        # Defino argumentos heredados de las superclase y subclase 

            self.__version = version   # Definicion self nuevos argumentos 
            self.__sistema_operativo = sistema_operativo
           

    def set_version(self, value):  # Funcion que define el set del argumento version    
        self.__version = value
    

    def get_version(self):        # Funcion que define el get del argumento version     
        return self.__version
    

    def set_sistema_operativo(self, value): # Funcion que define el set del sistema_operativo
        self.__sistema_operativo = value


    def get_sistema_operativo(self): # Funcion que define el get del sistema_operativo
        return self.__sistema_operativo


    def leer_datos(self):
        self.set_codigo (Fun.control_numeros_letras("Digite el codigo del software: "))
        self.set_titulo (Fun.control_letras("Digite el titulo del software : "))
        self.set_autor (Fun.control_letras("Digite el autor del software: "))
        self.set_version (Fun.control_numeros_letras("Escriba la version del software: "))
        self.set_sistema_operativo (Fun.control_numeros_letras("Digite el sistema operativo en que corre el software: "))
    # Funcion para el ingreso de datos de la clase libro ( codigo/titulo/autor/version/sistema_operativo) 

    def informacion_producto_sofware(self):
        print("El codigo del software es : {0} El titulo  del software es :  {1} El autor del software es : {2} La version del software es : {3} El sistema operativo en que corre el software es : {4} " . format( self.get_codigo(), self.get_titulo(), self.get_autor (), self.get_version(), self.get_sistema_operativo() ,end =""))
    # Funcion para imprimir los datos ingresados en la funcion leer datos      
     
    
          
    