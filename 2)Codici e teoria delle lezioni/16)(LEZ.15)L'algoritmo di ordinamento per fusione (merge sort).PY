
'''
L'algoritmo di ordinamento per fusione (merge sort): analisi, implementazione e complessità.

'''

#l'algortmo di fusione risolve diversi problemi come 

# bisogna avere due sequenze ordinate 

# a -> <=       b -> <=
#     n/2            n/2

# c -> 


#prendo entrambi i minimi tra le due meta' 

# metto in c il minimo di a e b , confrontaando entambi i minimi 
#             m      n 
# confronto a[i] e b[j]
# ad ogni passo esegue un op costante 


#--------------------------------------------------------------------------------------------------------------------------------------------------

# algoitmo di fusione 


a = [0, 5, 8, 10, 11, 11, 14]  # Prima lista ordinata
b = [1, 2, 6, 6, 6, 9, 10]     # Seconda lista ordinata

i, j = 0, 0  # Inizializzo due indici a 0. 'i' scorrerà la lista 'a', 'j' scorrerà la lista 'b'.
c = []       # Lista vuota che conterrà l'unione ordinata delle liste 'a' e 'b'.

# Eseguo il ciclo finché non raggiungo la fine di almeno una delle due liste.
while i < len(a) and j < len(b):
    # Confronto l'elemento corrente di 'a' con quello di 'b'.
    if a[i] <= b[j]:  # Se l'elemento di 'a' è minore o uguale a quello di 'b'...
        c.append(a[i])  # Aggiungo l'elemento di 'a' alla lista 'c'.
        i += 1          # Incremento l'indice 'i' per passare al prossimo elemento di 'a'.
    else:  # Altrimenti...
        c.append(b[j])  # Aggiungo l'elemento di 'b' alla lista 'c'.
        j += 1          # Incremento l'indice 'j' per passare al prossimo elemento di 'b'.

# Alla fine del ciclo, 'c' contiene gli elementi già ordinati fino al punto in cui una delle due liste è stata completamente scorsa.
print(c)  # Dovrebbe stampare: [0, 1, 2, 6, 6, 6, 9, 10]

''' 
# Usi un **while** invece di un **for** per i seguenti motivi:
'''

'''### 1. **Controllo su due liste con lunghezze diverse**  '''

# Il ciclo `while` è adatto quando vuoi continuare a iterare finché una 
# certa condizione è vera. In questo caso, vuoi scorrere 
# **due liste** (`a` e `b`) e fermarti **non appena una delle due viene completamente attraversata**.  
# Con un `for`, invece, dovresti specificare un range fisso, che non sarebbe adatto per liste di lunghezza diversa.

'''### 2. **Condizione basata su due indici indipendenti**  '''

# Nel tuo caso, hai **due indici indipendenti** (`i` per la lista `a` e `j` per la lista `b`). 
# Il ciclo `while` ti permette di aggiornare entrambi gli indici in modo flessibile, 
# base alla condizione `a[i] <= b[j]`.  
# Con un `for`, sarebbe complicato gestire due indici che non avanzano sempre nello stesso modo.

'''### 3. **Flessibilità nella logica del ciclo**  '''

# Nel ciclo `while`, puoi:
# - Fermarti quando vuoi (ad esempio, quando `i` o `j` raggiungono la fine delle rispettive liste).
# - Incrementare gli indici in modo indipendente (`i` o `j` a seconda della condizione).
# Un ciclo `for` invece scorre un intervallo predefinito, 
# che non è sempre pratico quando hai bisogno di una logica condizionale complessa per avanzare.


'''### Esempio con un ciclo `for` (non pratico in questo caso):'''
# Se usassi un `for`, dovresti iterare su un intervallo fisso e complicare il codice per gestire le liste:

'''
for k in range(len(a) + len(b)):  # Intervallo totale basato sulla somma delle lunghezze
    if i < len(a) and (j >= len(b) or a[i] <= b[j]):
        c.append(a[i])
        i += 1
    elif j < len(b):
        c.append(b[j])
        j += 1
'''''
# Come puoi vedere, diventa più complicato e meno leggibile rispetto al semplice ciclo `while`.


