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
            print("%d \t\t %d" % (i, distancia[i])) 
      
    
    def BellmanFord(self, src):
        global iteraciones
        iteraciones = 0
        distancia = [float("Inf")] * self.V 
        distancia[src] = 0 
  
        for i in range(self.V - 1): 
            for u, v, w in self.grafo: 
                iteraciones = iteraciones + 1
                if distancia[u] != float("Inf") and distancia[u] + w < distancia[v]: 
                        distancia[v] = distancia[u] + w 
  
  
        for u, v, w in self.grafo: 
                if distancia[u] != float("Inf") and distancia[u] + w < distancia[v]: 
                        print ("El grafo contiene algun peso negativo")
                        return
                          
        self.imprimir(distancia) 

g = Grafo(6)  
print ("Se creara un grafo de 0-5")
a1 = 2 # Distancia de 0-1
a2 = 5 # Distancia de 1-2 
a3 = 3 # Distancia de 1-3 
a4 = 4 # Distancia de 2-4 
a5 = 3 # Distancia de 3-4
a6 = 6 # Distancia de 3-5 
a7 = 4 # Distancia de 4-5

g.agregarEdge(0, 1, a1) 
g.agregarEdge(1, 2, a2) 
g.agregarEdge(1, 3, a3) 
g.agregarEdge(2, 4, a4) 
g.agregarEdge(3, 4, a5) 
g.agregarEdge(3, 5, a6) 
g.agregarEdge(4, 5, a7) 


print ("Camino mas corto desde el origen")

startime = perf_counter()
g.BellmanFord(0)
elapsed_time = perf_counter() - startime
print("Numero de iteraciones: ", iteraciones)
print("El tiempo de ejecución del algoritmo es: ", elapsed_time) 

#La complejidad de este algoritmo es de n^2, ya que existen tres
#bucles inmersos en él.