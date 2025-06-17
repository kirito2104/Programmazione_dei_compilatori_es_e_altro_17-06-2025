
'''La funzione zip(). 
I medoti keys(), values(), items() e get() della struttura dict.
Il problema dell'intersezione tra insiemi: approfondimenti sulla complessità.
'''

nomi = ['A','B','A','C','B','D','A','C']
pos = [  3 , 1 , 9,  0, 10 , 2,  4 , 2  ]

# al tempo i pos[i] e' la nuova posizione di nomi[i] 

# sono una serie di dati determinati in un tempo 

# quale e' l'ultima configurazione dei punti,
# Oveero la posizione dei alla fine della serie temporale 

# si vuole un algoritmo efficiente che mappi la posizione di ogni punto data dal valore di quel punto 

# d[k] = p se il punto k si trova in posizione p 

n = len(nomi)  
d = {}

'''for i in range(n):
    d[nomi[i]== pos[i]]
'''
# complessita'  temporale : O(n) medio 

# 


#------======================================================================================================================

''' Seconda versione :'''

# Lista dei nomi dei punti.
nomi = ['A', 'B', 'A', 'C', 'B', 'D', 'A', 'C']

# Lista delle posizioni associate ai punti in un dato momento.
pos = [3, 1, 9, 0, 10, 2, 4, 2]

# Ogni elemento di 'nomi' corrisponde a un elemento di 'pos' nello stesso indice.
# Ad esempio, nomi[0] = 'A' si trova inizialmente in pos[0] = 3.

# Questi dati rappresentano una serie temporale che indica le posizioni dei punti
# in vari momenti del tempo.

# Obiettivo:
# Determinare l'ultima posizione di ciascun punto dopo tutti i cambiamenti.
# Questo significa che vogliamo mappare ogni punto (nome) alla sua posizione finale.

# Vogliamo un dizionario 'd' che rappresenti questa relazione:
# d[k] = p, dove 'k' è il nome del punto e 'p' è la sua posizione finale.

# Determiniamo la lunghezza della lista 'nomi', ovvero il numero totale di dati.
n = len(nomi)

# Creiamo un dizionario vuoto per mappare i punti alle loro posizioni finali.
d = {}

# Iteriamo attraverso tutti i dati per aggiornare il dizionario con le posizioni finali.
for i in range(n):  # Complessità temporale O(n), poiché iteriamo su 'n' elementi.
    d[nomi[i]] = pos[i]  # Aggiorniamo la posizione del punto 'nomi[i]' con 'pos[i]'.

# Alla fine, il dizionario 'd' conterrà l'ultima posizione registrata per ciascun punto.
# Ad esempio, se l'ultimo valore di 'A' in 'nomi' è associato a 4 in 'pos',
# allora d['A'] = 4.

# Complessità temporale:
# - O(n) per iterare su tutti gli elementi di 'nomi' e 'pos'.

# Risultato atteso del dizionario 'd':
# d = {'A': 4, 'B': 10, 'C': 2, 'D': 2}


######################################################################################################################################################################
#################################################################################################################################################################################################################
''' CHE COS'E' UN ITERAZIONE? '''

#Un **iterabile** in Python è un oggetto che può essere percorso elemento per elemento,
# come liste, tuple, dizionari, set e stringhe. 
# Questi oggetti permettono l'iterazione utilizzando un ciclo `for` grazie al metodo `__iter__()`,
# che restituisce un iteratore.
# L'iteratore gestisce il processo di attraversamento degli elementi dell'iterabile,
# avanzando con il metodo `__next__()` e segnalando la fine dell'iterazione tramite 
# un'eccezione `StopIteration` quando tutti gli elementi sono stati esauriti.




##########################################################################################################################################
################################################################################################################################

'''
La funzione  'ZIP':
tale funzione prende in input un numero arbitario di iterabile ( ossia qualcosa su cui posso iterare ) 
la funzione zip si occupa di far ritornare ad ogni iterazione la prima volta il primo elemento, poi secondo , poi il terzo fino ad
esaurimento , crea una sequenza iterna composta dalla stessa posizione degli iterabili dellinput

'''

nomi = ['A', 'B', 'A', 'C', 'B', 'D', 'A', 'C']

# Lista delle posizioni associate ai punti in un dato momento.
pos = [3, 1, 9, 0, 10, 2, 4, 2]

d = {}  # Inizializza un dizionario vuoto, potenzialmente per uso futuro

# Il ciclo for itera contemporaneamente sugli iterabili 'nomi' e 'pos'
for nome, p in zip(nomi, pos):
    # Stampa ogni coppia di elementi corrispondenti da 'nomi' e 'pos'
    print(nome, p)

#Creazione del dizionario: Viene creato un dizionario vuoto d, 
# che si presuppone verrà utilizzato in seguito, 
# anche se non è mostrato nel frammento di codice fornito.

