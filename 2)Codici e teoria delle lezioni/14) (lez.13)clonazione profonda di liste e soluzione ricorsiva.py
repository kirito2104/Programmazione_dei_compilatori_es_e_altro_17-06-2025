
'''

Il problema della clonazione profonda di liste e una soluzione ricorsiva.
Calcolo della complessità di soluzioni ricorsive e valutazione della memoria 
supplementare necessaria per i frame delle chiamate ricorsive.

'''


# soluzioni ricorsive 

# per clonare una lista, e crearne una nuova si usa 'b = a[:]' :

a = [1,2,7,7,9,9,10,13,1]
b = a[:]
c = a

print(id(a) == id(b)) #identifica  in maniera univoca gli oggetti 

print(id(a)== id(c)) #faCENDO COSI' LEGGERA' L'ALIAS DI C E DI A ED HANNO LO STESSO CODICE UNIVOCO 

# NELLA PRIMA DIRA' CHE E' FALSA PERCHE IL CODICE UNIVOCO E' DIVERSO, 
# MENTRE NEL SECONDO E' UGULAE PERCHE' E' UN ALIAS 



#=========================================================================================================================================

def ricerca_intervallo(a, k):
    # Ciclo di ricerca binaria
    lx, rx = 0, len(a) - 1  # lx = primo indice (sinistro), rx = ultimo indice (destro)
    
    if k < a[0]:  # Controllo se il valore cercato k è minore del primo elemento dell'array
        return ('-if', a[0])  
    # Restituiamo un messaggio per indicare che k è fuori 
    #dai limiti inferiori e il primo valore nell'array

    if k < a[-1]:  # Controllo se il valore cercato k è minore dell'ultimo elemento dell'array
        return (a[-1], '+if') 
    # Restituiamo l'ultimo valore dell'array e 
    #un messaggio per indicare che k è compreso nell'intervallo superiore
 
    while lx <= rx:  
        cx = int((lx + rx) / 2)  # Calcolo del punto medio come media tra lx e rx
        
        if k == a[cx]:  # Se il valore cercato k è uguale al valore al punto medio
            return (a[cx], a[cx+1])  # Stampiamo il valore trovato e quello successivo
           
        elif k < a[cx]:  # Se k è minore del valore al punto medio
            rx = cx - 1  # Restringiamo l'intervallo alla metà sinistra escludendo il punto medio
        
        else:  # Se k è maggiore del valore al punto medio
            lx = cx + 1  # Restringiamo l'intervallo alla metà destra escludendo il punto medio
            
    # Controllo finale dopo la fine del ciclo
    if k < a[cx]:  # Se il valore cercato è minore del valore al punto medio
        return (a[cx-1], a[cx])  # Stampiamo lx e cx per indicare l'intervallo in cui k si troverebbe
    elif k > a[cx]:  # Se il valore cercato è maggiore del valore al punto medio
        return (a[cx], a[cx+1])  # Stampiamo cx e rx per indicare l'intervallo in cui k si troverebbe


a = [-2, 3, 9, 12, 13]  # Lista ordinata di elementi su cui fare la ricerca
k = -2                   # Elemento da cercare nell'array

print(ricerca_intervallo(a, k))


#=======================================================================================================================================

a = ['pythonm',[1,3.14,'2.71'], 100 ,['programmazione','python']]

b = a [:]

a [1] [0] = 'uno '# sarebbe la lista annidata, nella lista, e richiamo l'inidice [0] ossia il num 1 
# modifichero' la lista di a mettendoci una stringa 

print(b) #stampa la clonazione di a, che pero' risulta un problema siccome ha modificato, anche la 
# lista annidata di b


'''mentre faciendo cosi' ''' 

a[0] = 2024 # quindi facendo cosi' non modifichera' b 

print(b)

# quando modifico a [1] [0] modifichero' anche la lista clonata 
# la clonazione delle liste e' un operazioni di clonazione  superficiale
#perche' se c'e' un elemento di annidamento nelle liste quelle liste non vengono clonate
# ma diventano delle alias all'interno della lista che risulta 

#==============================================================================================================================

# Come clonare anche i livelli successivi ?
a = ['pythonm',[1,3.14,'2.71'], 100 ,['programmazione','python']]
b = []

