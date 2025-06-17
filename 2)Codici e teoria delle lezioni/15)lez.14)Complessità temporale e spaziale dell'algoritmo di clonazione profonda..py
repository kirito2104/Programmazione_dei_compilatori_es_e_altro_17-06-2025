
# Complessità temporale e spaziale dell'algoritmo di clonazione profonda.

# una copia profonda copia pure le sotto liste annidate in una lista 


def deep_copy(a): 
    '''
    Funzione per creare una copia profonda (deep copy) di una lista che può contenere elementi semplici 
    (numeri, stringhe, ecc.) o altre liste annidate.
    
    Parametri:
    - a: Lista da copiare profondamente.
    
    Restituisce:
    - Una nuova lista `b` che contiene una copia profonda di `a`.
    '''
    
    b = []  # Inizializziamo una lista vuota `b` dove inseriremo gli elementi copiati da `a`.

    for e in a:  # Iteriamo attraverso ogni elemento `e` della lista `a`.
        if type(e) != list:  # Controllo se `e` NON è una lista.
            # Se `e` non è una lista (ad esempio un numero, stringa, ecc.), lo aggiungiamo direttamente a `b`.
            b.append(e)  # Aggiungiamo `e` alla lista `b`.
        else:
            # Se `e` è una lista, richiamiamo ricorsivamente la funzione `deep_copy` su `e`.
            # Questo permette di gestire anche liste annidate (es. [[1, 2], [3, [4, 5]]]).
            b.append(deep_copy(e))  # Aggiungiamo il risultato della copia profonda di `e` a `b`.
    
    return b  # Restituiamo la lista `b`, che è una copia profonda di `a`.


a = ['pythonm', [1, 3.14, '2.71'], 100, ['programmazione', 'python']]  # Lista con elementi misti
b = deep_copy(a)  # Creiamo una copia profonda di `a`.

# `b` ora contiene una copia profonda di `a`, quindi eventuali modifiche a `b` non influenzeranno `a`.


# complessita' temporale , dell'input e' 
#
# la grandezza di a che contiene n elementi  se prendo la lunghezza di a di a e' 1, ma inrealta' quella lista contiene n elementi  
#
# la dimensione dell'input e' data  dal numero degli elementi scalari in 'a' ed in tutte le sotto liste annidate 
#
# t(n) =  a tutti glia ppartenenti alla lista : T(n**e) ossia il costo di clonazione, di ogni elemento appartenete alla lista
#
#   a :  per ogni elemento di a -> eseguiamo un append (il costo dell'append e' costante O(1)c )
#                               oppure -> usiamo un append della funzione  (depp.copy) ( il costo del append e'T(n**1))


# dove n e  e'il num di elementi in e  in e ed in tutte le liste 
#
# oppure e'1 nel caso in cui n non e'una lista 

'''Grazie per la correzione ulteriore. Ecco la trascrizione aggiornata correttamente:

∑ n**e=N
quindi sara'n perche' sono la somma delle le scansioni che esegue in una lista che e'n 



parentesi quadre rappresentanti 
liste o sotto-liste con una nota che indica "n" sotto un gruppo di queste liste,
che rappresenta la lunghezza totale delle liste quando sommate insieme.

∀ e ∈ Q", che indica che ogni elemento "e" appartiene all'insieme Q.
'''

#T(n) = T(n_3) + T(n_2) + T(n_1) + T(n_4)
#
#     = 1 + 1 + T(m_1) + T(m_4)=
#       T(m_1)    T(m_4)
#       /   \      /   \
#      T() T()    T() T()
#      1    1     1    1
# alla fine arrivero'a degli elementi scalari, e quindi non potro'piu'andare avanti 
# al livello piu'basso avro'1 perche'ho raggiunto tutti i valori scalari , quindi alla fine avro'tutti e quindi  staro sommando tutti gli elementi di 1 e gli 1 sommati saranno 
# ed e quindi ∑ 1 = n  T(n) O(n)
# sommo gli uno quando non trovo una lista , mentre se 



# Quindi la complessita' temporale :T(n) e'linera in n 
# Complessita'spaziale : (non va considerato l' output) bisogna valutare lo spazio aggiuntivo che crea la funzione 
#
# usa molta memoria suplementare perche' ogni frame che cresce in maniera dipendenete dall'ínput  
# quindi il numero'di frame annidati al massimo di frame che fanno parte della pila e'dato dal massimo annidamento delle lista allínterno della lista principale 
# ci sono n freme , ci sono quando n liste annidate e ogni sotto lista contiene esattamente un elemento 
# quindi nel caso peggiore avro n liste annidate in altre liste 

#complessita'spazziale : nel caso peggiore il costo sara' lineare O(n)




'''# Definizione del problema'''
# Supponiamo di avere una lista 'a' di lunghezza 'n', dove ciascun elemento 'e' può essere:
# - Un elemento semplice (es. un numero o una stringa).
# - Un'altra lista (annidata) di lunghezza arbitraria.