'''### Conclusione  '''
# Usi un **while** perché ti offre maggiore controllo e semplicità 
# quando lavori con due indici che avanzano in modo indipendente e dipendono dalla lunghezza delle liste.



#==========================================================================================================================================

# algoitmo di fusione 

'''
algoritmo di fusione o merge,  cheordina duesequenze ordinatein un unica 
'''

a = [0, 5, 8, 10, 11, 11, 14]  # Prima lista ordinata
b = [1, 2, 6, 6, 6, 9, 10]     # Seconda lista ordinata

i, j = 0, 0  # Inizializzo due indici a 0. 'i' scorrerà la lista 'a', 'j' scorrerà la lista 'b'.
c = []       # Lista vuota che conterrà l'unione ordinata delle liste 'a' e 'b'.

# Eseguo il ciclo finché non raggiungo la fine di almeno una delle due liste.
while i < len(a) and j < len(b):
    # Confronto l'elemento corrente di 'a' con quello di 'b'.
    if a[i] <= b[j]:  # Se l'elemento di 'a' è minore o uguale a quello di 'b'...
        c.append(a[i])  # Aggiungo l'elemento di 'a' alla lista 'c'.
        i += 1          # Incremento l'indice 'i' per passare al prossimo elemento di 'a'.
    else:  # Altrimenti...
        c.append(b[j])  # Aggiungo l'elemento di 'b' alla lista 'c'.
        j += 1          # Incremento l'indice 'j' per passare al prossimo elemento di 'b'.

# Alla fine del ciclo, 'c' contiene gli elementi già ordinati fino al punto in cui una delle due liste è stata completamente scorsa.


# Dopo il primo ciclo while, una delle due liste (a o b) è stata completamente attraversata.
# Tuttavia, potrebbero esserci ancora elementi rimanenti nell'altra lista.
# I due cicli while seguenti servono per aggiungere questi elementi rimanenti alla lista 'c'.

# Se ci sono ancora elementi nella lista 'a' (indice 'i' non ha raggiunto la fine della lista):
while i < len(a): 
    c.append(a[i])  # Aggiungo l'elemento corrente di 'a' alla lista 'c'.
    i += 1          # Incremento l'indice 'i' per passare al prossimo elemento di 'a'.

# Se ci sono ancora elementi nella lista 'b' (indice 'j' non ha raggiunto la fine della lista):
while j < len(b):
    c.append(b[j])  # Aggiungo l'elemento corrente di 'b' alla lista 'c'.
    j += 1          # Incremento l'indice 'j' per passare al prossimo elemento di 'b'.

# A questo punto, la lista 'c' contiene tutti gli elementi di 'a' e 'b' uniti in ordine crescente.



print(c)  # Dovrebbe stampare: [0, 1, 2, 6, 6, 6, 9, 10]


# la complessita' temporrale :  occupa in tempo costante perche' i e j occupano spazio costante e quindi la comp e' O(1)
# dove O(n) dove n = len(a)+ len(b)

# complessita' spaziale: O(1) non ci sono  strutture di appoggio 