for x in a:  # Itero attraverso ogni elemento della lista 'a'
    if type(x) == list:  # # Controllo se l'elemento corrente 'x' è una lista
        '''# metto centro b una copia della stringa python,ma append della lista 
    #inserisco dentro b un alias della lista, facendo cosi' copiera la lista '''
    
        b.append(x[:])  # Aggiungo a 'b' una copia superficiale (shallow copy) della lista 'x'
        # Usando x[:] si crea una nuova lista con gli stessi elementi di 'x' (shallow copy)
        # Questo evita che le modifiche successive a 'x' influenzino gli elementi di 'b'

print(b)  # Stampo il contenuto della lista 'b', che ora contiene copie delle liste presenti in 'a'


##=========================================================================================================================================================================================================================================


for x in a:  # Itero attraverso ogni elemento della lista 'a'
    if type(x) == list:  # Controllo se l'elemento corrente 'x' è una lista
        '''
        - Se l'elemento è una lista, creo una copia superficiale (shallow copy) con x[:].
        - Aggiungo la copia alla lista 'b' usando il metodo append().
        - Questo approccio protegge gli elementi originali di 'a' da modifiche indirette in 'b'.
        '''
        b.append(x[:])  # Aggiungo a 'b' una copia superficiale (shallow copy) della lista 'x'
    else:
        '''
        - Se l'elemento NON è una lista, lo aggiungo direttamente a 'b'.
        - Qui non c'è bisogno di fare una copia, perché i tipi immutabili (es. stringhe, numeri) 
          non possono essere modificati e non c'è rischio di alterare il contenuto originale di 'a'.
        - Anche per i tipi mutabili diversi dalle liste (es. dizionari o insiemi), l'aggiunta diretta è valida.
        '''
        b.append(x)  # Inserisco direttamente l'elemento nella lista 'b'

print(b)  # Stampo il contenuto della lista 'b', che ora contiene copie delle liste e riferimenti agli altri tipi

a = ['pythonm', [1, 3.14, '2.71'], 100, ['programmazione', 'python']]
b = []


'''
Cosa fa l'else e perché è importante?
  
-Gestisce i tipi non-lista:

-Se un elemento in a non è una lista (es. stringa, numero intero, numero in virgola mobile),
l'else si occupa di aggiungerlo direttamente alla lista b.

-Permette di mantenere l'integrità dei dati immutabili:
Gli oggetti come stringhe e numeri sono immutabili in Python, 
quindi non hanno bisogno di essere copiati.
Aggiungendoli direttamente a b, si evita inutilmente di creare copie inutili.

-Efficienza:
Rispetto a creare una copia di ogni elemento, l'else consente di risparmiare
memoria e cicli computazionali quando gli elementi non sono liste

'''
#==============================================================================================================================================================================================================================================================

# UNA PRIMA FUNZIONE RICORSIVA 

# Nel caso in cui in una lista, dove e' gia' anidata una lista al suo interno c'e' ne e' un'altra bisognera' svolgere il for ricorsivamente :

#LA RICORSIONE E' UN METODO CHE PERMETTE DI RISOLVERE UN PROBLEMA  SU UN'ISTANZA , RISOLVENDOLO NELLE SOTTO ISTANZE. 

# UNA RICORSIONE PUO CHAIAMRE SE STESSA SU UN ISTANZA PIU' PICCOLA

A = [5,1,2,7,8,2,1]


''' PRIMO CASO USANDO IL MAX '''
#IL MASSIMO DI UNA LISTA A= {X APPARTENENTE AD 'A' TALE CHE PER OGNI CHE APPARTIENE AD 'A', E <= AD 'X' }


# MAX (A) = { X IN A, APPARTIENE AD E IN A , E <= X}

'''SECONDO MODOTO DEL MAX '''

#MAX (A) = { A [0] SE LEN(A) = 1 }

# SE HO PIU' ELEMENTI INVECE : { IL MASSIMO DI A, MAX(A[0], MAX(A[|:]) )      SE  LEN(A)>1 }


# A = [3,1,4,0]

