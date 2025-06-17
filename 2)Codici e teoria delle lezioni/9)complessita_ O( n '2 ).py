


# In informatica, la notazione O(n²) (dove n è la dimensione dell'input) indica un algoritmo la cui complessità temporale cresce in
# modo quadratico al crescere della dimensione dell'input. Gli algoritmi con complessità O(n²)
# sono tipicamente meno efficienti di quelli con O(n log n) o O(n),
# soprattutto per input di grandi dimensioni. Ecco alcuni casi comuni di algoritmi con complessità O(n²):

# 1. Algoritmo di ordinamento a bolle (Bubble Sort):
# Descrizione: Il Bubble Sort è un algoritmo di ordinamento semplice che ripetutamente
# scambia gli elementi adiacenti in un array se sono nell'ordine sbagliato. 
# La complessità temporale è O(n²) perché per ogni elemento della lista 
# viene eseguito un ciclo che confronta e, se necessario, scambia gli elementi.
# Esempio: Confronto e scambio in un ciclo annidato: per ogni elemento del vettore,
# si confrontano e si scambiano con tutti gli altri elementi.
# Complessità: O(n²)

# 2. Algoritmo di ordinamento per selezione (Selection Sort):
# Descrizione: Selection Sort funziona selezionando iterativamente l'elemento più piccolo
# (o più grande) dalla parte non ordinata dell'array e mettendolo nella posizione corretta. 
# La complessità temporale è O(n²) a causa di due cicli annidati: uno per scorrere 
# l'array e uno per trovare l'elemento minimo (o massimo).
# Esempio: Per ogni elemento, viene trovato l'elemento minimo nel resto della lista,
# il che richiede un ciclo annidato.

# Complessità: O(n²)

# 3. Algoritmo di ordinamento per inserimento (Insertion Sort):
# Descrizione: Insertion Sort funziona inserendo ogni elemento nella sua posizione
# corretta in un array già ordinato. Inizia con il secondo elemento e lo confronta 
# con quelli precedenti, spostando gli elementi più grandi per fare spazio all'elemento corrente.
# La complessità è O(n²) nel caso peggiore, che si verifica quando gli elementi sono in ordine inverso.
# Esempio: In ogni iterazione, si scorre la parte già ordinata dell'array per trovare 
# la posizione corretta per l'elemento corrente.


# Complessità: O(n²)

# 4. Moltiplicazione di matrici (algoritmo standard):
# Descrizione: L'algoritmo di moltiplicazione di matrici standard moltiplica due matrici quadrate di dimensione n. Ogni elemento della matrice risultante è il risultato di un prodotto scalare tra una riga della prima matrice e una colonna della seconda matrice. Questo porta a un ciclo annidato di dimensione O(n²).
# Esempio: Moltiplicazione di matrici A (di dimensione n×n) e B (di dimensione n×n), dove ogni elemento della matrice risultato è il risultato di una somma di prodotti.
# Complessità: O(n²)

# 5. Ricerca del percorso in un grafo non ottimizzato:
# Descrizione: La ricerca del percorso in un grafo non ottimizzato, come la ricerca di un cammino tra due nodi in un grafo con rappresentazione matrice di adiacenza, può richiedere O(n²) nel caso peggiore.
# Esempio: Utilizzando un algoritmo di ricerca per tutti i percorsi possibili in un grafo completo (matrice di adiacenza), si devono verificare tutte le combinazioni di nodi, il che porta a una complessità quadratica.
# Complessità: O(n²)

# 6. Algoritmi di confronto a coppie:
# Descrizione: Algoritmi che confrontano tutte le possibili coppie di elementi in un array o lista hanno una complessità O(n²). Un esempio di questo potrebbe essere la ricerca di duplicati in un array, dove ogni elemento viene confrontato con ogni altro elemento.
# Esempio: Per verificare se ci sono duplicati, è necessario confrontare ogni elemento con tutti gli altri, richiedendo un ciclo annidato.
# Complessità: O(n²)

# 7. Algoritmo di determinazione di intersezione di due set non ordinati:
# Descrizione: Se si utilizzano due cicli annidati per confrontare ogni elemento di un set con ogni elemento dell'altro set per determinare l'intersezione, il tempo di esecuzione è O(n²). In altre parole, ogni elemento del primo set viene confrontato con ogni elemento del secondo set.
# Esempio: Confrontare ogni elemento di un set con ogni altro per trovare i valori comuni.
# Complessità: O(n²)

# 8. Algoritmi di confronto di sequenze o stringhe:
# Descrizione: Confrontare due sequenze o stringhe per trovare le differenze (es. distanza di Levenshtein, che calcola la distanza di modifica tra due stringhe) può richiedere O(n²).
# Esempio: La matrice della distanza di Levenshtein tra due stringhe di lunghezza n richiede un algoritmo che esegue operazioni su una matrice di dimensione n×n, portando a una complessità quadratica.
# Complessità: O(n²)

# 9. Costruzione di una matrice delle distanze tra tutti i nodi:
# Descrizione: Calcolare la distanza tra tutte le coppie di nodi in un grafo (come nel caso della matrice delle distanze di un grafo completo) richiede la comparazione di tutte le coppie di nodi, il che porta a una complessità quadratica.
# Esempio: Se si calcolano tutte le distanze tra i nodi in un grafo usando un algoritmo non ottimizzato.
# Complessità: O(n²)

# 10. Algoritmo di ricerca di sottosequenze o sottoinsiemi:
# Descrizione: Algoritmi che esplorano tutte le sottosequenze o sottoinsiemi di una lista o stringa di lunghezza n, esaminando ogni possibile coppia di indici o combinazione.
# Esempio: La ricerca di sottosequenze comuni tra due stringhe di lunghezza n, dove si devono esaminare tutte le possibili coppie di indici.
# Complessità: O(n²)

# Conclusione:
# Gli algoritmi con O(n²) sono generalmente inefficaci per dati di grandi dimensioni. 
# La complessità quadratica deriva spesso dalla presenza di cicli annidati che percorrono l'intero input per ogni elemento. Gli esempi descritti sono algoritmi che operano in modo inefficiente su grandi dataset, e quindi possono essere migliorati utilizzando algoritmi con complessità O(n log n) o O(n), a seconda del caso.

#=================================================================================================================================================================================================================================



# 1. Esempio: Algoritmo di ordinamento a bolle (Bubble Sort)
# Il Bubble Sort ha una complessità O(n²) perché confronta e scambia coppie di elementi in un ciclo annidato.
# Per ogni elemento della lista, il ciclo interno confronta e scambia con tutti gli altri elementi.
def bubble_sort(arr):
    n = len(arr)
    
    # Ciclo esterno: scorre attraverso ogni elemento
    for i in range(n):
        # Ciclo interno: confronta ogni coppia di elementi adiacenti
        for j in range(0, n-i-1):
            # Confronta gli elementi adiacenti e li scambia se necessario
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 2. Esempio: Algoritmo di ordinamento per selezione (Selection Sort)
# Il Selection Sort ha una complessità O(n²) poiché seleziona l'elemento minimo (o massimo) in ogni passaggio,
# richiedendo un ciclo annidato per trovare l'elemento minimo e metterlo nella posizione corretta.
def selection_sort(arr):
    n = len(arr)
    
    # Ciclo esterno: scorre attraverso ogni elemento
    for i in range(n):
        min_index = i
        # Ciclo interno: cerca l'elemento minimo nella parte non ordinata
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Scambia l'elemento minimo trovato con l'elemento alla posizione i
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 3. Esempio: Algoritmo di ordinamento per inserimento (Insertion Sort)
# L'Insertion Sort ha una complessità O(n²) nel caso peggiore, quando gli elementi sono in ordine inverso,
# poiché per ogni elemento si scorre la parte già ordinata per trovarne la posizione corretta.
def insertion_sort(arr):
    n = len(arr)
    
    # Ciclo esterno: scorre attraverso ogni elemento
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Ciclo interno: scorre gli elementi ordinati finché non trova la posizione giusta per 'key'
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 4. Esempio: Moltiplicazione di matrici (algoritmo standard)
# La moltiplicazione di due matrici quadrate di dimensione n richiede O(n²) operazioni,
# poiché ogni elemento della matrice risultante è il prodotto scalare di una riga della prima matrice con una colonna della seconda matrice.
def multiply_matrices(A, B):
    n = len(A)
    # Matrice risultato C
    C = [[0] * n for _ in range(n)]
    
    # Ciclo per la moltiplicazione
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# 5. Esempio: Ricerca del percorso in un grafo non ottimizzato
# In un grafo rappresentato tramite matrice di adiacenza, la ricerca del percorso tra tutti i nodi richiede O(n²) operazioni,
# poiché bisogna esaminare tutte le combinazioni di nodi per trovare un cammino.
def find_path(graph):
    n = len(graph)
    # Controlla tutte le possibili combinazioni di nodi
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                print(f"Percorso trovato tra {i} e {j}")

# 6. Esempio: Algoritmi di confronto a coppie
# Algoritmi che confrontano ogni coppia di elementi in una lista, come nella ricerca di duplicati, hanno una complessità O(n²),
# in quanto ogni elemento viene confrontato con tutti gli altri.
def has_duplicates(arr):
    n = len(arr)
    
    # Ciclo esterno
    for i in range(n):
        # Ciclo interno
        for j in range(i + 1, n):
            # Confronta ogni coppia di elementi
            if arr[i] == arr[j]:
                return True  # Duplicato trovato
    return False

# 7. Esempio: Algoritmo di determinazione dell'intersezione di due set non ordinati
# Quando si confrontano ogni elemento di un set con ogni elemento dell'altro set per determinare l'intersezione,
# la complessità è O(n²), poiché ogni elemento deve essere confrontato con tutti gli altri.
def intersection(set1, set2):
    result = []
    for elem1 in set1:
        for elem2 in set2:
            if elem1 == elem2:
                result.append(elem1)
    return result

# 8. Esempio: Algoritmi di confronto di sequenze o stringhe
# Algoritmi come la distanza di Levenshtein (che calcola la distanza di modifica tra due stringhe) richiedono O(n²),
# poiché devono esplorare una matrice di dimensione n×n per calcolare la distanza.
def levenshtein_distance(str1, str2):
    n, m = len(str1), len(str2)
    # Crea una matrice delle distanze
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n][m]