'''### Come ragiona l'algoritmo durante l'aggiunta di un elemento alla lista `c`:

# 1. **Confronto degli elementi correnti di `a` e `b`**  
#    L'algoritmo inizia confrontando gli elementi nelle posizioni correnti di `a` e `b`:
#    - Se `a[i]` è **minore o uguale** a `b[j]`, significa che l'elemento di `a` dovrebbe essere inserito per primo nella lista `c`.
#    - Altrimenti, viene inserito l'elemento di `b`.
#    Questo garantisce che ogni elemento venga aggiunto a `c` **in ordine crescente**.

# 2. **Avanzamento dell'indice**  
#    Dopo aver aggiunto un elemento a `c`:
#    - Se l'elemento aggiunto proviene da `a`, l'indice `i` viene incrementato per passare al prossimo elemento di `a`.
#    - Se invece l'elemento aggiunto proviene da `b`, l'indice `j` viene incrementato per passare al prossimo elemento di `b`.

# 3. **Ripetizione del processo**  
#    Il ciclo continua finché entrambe le liste non sono state almeno parzialmente attraversate (cioè finché `i < len(a)` e `j < len(b)`).

# 4. **Gestione degli elementi rimanenti**  
#    Quando una delle due liste viene completamente attraversata
# (ad esempio, quando `i == len(a)`), l'algoritmo entra nei due cicli `while`
# successivi per aggiungere gli eventuali **elementi rimanenti** dall'altra lista.

---

# ### Esempio passo per passo:

# Dati:  
# `a = [0, 5, 8, 10, 11, 11, 14]`  
# `b = [1, 2, 6, 6, 6, 9, 10]`  
# Inizialmente: `i = 0`, `j = 0`, `c = []`.

# 1. **Primo confronto**  
#    - `a[i] = 0`, `b[j] = 1`  
#    - `0 <= 1`, quindi aggiungo `0` a `c` e incremento `i`.  
#    - Risultato: `c = [0]`, `i = 1`, `j = 0`.

# 2. **Secondo confronto**  
#    - `a[i] = 5`, `b[j] = 1`  
#    - `5 > 1`, quindi aggiungo `1` a `c` e incremento `j`.  
#    - Risultato: `c = [0, 1]`, `i = 1`, `j = 1`.

# 3. **Terzo confronto**  
#    - `a[i] = 5`, `b[j] = 2`  
#    - `5 > 2`, quindi aggiungo `2` a `c` e incremento `j`.  
#    - Risultato: `c = [0, 1, 2]`, `i = 1`, `j = 2`.

# 4. **Quarto confronto**  
#    - `a[i] = 5`, `b[j] = 6`  
#    - `5 <= 6`, quindi aggiungo `5` a `c` e incremento `i`.  
#    - Risultato: `c = [0, 1, 2, 5]`, `i = 2`, `j = 2`.

# 5. **Continuo il processo...**  
#    Ogni volta confronto gli elementi correnti, aggiungo quello più piccolo e incremento l'indice corrispondente.

---

# ### Alla fine del primo ciclo `while`:  
# `c` contiene tutti gli elementi ordinati fino al punto in cui una delle liste è stata completamente attraversata.

# ### Nei cicli `while` successivi:  
# Se rimangono elementi in una delle liste, vengono aggiunti direttamente a `c` (poiché sono già ordinati).

---

# ### Conclusione:  
# L'algoritmo segue un approccio **greedy** (avido), aggiungendo l'elemento
# più piccolo disponibile a ogni passo per costruire una lista finale ordinata.
# Questo è il cuore dell'**algoritmo di fusione** (merge), che è fondamentale, ad esempio, nel merge sort.
'''

#-===========================--=-=-=-=-=-=-=-=-===-=-=-=-=-==-=-=-=-==--=-=-=-=-=-=-=-=-=-=---=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-==-==-==--====-=-=-=-=

# il merge sorrt funziona 

# 3, 1,2,9,4,5,7,0        # qui avevo n sequenze odinate da un elemento # QUI  8 LUNGHE DI N/4
# 1, 3   2,9  4,5   0,7   # qui avro' n/2 sequenze di questi elementi # QUI SARA' 4 LUNGHEZZA DI N/3

''' poi dopo ordino le due sequenze ordinate prima'''

# 1,2,3,9      0,4,5,7  # e qui dividero' n  # QUI DUE LUNGHEZE DI LUNCHEZA N/2

''' e poi riordino le ultime due sequenze '''

# 0,1,2,3,4,5,7,9 

''''''

# IL NUMRO DI PASSAGGI CHE EFFETUO SA NlogN
# qui ho propripo una legge logarritmica che associa il numero di livelli al numero di elementi 
# se la lista ha N elementi e mi servono i passaggi per rislvere i livelli i ris sara' t+1
# sara' la stessa llegge logaritmica della ricerca binaria 

# se il numero di livelli cresce in modo logaritmico, con un numero di passi raggiungo una fine, un passa non costera' tempo costante 
# ma tempo lineare, i passi sono logN quindi il costo sara' N* logN 

# e' un metodo ricorsivo 


# in quest' algorritmo divido a meta'piu' volte la lista 

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# Algoritmo Merge

# Algoritmo Merge

