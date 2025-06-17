'''
KEy e' un elemento che prende in input una lista e ne ritorna il secondo valore rispetto alla posizione 


'''
# In[]

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]
    
    n = len(a)
        
    b = sorted(a, key=t1)  # Tempo O(n log_2 n), 
    #spazio O(n) che' stiamo usando una lista di appoggio e anche perche' criamo una lista di appoggio    
    
    lx, rx = b[0][1], b[-1][1]
    
    # m = rx-lx+1   dimensione dell'output
    
    i = 0 # indice in b del prossimo punto da stampare
    
    for p in range(lx, rx+1):
        if i < n and p == b[i][1]:
            print(b[i][0], end='')
            i += 1
        else:
            print('*', end='')   # O(m)
 
    
     # Complessità: tempo O(n log_2 n + m) nel caso peggiore,
     #        spazio O(n)
    
'''
 
Quindi per ogni possibile valore nell'output, 
bisogna valutare se e' un punto in a oppure e' uno spazio 

''' 
# In[] 

a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]

disegna_punti_su_retta(a)

# In[Intersezione]

a = [9, 2, 1, 8, 4] # insieme
b = [1, 7, 0, 8, 2] # insieme

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]


disegna_punti_su_retta(a)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

''' Dizionario'''

# E' una struttura dati che consente di usare un associazione tra due diversi dati,
# va da un dato: chiamato chiave e valore
# E' una sorta di dominio tra le chiavi e un codominio associate ale chiavi 
# Sono consentite le op di ricerca di una chiave e di aggiornameto e cancellazione 
# Queste operazioni sono molto efficienti posoono essere eseguite in tempo costante o medio 
# permette di velocizzare l'algoritmo

#-------------------------------------------------------------------------------------------
'''
ho due liste le quali hannodue insiemi,quindi da tre coppie di numeri,
bisogna creare una nuova lista che abbia le intersezioni tra di esse
'''
# assumiamo Len(a) == Len(b) al valore n 
a = [9, 2, 1, 8, 4] # insieme
b = [1, 7, 0, 8, 2] # insieme


#un algoritmo che trovi o intersezione b, ossia un altra lista 

# c = [1, 2 , 8 ]

# Inizializziamo una lista vuota per raccogliere gli elementi che soddisfano una certa condizione.
c = []

# Supponiamo di avere due liste: 'a' e 'b'.
# L'obiettivo è iterare su ogni elemento di 'a' e verificare se è presente in 'b'.
for e in a:  # Scorriamo tutti gli elementi della lista 'a'.
    if e in b:  # Per ogni elemento 'e' di 'a', controlliamo se 'e' è presente nella lista 'b'.
        # L'operazione 'e in b' ha un costo O(n), dove n è la lunghezza della lista 'b'.
        c.append(e)  # Se 'e' è in 'b', lo aggiungiamo alla lista 'c' (costo O(1) per ogni append).

# Alla fine del ciclo, la lista 'c' conterrà tutti gli elementi di 'a' che si trovano anche in 'b'.
print(c)  # Stampiamo la lista risultante.

'''
Complessita' Temporale : O (n**2)
complessita' Spaziale : e' costante O(1) 

'''




# Analisi del costo computazionale:
# Supponendo che 'a' abbia m elementi e 'b' ne abbia n:
# - Il ciclo 'for e in a' itera m volte.
# - Per ogni iterazione, l'operazione 'e in b' ha un costo O(n) (ricerca lineare in 'b').
# Pertanto, il costo totale è O(m * n).

# Se sia 'a' che 'b' hanno dimensione n (caso peggiore in cui m = n):
# - Il costo diventa O(n * n) = O(n**2).
# Questo rende l'algoritmo inefficiente per liste molto lunghe, poiché il tempo di esecuzione
# cresce quadraticamente con la dimensione degli input.

# Nota: Una soluzione più efficiente potrebbe utilizzare un set per 'b',
# poiché la ricerca in un set ha un costo medio di O(1), riducendo il costo totale a O(m).

#===================================================================================================================================

#alg 2
'''
Complessita' Temporale O(n**2)
'''
a.sort()

b.sort()

# assumiamo Len(a) == Len(b) al valore n 

print(a)
print(b)

i, j = 0, 0
c = []
# Supponiamo di avere due liste ordinate 'a' e 'b'.
# L'obiettivo è trovare gli elementi comuni tra 'a' e 'b' e inserirli nella lista 'c'.

# Lista vuota per raccogliere gli elementi comuni.
c = []

# Inizializziamo due indici, 'i' e 'j', entrambi a 0.
# 'i' scorre la lista 'a', mentre 'j' scorre la lista 'b'.
i = 0
j = 0

