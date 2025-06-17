
''' 
Esempio di Complessità Quadratica (O(n²)) :
'''

# La complessità quadratica è indicata come O(n²) e significa che il tempo di esecuzione cresce
# proporzionalmente al quadrato della dimensione dell'input.
# Ecco alcuni esempi di algoritmi con complessità O(n²), escludendo il Merge Sort (che ha O(n log n)).

''' 
1️⃣ Bubble Sort 
'''

def bubble_sort(arr):
    # Algoritmo di ordinamento inefficiente che confronta coppie adiacenti
    n = len(arr)
    for i in range(n):  # Ciclo esterno
        for j in range(0, n - i - 1):  # Ciclo interno
            if arr[j] > arr[j + 1]:  # Scambio se necessario
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Esempio di utilizzo
print(bubble_sort([5, 3, 8, 4, 2]))

''' 
📌 Complessità: 
'''
# - Due cicli annidati → O(n²)
# - Peggiore e medio caso: O(n²)
# - Miglior caso: O(n) (se l'array è già ordinato)

''' 
2 Selection Sort 
'''

def selection_sort(arr):
    # Algoritmo che seleziona ripetutamente il valore più piccolo
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):  # Cerca il minimo nel resto dell'array
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Scambia gli elementi
    return arr

# Esempio di utilizzo
print(selection_sort([64, 25, 12, 22, 11]))

''' 
📌 Complessità: 
'''
# - Due cicli annidati → O(n²)
# - Peggiore, medio e miglior caso: O(n²)

''' 
3️⃣ Insertion Sort 
'''

def insertion_sort(arr):
    # Algoritmo che inserisce ogni elemento nella posizione corretta
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:  # Sposta gli elementi per trovare il posto corretto
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Esempio di utilizzo
print(insertion_sort([9, 5, 1, 4, 3]))

''' 
📌 Complessità: 
'''
# - Peggiore e medio caso: O(n²)
# - Miglior caso: O(n) (se l'array è già ordinato)

''' 
4️⃣ Algoritmo per trovare tutte le coppie in un array 
'''

def find_pairs(arr):
    # Confronta tutte le coppie possibili in un array
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):  # Confronta ogni coppia
            print(f"Coppia: ({arr[i]}, {arr[j]})")

# Esempio di utilizzo
find_pairs([1, 2, 3, 4])

''' 
📌 Complessità: 
'''
# - Due cicli annidati → O(n²)

''' 
5️⃣ Moltiplicazione di matrici 
'''

def multiply_matrices(A, B):
    # Moltiplicazione tra due matrici n x n
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):  # Scorre le righe
        for j in range(n):  # Scorre le colonne
            for k in range(n):  # Calcola il prodotto scalare (O(n³) in realtà)
                result[i][j] += A[i][k] * B[k][j]
    return result

# Esempio di utilizzo
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(multiply_matrices(A, B))

''' 
📌 Complessità: 
'''
# - In genere O(n³), ma versioni ottimizzate riducono a O(n²) in alcuni casi.

''' 
6️⃣ Problema del Viaggiatore (Approccio Greedy) 
'''

import random

def nearest_neighbor_tsp(distances):
    # Soluzione approssimata al problema del Commesso Viaggiatore (TSP)
    n = len(distances)
    visited = [False] * n
    path = [0]  # Partiamo dal nodo 0
    visited[0] = True
    for _ in range(n - 1):  # Visitiamo tutti i nodi una volta
        last = path[-1]
        next_city = min(
            [(i, distances[last][i]) for i in range(n) if not visited[i]], 
            key=lambda x: x[1]
        )[0]
        path.append(next_city)
        visited[next_city] = True
    return path

# Esempio di utilizzo
distances = [[0, 2, 9, 10],
             [1, 0, 6, 4],
             [15, 7, 0, 8],
             [6, 3, 12, 0]]
print(nearest_neighbor_tsp(distances))

''' 
📌 Complessità: 
'''
# - Il ciclo principale ha O(n) iterazioni e per ogni iterazione cerchiamo il nodo più vicino O(n) → O(n²).

''' 
📌 Conclusione 
'''
# La complessità O(n²) appare quando:
# - Usi due cicli annidati che dipendono dalla dimensione dell'input.
# - Devi confrontare tutti gli elementi con tutti gli altri (es. selezione di coppie).
# - Hai algoritmi di ordinamento semplici come Bubble Sort, Selection Sort e Insertion Sort.
# - Fai operazioni su strutture bidimensionali come matrici.
#
# Per ridurre la complessità quadratica, puoi spesso trovare algoritmi più efficienti,
# come QuickSort (O(n log n)) o Algoritmi Greedy e Programmazione Dinamica.


#############################################################################################################
''' 
Mentre la complessità quadratica: 
'''

''' 
📌 Complessità Quadratica (O(n²)) 
'''

# La complessità quadratica è indicata come O(n²) e significa che il tempo di esecuzione cresce
# proporzionalmente al quadrato della dimensione dell'input.
# Ecco alcuni esempi di algoritmi con complessità O(n²), 
# escludendo il Merge Sort (che ha O(n log n)).

''' 
1️⃣ Bubble Sort 
'''

def bubble_sort(arr):
    # Algoritmo di ordinamento inefficiente che confronta coppie adiacenti
    n = len(arr)
    for i in range(n):  # Ciclo esterno
        for j in range(0, n - i - 1):  # Ciclo interno
            if arr[j] > arr[j + 1]:  # Scambio se necessario
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Esempio di utilizzo
print(bubble_sort([5, 3, 8, 4, 2]))

''' 
📌 Complessità: 
'''
# - Due cicli annidati → O(n²)
# - Peggiore e medio caso: O(n²)
# - Miglior caso: O(n) (se l'array è già ordinato)

''' 
📌 Differenza tra Complessità Quadratica (O(n²)) e Logaritmica (O(log n)) 
'''
# La differenza principale tra O(n²) e O(log n) è il modo in cui il tempo di esecuzione cresce
# con l'aumento dell'input.
#
# - **O(n²)** significa che il tempo di esecuzione aumenta esponenzialmente rispetto all'input.
#   Se l'input diventa 10 volte più grande, il tempo di esecuzione diventa 100 volte più grande.
#
# - **O(log n)** significa che il tempo di esecuzione cresce molto più lentamente.
#   Se l'input raddoppia, il numero di operazioni aggiuntive è solo un piccolo incremento.
#
# **Perché O(log n) è più efficiente?**
# - Algoritmi con complessità **logaritmica** riducono il problema in sottoproblemi sempre più piccoli.
# - L'esempio più comune è la **Ricerca Binaria**, che dimezza l'input ad ogni passo, risultando molto veloce.
# - Un altro esempio è **QuickSort**, che ha complessità O(n log n) nel caso medio.
#
# **Esempio di Ricerca Binaria (O(log n))**:
#
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
#
# **Conclusione:**
# - Se possibile, è sempre meglio usare algoritmi **logaritmici** o **O(n log n)** invece di O(n²).
# - Per grandi dataset, un algoritmo logaritmico sarà **migliaia di volte più veloce** rispetto a uno quadratico.

''' 
🚀 Ora hai una panoramica sulla differenza tra O(n²) e O(log n)! 
'''



