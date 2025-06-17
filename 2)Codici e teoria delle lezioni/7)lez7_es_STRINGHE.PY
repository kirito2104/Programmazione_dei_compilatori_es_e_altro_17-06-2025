
#TRASFORMA LE MINUSCOLE IN MAISCOLE
# CI SONO DIVERSI MODI:

# FACENDO COSI' C'ERCHERO' DI MODIFICARE LA STRINGA CON UNA ' P ' MAISCOLA , MA NON E' MOLTO EFFICENTE siccome no posso modificare i caratteri
# e quindi non si potranno sostituire 
 
'''A = 'PROGRAMMAZIONE ' '''
'''A[0] = 'p' ''' # le stringe sono immutabili 

'''print('Ecco la sctringa modificata :',A)'''


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Ci sono diversi modi modi pero' per modificarla una stringa : 

# 1) E' QUELLO DI CREARE UNA NUOVA VARIABILE PER POI SCEGLIERE CHE ELEMENTO MOFICARE, AD ES COME QUI SOTTO:


# Assegna una stringa alla variabile `A`
A = 'programmaz'  # `A` contiene il valore 'programmaz'

# Crea una nuova stringa `l` sostituendo il primo carattere di `A` con 'P'
# Operazione:
# - `A[1:]` seleziona tutti i caratteri di `A` a partire dall'indice 1 fino alla fine.
#   - In questo caso, `A[1:]` è 'rogrammaz'.
# - `'P' + A[1:]` concatena il carattere 'P' con 'rogrammaz', creando la nuova stringa 'Programmaz'.

l = 'P' + A[1:]  # La stringa originale `A` non viene modificata.

# Stampa la nuova stringa `l`
print(l)  # Output: 'Programmaz'



'''FACENDO COSI SI COPIERA' UNA STRINGA CHE A SUA VOLTA SARA MODIFICANDOLA E CREANDONE COSI' UNA NUOVA '''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FACENDO COME QUI SOTTO ASSEGNERO LE DUE CIFRE, ALLA CORSPONDEZA DI ORDINE DELLE VARIABILI A, B ,C 

A , B , C = 1, 32 ,4 

# NATURALMENTE SE E' ASEGNATA UNA C DEVE AVERE IL SUO VALORE ANCHE ESSA, E SE NON C'E'  ' C ' NON CI DEVE ESSERE UNA TRAZA CIFRA 

# PERO' METTENDO UNA SINGOLA VARIABILE, SI POTRANNO INSERIRE PIU VARIABILI 
 

T = 12,32 , 1 , 3 , 5 # facendo cosi' sara' una tupla, si possono anche non mettere le parentesi 

print(T)

print(type(T)) #trpe leggera' che il tipo di 'T' e una tupla 

# UNA TUPLA E' UNA SEQUENZA DI OGGETTI, ELEMNTI DI QUALSIASI TIPO 

# SI POSSONO USARE ANCHE LE PARENTESI :


Y = (0, 'T ' , 5 ,(1,3,4),3.2)
print(Y)

# IN UNA TUPLA SI POTRENNO USARE DIVERSI TIPI COME I CARATTERI, I FLOAT E ANCHE I VALORI BOOLEANI 

# QUASI TUTTE LE OP. CON LE TUPLE SONO SIMILI ALLE STINGHE 


''' SI PUO OTTENERE ANCHE LA LUNGHEZZA DI ESSA CON 'LEN '''


print(len(Y)) # dira' la sua lunghezza ossia 5 


print(Y[2])#stampera' solo l'elemento 2 della stringa 

print(Y[:: -1 ]) # lo slising creara' una copia 

print (2*Y) # si potranno moltiplicare le tuple 

# si potranno anche concatenare piu' tuple 
# come qui sotto : 

print(Y+(1,2))

# si puo' iterare sulla tupla, come qui sotto 

for x in Y : 
    print(x)

# non si potra' pero' modificare una tupla perche' e' imutabile 



''' LE STRINGHE SONO IMMUTABILI '''
# T [1] = 0  # NON SI PUO' FARE 