# Utilizziamo un ciclo while per confrontare gli elementi di entrambe le liste
# finché non raggiungiamo la fine di una delle due.
while i < len(a) and j < len(b):  
    # Confrontiamo l'elemento corrente di 'a' con quello di 'b'.
    if a[i] == b[j]:  
        # Se gli elementi sono uguali, significa che l'elemento è comune.
        # Lo aggiungiamo alla lista 'c'.
        c.append(a[i])  
        
        # Incrementiamo entrambi gli indici per passare al prossimo elemento.
        i += 1  
        j += 1  
    
    # Se l'elemento di 'a' è minore di quello di 'b', significa che
    # dobbiamo incrementare l'indice 'i' per passare al prossimo elemento in 'a',
    # perché essendo le liste ordinate, nessun elemento successivo in 'b' potrà essere uguale a 'a[i]'.
    elif a[i] < b[j]:  
        i += 1  
    
    # Se l'elemento di 'b' è minore di quello di 'a', incrementiamo l'indice 'j'
    # per passare al prossimo elemento in 'b', poiché nessun elemento successivo in 'a'
    # potrà essere uguale a 'b[j]'.
    else:  
        j += 1  

# Dopo il ciclo, la lista 'c' contiene tutti gli elementi comuni tra 'a' e 'b'.
print(c)  # Stampiamo la lista risultante.

'''
Complessita' temporale : O(n log n + n)
Complessita' spaziale O(n) per via del metodo sort  che e' lineare 
'''



'''
Supponiamo di avere due liste 'a' e 'b'.
'''
# L'obiettivo è trovare gli elementi comuni tra 'a' e 'b' e inserirli nella lista 'c'.

# CASO 1: Se le liste 'a' e 'b' sono già ordinate.
# - L'algoritmo scorre entrambe le liste una sola volta usando due indici 'i' e 'j'.
# - In questo caso, la complessità è O(m + n), dove:
#   * 'm' è la lunghezza di 'a'.
#   * 'n' è la lunghezza di 'b'.
# - Questo avviene perché ogni elemento di 'a' e 'b' viene processato al massimo una volta.

# CASO 2: Se le liste 'a' e 'b' NON sono ordinate.
# - Dobbiamo ordinarle prima di procedere con il confronto.
# - Ordinare una lista ha complessità O(k log k), dove 'k' è la lunghezza della lista.
# - Perciò, se 'a' ha lunghezza 'n' e 'b' ha lunghezza 'm', il costo complessivo sarà:
#   O(n log n) per ordinare 'a' +
#   O(m log m) per ordinare 'b' +
#   O(m + n) per trovare gli elementi comuni.
# - Complessità totale: O(n log n + m log m + m + n).
# - Se 'm' è circa uguale a 'n', la complessità si approssima a O(n log n + n).

# SINTESI:
# - Se le liste sono già ordinate: O(m + n).
# - Se le liste non sono ordinate: O(n log n + n)

#----------------------------------------------------------------------------------------

'''# ANALISI DELLA complessita' in caso sia gia ordinata :
# 1. Numero di iterazioni:
#    - Il ciclo while scorre su ciascun elemento delle liste 'a' e 'b' una sola volta.
#    - Il numero massimo di iterazioni è proporzionale alla somma delle lunghezze di 'a' e 'b'.
#    - Indichiamo len(a) con 'm' e len(b) con 'n'. Quindi il ciclo esegue al massimo O(m + n) iterazioni.
#
# 2. Costo per operazione:
#    - Il confronto 'a[i] == b[j]' ha costo O(1).
#    - Le operazioni sugli indici ('i += 1' e 'j += 1') hanno costo O(1).
#    - L'aggiunta di un elemento a 'c' con 'c.append(a[i])' ha costo O(1).
#
# 3. Complessità totale:
#    - Poiché ogni operazione nel ciclo ha costo O(1) e il ciclo esegue al massimo O(m + n) iterazioni,
#      il costo totale dell'algoritmo è O(m + n).
#
# Questo rende l'algoritmo molto efficiente, soprattutto rispetto ad approcci meno ottimizzati
# che potrebbero richiedere un costo O(m * n) (ad esempio, confrontando ogni elemento di 'a' con ogni elemento di 'b').
'''

#-==================================================================================================================================

# Dizionario 

# Crea una metting tra un'insieme di valori chiamati chiavi con dei valori (k,v)

# d contiene (b0,v0), (k1,v1)
#proprieta': le chiavi sono univoche ki != kj se  i!=  j  principale le chiavi sono tuttte diverse 

