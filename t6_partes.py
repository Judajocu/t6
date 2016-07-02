# coding=utf-8
from QuickSort import *

jobs = open('jobs.txt') # Abrir el archivo que contiene los trabajos

lista = [] # Esta es la lista que se llenara con los datos originales del archivo

lista_map = [] # Este es la lista con la que se trabajara el programa

result = [] # Este es la lista que contendrá en archivo final el cual es el resultado


def maping_parte1(lista_temp):

    for i in lista[1:]: # Se recorre la lista para separar el peso y la longitud
        lista_map.append(tuple(map(int, i.split()))) # Se va entrando a la lista de tuplas y poder trabajar con esa lista

    for i in lista_map: # Aquí se recorre con el arreglo de tupla
        differ = abs(i[0]-i[1]) # Conseguir la diferencia de peso y la longitud
        sort_n = differ * 1000 + i[1] # identificador de diferencia con peso, por eso es que se multiplica por mil
        result.append(list(map(int, (sort_n, differ)))) # Aquí se Agrega a la lista final para mostrar el resultada, siendo una lista de listas

    quicksort(result) # sort :v

    result.reverse() # En el orden que desea :v

# Aquí hacemos por la magía del main()
def main():
    for i in jobs: # Aquí se recorre el archivo que contiene los datos
        lista.append(i.strip("\n")) # Aquí se va entrando a la lista
    jobs.close() # Aquí se cierra el archivo

    maping_parte1(lista) # Aquí se llama a la función con la que se hace las operaciones
    print "Tuplas"
    print lista_map # Imprimir lista de tupla con la que se trabajó :v
    print "Resultado"
    print (result) # # Imprimir parte 1 :v


main()