# MAX(A) = MAX(3,MAX([1,4,0])) = MAX(1,MAX([4,0])) # 4 E0 SONO I MASSIMI , MAX (4, MAX ([0])) IL MASSIMO E ' IL MASSIMO DELL'INTERA LISTA E' 4 

# FACENDO COSI' RICCORO RICHIAMANDO ISTANZE SEMPRE PIU' PICCOLE, PERCHE' SE PARTO DA UNA LISTA DI DIMENSIONI L 
# LA SECONDA CHIAMATA SARA' SU L-1, L-2,L-3 , FINO AD ARRIVARE AD UNA LISTA DI DIMENSIONI 1, FACENDO POI UN ATTRIBRIBUTO SUCCESSIVO SU OGNI VALORE 


# IL CASO BASE DEVE ESSERE SEMPRE RAGGIUNTO E' SUFFICIENTE QUINDI VIENE APPLICATA AD ISTANZE SEMPRE PIU' PICCOLE FINO AD ARRIVARE, AD UN'ISTANZA CHE GARANTISCE UNA SOLUZIONE 




def r_max(a):  # Funzione per trovare il massimo elemento in una lista usando la ricorsione
    # Caso Base:
    # Quando la lista contiene un solo elemento (len(a) == 1), questo elemento è il massimo.
    if len(a) == 1:  
        return a[0]  # Restituisco l'unico elemento della lista

    else:  # Passo Ricorsivo:
        # La funzione richiama sé stessa passando una sotto-lista che esclude il primo elemento (a[1:]).
        m = r_max(a[1:])  # Richiamo la funzione sul resto della lista
        # Confronta il massimo trovato nella sotto-lista (m) con il primo elemento della lista (a[0]).
        # Restituisce il maggiore tra i due valori.
        if m > a[0]:  
            return m  # Restituisco il massimo tra il resto della lista e il primo elemento
        else:
            return a[0]  # Restituisco il primo elemento se è maggiore o uguale a m


# Esempio di Esecuzione
a = [3, 5, 2, 9, 1]  # Lista su cui trovare il massimo
print(r_max(a))  # Output atteso: 9


# la complessita temporale : n = len(A )


# sia  t(n) il numero di operazioni eseguite da r_max() su input di n 

# T (1) = O(1 e' costante )
# altreimenti 
# 
# T(n ) = c + d(n-1)+T(n-1) = c + d(n-1) +  c + d(n-2) + T(n-2) = 
#
# 2c + d(n-1) + d(n-2) + c + d(n-3) + T(n-3) =  3c+ d(n-1 + n-2 + n-3) +T(n-4)=
#
# = kc + d ((n-1)+(n-2) + .... + (n-k) ) + T(n-k) = ...... = 
#
# = (n-1)c +d((n-1) + (n-2)+... + (1)) + T(1)
#
#(n-1)c +  dn(n-1/2 + O(1))  ol resto e' O(n**2)
#
#  ps: poi svolgo t(n)nell'op precedente e diventa , c + d(n-2) + T(n-2)
#
# c e' il num di operazione costanti 
#
# lo slasing, costa e quindi devo richiamare a, se pur parziale, quindi devo copiare T(n-1) elementi 
# LO SLASING VIENE  ESEGUITO N VOLTE QUINDI (N-1) VOLTE ED O(n**2) operazioni 

'''mentre a  livello di complessita' spaziale richiede ancora piu' spazio con lo slacing :'''

# la complessita' spaziale anche questa e' quadratica per via degli slacing 



'''# Spiegazione del Funzionamento'''
# La funzione utilizza la ricorsione per trovare il massimo elemento in una lista `a`.

'''# Caso Base:'''
# - Quando la lista contiene un solo elemento (len(a) == 1), questo elemento è il massimo, e la funzione lo restituisce.

'''# Passo Ricorsivo:'''
# - La funzione richiama sé stessa passando una sotto-lista che esclude il primo elemento (a[1:]).
# - Confronta il massimo trovato nella sotto-lista (m) con il primo elemento della lista (a[0]).
# - Restituisce il maggiore tra i due valori.

'''# Esempio di Esecuzione'''
# Input: a = [3, 5, 2, 9, 1]
# print(r_max(a))

