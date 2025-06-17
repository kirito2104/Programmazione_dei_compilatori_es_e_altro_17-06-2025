
#Es n.2

#Scrivere una funzione in Python che, date due liste l1e l2 entrambe le ordinate , 
# restituisce una lista che è l'intersezione delle due liste l1e l2. 
# La soluzione deve avere complessità temporale lineare in len(l1) + len(l2), 
# e memoria supplementare costante, possibilmente.

#Nota : considerando le liste come insiemi, ovvero, non ci sono elementi ripetuti.

#Esempio:

#Input:
#l1 =  [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
#l2 =  [1, 3, 4, 6, 7, 10, 13, 22, 23, 24, 25, 26, 45, 69, 99, 121]
#Output:  [1, 3, 6, 7, 22, 23, 45, 99]


def intersezione (L1,L2):
    
    i,j = 0,0 
    
    risultato = []
# scorri contemporaneamente le liste
    while  i < len(L1) and j < len(L2):
         # se i-esimo elemento di l1 e j-esimo
        # elemento di l2 sono uguali, allora
        # tale elemento appartiene alla intersezione
        # delle due liste
        if L1[i]== L2[j] :
            risultato.append(L1[i])
            i += 1
            j += 1
        # se l'i-esimo elemento di l1 è più piccolo
        # del j-esimo elemento di l2, allora, dato che la lista
        # l2 è ordinata, l'elemento i-esimo di l1 non si trova in l2,
        # dunque non fa parte dell'intersezione delle due liste.
        # Avanza l'indice i
        #Nel caso in cui non esita un elemento in l1  che sia  in l2  verra  scritto
        
            ''' 
            Problema risolto :
            
            🔴 Problema 1: Hai ripetuto due volte L1[i] == L2[j], una volta con if, una con elif. Ma se il primo if è falso, 
            il secondo elif sarà sempre falso, perché è lo stesso identico controllo. Questo elif non serve a nulla.

            🔴 Problema 2: Se L1[i] != L2[j], l'else incrementa sempre j, anche se magari dovrebbe essere i.
            Questo rompe l'equilibrio tra le due liste.
            '''
        
    
        elif L1[i] < L2[j] :
            i += 1
        # se il j-esimo elemento di l2 è più piccolo
        # del i-esimo elemento di l1, allora, dato che la lista
        # l1 è ordinata, l'elemento j-esimo di l2 non si trova in l1,
        # dunque non fa parte dell'intersezione delle due liste.
        # Avanza l'indice j.
        else:
            j += 1 # qui incremento l'indice di l2

    return risultato


"""
Complessità temporale: O(n+m), dove n = len(l1) e m = len(l2)
Complessità spaziale: O(1)
"""

'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


    # 🔁 Complessità temporale: O(n + m)
    # - i e j scorrono L1 e L2 una sola volta
    # - ogni iterazione incrementa almeno uno dei due
    # - al max fai n + m confronti (n = len(L1), m = len(L2))
    # - nessun ciclo annidato, nessuna ricerca binaria
    # → scansione lineare pura

    # 🧠 Complessità spaziale: O(1) (extra)
    # - usi solo 3 variabili: i, j, risultato
    # - nessuna struttura ausiliaria tipo set o dict
    # - output escluso dal calcolo → se incluso: O(k), con k = #elementi comuni



#Qui sotto il codice completo:



def intersezione1(L1, L2):
    i, j = 0, 0
    risultato = []

    # scorri contemporaneamente le liste
    while i < len(L1) and j < len(L2):
        # se i-esimo elemento di l1 e j-esimo
        # elemento di l2 sono uguali, allora
        # tale elemento appartiene alla intersezione
        # delle due liste
        if L1[i] == L2[j]:
            risultato.append(L1[i])
            i += 1
            j += 1
        # se l'i-esimo elemento di l1 è più piccolo
        # del j-esimo elemento di l2, allora, dato che la lista
        # l2 è ordinata, l'elemento i-esimo di l1 non si trova in l2,
        # dunque non fa parte dell'intersezione delle due liste.
        # Avanza l'indice i
        elif L1[i] < L2[j]:
            i += 1
        # se il j-esimo elemento di l2 è più piccolo
        # del i-esimo elemento di l1, allora, dato che la lista
        # l1 è ordinata, l'elemento j-esimo di l2 non si trova in l1,
        # dunque non fa parte dell'intersezione delle due liste.
        # Avanza l'indice j.
        else:
            j += 1

    return risultato

    
l1 = [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
l2 = [1, 3, 4, 6, 7, 10, 13, 22, 23, 24, 25, 26, 45, 69, 99, 121]

print("Input:")
print("l1 = ", l1)
print("l2 = ", l2) 
print("Output: ", intersezione1(l1, l2))


'''
#########################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################
'''

# Esercizio n.3 : 

# Scrivere una funzione in Python che implementa l'algoritmo di ricerca binaria destra usando la ricorsione.
# In particolare, data una lista `a` di numeri ordinati in modo non decrescente ed un numero `k`,
# la funzione restituisce la posizione dell'occorrenza più a destra di `k` in `a`.
# Se `k` non è in `a`, ritorna -1.




    



