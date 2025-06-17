##Il problema dell'ordinamento: l'algoritmo bubble sort; descrizione e complessità temporale;
#ottimizzazione dell'algoritmo. L'istruzione break. 
#Adattare la funzione bubble_sort() per personalizzare il creterio di ordinamento attraverso 
#una funzione di valutazione degli elementi della sequenza. Utilizzo dell'ordinamento per ottenere soluzioni più efficienti.


# SI PUO' RIDURRE IL COSTO DELLA  COMPLESSITA' TEMPORALE A SCAPITO DI DI QUELLA SPAZIALE 

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]
    
    # n = len(a)
    
    lx = min(a, key=t1)[1]
    rx = max(a, key=t1)[1]
    
    m = rx-lx+1
    
    retta = ['*']*m  # Tempo e spazio O(m)
    
    for e, p in a: # Tempo O(n)
        retta[p-lx] = e
        
    print(''.join(retta)) # Tempo O(m)
    
    # Complessità
    # Temporale    O(n+m)
    # Spaziale     O(m)
        
    
a = [ ('A', -6), ('B', -2), ('E', -3), ('C', 0), ('D', -5) ]



#=============================================================================================================================================================================================================================================================

# ABBIAMO TROVATO UNA SOLUZIONE , CHE NON POSSIAMO TROVARE  UNA SOLUZIONE DEL PROBLEMA, SOLTSNTO BASANDOCI SULLA DIMENSIONE DELL'INPUT 
# PERCHE C'E' UNA GRANDEZZA CHE MAI USCITA FUORI , CHE E' LA DIMENSIONE DELL'OUTPUT , CHE POTREBBE ESSERE SCORRELATA  DALLLA DIMENSIONE DELL'INPUT 

def disegna_punti_su_retta(a):
    def t1(e):
        return e[1]
   
    lx = min(a, key=t1)[1]
    rx = max(a, key=t1)[1]
'''
Nel codice Python, poni `key=t1` per dire alle funzioni `min()` e `max()`
di usare il risultato della funzione `t1` come base per confrontare
gli elementi nell'array `a` anziché i valori degli elementi stessi.

In pratica, quando `min(a, key=t1)` o `max(a, key=t1)` viene eseguito, 
Python chiama la funzione `t1` per ogni elemento in `a` e usa il valore 
ritornato da `t1` per determinare quale elemento è il minimo o il massimo.
Qui, `t1` prende un elemento `e` (che dovrebbe essere una coppia o una lista
con almeno due elementi) e restituisce il secondo elemento `e[1]`.


Ecco perché è utile specificare `key=t1`:

1. **Controllo**: Permette di specificare esattamente su quale criterio basare
il confronto, offrendo un controllo granulare su come gli elementi vengono confrontati.

2. **Flessibilità**: Rende il codice più flessibile e riutilizzabile. 
Puoi facilmente cambiare il comportamento di `min` o `max` semplicemente
cambiando la funzione passata a `key`.

3. **Ordinamento basato su proprietà**: È particolarmente utile quando
gli elementi dell'array sono strutture dati complesse come tuple, liste,
dizionari o oggetti personalizzati, e vuoi eseguire operazioni basate su 
una specifica proprietà di questi oggetti.

In sostanza, definire `key=t1` ti permette di indicare alle funzioni `min` e `max`
quale parte dell'elemento considerare per il confronto, che in questo caso è 
il secondo elemento di ciascuna tupla nella lista `a`.


'''
retta = ['#']# conterra' ogni carattera per la stringa finale 


#=================================================================================================================================================================================================================================
#=-----------------------=--=-=-=-=-=-==--==-=--=-=-=-==-=--==-=-=--==-=-=-=-=--==-=--=-==-=-=--=-==-=--=-=-==-=-=--=-==-=--=-=-==-=--=-=-=-=-=-=-==-=--==-=--==-=--=-=-=-=-=-=-=-==--==-=-=-=-=-=--=-==--=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-==-=--=-=-=-==-=-=--=-=-=-==-



def disegna_punti_su_retta(a):
    # Definizione di una funzione interna 't1' che accetta un elemento 'e' (assumendo che sia una tupla).
    # La funzione 't1' è destinata a essere utilizzata come chiave di ordinamento e restituisce il secondo elemento di 'e',
    # che rappresenta la posizione numerica di un punto sulla retta.
    def t1(e):
        return e[1]

    # Utilizzo della funzione 'min' con l'argomento 'key=t1' per determinare il punto sulla retta con la minima posizione.
    # 'min(a, key=t1)' scorre tutti gli elementi di 'a', applica 't1' ad ogni elemento e restituisce l'elemento completo
    # con il valore minimo restituito da 't1', ovvero l'elemento con la posizione minima.
    lx = min(a, key=t1)[1]

    # Analogamente, 'max(a, key=t1)' viene utilizzato per trovare l'elemento con la posizione massima sulla retta.
    # Il risultato è l'elemento di 'a' che, una volta passato a 't1', fornisce il valore massimo.
    rx = max(a, key=t1)[1]

    # Calcolo della lunghezza 'm' della lista 'retta' che dovrà contenere tutti i punti tra il minimo e il massimo inclusi.
    # Aggiungendo 1 ci assicuriamo che l'intervallo sia inclusivo di entrambi gli estremi. Per esempio, se 'lx' è 0 e 'rx' è 4,
    # senza l'aggiunta di 1, la lunghezza sarebbe 4 (da 0 a 3), ma con l'aggiunta di 1, la lunghezza diventa 5, coprendo l'indice 4.
    m = rx - lx + 1

    # Inizializzazione di una lista 'retta' riempita di asterischi '*'. Ogni asterisco rappresenta potenzialmente una unità di spazio
    # sulla retta che può essere sovrascritta con un'etichetta di un punto. La lunghezza di 'retta' è 'm', che è stata calcolata sopra.
    retta = ['*'] * m

    # Iterazione su ogni elemento della lista 'a', dove ogni elemento è una coppia contenente un'etichetta e una posizione.
    for e, p in a:
        # Calcolo dell'indice nella lista 'retta' per l'inserimento dell'etichetta 'e'.
        # 'p - lx' calcola l'offset di 'p' dalla posizione minima 'lx', convertendo la posizione in un indice valido per la lista.
        # Questo è necessario perché gli array in Python sono indicizzati a partire da 0, quindi dobbiamo adattare 'p' in base a 'lx'.
        retta[p - lx] = e

    # Concatenazione e stampa della lista 'retta'. La funzione 'join()' è utilizzata per convertire la lista di caratteri
    # in una stringa unica. Questo è utile per la visualizzazione finale della retta, dove ogni punto è rappresentato dalla sua etichetta
    # e gli spazi vuoti dalla retta sono rappresentati da asterischi.
    print(''.join(retta))

# Esempio di dati di input con posizioni relative e etichette.
a = [('A', -6), ('B', -2), ('E', -3), ('C', 0), ('D', -5)]
disegna_punti_su_retta(a)