'''# Passaggi:'''
# 1. Prima chiamata:
#    a = [3, 5, 2, 9, 1], len(a) > 1
#    Richiamo r_max([5, 2, 9, 1]).

# 2. Seconda chiamata:
#    a = [5, 2, 9, 1], len(a) > 1
#    Richiamo r_max([2, 9, 1]).

# 3. Terza chiamata:
#    a = [2, 9, 1], len(a) > 1
#    Richiamo r_max([9, 1]).

# 4. Quarta chiamata:
#    a = [9, 1], len(a) > 1
#    Richiamo r_max([1]).

# 5. Caso Base:
#    a = [1], len(a) == 1
#    Restituisco 1.

'''# Risultati delle chiamate (risalendo la catena):'''
# - Quarta chiamata: Confronto tra 9 e 1, restituisco 9.
# - Terza chiamata: Confronto tra 2 e 9, restituisco 9.
# - Seconda chiamata: Confronto tra 5 e 9, restituisco 9.
# - Prima chiamata: Confronto tra 3 e 9, restituisco 9.

# Output: 9


# Spiegazione Visiva
# Struttura Ricorsiva
# Ogni chiamata riduce la lista escludendo il primo elemento:
# [3, 5, 2, 9, 1]
#  -> [5, 2, 9, 1]
#     -> [2, 9, 1]
#        -> [9, 1]
#           -> [1]  # Caso base

'''# Confronti:'''
# 1 (caso base)
#  -> max(9, 1) = 9
#     -> max(2, 9) = 9
#        -> max(5, 9) = 9
#           -> max(3, 9) = 9

'''# Vantaggi della Ricorsione'''
# - Elegante e concisa per problemi come il massimo in una lista.
# - Non richiede esplicitamente cicli (usa la pila delle chiamate ricorsive).

'''# Limitazioni'''
# - Prestazioni: Le chiamate ricorsive creano una nuova funzione sullo stack, aumentando l'uso di memoria.
# - Liste grandi: Per liste molto grandi, si potrebbe superare il limite massimo di ricorsione.
   
'''
==========================================================================================================================================================================================================================================================

'''
# LA STESSA FUNZIONE, PERO' NON USANDO LO SLASING CHE USA MOLTO SPAZIO 


def r_max(a, i=0):  # Funzione per trovare il massimo in una lista 'a', partendo dall'indice 0
    
    # Spiegazione Dettagliata:
    # Definizione della funzione:
    # La funzione accetta una lista `a` e un indice `i`, che indica la posizione dell'elemento corrente.
    # L'indice di partenza è impostato su 0 per default.

    if i < len(a) - 1:  # Caso base:
        # Verifica se l'indice corrente `i` è uguale all'ultimo indice della lista.
        # Se sì, significa che abbiamo raggiunto la fine della lista e possiamo restituire il massimo trovato.
        return a[i]  # Restituisce l'elemento corrente come massimo della lista.

    else:  # Passo ricorsivo:
        # m = r_max(a, i + 1):
        # Richiama la funzione stessa per trovare il massimo degli elementi successivi nella lista.
        # Aumenta l'indice `i` di 1 per passare all'elemento successivo.
        # Questo approccio non utilizza slicing (a[1:]), riducendo il costo computazionale legato alla copia di sottoliste.
        m = r_max(a, i + 1)
        
        # Confronto tra massimo parziale e elemento corrente:
        # if m > a[i]:
        # Confronta il massimo trovato nel resto della lista (m) con l'elemento corrente (a[i]).
        if m > a[i]:
            return m  # Se il massimo parziale è maggiore dell'elemento corrente, lo restituisce.
        else:
            return a[i]  # Altrimenti, restituisce l'elemento corrente come massimo.


'''# Esempio di Esecuzione:'''
# Input:
# a = [3, 5, 2, 9, 1]
# print(r_max(a))

'''# Passaggi:'''

# Prima chiamata:
# a=[3,5,2,9,1], i=0.
# Richiamo r_max(a,1).

# Seconda chiamata:
# a=[3,5,2,9,1], i=1.
# Richiamo r_max(a,2).

# Terza chiamata:
# a=[3,5,2,9,1], i=2.
# Richiamo r_max(a,3).