'''# Costo per ogni elemento'''
# Per ogni elemento 'e' in 'a', la funzione controlla:
# - Se non è una lista: Il costo è costante O(1), perché si aggiunge direttamente l'elemento a 'b'.
# - Se è una lista: La funzione richiama sé stessa in modo ricorsivo, il che aggiunge un costo T(m'), dove m' è la lunghezza della sotto-lista.

'''# Costo complessivo'''
# La complessità T(n) dipende dal fatto che ogni chiamata ricorsiva esegue un'operazione per ogni elemento della lista corrente.
# Se la lista è completamente piatta (nessuna annidazione), il costo è O(n).
# Tuttavia, se ci sono liste annidate, la ricorsione può aggiungere livelli di complessità.

'''# Struttura della ricorrenza'''
# Per ogni elemento:
# T(n) = O(1) + sum(T(m') for each sublist m')

'''# Caso peggiore'''
# Se la lista è profondamente annidata (ogni elemento è una lista di un solo elemento), la ricorsione attraversa n livelli.
# Questo porta a una complessità lineare nella profondità della ricorsione:
# T(n) = O(n) per ogni livello, ma può essere ricorsivo fino a O(n^1).

'''# Perché T(n^1)?'''
# Nel caso generale, la funzione esplora tutti gli elementi della lista, inclusi quelli delle sotto-liste.
# Ogni elemento comporta:
# - Un'operazione di copia diretta (O(1)).
# - Una chiamata ricorsiva nel caso di sotto-liste, che aggiunge un livello.
# Se la lista è annidata fino alla profondità n, il costo totale diventa proporzionale al numero di livelli, cioè T(n^1).

'''# Sintesi'''
# Il costo T(n^1) rappresenta un caso lineare con profondità massima, dove ogni elemento viene visitato una sola volta, anche se ci sono annidamenti.
# Se la profondità di annidamento aumenta, il costo può crescere con la dimensione totale della struttura.


#=========================================================================================================================================================================================================================================

''' Es per cas '''

'''
facendo come qui sotto ci saranno dei problemi logici
'''


# data una lista di numeri ordinati in modo non decrescente ed un numero k

#trovare la posizione dell' occorenza  piu'a destra di k in a : nellésempio 
#l' algoritmo ritorna 5 
# se k non e in a, ritorna -1

'''def trova_el_destra(a, k):
    lx, rx = 0, len(a) - 1  # lx è l'indice dell'estremo sinistro, rx è l'indice dell'estremo destro dell'array

    # lx sarà l'indice del primo elemento dell'array, 
    # rx sarà l'indice dell'ultimo elemento dell'array
    
    while lx <= rx:  # Continua la ricerca finché lx è minore o uguale a rx
        cx = (lx + rx) // 2  # Calcola l'indice mediano dell'array. Utilizza la divisione intera per ottenere un indice intero

        # Se il valore cercato k è maggiore dell'elemento nell'indice mediano cx,
        # significa che l'elemento deve trovarsi nella metà superiore dell'array
        
        if k > a[cx]:  
            rx = cx - 1  # Aggiorna rx per restringere la ricerca alla metà inferiore escludendo cx
            
        elif k == a[cx] and a[cx+1] > k : # il problema potrebbe essere a[cx+1] perche'non sono sicuro che sia legale, 
            #perche' puo' succedere che sia uguale ad rx, e quindi cx+1 sfora
             
            return cx'''
    
  
    # Problemi nel Codice
# Gestione del Caso k > a[cx]:
# rx = cx - 1: Qui c'è un errore comune nella ricerca binaria. Se l'elemento che stiamo cercando, k, è maggiore dell'elemento all'indice mediano cx,
# dovremmo escludere la metà inferiore dell'array fino all'indice cx incluso. Quindi, dovremmo aggiornare l'indice di inizio della ricerca lx a cx + 1
# per continuare la ricerca nella metà superiore dell'array.
# Invece, nel codice che hai fornito, viene aggiornato rx, che è l'indice finale, riducendo erroneamente la ricerca alla parte inferiore anziché spostarsi verso 
# la parte superiore dove k potrebbe effettivamente trovarsi.

# Controllo dell'Elemento Successivo senza Verifica di Indice:
# elif k == a[cx] and a[cx+1] > k: Questa linea di codice può causare un errore di indice se cx si trova all'ultimo elemento dell'array. Accedere a a[cx+1] 
# senza prima verificare se cx+1 esiste nell'array (cx+1 < len(a)) può sollevare un'eccezione IndexError per tentativo di accesso fuori dai limiti dell'array.
# Inoltre, questa condizione cerca di identificare se l'elemento cx è l'ultimo elemento uguale a k nell'array. Tuttavia, senza la verifica appropriata, si rischia
# di saltare elementi o interrompere la ricerca prematuramente se la condizione non viene gestita correttamente.