#Operazioni : dato un dizionario si puo' usare un op. di ricerca, si puo' vedere se k e' contenuto all'interno di un dizionario come chiave 

#Lettuta : dato un elemento k voglio conoscre il valore associato a k 
#aggiorniamo se k, v 

#se e' un chiave ne viene aggiornato il valore e' v 
# altrimenti (k,v) viene aggiunta al dizionario 

# cancellazione : k 

#se e' una chiave,elimina le coppie ( k,v)
# altrimenti :Errore

'''
Le chiavi possono essere di diversi tipi :di tipo numerico, letterale float, booleano
Si puo' anche associare una tupla sul valore o una lista 

'''


d = {} # dizionario vuoto 
d ={ 5 : 'cinque', # facendo cosi' sto creando un metting, ossia un valore associato 
    'uno':1.6,
    'due' : (1,2) # si puo' anche associare una tupla o lista al suo interno 
    } 

''' la lunghezza del dizionario e' dato dal numero di coppie e quindi le chiavi di volere del dizionaripo  '''


print(d, len(d))

print( 5 in d ) # facendo cosi' chiedo se 5 e' il valore del dizionario e' si verifica cio' con un val booleeeano 

print('5' in d ) #restituisce False      

print(d['uno']) # facendo cosi' andra' a stampare solo il valore della chiave chiamata 

#print (d[1]) # non e' il valore 1, e' andra' in errore 

''' Mentre per l'aggiornamento di un valore '''
 # si fa cosi' 
 
d ['uno'] = 'UNO'

print(d)

d [18] = '2x5' # nuova coppia di chiavi- valore 

print(d)

#======================================================================
''' Mentre cosi' cancello :'''
del(d['uno'])

print(d)

#=-------------------------------------------------------------------------------------------------------------------------------------------
'''
Creazione del dizionario vuor, ricerca aggiorniamo , lettura e cancellazionee
hanno costo Temporale O(1) in media 

Comp. Spaziale : hanno sempre un costo costante O(1)

'''
#=----------------------------------------------------------------------------------------------------------------------------
# In[]
''' 1 soluz'''
# In[Intersezione]

# Definiamo due liste di interi, 'a' e 'b', che rappresentano due insiemi.
a = [9, 2, 1, 8, 4]  # Primo insieme
b = [1, 7, 0, 8, 2]  # Secondo insieme

# Assumiamo che le due liste abbiano la stessa lunghezza, indicata con 'n'.
# Questo sarà utile per analizzare la complessità dell'algoritmo.

# Creiamo due dizionari vuoti, 'da' e 'db'.
# Questi dizionari serviranno per rappresentare gli insiemi 'a' e 'b' sotto forma di hash table.
da, db = {}, {}

# Popoliamo il dizionario 'da' con gli elementi della lista 'a'.
# Ogni elemento di 'a' diventa una chiave nel dizionario 'da'.
# Il valore associato a ciascuna chiave è impostato a None (non rilevante per il nostro scopo).
for e in a: 
    # costo O(n) tempo
    
    da[e] = None  # Inseriamo l'elemento 'e' di 'a' come chiave nel dizionario 'da'.

# Facciamo la stessa cosa con il dizionario 'db', usando gli elementi della lista 'b'.
for e in b:
    #costo O(n)Tempo e anche spaziale, siccome definisco una nuova struttura dati
    
    
    db[e] = None  # Inseriamo l'elemento 'e' di 'b' come chiave nel dizionario 'db'.
    '''E' costante nel caso medio O(1) siccome definisco una nuova struttura dati'''
# A questo punto, 'da' e 'db' contengono gli elementi di 'a' e 'b' rispettivamente,
# rappresentati come chiavi nei loro dizionari.

# Lista vuota per raccogliere gli elementi comuni tra 'a' e 'b'.
c = []

# Iteriamo su ogni elemento 'e' del dizionario 'da'.
# Poiché 'da' rappresenta l'insieme degli elementi unici di 'a',
# scorreremo solo una volta ciascun elemento.
for e in da: 
    ''' itera all'iterno del dizionario sulle chiavi dei dizionari '''
    
    # Verifichiamo se l'elemento 'e' è presente anche nel dizionario 'db'.
    # Questo verifica se 'e' è presente sia in 'a' che in 'b'.
    if e in db:
        ''' O(1) nel caso medio '''
        
        # Se 'e' è in entrambi, lo aggiungiamo alla lista 'c'.
        c.append(e)

# Stampiamo la lista 'c', che contiene l'intersezione degli elementi di 'a' e 'b'.
print(c)  # Esempio di output: [1, 2, 8]