T = ('A', ' AF', 'C')

X,R,E = T 


# FACENDO COME QUI SOPRA ASSEGNERO IL VALORE DELLA TUPLA ALLE VARIABILI SOTTO, IN BASE ALL'ORDINE SPACCHETTA LA TUPLA 


# SI PUO' FARE ANCHE COSI' 

T = ('A', ' AF', 'C')

'''T = C, F , B '''

# IN UNA TUPLA NON SI POTRA' NE MODIFICARE, NE CACCELLARE UN ELEMNTO IN ESSA 
# UNA VOLTA CHE E' DEFINITA RIMANE COSI' 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Inizializza due variabili `A` e `B` con i valori 1 e 2 rispettivamente
A, B = 1, 2  # `A` = 1 e `B` = 2

# Crea una tupla `T` contenente i valori di `A` e `B`
T = (A, B)  # La tupla `T` contiene i valori `(1, 2)`

# Modifica il valore della variabile `A`, assegnandole il valore 10
# Questo modifica solo il valore di `A`, non la tupla `T`.
A = 10  # Ora `A` = 10, ma `T` resta invariata perché le tuple sono immutabili.

# Stampa la tupla `T`
print(T)  # Output: `(1, 2)` perché la tupla conserva i valori originali di `A` e `B` al momento della sua creazione


''' QUINDI FACENDO COSI' NON ANDRA' A MODIFICARE LA TUPLA MA SOLO A CHE SARA' , MUTATA QUAL VOLTA SI STAMPI A '''


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# LE LISTE A CONFRONTO CON LE TUPLE SONO MUTABILI ,
'''
- SI PUO :
* MOFICARE 
*AGGIUNGERE
*ELIMINARE 

'''

# UNA LISTA SI RICONOSCE TRA LE PARENTESI [ ]
# UNA LISTA PUO CONTENERE PIU' COSE COME: 


F = ['E', 4.3, 3 ,True , ('A', ' AF', 'C')]

# LEN , INDICIZZAZIONE , SLICING , ITERAZIONE , CONCATENAZIONE , RIPETIZIONE , SPACCHETTAMENTO 
# TUTTO CIO' ELENCATO SI PUO' FARE IN UNA LISTA 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

''' SONO MUTABILI, AD ES: COME QUI SOTTO '''


A = [ 0 , 'STRINGA ', ('D,',4)]

A [0] = '123'
print(A)

# si possono anche cancellare con la funzione qui sotto, che si puo' decide cosa eliminare o lasciare del che pulira' l'intera lista 


del (A[1]) # modifica la lista e cancella l'elemento 1 
print(A)

print(A,'ecco quanto e lungo: ', len(A)) # facendo cosi' misura la quanto e' grande Len 


# la funzione len invece gli si possono passare qualsiasi sequenza e mi tira fuori la lunghezza e il numero di qualsiasi elemento 
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#MENTRE PER AGGIUNGERE UN ELEMENTO IN UNA LISTA USO :

# per aggiungere in coda alla liste , quindi alla fine usiamo il metodo " APPEND "
# ps: il metodo e'; diverso dalla funzione perche' e' applicato ad un input di un tipo determinato 

# LA FUNZIONE " APPEND " INVECE SI APPLICA SOLO ALLE LISTE, (e un operazione che modifica la lista) 
# E' UNA FUNZIONE SPECIFICA DELLE LISTE E DELLA SUA STRUTTURA 

x = []

x.append(100) #PER RICHIAMARE UN METODO USIAMO IL NOME DELLA VARIABILE ALLA QUALE VOGLIAMO ACCODARE UN ELEMENTO E' METTIAMO IL METODO APPEND 
# DOVE DECIDEREMO CHE COSA ACCODARE ALLA LISTA 

x.append('t') # aggiungo un elemento alla lista  

print('ECCO X :',x)