# Soluzioni
# Correzione dell'Aggiornamento dell'Indice:
# Modifica rx = cx - 1 in lx = cx + 1 quando k > a[cx] per spostare correttamente la ricerca nella metà superiore dell'array.

# Aggiunta di Controlli di Sicurezza per l'Indice:
# Prima di accedere a a[cx+1], assicurati che cx+1 sia un indice valido all'interno dell'array:
# elif k == a[cx] and (cx + 1 < len(a) and a[cx+1] > k):
# Questo evita errori di indice e assicura che la condizione sia verificata solo se esiste un elemento successivo.

# Implementando queste correzioni, il codice diventa più robusto e sicuro, evitando errori comuni di implementazione nella ricerca binaria e garantendo che la ricerca
# dell'elemento k nell'array sia corretta e efficiente.



#trova_el_destra(a,k)
a = [1,5,5,7,7,7,9,9,10,13,13,14,17]
k=7

#=============================================================================================================================================================================================================================================

'''
problema di sopra risolto :

'''


def ricerca_dx(a,k):
    lx, rx = 0, len(a) - 1  # lx è l'indice dell'estremo sinistro, rx è l'indice dell'estremo destro dell'array
    n = len(a)
    # lx sarà l'indice del primo elemento dell'array, 
    # rx sarà l'indice dell'ultimo elemento dell'array
    while lx <= rx:  # Continua la ricerca finché lx è minore o uguale a rx
        # se nega tale condizione restituisce -1 
        
        cx =int((lx + rx)/2)  # Calcola l'indice mediano dell'array. Utilizza la divisione intera per ottenere un indice intero

        # Se il valore cercato k è maggiore dell'elemento nell'indice mediano cx,
        # significa che l'elemento deve trovarsi nella metà superiore dell'array
            
        if k < a[cx]:   
            rx = cx - 1  # Aggiorna rx per restringere la ricerca alla metà inferiore escludendo cx
            # Questo passo esclude la metà superiore dell'array poiché k è minore dell'elemento a cx.
                
        elif k == a[cx] and (cx == n - 1 or a[cx+1] > k): 
            # Questo blocco verifica se l'elemento corrente a[cx] è l'ultimo elemento uguale a k.
            # cx == len(a) - 1 controlla se cx è l'ultimo indice dell'array, quindi non ci sono elementi dopo di esso.
            # a[cx+1] > k controlla se l'elemento successivo è maggiore di k, il che significherebbe che a[cx] è l'ultimo k.
            # È importante controllare che cx + 1 non ecceda len(a) - 1 per evitare IndexError.
            return cx  # Restituisce cx se è l'ultimo elemento uguale a k

        else:
            lx = cx +1 #perche andrermo a destra di cx 
    return -1


a = [1,5,5,7,7,7,9,9,10,13,13,14,17]
k=9

print(ricerca_dx(a,k))

#  la complessita' temporale e' O(NlogN)
# lo comp. spaziale il costo e' 

''' la ricerca sensa ordinamento richiede tempo lineare ''' 
#==========================================================================================================================================================================================================================================================


# Contenuto Trascritto
# 1. O(m * m) perche' ho n ricerche 

# 2. Costo ordine lineare + m log n
# 3. O(n^2) + O(m log m)
# 4. O(m log n + m log m)
# 5. Bubble sort


# |a| = n se lo ordino il costo sara' costo (oridinamento (n)) + m * log N
 


# Spiegazioni
# - O(m * m): Indica una complessità computazionale quadratica, tipicamente associata con algoritmi 
# che devono eseguire operazioni su ogni coppia di elementi in un dataset di dimensione m.
# Potrebbe riferirsi a un'operazione che richiede confronti o calcoli tra tutti gli elementi.

# - Costo ordine lineare + m log n: Questo suggerisce un processo che ha una parte con complessità lineare 
# (probabilmente un passaggio attraverso un dataset) e un'altra parte che coinvolge un algoritmo di
# complessità m log n, come un algoritmo di ordinamento o ricerca logaritmica applicato m volte.

# - O(n^2) + O(m log m): Combina la complessità quadratica, come potrebbe essere trovata in un algoritmo di 
# ordinamento inefficiente o in un'operazione che considera tutte le coppie di n elementi, con un'altra 
# operazione che ordina un set di m elementi con un algoritmo di complessità logaritmica (come mergesort o heapsort).

# - O(m log n + m log m): Suggerisce che ci sono due principali processi computazionali: uno che dipende dalla logaritmica
# di n eseguita m volte, e un altro che dipende dalla logaritmica di m, anch'esso eseguito m volte. Questo potrebbe indicare
# una combinazione di operazioni di ricerca e di ordinamento su diversi set di dati.

# - Bubble sort: Una menzione di un algoritmo di ordinamento specifico noto per la sua semplicità
# ma inefficienza in termini di complessità temporale, che è tipicamente O(n^2) nel caso peggiore.
# per ricercare un valore sara' O(n*2)+ O(m log N )
 






































