# la ricerca sul dizionario richiede tempo costante 


''' nel caso dei dizionari va fatto cosi' '''

# Complessita' Temporale : O(n) nel caso medio 
# Comp. Spaziale : O(n ) sempre nel caso medio 

# COSTO  DI RICERCA SU LISTA E' NEL CASO MEDIO 

# e e' b[0]  1 confronto 
# e e' b[1]  2 confronti 
# e e' b[2]  3 confronti 
#'''
# e e' b [n-1] n confronti 
# e non e' in b     n+1 confonti 

# il costo medio 1+ 2+3+................+(n-1)+n+(n+1)/(n+1) = (n+2)n/2(n+1) = n/2 circa 
# anche nel caso medio la complessita' e' costo quadratico nel caso non sia un dizionario 






'''
# ANALISI DEL FUNZIONAMENTO E DELLA COMPLESSITÀ

# 1. Creazione dei dizionari 'da' e 'db':
#    - Per ogni elemento delle liste 'a' e 'b', inseriamo un elemento nei rispettivi dizionari.
#    - Questo richiede O(n) tempo per ciascuna lista, poiché ogni inserimento in un dizionario ha complessità O(1).
#    - Totale: O(n) + O(n) = O(n).

# 2. Confronto degli elementi di 'da' con 'db':
#    - Scorriamo ciascun elemento di 'da' (al massimo 'n' elementi).
#    - Per ogni elemento, controlliamo se è una chiave in 'db', operazione che ha costo O(1).
#    - Totale: O(n).

# Complessità complessiva dell'algoritmo:
# - O(n) per creare 'da' e 'db'.
# - O(n) per verificare gli elementi comuni.
# - Totale: O(n).

# L'algoritmo è molto efficiente, grazie all'uso dei dizionari (hash table) per verificare la presenza
# degli elementi con complessità O(1) per operazione di lookup.
# 
'''
#-===============================================================================================================================

''' 2 soluz. '''
''' Qui sotto spiego in modo molto approfondito la complessita' :  '''

# Definiamo due liste di interi, 'a' e 'b', che rappresentano due insiemi.
# L'obiettivo è trovare l'intersezione tra questi due insiemi.
a = [9, 2, 1, 8, 4]  # Primo insieme
b = [1, 7, 0, 8, 2]  # Secondo insieme

# Assumiamo che le due liste abbiano la stessa lunghezza, indicata con 'n'.
# Questo ci aiuterà a calcolare la complessità del programma.

# Creiamo due dizionari vuoti, 'da' e 'db'.
# Questi dizionari rappresentano gli insiemi 'a' e 'b' sotto forma di hash table,
# dove ogni elemento della lista diventa una chiave del dizionario.
da, db = {}, {}

# --- 1. CREAZIONE DEI DIZIONARI 'da' E 'db' ---
for e in a:
    da[e] = None  # Inseriamo ogni elemento di 'a' come chiave nel dizionario 'da'.
    # Complessità temporale: O(1) per ogni inserimento, quindi O(n) per l'intera lista 'a'.

for e in b:
    db[e] = None  # Inseriamo ogni elemento di 'b' come chiave nel dizionario 'db'.
    # Complessità temporale: O(1) per ogni inserimento, quindi O(n) per l'intera lista 'b'.

# A questo punto, 'da' e 'db' contengono gli elementi di 'a' e 'b' come chiavi.

# Complessità spaziale per questa fase: O(n) per 'da' e O(n) per 'db',
# perché ogni elemento occupa spazio come chiave in un dizionario.

# --- 2. TROVARE GLI ELEMENTI COMUNI ---
# Creiamo una lista vuota per raccogliere gli elementi comuni tra 'a' e 'b'.
c = []

# Iteriamo su ogni elemento 'e' del dizionario 'da'.
for e in da:
    # Per ciascun elemento di 'da', controlliamo se è presente in 'db'.
    if e in db:
        # Se l'elemento 'e' è presente in entrambi i dizionari, lo aggiungiamo alla lista 'c'.
        c.append(e)  # Aggiungere un elemento a 'c' ha complessità O(1).
    # L'operazione 'e in db' ha complessità O(1) nel caso medio grazie alla struttura hash.



