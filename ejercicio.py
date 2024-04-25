#Elaborar u progma en python que permita calcular  el valor de  un lote dependiendo de las siguientes condiciones
#PEDIR MEDIDAS(MT)

#1.URBANO
#M2= 25000
#permiso de cosntruccion = 0.45
#2.comercial
#m2 = 60000
#permiso de construccion = 0.75
#3.Campestre
#m2 = 35000 
#permiso de contruccion = 0.15

import os

def fnt_pantalla():
    os.system('cls')
    print('Autor:Andres Felipe')
    print('25-04-2024')

def fnt_registar():
    fnt_pantalla()
    nombre = input('Nombre:')
    identificacion = input('Identificacion:')
    area = input('Area:')
    tipo = input('Tipo:')
    if nombre == '' or identificacion == '' or area == '' or tipo == '':
        input('Ingrese todos los datos correctamerte')
    else:
        input('Datos registrados correctamente <ENTER> para continuar')

def fnt_selector(opcion):
    global sw
    if opcion == '0':
        sw = False
    elif opcion == '1':
        fnt_registar()
        
sw = True

while sw == True:
    fnt_pantalla()
    opcion= input('<<<<<< Menu de opciones >>>>>> \n0.Salirn\n1.Agregar un nuevo lote\n2.Mostrar lotes')
    fnt_selector(opcion)