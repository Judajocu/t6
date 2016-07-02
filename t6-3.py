from heapq import *
import random

graph = []
monti = []
chosens = []
priming = []
edges = []

def Prim(list_inicial):

    for i in list_inicial[1:]:
        graph.append(list(map(int, i.split(' '))))

    rand_init = random.randint(1,500)

    heappush(monti, rand_init)
    
    while len(chosens) < 500:
        curry = heappop(monti)
        if not chosens.__contains__(curry):
            if curry is not rand_init:
                for i in graph:
                    for j in chosens:
                        if (i[0] == curry and i[1] == j) or (i[1] == curry and i[0] == j):
                            edges.append(i)
                decente = sorted(edges, key=lambda a: a[2])
                if len(decente) > 0:
                    priming.append(decente[0])
            chosens.append(curry)
            for i in graph:
                if i[0] == curry:
                    if not chosens.__contains__(i[1]):
                        heappush(monti,i[1])
                if i[1] == curry:
                    if not chosens.__contains__(i[0]):
                        heappush(monti,i[0])
        edges = []

    path = 0
    for i in priming:
        path += i[2]
    print(path)


def main():
    init = []
    tarea = open('edges.txt')

    for linea in tarea:
        init.append(linea.replace('\n', ''))
    tarea.close()
    Prim(init)
    

if __name__ == '__main__':
    main()