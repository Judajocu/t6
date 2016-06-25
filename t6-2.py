# coding=utf-8
from QuickSort import *

jobs = open('jobs.txt')

lista = []

lista_map = []

result = []

# LO MISMO PERO CON UNA DIVISIÓN :v

def maping_parte1(lista_temp):

    for i in lista[1:]:
        lista_map.append(tuple(map(int, i.split())))

    for i in lista_map:
        diver = abs(i[0]/i[1])
        sort_n = diver * 1000 + i[1]
        result.append(list(map(int, (sort_n, diver))))

    quicksort(result)

    result.reverse()

# LO MISMO PERO CON UNA DIVISIÓN :v

def main():
    for i in jobs:
        lista.append(i.strip("\n"))
    jobs.close()

    maping_parte1(lista)
    print lista_map
    print (result)

# LO MISMO PERO CON UNA DIVISIÓN :v

main()
