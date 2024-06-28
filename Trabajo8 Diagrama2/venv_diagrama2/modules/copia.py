#------------------------APP------------------------------

from modules import clases  # Importo modulo clases don esta la informacion principal del programa 
from random import randint # Importo randint para sacar valore aleatorios en algunos estados 
from modules import functions as Fun # Importo funciones donde se encuentran funciones de control de entrada 

def main():

 while True:
  print("-----------------------")
  print("EJERCICIO CLASES PRODUCTOS:")# Menu de control pra hacer mas organizada la presentacion del programa 
  print("1. Datos Revista") # Opcion 1 datos de revista 
  print("2. Datos Libro")   # Opcion 1 datos de libro
  print("3. Datos Producto Grabado") # Opcion 1 datos producto grabado
  print("4. Datos Sofware") # Opcion 1 datos sofware
  print("5. Salir") # Opcion para salir del progrma 
  print("-----------------------")
  opcion = float(input("Escoge una opcion: "))

  if opcion == 1:
    revista1 = clases.Revista (0, "", "", "", 0, 0 , 0) # Defino revista1 como objeto de super clase producto impreso 

    revista1.leer_datos()       # Esta funcion de revista1 me recibe todos los datos ingresados por el usuario 

    revista1.informacion_revista() # Esta funcion de revista1 imprime los datos de la instancia revista1 

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


if __name__ == "__main__": # Declaracion que me indica que este es el modulo principal del programa 
  main()


#----------------------------clases------------------------

from modules import clases  # Importo modulo clases don esta la informacion principal del programa 
from random import randint # Importo randint para sacar valore aleatorios en algunos estados 
from modules import functions as Fun # Importo funciones donde se encuentran funciones de control de entrada 

def main():

 while True:
  print("-----------------------")
  print("EJERCICIO CLASES PRODUCTOS:")# Menu de control pra hacer mas organizada la presentacion del programa 
  print("1. Datos Revista") # Opcion 1 datos de revista 
  print("2. Datos Libro")   # Opcion 1 datos de libro
  print("3. Datos Producto Grabado") # Opcion 1 datos producto grabado
  print("4. Datos Sofware") # Opcion 1 datos sofware
  print("5. Salir") # Opcion para salir del progrma 
  print("-----------------------")
  opcion = float(input("Escoge una opcion: "))

  if opcion == 1:
    revista1 = clases.Revista (0, "", "", "", 0, 0 , 0) # Defino revista1 como objeto de super clase producto impreso 

    revista1.leer_datos()       # Esta funcion de revista1 me recibe todos los datos ingresados por el usuario 

    revista1.informacion_revista() # Esta funcion de revista1 imprime los datos de la instancia revista1 

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


if __name__ == "__main__": # Declaracion que me indica que este es el modulo principal del programa 
  main()

#-----------------------------------funtions----------------------------------------------------------------

from modules import clases # Impórto el modulo clases para vincular con los inputs de acceso 

def control_letras(prompt):   # Control para validar que el usuario solo digite letras en en el input 
    while True:
      entrada = input(prompt) # El while condiciona la entrada con isalpha 
      if (entrada.replace("","").isalpha()):
        break  # Declaracion para finalizar el bucle while 
      else:     # Si el usuario digita numeros o caractes diferentes a isalpha envia un mensaje 
        print("Solo digite caracteres alfabeticos") # Mensaje por que se digito caracteres diferentes a isalpha 
    return entrada # despues de mostrar el mensaje de la linea anterior retorna al inicio de la entrada 


def control_numeros(prompt): # Control para validar que el usuario solo digite numeros en en el input 
    while True:   # El while condiciona la entrada con isnumeric 
        entrada = input(prompt)
        if (entrada.isnumeric()):  # Si el usuario digita numeros o caractes diferentes a isnumeric envia un mensaje 
          break  # Declaracion para finalizar el bucle while 
        else:    # Mensaje por que se digito caracteres diferentes a caracteres numericos 
             print ("Solo digite caracteres numericos")
    return entrada # despues de mostrar el mensaje de la linea anterior retorna al inicio de la entrada 


def control_numeros_letras(prompt): # Control para validar que el usuario solo digite numeros o letras 
    while True: # El while condiciona la entrada con isalnum
        entrada = input(prompt)
        if entrada.isalnum():
            break # Declaracion para finalizar el bucle while 
        else:  # Si el usuario digita numeros o caractes diferentes a isalnum envia un mensaje 
            print("Solo digite caracteres alfabéticos y números")
    return entrada # despues de mostrar el mensaje de la linea anterior retorna al inicio de la entrada 