#Iterazione con zip(): Il ciclo for utilizza la funzione zip(nomi, pos)
# per combinare elementi corrispondenti dei due iterabili nomi e pos.
# In ogni iterazione del ciclo, zip() restituisce una tupla con un elemento da nomi e uno da pos.

#Stampa dei risultati: All'interno del ciclo, ogni coppia di elementi (nome, p) viene stampata.
# Questo mostra l'accoppiamento degli elementi come risultato dell'aggregazione fatta da zip().




'''
La funzione zip() in Python è utilizzata per aggregare elementi da due o più iterabili
(liste, tuple, stringhe, etc.), creando un nuovo iteratore di tuple. Ogni tuple generata da zip()
contiene elementi presi dalla stessa posizione in ciascun iterabile di input.
L'iterazione termina quando l'iterabile più corto è esaurito, il che significa che zip()
allinea la lunghezza dell'iteratore risultante alla lunghezza del più corto degli iterabili di input.
'''


#La funzione `zip()` in Python prende in input uno o più iterabili 
# (come liste, tuple, o stringhe) e restituisce un iteratore che produce tuple. 
# Ogni tupla contiene elementi dalle stesse posizioni corrispondenti di ciascun iterabile input.
# L'iterazione con `zip()` termina non appena l'iterabile più corto tra quelli forniti è esaurito.

#Quando si usa `zip()` :
# in un ciclo `for`, si itera su questi elementi accoppiati,
# eseguendo il blocco di codice del `for` per ogni coppia prodotta da `zip()`.
# Questo consente di lavorare facilmente con dati correlati da più sorgenti, in modo sincronizzato e ordinato.


'''
##############################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################
'''


nomi = ['A', 'B', 'A', 'C', 'B', 'D', 'A', 'C']

# Lista delle posizioni associate ai punti in un dato momento.
pos = [3, 1, 9, 0, 10, 2, 4, 2]

d = {}  # Inizializza un dizionario vuoto, potenzialmente per uso futuro

# Il ciclo for itera contemporaneamente sugli iterabili 'nomi' e 'pos'
for nome, p in zip(nomi, pos):
    d[nome]=p
    # Stampa ogni coppia di elementi corrispondenti da 'nomi' e 'pos'
    print(nome, p)

'''
Nel caso in cui le liste non avessero la stessa dimensione, si ferma appena finisce la lista nomi o vice versa
'''

##############################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################

# Lista delle posizioni associate ai punti in un dato momento.
pos = [3, 1, 9, 0, 10, 2, 4, 2]

# Inizializza un dizionario vuoto, potenzialmente per uso futuro
d = {}

# Il ciclo for itera contemporaneamente sugli iterabili 'nomi' e 'pos'
for nome, p in zip(nomi, pos):
    # Assegna ogni posizione p dalla lista 'pos' al corrispondente nome in 'nomi'
    # e salva la coppia nel dizionario 'd'
    d[nome] = p

# A questo punto, 'd' contiene una mappa di nomi a posizioni, dove ogni chiave è un nome
# e ogni valore è la posizione corrispondente presa dalla lista 'pos'

'''
##############################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################
'''

# i metodi dei dizionari :

# il metodo keys

print(d.keys()) # restituisce una struttura dati che contiene la sequenza di tutte le chiavi 

# e restiruisce : dict_keys(['A', 'B', 'C', 'D'])


# il metodo values : 

print(d.values()) #che permette di far tornare tutti i valori 

# e restituisce : dict_values([4, 10, 2, 2])

#il metodo items:

print(d.items()) # che fa tornare una sequenza di coppie ossia chiave e valore 

# e restituisce le coppie del dizionario: dict_items([('A', 4), ('B', 10), ('C', 2), ('D', 2)])

'''
##############################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################
'''
nomi = ['A', 'B', 'A', 'C', 'B', 'D', 'A', 'C']
# Lista delle posizioni associate ai punti in un dato momento.
pos = [3, 1, 9, 0, 2, 2, 4, 2]

# Inizializza un dizionario vuoto, potenzialmente per uso futuro
d = {}

# Il ciclo for itera contemporaneamente sugli iterabili 'nomi' e 'pos'
for nome, p in zip(nomi, pos):
    # Assegna ogni posizione p dalla lista 'pos' al corrispondente nome in 'nomi'
    # e salva la coppia nel dizionario 'd'
    '''# d [nome] = [lista dei posizioni occupate da nome ]'''
    if nome in d :
        d[nome].append(p)
    d[nome] = p
else:
    d[nome]= [p]
print(d)

# nomi e pos : diventeranno quindi a far parte del dizionario : 

d={'A': 4, 'B': 10, 'C': 2, 'D': 2}






































