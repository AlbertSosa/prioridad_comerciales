import heapq
from multiprocessing import heap

from urllib.request import urlopen

import time
import webbrowser

"""
TODO 
algoritmo de prioridades
conexion con la BD
proyectar comercial
"""

list1=[
    (1,"telcel", "https://www.youtube.com/watch?v=99gVx3Nd8vc", 6), 
    (8, "PRD", "https://www.youtube.com/watch?v=CPLZF2a71Xg", 10), 
    (6,"telefonia", "https://www.youtube.com/watch?v=o0wg_w5VcDo", 8), 
    (3,"boletos", "https://www.youtube.com/watch?v=pSGcQ-omm-U", 2)
    ]

heapq.heapify(list1)                #ordenar en un monticulo por piroridades
#print(list1)

for i in range (len(list1)):        #ciclo para vaciar el moticulo
    #print(heapq.heappop(list1))
    print(list1[i][2],list1[i][0])          #Imprimimos la informacion del comercial
    webbrowser.open(list1[i][2], new=0)     #abrimos el comercial
    time.sleep(list1[i][3])                 #esperamos a que se termine el tiempo de ejecucion

    