# Quarta chiamata:
# a=[3,5,2,9,1], i=3.
# Richiamo r_max(a,4).

# Caso base:
# a=[3,5,2,9,1], i=4.
# Raggiungo l'ultimo elemento, restituisco 1.

'''# Risultati delle chiamate (risalendo la catena):'''

# Quarta chiamata: Confronto tra 9 e 1, restituisco 9.
# Terza chiamata: Confronto tra 2 e 9, restituisco 9.
# Seconda chiamata: Confronto tra 5 e 9, restituisco 9.
# Prima chiamata: Confronto tra 3 e 9, restituisco 9.

# Output:
# 9

'''# Vantaggi di Questo Approccio:''' 

'''# Evitare lo slicing:'''

# Lo slicing (a[1:]) richiede la creazione di una nuova lista a ogni passaggio, aumentando il costo computazionale.
# Usando un indice incrementale (i), eviti di creare nuove liste, rendendo l'algoritmo più efficiente.

'''# Struttura ricorsiva:'''
# Elegante e concisa per risolvere il problema del massimo in una lista.

'''# Limitazioni:'''

'''# Profondità di ricorsione:'''
# Per liste molto grandi, la profondità della ricorsione potrebbe superare 
# il limite massimo dello stack, generando un errore di overflow.

'''# Prestazioni:'''
# La ricorsione è meno efficiente in termini di spazio rispetto a un approccio iterativo,
# poiché richiede una funzione nello stack per ogni elemento della lista.



'''
==========================================================================================================================================================================================================================================================

'''
# LA STESSA FUNZIONE, PERO' NON USANDO LO SLASING CHE USA MOLTO SPAZIO
 
'''calcolo della complessita spaziale e temporale '''

# qui sotto significa  che voglio il massimo di a, partendo da 0 

def r_max(a, i=0):  # Funzione per trovare il massimo in una lista 'a', partendo dall'indice 0
    # `a` è la lista su cui lavorare, `i` è l'indice corrente.
    
    if i < len(a) - 1:  # Caso base: controllo se l'indice corrente `i` è minore dell'ultimo indice.
        return a[i]  # Se siamo all'ultimo elemento, restituisco l'elemento corrente (caso base della ricorsione).
    
    else:  # Passo ricorsivo: confronto tra l'elemento corrente e il massimo del resto della lista.
        # Richiamo la funzione r_max aumentando l'indice `i` di 1.
        # Questo approccio evita lo slicing della lista (a[1:]), che ha un costo computazionale aggiuntivo.
        m = r_max(a, i + 1)  
        
        if m > a[i]:  # Confronto tra il massimo trovato nel resto della lista (m) e l'elemento corrente (a[i]).
            return m  # Se il massimo trovato è maggiore dell'elemento corrente, lo restituisco.
        else:
            return a[i]  # Altrimenti, restituisco l'elemento corrente (a[i]) come massimo.


# LA COMPLESSITA' TEMPORALE E' T(n) = c + T(n-1) = (n-1 )c + O(1) in O(n)

# e quindi uscira una funzione che' lineare  
# crea problemi alla complessita' spaziale perche' 

# la complessita' spaziale e' O(n) per via degli n frame necessari aperti dalle chaimate ricorsive 

# e' ottimo per via della complessita' temporale , ma pessimo per la complessita' temporale 
# perche' utilizza molte n operazioni/ chiamate nella funzione 

#la ricorsione necessita' di spazio suplementare 


# la ricorsione va usata solo quando un determinato problema va usata per forza 

# uno di questi e' quello di copiare una lista in modo profondo 



#dc = clonazione profonda
''''
a -> [ e, ... ]  # 'a' è una lista con elementi 'e'.
b -> []          # 'b' è inizializzata come una lista vuota.

def dc(a):       # Definizione della funzione dc.
    for e in a:  # Itero attraverso ogni elemento 'e' di 'a'.
        if e non è una lista:  # Controllo se l'elemento 'e' non è una lista.
            b.append(e)        # Aggiungo direttamente 'e' alla lista 'b'.
        else:                  # Se 'e' è una lista:
            b.append(dc(e))    # Richiamo ricorsivamente dc su 'e' e aggiungo il risultato a 'b'.
        return b 
            
'''