def Merge(a, lx, cx, rx):
    '''
        input  : una sequenza di elementi da ordinare
                 lx, cx e rx sono indici tali che lx <= cx <= rx
                 con la proprieta' che a[lx:cx] e a[cx:rx] sono ordinate
        output : None
        effetti collaterali (E.C.): modifica la lista `a` in-place
    '''
    i, j = lx, cx  # Inizializzo gli indici per le due sottoliste ordinate
    c = []         # Lista temporanea per memorizzare gli elementi uniti

    # Eseguo il ciclo finché non raggiungo la fine di almeno una delle due sottoliste
    while i < cx and j < rx:
        # Confronto gli elementi delle due sottoliste
        if a[i] <= a[j]:  # Se l'elemento della prima sottolista è minore o uguale...
            c.append(a[i])  # Aggiungo l'elemento dalla prima sottolista a 'c'
            i += 1          # Incremento l'indice della prima sottolista
        else:
            c.append(a[j])  # Aggiungo l'elemento dalla seconda sottolista a 'c'
            j += 1          # Incremento l'indice della seconda sottolista

    # Aggiungo eventuali elementi residui della prima sottolista
    while i < cx:
        c.append(a[i])  # Copio il restante degli elementi dalla prima sottolista
        i += 1          # Avanzo l'indice della prima sottolista

    # Aggiungo eventuali elementi residui della seconda sottolista
    while j < rx:
        c.append(a[j])  # Copio il restante degli elementi dalla seconda sottolista
        j += 1          # Avanzo l'indice della seconda sottolista
        
    # Copio gli elementi uniti dalla lista temporanea 'c' nella lista originale 'a'
    i = lx
    for e in c:
        a[i] = e
        i += 1
    # Sovrascrivo la porzione originale della lista con gli elementi 
    
#a=  [10,21, 0, 30, 34,34,39,11,13, 16, 17, 19, 0, 0,10 ,10]
#Merge(a, 3,7,12)
#print(a)
# Nota: la lista `a` deve essere definita a livello globale o passata come parametro esplicito.

#print(a)
# Nota: la lista `a` deve essere definita a livello globale o passata come parametro esplicito.



#complessita' Temporale: O(n) dove ne' la lunghezza
# dellle sottosequenze da orinare
# la comp.sspaziale :  abbiamo una  listadi appoggio ossia c, a differenza dell'altrro programma qui c, non viene piu' considerato come output
# ma come memoria di appoggio o supplementare, la comp. e' O(n) per via della lista c 