'''
# Complessità temporale di questa fase: O(n),
# perché iteriamo su tutti gli elementi di 'da' (al massimo 'n' elementi) 
# e ogni verifica di appartenenza in 'db' è O(1).

# --- 3. STAMPA DEL RISULTATO ---
# Stampiamo la lista 'c', che contiene l'intersezione degli elementi di 'a' e 'b'.
print(c)  # Complessità di stampa: O(len(c)), al massimo O(n).

# --- COMPLESSITÀ COMPLESSIVA ---
# 1. Creazione dei dizionari 'da' e 'db': O(n) + O(n) = O(n).
# 2. Iterazione su 'da' e verifica in 'db': O(n).
# 3. Stampa del risultato: O(n).
# Complessità totale temporale: O(n) nel caso medio.

# --- COMPLESSITÀ SPAZIALE ---
# Dizionari 'da' e 'db': O(n) ciascuno.
# Lista 'c': O(n) nel caso peggiore (tutti gli elementi comuni).
# Complessità totale spaziale: O(n).

# --- PERCHÉ O(n) NEL CASO MEDIO? ---
# Inserire elementi e verificare la loro presenza nei dizionari ha complessità O(1) nel caso medio,
# grazie alla funzione hash delle hash table. L'algoritmo scorre ogni elemento una sola volta,
# quindi sia il tempo che lo spazio crescono linearmente rispetto alla lunghezza delle liste.

# --- NOTA SUL CASO PEGGIORE ---
# Nel caso peggiore, se la funzione hash causa molte collisioni, la complessità di ogni operazione
# potrebbe degradare a O(n). In tal caso, la complessità totale dell'algoritmo diventerebbe O(n²).
# Tuttavia, nel caso medio, la complessità rimane O(n).
'''








#-==============================================================================================================================

# il caso medio e' quando conto il numero di confronti che ho nel programma che E' IL COSTO COMPLESSIVO 
''' nel caso dell'intersezione : '''

def disegna_punti_su_retta(a):
    # Definiamo una funzione interna 't1' per estrarre la seconda componente (coordinata) di ciascun elemento.
    def t1(e):
        return e[1]  # Restituisce la coordinata associata al punto.

    # Calcoliamo la coordinata più a sinistra (lx) e più a destra (rx) tra i punti.
    # La funzione min() e max() viene utilizzata con la chiave 't1' per trovare queste coordinate.
    lx = min(a, key=t1)[1]  # lx è il valore minimo delle coordinate.
    rx = max(a, key=t1)[1]  # rx è il valore massimo delle coordinate.

    # La dimensione dell'output sarà data dalla distanza tra lx e rx.
    # m = rx - lx + 1
    # 
    # indica il numero totale di punti sulla retta che considereremo.
    # Questo determina il numero di iterazioni necessarie nel ciclo successivo.

    # Creiamo un dizionario vuoto 'd' per mappare le coordinate ai nomi dei punti.
    d = {}

    # Popoliamo il dizionario 'd' con i punti forniti nella lista 'a'.
    
    for nome, coordinata in a:  # Complessità temporale O(n), dove n è il numero di punti in 'a'.
        
        d[coordinata] = nome  # Ogni coordinata diventa una chiave, associata al nome del punto.

    # Iteriamo su tutte le posizioni comprese tra lx - 1 e rx + 1 (estendiamo leggermente la retta).
    for p in range(lx - 1, rx + 2):  # Complessità temporale O(m), dove m = rx - lx + 3.
        if p in d:  # Verifichiamo se la coordinata 'p' è presente nel dizionario 'd'. Complessità O(1).
            print(d[p], end='')  # Se 'p' è una chiave in 'd', stampiamo il nome associato al punto.
        else:
            print('*', end='')  # Altrimenti, stampiamo un asterisco per rappresentare una posizione vuota.

    # Aggiungiamo una nuova linea per separare l'output.
    print('\nfine')  # Indica la fine del disegno.

    # Complessità temporale:
    # - O(n) per popolare il dizionario.
    # - O(m) per il ciclo che disegna i punti sulla retta.
    # - Complessità totale: O(n + m), dove n è il numero di punti e m è la lunghezza della retta da lx a rx.
    
    # Complessità spaziale:
    # - O(n) per il dizionario 'd', che contiene al massimo 'n' chiavi.

# Definiamo una lista di punti, ciascuno con un nome e una coordinata.
a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]

# Chiamiamo la funzione per disegnare i punti sulla retta.
disegna_punti_su_retta(a)

# complessita' 
# Temp : O(n+m) in media
# spaziale : O(n)

'''
    Complessità del programma (riassunto):
    Complessità temporale:
    
    O(n): Per costruire il dizionario dai punti.
    O(m): Per iterare sulle coordinate da lx - 1 a rx + 1.
    Totale: O(n + m), dove n è il numero di punti e m la lunghezza della retta da considerare.
    
    Complessità spaziale:
    
    O(n): Per il dizionario d, che memorizza al massimo n punti.
'''

