# 9. Esempio: Costruzione di una matrice delle distanze tra tutti i nodi
# Calcolare tutte le distanze tra i nodi di un grafo completo usando la matrice delle distanze richiede O(n²),
# poiché per ogni coppia di nodi deve essere calcolata una distanza.
def calculate_all_pairs_distances(graph):
    n = len(graph)
    dist_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = graph[i][j]
    return dist_matrix

# 10. Esempio: Algoritmo di ricerca di sottosequenze o sottoinsiemi
# Algoritmi che esplorano tutte le sottosequenze o sottoinsiemi di una lista o stringa richiedono O(n²),
# poiché devono esaminare tutte le possibili coppie di indici o combinazioni.
def subsequences(arr):
    subseq = []
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            subseq.append(arr[i:j+1])
    return subseq

    '''
        Passo 1: Analisi dei Cicli:
        Ogni esempio di algoritmo ha cicli annidati. Il ciclo esterno itera sull'intero array (o set),
        e il ciclo interno scorre l'array a partire dall'elemento successivo, confrontando tutti gli altri elementi.
        Passo 2: Calcolo del Numero di Operazioni:
        Ogni elemento viene confrontato con ogni altro, il che porta a una somma di operazioni che cresce come O(n²).
        Passo 3: Analisi della Complessità Asintotica:
        La somma totale delle operazioni è O(n²), poiché ci sono due cicli annidati che percorrono l'intero set di dati.
        Conclusione:
        Ogni esempio mostra come un algoritmo che utilizza due cicli annidati, uno all'interno dell'altro,
        comporti una complessità quadratica. Questo aumenta in modo esponenziale il numero di operazioni 
        quando la dimensione dell'input cresce, rendendo l'algoritmo inefficiente per grandi dataset. 
    '''
        
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       
# La trasformazione della complessità temporale di un algoritmo da O(n) a O(n²) 
# può essere dovuta a vari fattori 
# che modificano il modo in cui il codice elabora i dati. 
# 
# Qui sotto sono descritte alcune delle ragioni comuni per un tale cambiamento:

