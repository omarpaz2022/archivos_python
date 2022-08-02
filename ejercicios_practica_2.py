# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion  

    with open ('stock.csv','r')  as csvfile: 
        data = list(csv.DictReader(csvfile)) 
        columna='tornillos'
        suma=0 

    for i in range(len(data)):
        valor=data[i]
        for k,v in valor.items():
            if k==columna:
                suma=suma+int(v) 

    print('la suma de tornillos es de: ', suma)                                 
    


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion 

    with open ('propiedades.csv','r')  as csvfile: 
        data = list(csv.DictReader(csvfile)) 
        suma_2_ambientes=0
        suma_3_ambientes=0 

    for i in range(len(data)):
        valor=data[i]
        for k,v in valor.items():
            if k=='ambientes':
                if v==None:
                    break
                elif v=='2':
                    suma_2_ambientes=suma_2_ambientes+int(v)
                elif v=='3':
                    suma_3_ambientes=suma_3_ambientes+int(v)        

    print('Total de departamentos con 2 ambientes: ', suma_2_ambientes)
    print('Total de departamentos con 3 ambientes: ', suma_3_ambientes)




if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
