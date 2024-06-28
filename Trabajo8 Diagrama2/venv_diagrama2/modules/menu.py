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


from modules import clases  # Importo modulo clases donde esta la informacion principal del programa 
from random import randint # Importo randint para sacar valore aleatorios en algunos estados 
from modules import functions as Fun # Importo funciones donde se encuentran funciones de control de entrada 
from colorama import Fore,Back # Importo colorama para color fondo y fuente
print(Fore.BLACK + Back.BLUE)# Defino colores fondo y fuente 

while True:
  print("-----------------------")
  print("EJERCICIO CLASES PRODUCTOS:")# Menu de control para hacer mas organizada la presentacion del programa 
  print("1. Datos Revista") # Opcion 1 datos de revista 
  print("2. Datos Libro")   # Opcion 2 datos de libro
  print("3. Datos Producto Grabado") # Opcion 3 datos producto grabado
  print("4. Datos Sofware") # Opcion 4 datos sofware
  print("5. Salir") # Opcion 5 para salir del progrma 
  print("-----------------------")
  
  while True:
      try:
          opcion = int(input("Escoge una opción: "))
          break  # Salimos del bucle si se ingresa un número válido
      except ValueError:
          print("Opción inválida. Inténtalo nuevamente.")
    # opcion = int(input("Escoge una opcion: ")) # El usuario escoge una opcion 


  if opcion == 1:
    revista1 = clases.Revista (0, "", "", "", 0, 0 , 0) # Defino revista1 como objeto de super clase producto impreso 

    revista1.leer_datos()       # Esta funcion de revista1 me recibe todos los datos ingresados por el usuario 

    revista1.informacion_revista() # Esta funcion de revista1 imprime lo que se almacena en la funcion ler datos 

    revista1.estado() # Esta funcion me imprime el estado de revista1 ( Impresion/ revision / publicacion / en diagramacion)


  elif opcion== 2:
    libro1 = clases.Libro (0, "", "", "", 0, 0, "") # Defino libro1 como objeto de super clase producto impreso 

    libro1.leer_datos()  # Esta funcion me recibe todos los datos ingresados por el usuario 

    libro1.informacion_libro() # Esta funcion de imprime los datos de la instancia libro1

    libro1.estado() # Esta funcion me imprime el estado de libro1 ( En revision/En publicacion/En impresion/En diagramacion)


  elif opcion== 3:
    grabado1 = clases.ProductoGrabado (0, "", "", 0, "")  # Defino grabado1 como objeto de super clase producto  

    grabado1.leer_datos()  # Esta funcion me recibe todos los datos ingresados por el usuario 

    grabado1.informacion_producto_grabado() # Esta funcion de imprime los datos de la instancia producto grabado


  elif opcion== 4:
    software1 = clases.ProductoSofware (0, "", "", 0, "")  # Defino sofware1 como objeto de super clase producto

    software1.leer_datos() # Esta funcion me recibe todos los datos ingresados por el usuario 

    software1.informacion_producto_sofware()  # Esta funcion de imprime los datos de la instancia producto sofware
    

  elif opcion== 5:
    print("Adios") # Al digitar tecla 5 el usuario sale del programa y aparece el letrero ADIOS 
    break          # Declaracion para la finalizacion del bucle while del menu 
  else:
    print("Opcion no valida") # Si se llegase a digitar un numero diferente de 1 a 5 aparece opcion no valida 