# 1. Aggiunta di un Ciclo Annidato
# Il passaggio più diretto e comune da O(n) a O(n²) avviene quando si aggiunge
# un ciclo interno annidato all'interno di un ciclo esistente. 

# Questo può succedere per diversi motivi:
# - Esigenza di Confronti o Calcoli Aggiuntivi: Se le esigenze dell'algoritmo
# cambiano in modo da richiedere confronti o calcoli aggiuntivi che coinvolgono 
# ogni coppia di elementi, si potrebbe introdurre un secondo ciclo. 
# Ad esempio, un algoritmo che inizialmente aggiungeva valori da un 
# array potrebbe essere modificato per calcolare una matrice di distanze o similitudini tra tutte le coppie di punti.

# - Esplorazione di Relazioni tra Elementi: In alcuni casi, un algoritmo 
# che originariamente processava elementi in modo indipendente 
# potrebbe essere esteso per esaminare relazioni o interazioni 
# tra coppie di elementi, come nel controllo di duplicati o nella 
# ricerca di sottosequenze comuni.

# 2. Modifica dell'Operazione Principale
# A volte, un cambiamento nel tipo di operazione eseguita può aumentare la complessità:

# - Da Elaborazioni Singole a Combinazioni: Un algoritmo che originariamente 
# elaborava ogni elemento singolarmente (ad esempio, moltiplicando ogni elemento
# di un array per un fattore) potrebbe essere esteso per elaborare combinazioni
# di elementi (ad esempio, moltiplicando ogni coppia di elementi).