'''
-Indice di retta: L'indice p - lx assume che p possa essere qualsiasi
valore numerico e che lx sia il minimo valore possibile per p nell'insieme di dati. 
Questa assunzione permette di utilizzare la differenza come indice diretto in retta,
posizionando correttamente l'etichetta e senza andare fuori dai limiti della lista.

-Validazione: Potrebbe essere utile aggiungere una validazione per assicurarsi
che p - lx non generi un indice negativo o un indice che superi la lunghezza di retta,
per evitare errori di runtime.

-Efficienza e errore: La gestione efficiente di questo codice richiede che la lista
retta sia correttamente dimensionata e che gli indici siano sempre validi. 
Se retta non è abbastanza grande o se gli indici calcolati escono dal range valido,
potrebbero verificarsi errori o comportamenti imprevisti.

'''
    
    
    
    
    
#=============================================================================================================================================================================================================================

'''VERSIONE CON MENO DETTAGLI NEI COMMENTI, 2 parte  :'''


# Definizione della funzione per disegnare punti su una retta data una lista 'a' di tuple o liste.
def disegna_punti_su_retta(a):
    # Funzione interna che ritorna il secondo elemento di una tupla o lista.
    def t1(e):
        return e[1]
   
    # Calcolo dell'elemento con il minimo e massimo secondo elemento in 'a'.
    lx = min(a, key=t1)[1]
    rx = max(a, key=t1)[1]

    # Calcolo della distanza tra i punti più estremi sulla retta. (m = (lx - rx)) e sbagliato 
    '''
    Prima Soluzione: m = lx - rx
La prima soluzione m = lx - rx potrebbe risultare errata 
se lx rappresenta il valore minimo tra le posizioni e rx il valore massimo,
poiché sottraendo il valore massimo dal minimo si otterrebbe un valore negativo o zero,
che non rappresenta correttamente una distanza o un intervallo.

Tuttavia, anche se invertito a m = rx - lx (assumendo di voler correggere l'ordine di sottrazione),
questa soluzione ignora il fatto che si vuole includere entrambi i punti estremi nella distanza calcolata.

Seconda Soluzione: m = rx - lx + 1
La seconda soluzione m = rx - lx + 1 è corretta per i seguenti motivi:

-Inclusione Completa: 

Aggiungendo 1 alla differenza tra rx e lx,
si include nella conte del segmento sia il punto a lx sia quello a rx.
In termini di indici di array o di posizioni in una rappresentazione grafica,
se si desidera includere sia il punto iniziale sia quello finale in un conteggio,
è necessario aggiungere 1. Per esempio, se lx è 0 e rx è 4, rx - lx dà 4,
che sono il numero di passi tra lx e rx, ma ci sono 5 posizioni da considerare (0, 1, 2, 3, 4).

-Corretta Rappresentazione di Intervallo:
Questo approccio riflette correttamente l'intervallo totale tra 
i due estremi inclusivi, che è un concetto chiave nella 
creazione di strutture dati o rappresentazioni grafiche che
richiedono l'inclusione di tutti i punti da un minimo a un massimo.

-In sostanza:
la seconda formula è preferibile quando si lavora con indici
o posizioni in array o liste in Python e si vuole rappresentare un intervallo 
che includa entrambi gli estremi. Questa è una prassi comune in programmazione 
per assicurarsi che tutti i punti rilevanti siano inclusi nel calcolo o nella visualizzazione.
'''
    
    
    
    
    
    
    m = rx- lx+1 

    # Creazione di una lista di asterischi '*' di lunghezza 'm' che rappresenta la retta.
    
    retta = ['*']*m     # TEMPO E SPAZIO E' O(M)


    for e,p in a : 
        ''' il tempo di costo e' o(n)'''
        # il primo elemento della coppia e' un etichetta, 
        #quindi il carattere , il secondo e' un intero ossia la posizione 
       
        # retta[ qualcosa che dipende da m e p ] = e
        
        retta[p-lx] = e # Assegna l'etichetta 'e' alla posizione calcolata, normalizzata rispetto a 'lx'.



    # Stampa della stringa risultante dalla lista 'retta'.
    # Unisce tutti gli elementi della lista 'retta' in una singola stringa.
    print(''.join(retta))  # Questa operazione ha un costo di tempo O(m), dove 'm' è la lunghezza della lista 'retta'.