'''
# Per eseguire il codice e illustrarne i vari passaggi, definiamo la lista globale `a` e mostriamo l'output passo dopo passo.
# Usando la funzione `Merge`, vedremo come vengono uniti due sottoliste ordinate.

# Ecco una prova di esecuzione:

# Definisco la lista globale
a = [1, 3, 5, 2, 4, 6]

# Indici che delimitano le sottoliste ordinate:
# Prima sottolista: a[0:3] -> [1, 3, 5]
# Seconda sottolista: a[3:6] -> [2, 4, 6]
lx, cx, rx = 0, 3, 6

# Eseguo la funzione Merge
Merge(lx, cx, rx)

# Risultato finale
print(a)

# Vediamo passo per passo cosa succede durante l'esecuzione di `Merge`:

# 1. **Inizializzazione:**
#    - `i = lx = 0`
#    - `j = cx = 3`
#    - `c = []` (lista temporanea vuota)

# 2. **Confronti ed elementi aggiunti a `c`:**
#    - `a[i] = 1` e `a[j] = 2`, quindi `1 <= 2`. Aggiungo `1` a `c` → `c = [1]`. Incremento `i` → `i = 1`.
#    - `a[i] = 3` e `a[j] = 2`, quindi `3 > 2`. Aggiungo `2` a `c` → `c = [1, 2]`. Incremento `j` → `j = 4`.
#    - `a[i] = 3` e `a[j] = 4`, quindi `3 <= 4`. Aggiungo `3` a `c` → `c = [1, 2, 3]`. Incremento `i` → `i = 2`.
#    - `a[i] = 5` e `a[j] = 4`, quindi `5 > 4`. Aggiungo `4` a `c` → `c = [1, 2, 3, 4]`. Incremento `j` → `j = 5`.
#    - `a[i] = 5` e `a[j] = 6`, quindi `5 <= 6`. Aggiungo `5` a `c` → `c = [1, 2, 3, 4, 5]`. Incremento `i` → `i = 3`.

# 3. **Elementi residui:**
#    - La prima sottolista è esaurita (`i >= cx`).
#    - Copio l'elemento rimanente dalla seconda sottolista: aggiungo `6` a `c` → `c = [1, 2, 3, 4, 5, 6]`.

# 4. **Copia in `a`:**
#    - Copio gli elementi da `c` nella lista originale `a` → `a = [1, 2, 3, 4, 5, 6]`.

# Risultato finale: la lista `a` è stata ordinata unendo le due sottoliste.
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# codice sensa commenti:

def merge(a, lx, cx, rx):
    '''
        Input: a una lista di elementi
            lx, cx e rx indici in a t.c. lx <= cx <= rx
            con la proprietà che a[lx:cx] e a[cx:rx] sono ordinate
        Output: None
        
        Effetto collaterale a[lx:rx] è ordinata
    '''

    i, j = lx, cx
    c = []
    while i < cx and j < rx:
        if a[i] <= a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
    
    while i < cx:
        c.append(a[i])
        i+=1
        
    while j < rx:
        c.append(a[j])
        j += 1
        
    i = lx
    for e in c:
        a[i] = e
        i += 1
        
    # complessità temporale: O(n) dove n è la lunghezza
    #    della sottosequenza da ordinare
    # complessità spaziale: O(n) per via della lista c
    
a = [10, 21, 0, 30, 34, 34, 38, 11, 13, 16, 17, 19, 0, 0, 10, 10]
merge(a, 3,7,12)
print(a)











#-===============================================================================================================================================================
def merge_sort( a,lx = 0 ,rx = None):
    # lx estremo sinistro 
    # rx estremo destro 
    # gli assegno il valore None , perche solo quando la richiamo  la funz. legge len di a 
    # quindi gli assegno None, per poi assegnargli il val ossia di iniziare il confronto  all'estremo destro 
    
    
    '''
        input : a una lunghezza di elementi che possono essere conforontati, ossia che in a posso essere confrontati
        ( ossia che in a posso applicare l'operatore di confronto < o = )
        lx < rx: indice sinitro e destro di a 
        ouput : None 
        Effetto colllaterale : ossia ordinare in loco gli elementi di a (modificare gli el di a )
    '''
    ''' non servira' perche lavorero' con i due parametri sopra 
    if n <= 1: 
             return None 
    '''

    if rx == None:
        rx = len (a )# Se rx non è definito, viene settato alla lunghezza di `a`.

    if lx+1 >= rx:
        return None
    
    cx = int((lx+rx)/2)     # che indica la posizione intermedia tra due 
        #riguarda un indice quindi prendera'una parte intera  
    
    ''' Adesso bisognera' ordinare in modo ricorsiva  '''
    
    
    merge_sort(a, lx, cx)
    merge_sort(a, cx, rx)
    Merge(a, lx, cx, rx)
    



    
a=  [10,21, 0, 30, 34,34,39,11,13, 16, 17, 19, 0, 0,10 ,10]

merge_sort(a)
print(a)
    # n = len(a)
    #ordinare a[:n/2], ordinare a [n/2:]
    #fondere delle porzioni di a 
    # la fusione va fatta tra sotto liste consecutive 
    # bisognera creare due indici ossia quello destro e sinitro, 
    


'''Dimostrazione:

-0   abbiamo un punto per ogni elemento che sono n elementi da ordinare n=2*k

-1   nel  secondo punto abbiamo n/2 liste di dimensione 2 ordinate  # ogni fusione mi  e' costata 2=n  e'abbiamo n fusioni il costo sara' n

-2 nel terzo livelloavro n/4 liste di dimensione 4  # ogni fusione micostera' 4 =n la fusione di tale costo mi costera' n 

-3 nel quarto liv. ci sra'un costo di n/2*3 quindi ogni lista avrebbe il costo di 2*3 che e' = n 

-i ennesio ho n/2*i  che saraa il costo ennesimo 2*i = O(n)

- t contiene una lista quindi n/2*t sara' = 1 e quiondi t = long_2

    quindi sar' O(NlogN_2)


'''  
    # complessità temporale: O(n log_2 n), sara' sempre cosi' siaa nel migliore che nel caso peggiore 
    # complessità spaziale: O(log_2 n) + O(n) ( che sarebbe quella di appoggio ) = O(n)
    #
    #   
    
''' Complessita' spaziale: 
Per un funz ricorsiva, n e' la dimensione che stimao ordiando, richiede come prima cosa ordinare la parte sinistra n/2, 

la second n/4 e fino ad arrivare ad i, la lunghezza della catena sinistra sara' O(log_2) dei frame aperti e logarimica

appena ho ordina lasinistra passo alla destra 

il  numero di frame e' sempre uguale sullo stock <= log(n) = O(logN)
tutti i frame usati non avranno usato la memoria per c (in caso si voglia copiare in un alias la slissta ) 
'''    
    
         
# Approfondiamo la spiegazione della complessità del Merge Sort, analizzando sia la **complessità temporale** che i passi del tuo ragionamento:

# Struttura dell'algoritmo Merge Sort:
# 1. **Divide**: Divide l'array iniziale in due metà finché ogni sottovettore non contiene un solo elemento (casi base).
# 2. **Conquer**: Ordina e fonde le sottoliste ordinate.
# 3. **Combine**: Combina le sottoliste ordinate per ottenere l'array ordinato finale.

# Complessità temporale di Merge Sort:
# L'analisi della complessità si basa su:
# - **Livelli di ricorsione**: Ogni volta che dividiamo l'array in due, creiamo un nuovo livello.
# - **Costo di fusione**: A ogni livello, dobbiamo fondere le sottoliste ordinate.

# Dettaglio del ragionamento:

# 1. **Primo livello (array intero)**:  
#    L'array iniziale di dimensione n è diviso in due sottoliste di dimensione n/2. Non si esegue ancora nessuna fusione.

# 2. **Secondo livello**:  
#    - L'array è diviso in n/2 sottoliste di dimensione 2.  
#    - Ogni fusione combina due elementi, e ci sono n/2 fusioni.  
#    - Costo complessivo per questo livello: (n/2) * 2 = n.

# 3. **Terzo livello**:  
#    - Abbiamo n/4 sottoliste di dimensione 4.  
#    - Ogni fusione combina 4 elementi, e ci sono n/4 fusioni.  
#    - Costo complessivo: (n/4) * 4 = n.

# 4. **Quarto livello**:  
#    - Ci sono n/8 sottoliste di dimensione 8.  
#    - Costo complessivo: (n/8) * 8 = n.

# 5. **i-esimo livello**:  
#    - A ogni livello, il numero di sottoliste è n / (2^i), e ciascuna ha dimensione 2^i.  
#    - Il costo totale per il livello rimane (n / 2^i) * 2^i = n.  
#    - Siccome il numero totale di livelli è log_2(n), il costo totale di tutti i livelli è:  
#      O(log n) * O(n) = O(n log n).

# 6. **Ultimo livello (livello t)**:
#    - Il livello t corrisponde a quando abbiamo solo sottoliste di dimensione 1 (cioè array indivisibili).
#    - A questo punto, tutte le fusioni sono completate e l'array finale è completamente ordinato.
#    - Il costo rimane O(n) per ogni livello, e il numero di livelli t è log_2(n).
#    - Nota: non c'è alcun fattore moltiplicativo 2 associato a log_2(n). 
# Questo equivoco potrebbe derivare dalla somma dei costi totali per tutti i livelli, ma il numero di livelli rimane log_2(n).

# Complessità spaziale:
# La **complessità spaziale** di Merge Sort è O(n) perché serve spazio aggiuntivo per il vettore temporaneo usato nella fusione.

# Conclusione:
# La **complessità temporale** di Merge Sort è O(n log n), dovuta al costo O(n) per ogni livello moltiplicato per il numero di livelli O(log n).




#-===========================-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


'''
# Approfondiamo la spiegazione della complessità del Merge Sort, analizzando sia la **complessità temporale** che i passi del tuo ragionamento:

# Struttura dell'algoritmo Merge Sort:
# 1. **Divide**: Divide l'array iniziale in due metà finché ogni sottovettore non contiene un solo elemento (casi base).
# 2. **Conquer**: Ordina e fonde le sottoliste ordinate.
# 3. **Combine**: Combina le sottoliste ordinate per ottenere l'array ordinato finale.

# Complessità temporale di Merge Sort:
# L'analisi della complessità si basa su:
# - **Livelli di ricorsione**: Ogni volta che dividiamo l'array in due, creiamo un nuovo livello.
# - **Costo di fusione**: A ogni livello, dobbiamo fondere le sottoliste ordinate.

# Dettaglio del ragionamento:

# 1. **Primo livello (array intero)**:  
#    L'array iniziale di dimensione n è diviso in due sottoliste di dimensione n/2. Non si esegue ancora nessuna fusione.

# 2. **Secondo livello**:  
#    - L'array è diviso in n/2 sottoliste di dimensione 2.  
#    - Ogni fusione combina due elementi, e ci sono n/2 fusioni.  
#    - Costo complessivo per questo livello: (n/2) * 2 = n.

# 3. **Terzo livello**:  
#    - Abbiamo n/4 sottoliste di dimensione 4.  
#    - Ogni fusione combina 4 elementi, e ci sono n/4 fusioni.  
#    - Costo complessivo: (n/4) * 4 = n.

# 4. **Quarto livello**:  
#    - Ci sono n/8 sottoliste di dimensione 8.  
#    - Costo complessivo: (n/8) * 8 = n.

# 5. **i-esimo livello**:  
#    - A ogni livello, il numero di sottoliste è n / (2^i), e ciascuna ha dimensione 2^i.  
#    - Il costo totale per il livello rimane (n / 2^i) * 2^i = n.  
#    - Siccome il numero totale di livelli è log_2(n), il costo totale di tutti i livelli è:  
#      O(log n) * O(n) = O(n log n).

# 6. **Ultimo livello (livello t)**:
#    - Il livello t corrisponde a quando abbiamo solo sottoliste di dimensione 1 (cioè array indivisibili).
#    - A questo punto, tutte le fusioni sono completate e l'array finale è completamente ordinato.
#    - Il costo rimane O(n) per ogni livello, e il numero di livelli t è log_2(n).

# La relazione t = log_2 N deriva dal modo in cui l'algoritmo Merge Sort divide l'array in sottoliste. Vediamo il motivo passo dopo passo:

# 1. Divisione binaria
#    L'algoritmo Merge Sort divide ricorsivamente l'array in due parti uguali a ogni livello. Se l'array iniziale ha dimensione N, al primo livello si hanno due sottoliste di dimensione N/2, poi quattro sottoliste di dimensione N/4, e così via.
#    Questa divisione continua fino a raggiungere sottoliste di dimensione 1. Ogni livello di questa divisione corrisponde a un passo ricorsivo.

# 2. Numero totale di livelli
#    La domanda è: quanti livelli t servono per dividere un array di dimensione N fino a ottenere sottoliste di dimensione 1?
#    Alla i-esima divisione, il numero di sottoliste è 2^i, e la dimensione di ciascuna sottolista è N / 2^i. Quando la dimensione di una sottolista diventa 1, vale la relazione:
#    N / 2^t = 1

# 3. Risoluzione dell'equazione
#    Per trovare t, risolviamo l'equazione N / 2^t = 1:
#    N = 2^t
#    Applichiamo il logaritmo in base 2 a entrambi i membri:
#    log_2 N = t

# 4. Conclusione
#    Il numero totale di livelli t richiesti per dividere l'array fino a ottenere sottoliste di dimensione 1 è t = log_2 N.

# Intuizione pratica
#    Il numero t rappresenta il numero di volte che devi dividere l'array a metà per passare da una dimensione N a 1. Ad esempio:
#    - Se N = 8, t = log_2 8 = 3.
#    - Se N = 16, t = log_2 16 = 4.
#    Ogni livello richiede un costo O(n), e il numero di livelli t = log_2 N determina la complessità totale O(n log N).

# Complessità spaziale:
# La **complessità spaziale** di Merge Sort è O(n) perché serve spazio aggiuntivo per il vettore temporaneo usato nella fusione.

# Conclusione:
# La **complessità temporale** di Merge Sort è O(n log n), dovuta al costo O(n) per ogni livello moltiplicato per il numero di livelli O(log n).

'''