# 3. Cambiamento nella Struttura dei Dati
# L'introduzione di una struttura dati più complessa che richiede operazioni annidate 
# per il suo aggiornamento o la sua interrogazione può anche portare un algoritmo da O(n) a O(n²):
# - Da Array a Matrici o Tabelle: Se un algoritmo inizia a utilizzare una matrice 
# o una tabella bidimensionale per memorizzare o calcolare relazioni, questo può 
# richiedere due cicli per accedere o aggiornare ogni elemento.

# 4. Modifiche nei Requisiti di Precisione o Nelle Esigenze Analitiche
# In alcuni casi, la necessità di una maggiore precisione o di un'analisi più dettagliata può trasformare un algoritmo:
# - Da Analisi Grezza a Dettagliata: Ad esempio, un algoritmo che valutava una stima 
# grezza che poteva essere calcolata linearmente potrebbe necessitare di un approccio
# più dettagliato che richiede un confronto ogni-a-ogni.

# 5. Ottimizzazione Inadeguata o Compromessi di Progettazione
# Talvolta, la scelta di una struttura di dati inadatta o compromessi
# di design per la facilità di implementazione possono causare inefficienze:
# - Scelte di Design Conservativo: Sviluppatori potrebbero scegliere un approccio
# più semplice da implementare, ma meno efficiente, accettando una complessità O(n²) 
# per evitare la complessità del codice.


