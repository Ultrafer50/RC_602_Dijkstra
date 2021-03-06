# -*- coding: utf-8 -*-
"""
Esta version del programa fue creada para ejecutar rápidamente el escenario de 
complejidad alta.
"""
import time

class Nodo:
    def __init__(self, i):
        self.id = i
        self.vecinos = []
        self.visitado = False
        self.padre = None
        self.distancia = float('inf')
    
    def agregarVecino(self, n, p):
        if n not in self.vecinos:
            self.vecinos.append([n, p])
    
class Grafo:
    def __init__(self):
        self.nodos = {}
    
    # Crear un nodo que es agregado al diccionario 'nodos'
    def agregarNodo(self, id):
        if id not in self.nodos:
            self.nodos[id] = Nodo(id)
    
    # Agregar a 'a' como vecino de 'b' y viceversa
    def agregarArista(self, a, b, p):
        if a in self.nodos and b in self.nodos:
            self.nodos[a].agregarVecino(b, p)
            self.nodos[b].agregarVecino(a, p)
    
    # Encontrar el nodo con menor distancia de una lista
    def minimo(self, lista):
        if len(lista) > 0:
            m = self.nodos[lista[0]].distancia
            n = lista[0]
            
            for e in lista:
                if m > self.nodos[e].distancia:
                    m = self.nodos[e].distancia
                    n = e
            return n
        return None
    
    # Metodo dijkstra del Grafo
    def dijkstra(self, a):
        global iteraciones
        iteraciones = 0
        if a in self.nodos:
            self.nodos[a].distancia = 0
            actual = a
            noVisitados = []
            
            for n in self.nodos:
                if n != a:
                    # Distancia infinita a todos los demas nodos
                    self.nodos[n].distancia = float('inf')
                # Se indica que ninguno tiene predecesores y no han sido visitados
                self.nodos[n].padre = None
                noVisitados.append(n)
                
                
            #Repetir hasta que se visiten todos los nodos
            while len(noVisitados) > 0:
                
                # Se recorre los vecinos del nodo actual
                for vecino in self.nodos[actual].vecinos:
                    iteraciones = iteraciones + 1
                    # Considerando los vecinos no visitados 'v' del nodo actual 'n' si la distancia 
                    # de 'n' más el peso de la arista de su vecino es menor a la distancia de 'v', 
                    # se actualiza la distancia de 'v' y se guarda a 'n' como su predecesor
                    if self.nodos[vecino[0]].visitado == False:
                        if self.nodos[actual].distancia + vecino[1] < self.nodos[vecino[0]].distancia:
                            self.nodos[vecino[0]].distancia = self.nodos[actual].distancia + vecino[1]
                            self.nodos[vecino[0]].padre = actual
                
                # Se actualiza al nodo actual como visitado
                self.nodos[actual].visitado = True
                noVisitados.remove(actual)
                
                # El nuevo nodo actual es el de menor distancia
                actual = self.minimo(noVisitados)
            
        else:
            print("El nodo no existe")
    
    # Imprimir datos básicos de cada nodo
    def imprimirDatos(self, a):
        print("Desde el nodo '" + a + "':")
        for n in self.nodos:
            print("La distancia hasta '" + n + "' es de " + 
                  str(self.nodos[n].distancia) + " llegando desde '" + 
                  str(self.nodos[n].padre) + "'")
    
    # Obtener e imprimir el camino que se debe seguir entre los nodos 'a' y 'b'
    def imprimirCamino(self, a, b):
        camino = []
        actual = b
        while actual != None:
            camino.insert(0, actual)
            actual = self.nodos[actual].padre
        
        print("\nLa ruta mas rapida por Dijkstra entre '" + a + "' y '" + b + "' es:")
        print(camino, "\nCon un costo de: " ,self.nodos[b].distancia, "\n")
    
class main:
    g = Grafo()
    
    g.agregarNodo("R-1")
    g.agregarNodo("R-2")
    g.agregarNodo("R-3")
    g.agregarNodo("R-4")
    g.agregarNodo("R-5")
    g.agregarNodo("R-6")
    g.agregarNodo("R-7")
    g.agregarNodo("R-8")
    g.agregarNodo("R-9")
    g.agregarNodo("R-10")
    g.agregarNodo("R-11")
    
    g.agregarArista("R-1", "R-2", 3)
    g.agregarArista("R-1", "R-3", 6)
    g.agregarArista("R-2", "R-6", 5)
    g.agregarArista("R-2", "R-5", 9)
    g.agregarArista("R-2", "R-4", 5)
    g.agregarArista("R-3", "R-4", 1)
    g.agregarArista("R-6", "R-5", 3)
    g.agregarArista("R-5", "R-7", 1)
    g.agregarArista("R-4", "R-7", 4)
    g.agregarArista("R-4", "R-8", 2)
    g.agregarArista("R-7", "R-11", 2)
    g.agregarArista("R-8", "R-11", 5)
    g.agregarArista("R-8", "R-9", 1)
    g.agregarArista("R-9", "R-10", 3)
    g.agregarArista("R-11", "R-10", 8)

    
    print("Nodos: 'R-1', 'R-2', 'R-3', 'R-4', 'R-5', 'R-6', 'R-7', 'R-8', 'R-9', 'R-10', 'R-11'")
    
    nodoInicio = input("Nodo de inicio: ")
    nodoDestino = input("Nodo de fin: ")
    
    start = time.perf_counter()
    
    g.dijkstra(nodoInicio)
    g.imprimirCamino(nodoInicio, nodoDestino)
    g.imprimirDatos(nodoInicio)
    
    end = time.perf_counter()
    print("Iteraciones: ", iteraciones)
    print("Tiempo de ejecucion:", (end - start))