'''

x = x.append(0) #facendo cosi' non restituisce nulla, e quindidara' come risultato None 

print(a) # RITORNA NONE 

'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------
# Metodi delle Liste in Python: Guida Completa
# ----------------------------------------------

# 1. append(item)
# Aggiunge un elemento alla fine della lista.
# Esempio:
# lista = [1, 2, 3]
# lista.append(4)  # Lista diventa [1, 2, 3, 4]

# 2. extend(iterable)
# Estende la lista aggiungendo tutti gli elementi di un iterabile (ad esempio, un'altra lista, una stringa).
# Esempio:
# lista = [1, 2, 3]
# lista.extend([4, 5])  # Lista diventa [1, 2, 3, 4, 5]

# 3. insert(index, item)
# Inserisce un elemento nella lista in una posizione specifica.
# Esempio:
# lista = [1, 2, 3]
# lista.insert(1, 10)  # Lista diventa [1, 10, 2, 3]

# 4. remove(item)
# Rimuove il primo elemento della lista con il valore specificato.
# Genera un errore se l'elemento non è presente.
# Esempio:
# lista = [1, 2, 3, 2]
# lista.remove(2)  # Lista diventa [1, 3, 2]

# 5. pop(index=-1)
# Rimuove e restituisce l'elemento nella posizione specificata (di default l'ultimo elemento).
# Esempio:
# lista = [1, 2, 3]
# elemento = lista.pop()  # Lista diventa [1, 2], elemento = 3

# 6. clear()
# Rimuove tutti gli elementi dalla lista.
# Esempio:
# lista = [1, 2, 3]
# lista.clear()  # Lista diventa []

# 7. index(item, start=0, end=len(lista))
# Restituisce l'indice del primo elemento con il valore specificato.
# Genera un errore se l'elemento non è presente.
# Esempio:
# lista = [1, 2, 3, 2]
# indice = lista.index(2)  # indice = 1

# 8. count(item)
# Restituisce il numero di occorrenze di un elemento nella lista.
# Esempio:
# lista = [1, 2, 3, 2]
# occorrenze = lista.count(2)  # occorrenze = 2

# 9. sort(key=None, reverse=False)
# Ordina la lista in ordine crescente (modificabile con `key` e `reverse`).
# Esempio:
# lista = [3, 1, 2]
# lista.sort()  # Lista diventa [1, 2, 3]
# lista.sort(reverse=True)  # Lista diventa [3, 2, 1]

# 10. reverse()
# Inverte l'ordine degli elementi nella lista.
# Esempio:
# lista = [1, 2, 3]
# lista.reverse()  # Lista diventa [3, 2, 1]

# 11. copy()
# Restituisce una copia superficiale della lista.
# Esempio:
# lista = [1, 2, 3]
# copia_lista = lista.copy()  # copia_lista = [1, 2, 3]

# ----------------------------------------------
# Altri Operatori Utilizzabili con Liste
# ----------------------------------------------

# 12. Concatenazione (+)
# Combina due liste in una nuova lista.
# Esempio:
# lista1 = [1, 2]
# lista2 = [3, 4]
# nuova_lista = lista1 + lista2  # nuova_lista = [1, 2, 3, 4]

# 13. Ripetizione (*)
# Ripete la lista un certo numero di volte.
# Esempio:
# lista = [1, 2]
# lista_ripetuta = lista * 3  # lista_ripetuta = [1, 2, 1, 2, 1, 2]

# 14. Controllo di Appartenenza (in e not in)
# Verifica se un elemento è presente o meno nella lista.
# Esempio:
# lista = [1, 2, 3]
# print(2 in lista)  # Output: True
# print(4 not in lista)  # Output: True

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# ------------------------------------------------------
# Differenze tra Liste e Tuple in Python
# ------------------------------------------------------

# 1. **Mutabilità**
# - Lista: Mutabile. Può essere modificata dopo la sua creazione (aggiungere, rimuovere o cambiare elementi).
#   Esempio:
#   lista = [1, 2, 3]
#   lista[0] = 10  # Modifica un elemento
#   lista.append(4)  # Aggiunge un nuovo elemento
#   print(lista)  # Output: [10, 2, 3, 4]
# 
# - Tupla: Immutabile. Non può essere modificata dopo la sua creazione.
#   Esempio:
#   tupla = (1, 2, 3)
#   # tupla[0] = 10  # Errore: le tuple non possono essere modificate
#   print(tupla)  # Output: (1, 2, 3)

# ------------------------------------------------------

# 2. **Sintassi**
# - Lista: Utilizza parentesi quadre [ ].
#   Esempio:
#   lista = [1, 2, 3]
# - Tupla: Utilizza parentesi tonde ( ).
#   Esempio:
#   tupla = (1, 2, 3)

# ------------------------------------------------------

# 3. **Prestazioni**
# - Lista: Più lenta delle tuple, perché supporta operazioni di modifica (append, remove).
# - Tupla: Più veloce delle liste, perché è immutabile e quindi ottimizzata per operazioni fisse.

# ------------------------------------------------------

# 4. **Uso Tipico**
# - Lista: Utilizzata quando i dati possono cambiare nel tempo (raccolta dinamica di elementi).
#   Esempio:
#   lista = ["mela", "banana", "arancia"]
#   lista.append("kiwi")  # Aggiunge un elemento
#   print(lista)  # Output: ["mela", "banana", "arancia", "kiwi"]
# 
# - Tupla: Utilizzata per rappresentare dati fissi, come coordinate o costanti.
#   Esempio:
#   tupla = (10, 20, 30)  # Coordinate immutabili
#   print(tupla)  # Output: (10, 20, 30)

# ------------------------------------------------------

# 5. **Operazioni Comuni**
# Sia le liste che le tuple supportano alcune operazioni comuni:
# - Indicizzazione:
#   lista = [1, 2, 3]
#   tupla = (1, 2, 3)
#   print(lista[0])  # Output: 1
#   print(tupla[0])  # Output: 1
#
# - Iterazione:
#   for x in lista:
#       print(x)
#   for x in tupla:
#       print(x)
#
# - Lunghezza:
#   print(len(lista))  # Output: 3
#   print(len(tupla))  # Output: 3

# ------------------------------------------------------

# 6. **Dimensione in Memoria**
# - Lista: Occupa più spazio in memoria perché include dati per supportare la mutabilità.
# - Tupla: Occupa meno memoria rispetto alle liste.

# ------------------------------------------------------

# 7. **Hashability**
# - Lista: Non hashabile, perché mutabile. Non può essere usata come chiave in un dizionario.
#   Esempio:
#   dizionario = {}
#   # dizionario[[1, 2, 3]] = "valore"  # Errore: le liste non sono hashabili
#
# - Tupla: Hashabile, se contiene solo elementi immutabili. Può essere usata come chiave in un dizionario.
#   Esempio:
#   dizionario = {}
#   dizionario[(1, 2, 3)] = "valore"
#   print(dizionario)  # Output: {(1, 2, 3): "valore"}

# ------------------------------------------------------

# 8. **Quando Usare Liste o Tuple**
# - Usa una lista se:
#   - Hai bisogno di aggiungere, rimuovere o modificare elementi.
#   - La raccolta di dati cambierà nel tempo.
# - Usa una tupla se:
#   - I dati sono immutabili e non devono cambiare.
#   - Vuoi migliorare le prestazioni.
#   - I dati devono essere hashabili (ad esempio, per usarli come chiave in un dizionario).

# ------------------------------------------------------

# **Tabella Riassuntiva**

# | Caratteristica       | Lista           | Tupla           |
# |----------------------|-----------------|-----------------|
# | **Mutabilità**       | Mutabile        | Immutabile      |
# | **Sintassi**         | `[ ]`           | `( )`           |
# | **Prestazioni**      | Più lenta       | Più veloce      |
# | **Hashability**      | No              | Sì (se contiene solo elementi immutabili) |
# | **Dimensione memoria** | Maggiore      | Minore          |
# | **Uso**              | Dati dinamici   | Dati fissi      |

# ------------------------------------------------------





















































