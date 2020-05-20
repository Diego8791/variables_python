#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para poner a prueba los conocimientos adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica numérica
    
    # Operadores con números decimales
    print('Ingrese el primer número decimal a operar:')
    numero_1 = int(input()) # ¿Aqui habria que cambiar el tipo de variable?

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = int(input()) # ¿aqui habria que cambiar el tipo de variable?
    
    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)
    print('Los números ingresados son',numero_1,'y',numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    suma_1 = numero_1 + numero_2
    resta_1 = numero_1 - numero_2
    division_1 = numero_1 / numero_2
    multiplicacion_1 = numero_1 * numero_2

    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6
    
    # Utilizo la funcion round() para redondear el resultado a 2 decimales

    print('El resultado de sumar',numero_1,'y',numero_2, 'es', round(suma_1,2))
    
    print('La resultado de restar',numero_1,'y',numero_2, 'es', round(resta_1,2))
    
    print('La resultado de dividir',numero_1,'y',numero_2, 'es', round(division_1,2))
    
    print('La resultado de multiplicar',numero_1,'y',numero_2, 'es', round(multiplicacion_1,2))

def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números reales
    print('Ingrese el primer número real a operar:')
    numero_3 = float(input())

    print('Ingrese el segundo número real a operar:')
    numero_4 = float(input())

    # Alumno: Imprima en pantalla los dos números reales solicitados
    # print(....)

    print('El primer numero ingresado es',numero_3,'y el segundo es',numero_4)
 
    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_3, numero_4
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    suma_2 = numero_3 + numero_4
    resta_2 = numero_3 - numero_4
    division_2 = numero_3 / numero_4
    multiplicacion_2 = numero_3 * numero_4

    print('El resultado de sumar',numero_3,'y',numero_4,'es',round(suma_2,2))
    print('El resultado de restar',numero_3,'y',numero_4,'es',round(resta_2,2))
    print('El resultado de dividir',numero_3,'y',numero_4,'es',round(division_2,2))
    print('El resultado de multiplicar',numero_3,'y',numero_4,'es',round(multiplicacion_2,2))
  
   
def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo

    print(nombre,apellido)

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....
    
    nombre_completo = nombre + apellido

    # Imprimir la cantidad de letras que posee su nombre completo
    print('La cantidad de letras que tiene mi nombre es',len(nombre_completo))

def ej5():                              # Habian dos ej3
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    
    acronimo = palabra_1[0] + palabra_2[0] + palabra_3[0] # Tomo la letra en la posicion 0 de cada palabra
    acronimo = acronimo.upper()  # el acronimo convertira todas las letras a mayusculas
  
    # Imprimir el resultado en pantalla

    print('El acronimo de las palabras',palabra_1,',',palabra_2,'y',palabra_3,'es',acronimo)

def ej4():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    recorte_pal_1 = palabra_1[:3]
    recorte_pal_2 = palabra_2[len(palabra_2)-3:]
    
    # Formar una nueva palabra con los recortes solicitados
    nueva_palabra = recorte_pal_1 + recorte_pal_2

    # Imprima en pantalla los resultados
    print('La nueva palabra es',nueva_palabra)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()  
