# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 5. Ejercicio 2

import networkx as nx
from sympy import isprime

# Recibe un conjunto de numeros positivos c
# y retorna la cantidad minima de numeros a eliminar de c
# tal que no existan dos numeros que sumados den como resultado un numero primo
def min_eliminar(c):
    grafo = nx.Graph()

    # Se itera sobre cada par de numeros para determinar si su suma es un numero primo
    # Si es asi, se agrega una arista entre los dos numeros en el grafo
    # Tiempo de ejecucion: O(n^2)
    for i in range(len(c)):
        for j in range(i+1, len(c)):
            if isprime(c[i] + c[j]):
                grafo.add_edge(c[i], c[j])

    # Se obtiene el conjunto independiente maximal del grafo,
    # es decir, el mayor conjunto de nodos que no estan conectados por ninguna arista
    # Como todos los numeros que sumados dan como resultado un numero primo
    # estan conectados, en este conjunto se obtendran los numeros que no suman
    # un numero primo
    max_independent_set = nx.maximal_independent_set(grafo)

    # La solucion se obtiene al restar la cantidad de nodos del emparejamiento maximo
    # a la cantidad de nodos del grafo
    return len(c) - len(max_independent_set)

# Si se considera que determinar si un numero es primo toma tiempo O(1),
# entonces el tiempo de ejecucion de es O(n^2)
# Caso contrario, el tiempo de ejecucion pasa a ser de O(n^2*√n)
c = [9, 2, 1, 5]
resultado = min_eliminar(c)
print(f"Números a eliminar para que no sumen numeros primos: {resultado}")