a = [('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5)]
# Chiamata alla funzione
'''disegna_punti_su_retta(a)'''








#=============================================================================================================================================================================================================================

'''VERSIONE CON MENO DETTAGLI NEI COMMENTI, 3 parte  :'''


# Definizione della funzione per disegnare punti su una retta data una lista 'a' di tuple o liste.
def disegna_punti_su_retta(a):
    # Funzione interna che ritorna il secondo elemento di una tupla o lista.
    def t1(e):
        return e[1]
   
    # Calcolo dell'elemento con il minimo e massimo secondo elemento in 'a'.
    lx = min(a, key=t1)[1]
    rx = max(a, key=t1)[1]

    # Calcolo della distanza tra i punti più estremi sulla retta. (m = (lx - rx)) e sbagliato 
    m = rx- lx+1 

    # Creazione di una lista di asterischi '*' di lunghezza 'm' che rappresenta la retta.
    
    retta = ['*']*m     
    
    '''# TEMPO E SPAZIO E' O(M)'''


    for e, p in a : 
        ''' il tempo di costo e' o(n)'''
        # il primo elemento della coppia e' un etichetta, 
        #quindi il carattere , il secondo e' un intero ossia la posizione 
       
        # retta[ qualcosa che dipende da m e p ] = e
        
        retta[p-lx] = e # Assegna l'etichetta 'e' alla posizione calcolata, normalizzata rispetto a 'lx'.



    # Stampa della stringa risultante dalla lista 'retta'.
    # Unisce tutti gli elementi della lista 'retta' in una singola stringa.
    
    print('0'.join(retta))  # Questa operazione ha un costo di tempo O(m), dove 'm' è la lunghezza della lista 'retta'.
    '''
    TEMPO O(M)
    '''
    
    ''''''



    # Complessita' 
    # Temporale O(n+m)
    # Spaziale  O(m)



a = [('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5)]
# Chiamata alla funzione
disegna_punti_su_retta(a)


################################################################################################################################################################################################################################################################################################

'''
Complessità Temporale: O(n + m)
Calcolo di lx e rx: Le funzioni min() e max() sono entrambe chiamate con la lista a come argomento
e utilizzano la funzione t1 per determinare l'elemento con il valore minimo e massimo di p.
Queste operazioni hanno una complessità temporale di O(n) ciascuna, dove n è il numero di elementi
in a, perché devono passare attraverso tutti gli elementi della lista per trovare i valori minimi e massimi.

Iterazione su a: Dopo aver determinato lx e rx, il ciclo for attraversa ogni elemento di a per posizionare
le etichette sulla retta. Questa iterazione è ancora una volta O(n), poiché ogni elemento viene esaminato
una sola volta per posizionare l'etichetta.

Inizializzazione di retta e operazioni di assegnazione: L'inizializzazione di retta è O(m), dove m è
la lunghezza calcolata come rx - lx + 1. Ogni posizione in retta viene inizializzata una volta. 
L'assegnazione all'interno del ciclo for non aggiunge complessità significativa oltre a quella dell'iterazione di a.

Quindi, combinando queste operazioni, la complessità temporale totale diventa O(n + m), 
rappresentando il passaggio attraverso tutti gli elementi di a e la gestione delle operazioni relative alla lista retta di lunghezza m.

Complessità Spaziale: O(m)
Spazio per retta: L'allocazione di memoria principale in questo script è per la lista retta, la cui lunghezza è m.
Questo rappresenta lo spazio occupato per mantenere tutti i caratteri o le etichette sulla retta. Poiché m dipende
dai valori massimi e minimi di p in a, questa lista può essere grande quanto il range di posizioni coperte da p.

Altri usi di memoria: La funzione t1 e le variabili lx, rx, e, e p usano memoria, ma il loro impatto è trascurabile 
rispetto alla lista retta. La memoria utilizzata da queste variabili è costante, mentre retta può variare in dimensione.

In sintesi, la complessità spaziale del codice è dominata dalla lunghezza di retta, che è O(m), e questo riflette 
lo spazio richiesto per rappresentare visivamente la retta basata sul range di posizioni tra lx e rx.



'''

#=========================================================================================================================================================================================================================================

# L'algoritmo di ordinamento Bubble Sort è uno dei metodi più semplici e intuitivi per ordinare una lista. 
# L'algoritmo funziona "bollendo" ripetutamente gli elementi più grandi verso la fine della lista 
# attraverso scambi successivi tra elementi adiacenti che non sono in ordine corretto.

'''### Descrizione dell'Algoritmo'''
# 1. **Confronto e Scambio**: Inizia dal primo elemento della lista e confrontalo con il successivo. 
#    Se il primo elemento è maggiore del secondo, scambiali.
# 2. **Continua per la Lista**: Prosegui con questo metodo per ogni coppia successiva lungo la lista, 
#    spingendo così l'elemento più grande verso la fine dopo il primo passaggio completo.
# 3. **Ripetizione senza l'ultimo elemento**: Una volta che l'elemento più grande è stato posizionato alla fine 
#    della lista (dopo il primo passaggio completo), ripeti il processo per la parte restante della lista 
#    (escludendo l'ultimo, già ordinato).
# 4. **Iterazione fino al completamento**: Continua il processo fino a quando non sarà necessario fare altri scambi, 
#    il che significa che la lista è completamente ordinata.

'''### Proprietà dell'algoritmo'''
# - **Stabile**: mantiene l'ordine relativo degli elementi uguali.
# - **Adattivo**: ha prestazioni migliori su liste parzialmente ordinate.
# - **Complessità Temporale**: O(n^2) nel caso medio e peggiore, O(n) nel miglior caso (quando la lista è già ordinata).
# - **Complessità Spaziale**: O(1) - Bubble Sort è un algoritmo in-place, poiché richiede una quantità di memoria 
#   extra limitata a poche variabili per gli indici e gli scambi.

'''### Esempio Pratico'''
# Prendiamo la lista `[6, 1, 9, 0, -4, 5, 8, 10, 4]` e applichiamo il Bubble Sort. Seguirò passo dopo passo il processo:

'''# **Primo Passaggio:**'''
# - Confronta 6 e 1, scambia perché 6 > 1: `[1, 6, 9, 0, -4, 5, 8, 10, 4]`
# - Confronta 6 e 9, non scambia perché 6 < 9: `[1, 6, 9, 0, -4, 5, 8, 10, 4]`
# - Confronta 9 e 0, scambia perché 9 > 0: `[1, 6, 0, 9, -4, 5, 8, 10, 4]`
# - Confronta 9 e -4, scambia perché 9 > -4: `[1, 6, 0, -4, 9, 5, 8, 10, 4]`
# - Confronta 9 e 5, scambia perché 9 > 5: `[1, 6, 0, -4, 5, 9, 8, 10, 4]`
# - Confronta 9 e 8, scambia perché 9 > 8: `[1, 6, 0, -4, 5, 8, 9, 10, 4]`
# - Confronta 10 e 4, scambia perché 10 > 4: `[1, 6, 0, -4, 5, 8, 9, 4, 10]`

'''# **Secondo Passaggio:**'''
# - Confronta 1 e 6, non scambia: `[1, 6, 0, -4, 5, 8, 9, 4, 10]`
# - Confronta 6 e 0, scambia: `[1, 0, 6, -4, 5, 8, 9, 4, 10]`
# - Confronta 6 e -4, scambia: `[1, 0, -4, 6, 5, 8, 9, 4, 10]`
# - Confronta 6 e 5, scambia: `[1, 0, -4, 5, 6, 8, 9, 4, 10]`
# - Confronta 6 e 8, non scambia: `[1, 0, -4, 5, 6, 8, 9, 4, 10]`
# - Confronta 9 e 4, scambia: `[1, 0, -4, 5, 6, 8, 4, 9, 10]`

'''# **Terzo Passaggio:**'''
# - Continua questo schema di scambi fino a quando non ci sono più scambi necessari in un intero passaggio, 
#   segnalando che la lista è ordinata.

# Dopo alcuni passaggi, la lista sarà completamente ordinata. Questo processo dimostra come, attraverso iterazioni successive, 
# gli elementi "bollono" verso la loro posizione corretta nella lista.

#=========================================================================================================================================================================================================================================================

# CON IL BOUBLESORT

# conforntiamo i primi due elementi della lista tra di loro, una volta ordinati il secondo valore viene 
# confrontato con il terzo, epoi viene sostitutito in base alla sua dimensione, lo stesso 
# il valore fino ad arrivare alla fine della lista, per poi ripartire alla fine con delle nuove scansioni 
# nel secondo giro, l'ultimo numero ossia im questo caso : 10 e' arrivato alla fine
# #siccome 9 e' piu' piccolo, quinddi riparto da 9, fino ad arrivare all'oriddnamento in fondo,


#una volta arrivato alla fine serviranno n-1 scansioni, una scansione richiede n-1 confronti  siccome devo confrontare
# O( n ) operazioni 
# quindi e' un'algoritmo  che costa O(n**2)
# nel caso peggiore faccio O(n) operazioni , i costo quindi e' quadratico, (O(n**2))   

#=====================================================================================================================================

''' Algoritmo per una scansione  '''
a = [6,1,9,0,-4,5,8,10,4] 

#per una scasione 

n = len(a) # Calcoliamo la lunghezza della lista 'a'



# Iniziamo un ciclo per eseguire una scansione della lista
# La scansione serve a confrontare elementi adiacenti della lista

for i in range (n-1): # metto n-1 ,per far si che si fermi un passo prima, altrimenti se ci fosse n, non si muove. 
    # Utilizziamo 'n-1' come limite superiore:
    # Questo perché l'ultimo elemento non ha un successivo elemento da confrontare.
    # Se usassimo 'n', l'indice 'i+1' provocherebbe un errore (fuori dai limiti).
    
    # Confrontiamo l'elemento corrente 'a[i]' con il successivo 'a[i+1]'
    if a[i] > a[i+1]: 
        # Se l'elemento corrente è maggiore del successivo:
        # Eseguiamo lo scambio di posizione tra 'a[i]' e 'a[i+1]'
        
        # Lo scambio avviene utilizzando un'assegnazione simultanea:
        # Il valore di 'a[i]' diventa 'a[i+1]' e viceversa.
       
        a[i], a[i+1] = a[i+1], a[i] # in python la variabile ddi appoggio e' nascosta ,
        #perche creaiamo un'assegnamento multiplo, spacchettando una tupla, 
        #in fatti notando qui si cambiera' l'ordine sostituendo il numero, con il precedente 
        # quinddi faacendo cosi' crea un nuovo oggetto nella memoria e lo spacchetta questa variabile in ddue parti 
        
        # Esempio: 
        # Se a = [6, 1, ...] e 'a[i]' è 6 e 'a[i+1]' è 1,
        # Dopo lo scambio, a diventerà [1, 6, ...]

'''============================================================================================================================================================'''
''' Algoritmo per una scansione '''
a = [6, 1, 9, 0, -4, 5, 8, 10, 4] 

# BubbleSort 

n = len(a)   # Lunghezza della lista
# print(n-1) leggera' la lunghezza di a, siccome e' una lista facciamo n-1 e quindi invece di 9 sara' di 8
'''
2) CREO UN NUOVO CICLO FOR: 
'''
# creo un altro ciclo dove lo faro' ripetere n-1 volte, n-1 perche' se ho una lista di n elementi 
# e ne sistemo a loro posto  n- 1 e quinddi chiaro' che l'ultimo elemennto si trovera'
# nell'ultima posizione disponibile ossia quella corretta. 


# Ciclo esterno: ripete la scansione della lista 'n-1' volte
# Ogni passata sposta l'elemento più grande disponibile verso la fine della lista.
for _ in range(n-1):
    for i in range(n-1):  # Scansiona fino alla penultima posizione per evitare errori su a[i+1]
        if a[i] > a[i+1]:  # Confronta elemento corrente con il successivo
            a[i], a[i+1] = a[i+1], a[i]  # Scambia i due elementi utilizzando assegnazione simultanea


#COMPLESSITA' TEMPORALE  O(N**2) A PRESCINDERE DELLA ISTANZA, SEMPRE 
# SI PUO MIGLIORARE ? 


#==============================================================================================================================
#==========================================================================================================================================

'''
L'uso di range(n-1) in un ciclo for permette di iterare dalla posizione 0
alla posizione n-2 di una sequenza (o lista) di lunghezza n.

Dettaglio di range(n-1):
Genera una sequenza di indici:

La funzione range(x) produce numeri interi da 0 a x-1 inclusi.
Ad esempio, se n = 5, allora range(n-1) equivale a range(4), cioè genera:
csharp
Copia codice
[0, 1, 2, 3]
In totale ci sono n-1 valori generati.
Permette di evitare errori di indice:

Quando si accede a a[i+1] all'interno del ciclo, bisogna fermarsi alla penultima posizione (i = n-2).
Se usassimo range(n), l'istruzione a[i+1] provocherebbe un errore IndexError sull'ultimo valore.
Significato pratico:

In algoritmi come il Bubble Sort o altre scansioni su una lista, 
range(n-1) assicura che l'indice i abbia sempre un elemento successivo valido (a[i+1]) da confrontare o elaborare.

'''
#================================================================================================================================
''' Algoritmo per una scansione '''
a = [6, 1, 9, 0, -4, 5, 8, 10, 4] 

# BubbleSort 

n = len(a)  # Lunghezza della lista
# print(n-1) leggera' la lunghezza di a, siccome e' una lista facciamo n-1 e quindi invece di 9 sara' di 8 
'''
3) MIGLIORO IL PROGRAMMA, FACENDO IN MODO CHE UNA VOLTA CHE IL 10 NON VENGA CONFRONTATO 
UNA VOLTA CHE E' ARRIVATO ALLA FINE: 
'''
# Ciclo esterno: ripete la scansione della lista 'n-1' volte
# Ogni passata sposta l'elemento più grande disponibile verso la fine della lista.
for c in range(n-1):
    for i in range(n-1-c):  # Scansiona fino alla penultima posizione per evitare errori su a[i+1]
        '''L'uso di for i in range(n-1-c) introduce un ulteriore elemento "c" (contatore o indice),
        che permette di ridurre il numero di confronti ad ogni passata del ciclo. 
        Questo è particolarmente utile negli algoritmi come il Bubble Sort, dove, 
        ad ogni iterazione, l'elemento più grande viene "spinto" verso la fine 
        della lista e non ha bisogno di essere considerato nelle iterazioni successive.'''
        
        if a[i] > a[i+1]:  # Confronta elemento corrente con il successivo
            a[i], a[i+1] = a[i+1], a[i]  # Scambia i due elementi utilizzando assegnazione simultanea

print(a)
#COMPLESSITA' TEMPORALE  O(N**2) A PRESCINDERE DELLA ISTANZA, SEMPRE 
# SI PUO MIGLIORARE ? 
'''
Spiegazione approfondita di 'range(n-1-c)':

1. **'c' come contatore**:
   - Ogni volta che il ciclo esterno (`for c`) esegue una passata completa,
     l'elemento più grande viene spostato alla sua posizione finale.
   - La parte finale della lista diventa **già ordinata**.

2. **Riduzione della scansione con 'n-1-c'**:
   - Ad ogni passata, il numero di elementi da controllare diminuisce di 1 (valore di 'c').
   - Se, ad esempio, `c = 0`, il ciclo scansiona tutti gli `n-1` elementi.
   - Se `c = 1`, il ciclo scansiona solo fino a `n-2` (ignora l'ultimo elemento, già ordinato).
   - Questo **ottimizza il numero di confronti**, evitando controlli inutili.

3. **Effetto finale**:
   - Dopo **n-1** passate, tutti gli elementi saranno ordinati.
   - Il numero totale di confronti si riduce, migliorando leggermente l'efficienza rispetto alla versione base.

'''
#==================================================================================================================================================================

''' Algoritmo Bubble Sort ottimizzato '''
a = [6, 1, 9, 0, -4, 5, 8, 10, 4]
n = len(a)  # Lunghezza della lista
'''4) Calcolo della COMPLESSITA E' DI QUANTO SIA MIGLIORATO L'ALGORITMO :'''

# Ciclo esterno: esegue 'n-1' passate, una per ogni elemento della lista (escluso l'ultimo).
for c in range(n-1):  # 'c' tiene traccia della passata corrente (contatore)
    # Ciclo interno: scansiona solo la parte non ancora ordinata della lista.
    # Ad ogni passata, il numero di elementi da controllare diminuisce di 'c'.
    for i in range(n-1-c):  # Riduce il numero di confronti alla fine della lista ordinata
        if a[i] > a[i+1]:  # Confronta elemento corrente con il successivo
            a[i], a[i+1] = a[i+1], a[i]  # Scambia gli elementi se sono fuori ordine
            # Lo scambio sposta l'elemento più grande verso destra,
            # avvicinandolo progressivamente alla sua posizione finale.
print(a)


# facendo cosi' la complessitaa' dell'algoritmo :

# nella prima scansione fa (n-1) confronti, nella seconda scansione andro' ha fare (n-2) fino ad arrivare all'ultima scansione (n-8)\
# equivale a 1+2+3......+(n-3) + (n-2)+(n-1) e sara' tutto uguale n* n-1/2 = e' sara' tutto uguale add n** 


#Complessita temporale : e' migliorato l'algoritmo, ma il costo resta quadratico 

#=======================================================================================================================================================

''' SE La lista e' ordinata l'algoritmo quante op esegue?, il costo rimane invariato rimane O(n**2)'''

# ma se la lista e' ordinata, cosa fare per evitare cicli inutile se lo e' 
''' Algoritmo Bubble Sort ottimizzato '''
a = [6, 1, 9, 0, -4, 5, 8, 10, 4]
n = len(a)  # Lunghezza della lista

'''
5) ottimizazione dell'algoritmo, se e' gia' oridnata restituisce True, mentre se non lo e' da false come valore e la ordina, 
creo poi un if sotto al for dove controlla che sia ordinata la lista, per poi farla terminare se ha finito,
quindi interompere il ciclo definitivamentee.

'''





# Ciclo esterno: esegue 'n-1' passate, una per ogni elemento della lista (escluso l'ultimo).

for c in range(n-1): 
    ''' SE NON EFFETTUA SCAMBI, LA LISTA E' ORDDINATA'''
    # 'c' tiene traccia della passata corrente (contatore)
    # Ciclo interno: scansiona solo la parte non ancora ordinata della lista.
    # Ad ogni passata, il numero di elementi da controllare diminuisce di 'c'.
    
    TERMINATO = True # se' uguale a true significa che la lista e' ordinata 
    for i in range(n-1-c):  # Riduce il numero di confronti alla fine della lista ordinata
        if a[i] > a[i+1]:  # Confronta elemento corrente con il successivo
            a[i], a[i+1] = a[i+1], a[i]  # Scambia gli elementi se sono fuori ordine
            # Lo scambio sposta l'elemento più grande verso destra,
            # avvicinandolo progressivamente alla sua posizione finale.
            
            TERMINATO = False # sara' false quando la lista non e' oridinata, e significa che avro' fatto almeno uno scambio 
             # Se viene effettuato almeno uno scambio, la lista non è ancora ordinata
             
    # Verifica di terminazione: se non sono stati fatti scambi, interrompi il ciclo
    if TERMINATO :
        # la lista e' oridnata ed interrompe il ciclo 
        break 
        # La lista è già ordinata, quindi interrompiamo l'algoritmo prematuramente

print(a)

#La variabile TERMINATO controlla se sono stati fatti scambi.
#Se nessuno scambio è effettuato, significa che la lista è già ordinata, quindi il ciclo esterno viene interrotto usando break.
#Questo rende l'algoritmo più efficiente nei casi in cui la lista sia già parzialmente o totalmente ordinata.

'''Spiegazione approfondita:
-Variabile TERMINATO:

Inizialmente impostata su True ad ogni iterazione del ciclo esterno.
Significato: Si assume che la lista sia già ordinata.
Durante il ciclo interno, se viene effettuato almeno uno scambio, 
significa che la lista non è ancora completamente ordinata,
quindi TERMINATO viene impostato a False.

-Ciclo interno:

Confronta elementi adiacenti (a[i] e a[i+1]) e li scambia se sono fuori ordine.
Ogni scambio indica che la lista non è ancora ordinata.
TERMINATO = False segnala che è necessario continuare con altre passate.
Condizione if TERMINATO::

Viene eseguita dopo il ciclo interno.

-Significato:
Se nessuno scambio è stato effettuato (quindi TERMINATO rimane True), significa che:
Gli elementi della lista sono già in ordine crescente.
Non è necessario continuare con ulteriori passate.
A questo punto, l'algoritmo termina anticipatamente.

-break:

La funzione break interrompe immediatamente il ciclo esterno.

-Vantaggio:
Evita passate inutili se la lista è già ordinata.
Ottimizza l'algoritmo riducendo il numero di iterazioni.
Senza il break, l'algoritmo continuerebbe a scansionare la 
lista anche quando è già ordinata, sprecando tempo e risorse.
'''


#===================================================================================================================================================================



''' Algoritmo Bubble Sort ottimizzato '''
a = [6, 1, 9, 0, -4, 5, 8, 10, 4]
n = len(a)  # Lunghezza della lista

'''6) calcolo della complessita' dopo il miglioramento del codice : '''

# Ciclo esterno: ripete 'n-1' passate, una per ogni elemento
for c in range(n-1):  
    TERMINATO = True  # Assumiamo che la lista sia ordinata all'inizio della passata

    # Ciclo interno: confronta e scambia elementi nella parte non ancora ordinata
    for i in range(n-1-c):  # Diminuisce i confronti ad ogni passata
        if a[i] > a[i+1]:  # Se due elementi sono fuori ordine
            a[i], a[i+1] = a[i+1], a[i]  # Scambiali
            TERMINATO = False  # Se c'è uno scambio, la lista non è ancora ordinata

    # Se non sono stati effettuati scambi, la lista è ordinata: termina il ciclo
    if TERMINATO:
        break

print(a)  # Stampa la lista ordinata

#Complessita' temporale O(n**2)nel caso peggiore 
# nel caso migliore la complessita' sara' lineare e quindi O(n)

# nelle altre versioni il costo e' sempre quadratico 



#=========================================================================================================================================================


''' iil ciclo sopra la renddo una funzione '''

# rendiamo piu' generale i ciclo qui sopra per far in modo  che le sequenze usino il confronto diretto per confrontarli 


n = len(a)  # Lunghezza della lista

'''7)Aggiunta della funzione t1 che permette di far prende un elemento della lista 
e ritorna il secondo elemento e[1] : '''

'''
def t1(e): # usiamo t1 come funz. che attribuisce valore degli elementi della lista usiamo t1, che ritorna i secondi elementi della sequen
         return e[1]

# Ciclo esterno: ripete 'n-1' passate, una per ogni elemento
for c in range(n-1):  
    TERMINATO = True  # Assumiamo che la lista sia ordinata all'inizio della passata

    # Ciclo interno: confronta e scambia elementi nella parte non ancora ordinata
    for i in range(n-1-c):  # Diminuisce i confronti ad ogni passata
         if t1(a[i]) > t1(a[i+1]):  # Se due elementi sono fuori ordine
           #aggiungendo t1 permette di confrontare e riportsre solo il secondo valore della tupla 
            
            a[i],a[i+1] = a[i+1], a[i]  # Scambiali
            TERMINATO = False  # Se c'è uno scambio, la lista non è ancora ordinata

    # Se non sono stati effettuati scambi, la lista è ordinata: termina il ciclo
    if TERMINATO:
        break'''

a = [('A', -6), ('B', -2), ('E', -3), ('C', 0), ('D', -5)]


'''Funzione t1:

La funzione t1(e) prende un elemento della lista (ad esempio una tupla) e ritorna il secondo elemento e[1].
Questo permette di personalizzare il confronto nel Bubble Sort.
Ciclo Esterno:

Ripete il processo di scansione della lista per spingere l'elemento più grande verso la fine.
Si interrompe prematuramente se TERMINATO è True, cioè se nessuno scambio viene effettuato.
Ciclo Interno:

Utilizza la funzione t1 per confrontare gli elementi in base al loro secondo valore.
Se il secondo valore di a[i] è maggiore di quello di a[i+1], scambia le due tuple.
Scambio:

La riga a[i], a[i+1] = a[i+1], a[i] scambia interamente le tuple.
Ottimizzazione con TERMINATO:

Se nessuno scambio avviene durante una passata,
l'algoritmo termina anticipatamente con break, poiché la lista è già ordinata.'''


#==============================================================================================================================================================
'''
8)Faccio diventare l'algoritmo una funzione, mettendo invece di t1, ky =None
e aggiungo una sotto funzione identiy come valore di appoggio che poi usp per far 
in modo che possa leggere e confrontaare il secondo valore di una tupla 

'''


# key e' uguale alla funzione identita 


'''
#Trova il massimo in una lista 'a' usando 'key' per il confronto.
#Se key è None, usa identity per confrontare direttamente gli elementi.
'''     
def bubbleSort(a, key=None):  
    ''' Algoritmo Bubble Sort con supporto per una funzione chiave 'key'.
        - Trova l'ordine corretto degli elementi nella lista 'a'.
        - Se 'key' non è specificata, confronta direttamente i valori usando la funzione di default 'identity'.
        - La funzione 'key' permette di personalizzare il criterio di confronto.
    '''
    
    # Funzione 'identity': restituisce l'elemento stesso.
    # Serve come valore di default per 'key' quando questa non è specificata.
    def identity(e):
        return e  # Restituisce l'input originale (funzione identità).
     # METTENDO LA FUNZIONE IDENTITY SL SUO INTERNO DIVENTA UNA FUNZIONE LOCALE 
        # CHE VIENE USATA SOLO DENTRO QUESTA FUNZIONE 
        # QUINID LE FUNZIONI SI POSSO METTERE ANCHE ALLL'INTENO DI ALTRE A SUA VOLTA 
        
    # Lunghezza della lista
    n = len(a)

    # Se 'key' non è specificata, usiamo 'identity' come funzione di confronto.
    if key is None:
        key = identity

    # Ciclo esterno: esegue 'n-1' passate per l'ordinamento
    for c in range(n-1):  
        TERMINATO = True  # Assume che la lista sia già ordinata all'inizio della passata

        # Ciclo interno: scansiona e confronta elementi adiacenti
        for i in range(n-1-c):  # Riduce il numero di confronti ad ogni passata
            if key(a[i]) > key(a[i+1]):  # Confronto basato sulla funzione 'key'
                # Scambio degli elementi se sono fuori ordine
                a[i], a[i+1] = a[i+1], a[i]
                TERMINATO = False  # Imposta False se c'è stato uno scambio

        # Se non ci sono stati scambi, la lista è ordinata
        if TERMINATO:
            break

# Lista di input composta da tuple
a = [('A', -6), ('B', -2), ('E', -3), ('C', 0), ('D', -5)]

'''
Cosa fa key?

-Il parametro key permette di specificare una funzione personalizzata
che estrae un valore su cui effettuare i confronti.
È utile quando si vuole ordinare una lista non in base all'elemento intero,
ma a una proprietà o sottocomponente degli elementi (es. il secondo valore di una tupla).
Funzione identity:

-Se key non viene fornita (ossia key=None), la funzione identity diventa il valore predefinito.
identity restituisce direttamente l'elemento passato come input, permettendo di confrontare 
gli elementi "così come sono".

-Linea if key(a[i]) > key(a[i+1]):

-Cosa fa: Utilizza la funzione key per confrontare due elementi.
Ad esempio, se key = lambda x: x[1], allora key(a[i]) e key(a[i+1]) estraggono il secondo valore della tupla e li confrontano.
Questo permette di ordinare in base al secondo elemento della tupla anziché l'intera tupla.
Personalizzazione con lambda:

-Quando chiami bubbleSort(a, key=lambda x: x[1]), stai passando una funzione anonima che ritorna x[1]
(il secondo valore della tupla).

'''



#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


'''10)Qui faccio in mod che la funzione si possa stampare, ecco qui il codice completo : '''
# Funzione che ritorna il secondo elemento della tupla

def t1(e):
    return e[1]

def bubbleSort(a, key=None):  
    ''' Algoritmo Bubble Sort con supporto per una funzione chiave 'key'.
        - Se 'key' è specificata, usa questa funzione per confrontare gli elementi.
        - Se 'key' è None, confronta direttamente i valori.
    '''
    
    # Funzione locale 'identity': restituisce l'elemento stesso (default per key)
    def identity(e):
        return e  
    
    n = len(a)  # Lunghezza della lista

    # Se 'key' non è specificata, usa 'identity' come funzione di confronto
    if key is None:
        key = identity

    # Ciclo esterno: esegue 'n-1' passate per spostare gli elementi in ordine
    for c in range(n-1):  
        TERMINATO = True  # Assume che la lista sia ordinata

        # Ciclo interno: confronta elementi adiacenti nella parte non ancora ordinata
        for i in range(n-1-c):  
            if key(a[i]) > key(a[i+1]):  # Confronto usando la funzione 'key'
                a[i], a[i+1] = a[i+1], a[i]  # Scambia se fuori ordine
                TERMINATO = False  # Imposta False se c'è stato uno scambio

        # Se nessuno scambio è stato fatto, la lista è già ordinata
        if TERMINATO:
            break

# Lista di input composta da tuple
a = [('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5)]

bubbleSort(a, key= t1)

# Stampa la lista ordinata
print(a)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


'''11) qui creo una nuova funzione che richiama il bubbleSort e' fa in modo che '''

''' questa funz: 

    Trova il minimo e il massimo dei secondi valori delle tuple presenti nella lista a (con t1).
    Calcola la lunghezza dell'intervallo tra il minimo e il massimo valore (inclusi entrambi).
    Ordina la lista a in base al secondo elemento delle tuple usando bubbleSort.
    '''
def disegna_punti_su_retta(a):
    def t1(e):  # Funzione interna 't1' che ritorna il secondo elemento della tupla
        return e[1]
    

    # Trova il valore minimo del secondo elemento nella lista 'a' usando t1
    lx = min(a, key=t1)[1]  # Estrae il secondo valore minimo tra le tuple
    
    # Trova il valore massimo del secondo elemento nella lista 'a' usando t1
    rx = max(a, key=t1)[1]  # Estrae il secondo valore massimo tra le tuple
    
    # Calcola la lunghezza della retta (intervallo tra il minimo e il massimo)
    m = rx - lx + 1
    
    b = a[:]
    # Ordina la lista 'a' in base al secondo elemento delle tuple
   
    bubbleSort(b, key=t1) 
    
    
    
    # la complessita' temporale O(n**2), spazio O(n) 
    #quindi di consequenza sara con piu' tempo e meno spazio 

# questa funzione e' sbagliata perche' modifico l'input  
    
    # Complessità
    # Temporale    O(n+m)
    # Spaziale     O(m)
        
'''1. Cosa è cambiato
Introduzione della variabile b:

python
Copia codice
b = a[:]
La lista b è una copia della lista a usando slicing (a[:]).
In questo modo, la lista originale a non viene modificata quando viene passata a bubbleSort.
bubbleSort lavora solo sulla copia b.
Chiamata a bubbleSort(b, key=t1):

Ora l'ordinamento viene applicato sulla lista copia b, non direttamente su a.
2. Qual era l'errore precedente
Nel codice precedente, avevi chiamato:

python
Copia codice
bubbleSort(a, key=t1)
Questo faceva sì che la funzione bubbleSort ordinasse direttamente la lista originale a. 

-Di conseguenza:

Effetto collaterale: La lista a veniva modificata.

Se avevi bisogno di mantenere l'ordine originale di a, perdevi quei dati.

-Possibile confusione nei risultati:
Quando successivamente lavoravi su a (ad esempio per calcolare altre proprietà o stamparla),
non avresti avuto la versione originale, ma quella ordinata.
3. Soluzione introdotta
Creando una copia con:
python
Copia codice
b = a[:]
hai risolto il problema. 

-Ora:
a rimane inalterata.
La lista b viene ordinata con bubbleSort.
Perché fare una copia della lista?
Protegge i dati originali: La copia garantisce che la funzione non alteri l'input originale.
Evita effetti collaterali: Se l'input viene riutilizzato altrove nel programma,
può ancora mantenere il suo ordine originale.
Buona pratica: Quando si lavora con funzioni di ordinamento,
è sempre meglio chiarire se si vuole modificare la lista originale o lavorare su una copia.'''

#-==========================--=-=-=-=-=-=-=-=-===-=-=-=-===============================================================-=-=-=-=

'''12) qui sotto ho ripotato il codice su spiegato per bene '''


# La funzione t1 prende un elemento della lista a (una tupla, come ('A', -6)) 
# e ritorna il secondo valore della tupla.
def t1(e):
    return e[1]

# Esempio:
# t1(('A', -6)) → restituisce -6.
# La funzione t1 serve come funzione chiave (key) per confrontare i valori 
# durante le operazioni di minimo, massimo e ordinamento.

# Trova il valore minimo lx e massimo rx del secondo elemento:
lx = min(a, key=t1)[1]  # Trova la tupla nella lista a che ha il secondo valore più piccolo.
rx = max(a, key=t1)[1]  # Trova la tupla nella lista a con il secondo valore più grande.

# Spiegazione:
# min(a, key=t1):
# Trova la tupla nella lista a che ha il secondo valore più piccolo.
# [1] estrae il secondo valore di quella tupla.
# max(a, key=t1):
# Trova la tupla nella lista a con il secondo valore più grande.

# Esempio:
# Lista a = [('A', -6), ('B', 3), ('C', 1), ('D', -2)]
# min(a, key=t1) → ('A', -6), quindi lx = -6
# max(a, key=t1) → ('B', 3), quindi rx = 3

# Calcola la lunghezza dell'intervallo:
m = rx - lx + 1  # Calcola il numero totale di posizioni che coprono l'intervallo 
# tra il valore minimo (lx) e il valore massimo (rx), inclusi entrambi.

# Spiegazione:
# La formula rx - lx + 1 garantisce che il risultato sia intero e inclusivo.

# Esempio:
# lx = -6, rx = 3
# m = 3 - (-6) + 1 = 10
# Questo indica che l'intervallo copre 10 posizioni.

# Crea una copia della lista:
b = a[:]  # La variabile b è una copia della lista a.
# Viene usata per evitare di modificare la lista originale durante l'ordinamento.

# Ordina la lista b usando bubbleSort:
bubbleSort(b, key=t1)  # bubbleSort ordina la lista b in base al secondo valore delle tuple,
# utilizzando la funzione t1 come chiave di confronto.
# La lista originale a rimane inalterata.

# Stampa i risultati:
print("Lista ordinata:", b)  # b è la lista ordinata in base al secondo valore delle tuple.
print("Intervallo (m):", m)  # m è la lunghezza dell'intervallo tra i valori minimo e massimo.

# Stampa la lista originale:
print("Lista originale:", a)  # Mostra che la lista originale a non è stata modificata.

# Esempio di Input/Output
# Input:
a = [('A', -6), ('B', 3), ('C', 1), ('D', -2)]

# Output:
# Lista ordinata: [('A', -6), ('D', -2), ('C', 1), ('B', 3)]
# Intervallo (m): 10
# Lista originale: [('A', -6), ('B', 3), ('C', 1), ('D', -2)]

# Cosa fa complessivamente il codice?
# Trova il minimo (lx) e il massimo (rx) dei secondi valori delle tuple.
# Calcola la lunghezza dell'intervallo tra minimo e massimo (m).
# Ordina la lista copia in base al secondo valore usando la funzione bubbleSort e la funzione chiave t1.
# Stampa:
# - La lista ordinata.
# - La lunghezza dell'intervallo.
# - La lista originale per dimostrare che non è stata modificata.

# Punti Chiave:
# - La funzione t1 permette di personalizzare il criterio di confronto.
# - Viene usata una copia della lista per proteggere i dati originali.
# - L'intervallo m rappresenta quanti "punti" esistono tra il valore minimo e il massimo (inclusivi).

'''============================================================================================================================================================'''
''' 
13) qui aggiungio un olterio ciclo per stampare il primo valore della prima tupla 
della lista a senza andare a capo. 

'''
def disegna_punti_su_retta(a):
    def t1(e):  # Funzione interna 't1' che ritorna il secondo elemento della tupla
        return e[1]
    

    # Trova il valore minimo del secondo elemento nella lista 'a' usando t1
    lx = min(a, key=t1)[1]  # Estrae il secondo valore minimo tra le tuple
    
    # Trova il valore massimo del secondo elemento nella lista 'a' usando t1
    rx = max(a, key=t1)[1]  # Estrae il secondo valore massimo tra le tuple
    
    # Calcola la lunghezza della retta (intervallo tra il minimo e il massimo)
    m = rx - lx + 1
    
    b = a[:]
    # Ordina la lista 'a' in base al secondo elemento delle tuple
   
    bubbleSort(b, key=t1) 

for i in range(n):  # Cicla sugli indici da 0 a n-1 (dove n è la lunghezza della lista b)
    e, p = b[i]  # Estrae i due elementi della tupla nella posizione i della lista b
    
    if i == 0:  # Verifica se l'indice è 0, cioè se stiamo esaminando la prima tupla
        print(e, end='')  # Stampa il primo elemento 'e' della tupla senza andare a capo
    else: 
        print()
'''
-Cosa Fa il Codice Complessivamente:
Cicla sugli elementi della lista b (lista di tuple).

-Se l'indice i è 0 (prima tupla):
Estrae il primo valore e della tupla.
Lo stampa senza andare a capo.
Ignora le altre tuple perché la condizione if i == 0 è vera solo al primo giro.

'''

#=========================================================================================================================
def disegna_punti_su_retta(a):
    def t1(e):  # Funzione interna 't1' che ritorna il secondo elemento della tupla
        return e[1]
   
   
    n = len(a)
    
    # Calcola la lunghezza della retta (intervallo tra il minimo e il massimo)
    #m = rx - lx + 1
    b = a[:]  # Crea una copia della lista 'a' in 'b' usando lo slicing. La lista originale 'a' non viene modificata.

# Ordina la lista 'b' in base al secondo elemento delle tuple.
    bubbleSort(b, key=t1)  
    # 'bubbleSort' utilizza 't1' come funzione chiave per ordinare le tuple in base al secondo valore (b[i][1]).
    # Ad esempio, se 'b' è [('A', -6), ('B', 3)], il risultato sarà ordinato in base a -6 e 3.

    # lx è il valore minimo del secondo elemento della prima tupla ordinata.
    # rx è il valore massimo del secondo elemento della lista ordinata (ultima tupla).
    lx, rx = b[0][1], b[-1][1]  

    i = 0  # Inizializza l'indice 'i' per indicare il prossimo elemento della lista 'b' da stampare.

    # Il ciclo 'for' scorre attraverso l'intervallo tra lx (minimo) e rx (massimo), inclusi entrambi.
    for p in range(lx, rx+1):  
        # Verifica se ci sono ancora elementi nella lista 'b' da controllare (i < n)
        # e se il valore corrente 'p' corrisponde al secondo valore della tupla 'b[i]'.
        if i < n and p == b[i][1]:  
            print(b[i][0], end='')  # Stampa il primo elemento della tupla 'b[i]' (ad esempio 'A').
            i += 1  # Incrementa 'i' per passare alla prossima tupla nella lista 'b'.
        else:
            print('*', end='')  # Se 'p' non corrisponde a nessuna tupla, stampa un asterisco '*'. # O(m)

#complessita' tempo : nel caaso peggiore  O(n*2+m)

# e spaziale :O(n)



#==============================================================================================================================
'''Spiegazione Passo per Passo:
Copia della lista:

python
Copia codice
b = a[:]
b diventa una copia della lista a.
Questo protegge a da modifiche quando viene ordinata o manipolata.
Ordinamento della lista:

python
Copia codice
bubbleSort(b, key=t1)
Utilizza l'algoritmo bubbleSort per ordinare la lista b in base al secondo elemento delle tuple.
La funzione t1 è la funzione chiave che estrae e[1] (il secondo valore di ogni tupla) per il confronto.
Calcolo di lx e rx:

python
Copia codice
lx, rx = b[0][1], b[-1][1]
b[0][1]: È il secondo valore della prima tupla nella lista ordinata (minimo).
b[-1][1]: È il secondo valore dell'ultima tupla nella lista ordinata (massimo).
lx e rx rappresentano il range di valori del secondo elemento nella lista ordinata.
Inizializzazione dell'indice i:

python
Copia codice
i = 0
i è l'indice che tiene traccia della prossima tupla da stampare nella lista b.
Ciclo for con range:

python
Copia codice
for p in range(lx, rx+1):
Scorre tutti i valori p nell'intervallo tra lx (valore minimo) e rx (valore massimo), inclusi entrambi.
Condizione if:

python
Copia codice
if i < n and p == b[i][1]:
i < n: Verifica che ci siano ancora elementi nella lista b da controllare.
p == b[i][1]: Controlla se il valore corrente p corrisponde al secondo elemento della tupla b[i].
Stampa il primo elemento della tupla:

python
Copia codice
print(b[i][0], end='')
i += 1
Se la condizione è soddisfatta:
Stampa il primo elemento della tupla corrente b[i][0].
Incrementa i per passare alla prossima tupla.
Stampa l'asterisco *:

python
Copia codice
else:
    print('*', end='')
Se il valore p non corrisponde a nessuna tupla in b, stampa un asterisco *.
Esempio di Input/Output:
Input:

python
Copia codice
a = [('A', -6), ('B', -3), ('C', -1), ('D', 0)]
n = len(a)
b = a[:]
bubbleSort(b, key=t1)

lx, rx = b[0][1], b[-1][1]
i = 0

for p in range(lx, rx+1):
    if i < n and p == b[i][1]:
        print(b[i][0], end='')
        i += 1
    else:
        print('*', end='')
Output:

css
Copia codice
A**B*C*D
Spiegazione:

La lista a contiene 4 tuple ordinate in base al secondo elemento:
python
Copia codice
[('A', -6), ('B', -3), ('C', -1), ('D', 0)]
Il range lx e rx è da -6 a 0.
Il ciclo for percorre tutti i valori da -6 a 0:
Quando il valore p coincide con b[i][1], stampa il primo elemento della tupla.
Altrimenti stampa un *.
Passo per passo:

p = -6 → stampa 'A'
p = -5 → stampa '*'
p = -4 → stampa '*'
p = -3 → stampa 'B'
p = -2 → stampa '*'
p = -1 → stampa 'C'
p = 0 → stampa 'D'
Cosa Fa Complessivamente il Codice:
Crea una copia della lista a e la ordina in base al secondo elemento delle tuple.
Trova il range di valori tra il minimo (lx) e il massimo (rx) del secondo elemento.
Scansiona l'intero intervallo:
Stampa il primo valore delle tuple corrispondenti al secondo valore.
Stampa * dove non esistono corrispondenze.
Restituisce una rappresentazione grafica "a punti" dei valori nella lista ordinata.
Punti Chiave:
bubbleSort ordina la lista in base al secondo valore delle tuple.
Il ciclo percorre l'intero intervallo [lx, rx] includendo eventuali lacune.
* riempie i valori mancanti nell'intervallo.'''






