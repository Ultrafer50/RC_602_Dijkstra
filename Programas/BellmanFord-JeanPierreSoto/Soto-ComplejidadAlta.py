# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:35:48 2021

@author: USUARIO
"""

#from pip._vendor.distlib.compat import raw_input

'''
'''

from time import perf_counter
  
class Grafo: 
  
    def __init__(self,vertices): 
        self.V= vertices 
        self.grafo = []  
   
    
    def agregarEdge(self,u,v,w): 
        self.grafo.append([u, v, w]) 
          
    
    def imprimir(self, distancia): 
        print("Vertice    Distancia desde el origen") 
        for i in range(self.V): 
            print(str(i) + "\t\t" + str(distancia[i])) 
      
    
    def BellmanFord(self, src): 
        distancia = [float("Inf")] * self.V 
        distancia[src] = 0 
  
        for i in range(self.V - 1):
            global iteraciones
            iteraciones = 0
            for u, v, w in self.grafo: 
                iteraciones = iteraciones + 1
                if distancia[u] != float("Inf") and distancia[u] + w < distancia[v]: 
                        distancia[v] = distancia[u] + w 
  
  
        for u, v, w in self.grafo: 
                if distancia[u] != float("Inf") and distancia[u] + w < distancia[v]: 
                        print ("El grafo contiene algun peso negativo")
                        return
                          
        self.imprimir(distancia) 

g = Grafo(15)  
print ("Se creara un grafo de 0-14")
a1 = 3  # Distancia de 0-1
a2 = 6  # Distancia de 0-2 
a3 = 5  # Distancia de 1-5 
a4 = 9  # Distancia de 1-4 
a5 = 5  # Distancia de 1-3
a6 = 1  # Distancia de 2-3 
a7 = 4  # Distancia de 3-6
a8 = 2  # Distancia de 3-7
a9 = 3  # Distancia de 4-5
a10 = 1 # Distancia de 4-6
a11 = 2 # Distancia de 6-10
a12 = 5 # Distancia de 7-10
a13 = 1 # Distancia de 7-8
a14 = 3 # Distancia de 8-9
a15 = 8 # Distancia de 9-10

g.agregarEdge(0, 1, a1)
g.agregarEdge(0, 2, a2)
g.agregarEdge(1, 5, a3)
g.agregarEdge(1, 4, a4)
g.agregarEdge(1, 3, a5)
g.agregarEdge(2, 3, a6)
g.agregarEdge(3, 6, a7)
g.agregarEdge(3, 7, a8)
g.agregarEdge(4, 5, a9)
g.agregarEdge(4, 6, a10)
g.agregarEdge(6, 10, a11)
g.agregarEdge(7, 10, a12)
g.agregarEdge(7, 8, a13)
g.agregarEdge(8, 9, a14)
g.agregarEdge(9, 10, a15)


print ("Camino mas corto desde el origen")

startime = perf_counter()
g.BellmanFord(0)
elapsed_time = perf_counter() - startime
print("Numero de iteraciones: ", iteraciones)
print("El tiempo de ejecución del algoritmo es: ", elapsed_time) 

#La complejidad de este algoritmo es de n^2, ya que existen tres
#bucles inmersos en él.