# Esempio Pratico
# Immagina un algoritmo che inizialmente somma tutti gli elementi di un array (complessità O(n)). 
# Se la specifica cambia e ora richiede la somma di ogni possibile coppia di elementi, l'algoritmo
# avrà bisogno di due cicli annidati, uno per scegliere il primo elemento di ogni coppia e uno per
# scegliere il secondo, portando la complessità a O(n²).

# In sintesi, il passaggio da O(n) a O(n²) avviene tipicamente a causa dell'introduzione di operazioni
# o strutture più complesse che richiedono un livello aggiuntivo di iterazione o confronto, spesso a causa
# di cambiamenti nei requisiti o nelle funzionalità dell'algoritmo.




















#--------------------------------------------------------------------------------------------===============================================================================================================================
'''La spiegazione che hai fornito riguarda le implicazioni di efficienza legate alla rimozione di elementi 
da una lista in Python, in particolare la differenza tra rimuovere elementi dall'inizio ("dalla testa") 
rispetto alla fine ("dalla coda") della lista. Ecco un'analisi dettagliata dei punti che hai menzionato:

Costo Computazionale dell'Ultimo while
Nel codice originale, dopo aver copiato gli elementi necessari dalla lista originale 
a alla lista temporanea b, rimuovi gli elementi in eccesso in a utilizzando del(a[i]). 
Questo approccio, però, può portare a una complessità computazionale quadratica, O(n²), nel caso peggiore.
Questo accade perché ogni volta che rimuovi un elemento dalla lista con del(a[i]), tutti gli elementi 
successivi nella lista devono essere spostati indietro di una posizione per riempire lo spazio lasciato
dall'elemento rimosso. Se molti elementi devono essere rimossi, questo spostamento diventa significativo 
e ripetitivo, causando un alto costo computazionale.

Efficienza della Rimozione dalla Coda
Rimuovere elementi dalla fine della lista, o "dalla coda", è molto più efficiente in Python.
Questo perché, quando rimuovi l'ultimo elemento di una lista con il metodo .pop(),
non ci sono altri elementi che devono essere spostati. L'operazione di rimozione dell'ultimo
elemento ha un costo temporale costante, O(1), indipendentemente dalla dimensione della lista.

Implicazioni Pratiche
Inefficiente: Rimuovere elementi dall'inizio o dalla "testa" della lista, specialmente in un ciclo 
che richiede la rimozione di più elementi, può portare a una notevole inefficienza. 
Per esempio, se hai una lista di 1000 elementi e devi rimuovere i primi 500, ogni operazione 
di rimozione costringerà gli altri 500+ elementi a spostarsi, causando un'enorme quantità di operazioni di spostamento.

Efficiente: Rimuovere gli elementi dalla fine riduce drasticamente il numero di operazioni necessarie,
rendendo l'azione di rimozione molto più veloce e meno costosa in termini di risorse di calcolo.

Come Migliorare il Codice
Per migliorare l'efficienza del codice nel contesto della rimozione degli elementi, una strategia consiste
nel modificare completamente l'approccio dopo aver copiato gli elementi validi indietro da b a a:

Svuotare a completamente e poi riempirla solo con gli elementi di b, utilizzando a.clear() 
seguito da a.extend(b). Questo evita completamente la necessità di rimuovere gli elementi
uno ad uno, riducendo la complessità operativa a O(n), poiché clear() è O(1) e extend() è O(n) per la lunghezza di b.
Ecco un esempio di come potresti riscrivere il codice:

python

def del_item(a, v):
    b = []
    for x in a:
        if x != v:
            b.append(x)

    a.clear()  # Rimuove tutti gli elementi da 'a' in modo efficiente
    a.extend(b)  # Aggiunge tutti gli elementi di 'b' a 'a'

l = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
del_item(l, 1)
print('Ecco i valori aggiornati: ', l)
Questo approccio non solo è sintatticamente più pulito ma è anche molto più efficiente per le operazioni
che potrebbero altrimenti richiedere spostamenti multipli di elementi all'interno della lista.'''

























