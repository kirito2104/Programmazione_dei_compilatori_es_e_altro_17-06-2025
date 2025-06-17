# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:28:33 2024

@author: gianluca
"""

# Algoritmo di fusione (merge)

# Ordina due sequenze ordinate in un'unica sequenza

a = [0, 5, 8, 10, 11, 11, 14]  # Lista ordinata a
b = [1, 2, 6, 6, 6, 9, 10]     # Lista ordinata b

i, j = 0, 0  # Indici per scorrere le liste a e b
c = []       # Lista risultante unificata

# Ciclo per confrontare gli elementi di a e b e unirli in c
while i < len(a) and j < len(b):
    if a[i] <= b[j]:  # Confronto tra l'elemento corrente di a e b
        c.append(a[i])  # Aggiunge l'elemento di a a c se minore o uguale
        i += 1  # Incrementa l'indice di a
    else:
        c.append(b[j])  # Aggiunge l'elemento di b a c altrimenti
        j += 1  # Incrementa l'indice di b

# Aggiunge gli elementi rimanenti di a, se presenti
while i < len(a):
    c.append(a[i])
    i += 1

# Aggiunge gli elementi rimanenti di b, se presenti
while j < len(b):
    c.append(b[j])
    j += 1

# Complessità temporale: O(n) dove n = len(a) + len(b)
# Complessità spaziale: O(n), per la lista di appoggio c

# Funzione merge con supporto per la funzione `key`
def merge(a, lx, cx, rx, key=lambda x: x):
    '''
    Input:
        a: lista di elementi
        lx, cx, rx: indici che delimitano le due sottosequenze da fondere
        key: funzione per determinare il criterio di ordinamento
    Output:
        None. Effetto collaterale: a[lx:rx] è ordinata
    '''

    i, j = lx, cx  # Indici iniziali per le due sottosequenze
    c = []  # Lista temporanea per l'unione

    # Fusione delle sottosequenze basata su `key`
    while i < cx and j < rx:
        if key(a[i]) <= key(a[j]):  # Confronto basato sul risultato di key()
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1

    # Aggiunta degli elementi rimanenti della prima sottosequenza
    while i < cx:
        c.append(a[i])
        i += 1

    # Aggiunta degli elementi rimanenti della seconda sottosequenza
    while j < rx:
        c.append(a[j])
        j += 1

    # Copia degli elementi ordinati in `c` nella lista originale `a`
    i = lx
    for e in c:
        a[i] = e
        i += 1

# Funzione merge_sort con supporto per `key`
def merge_sort(a, lx=0, rx=None, key=lambda x: x):
    '''
    Input:
        a: lista di elementi da ordinare
        lx: indice sinistro di partenza
        rx: indice destro di fine
        key: funzione per determinare il criterio di ordinamento
    Output:
        None. Effetto collaterale: a è ordinata in loco
    '''
    
    if rx is None:
        rx = len(a)

    if lx + 1 >= rx:  # Caso base: una sola elemento, già ordinato
        return None

    cx = (lx + rx) // 2  # Calcolo della metà per dividere la lista

    # Chiamate ricorsive per ordinare le due metà
    merge_sort(a, lx, cx, key)
    merge_sort(a, cx, rx, key)

    # Fusione delle due metà ordinate
    merge(a, lx, cx, rx, key)

# Esempio di utilizzo con un criterio `key`
a = [10, 21, 30, 34, 34, 38, 11, 13, 16, 17, 19, 0, 0, 10, 10]
merge_sort(a, key=lambda x: x)  # Ordina normalmente
print(a)



#In [lambda fuction ]
v= (lambda x: x**2)(2)
f = lambda x : x


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# In[] una lista che contiene sia liste  che stringhe 

#prima i numeri poi stringhe 


a[10.4,3.14,'programmazione',0, "dei",0 ," calcolatori",8,"2024/2025"]
def f (x):
    if type (x) in (int, float ):
        return 0
    else:
        return 1
    
# merge_sort(a,key = f)
# oppure
    
    
    
#merge_sort(a, key=str)   #uso str che diventa una stinga

merge_sort( a,key = lambda x: 0 if type(x) in (float, int) else 1)

print(a)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# In []

def f (x):
    if type (x) in (int, float):
        return(0, x)
    elif type (x) == str:
        return(1,x)
    
merge_sort(a, key = f)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# In []

a = (10,9,11, 0, 4)

print(sorted(a))

print(sorted('python'))

a = [10.4,3.14,'programmazione',0, "dei",0 ," calcolatori",8,"2024/2025"]

print (sorted(a, key=str))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# In[metodo sort del tipo list]

a = (10,9,11, 0, 4)

a.sort()

#applica un ordinamento in loco, il valore di a viene modificato

a = [10.4,3.14,'programmazione',0, "dei",0 ," calcolatori",8,"2024/2025"]








