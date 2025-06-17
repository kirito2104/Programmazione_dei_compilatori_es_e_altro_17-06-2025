#La funzione range(). Il metodo join() del tipo str e come usarlo per evitare concatenazioni ripetute.
# L'operatore di assegnazione tra liste e aliasing; copiare una lista (clonazione). La funzione id()


''' n operazioni di append hanno costo lineare (costante )'''


a = [ ('A', 2, 7), ('B', 3, -1), ('C', 0, 1), ('D', -2, -2) ]
r = 2.9

# n = len(a)

# Creare una lista che contiene i nomi dei punti in a a distanza al più r da (0, 0,0)
b = []

for nome, x, y in a:
    if x**2 + y**2 <= r**2:
        b.append(nome)  # Tempo costante "in media" O(1)

print(b)
# il costo complessivo del programma e' 0(n)

# Complessità temporale è O(n) e' la somma dei costi di n operazioni in cui il costo di ciascun operazione e' costante in media 
# complessivate l'algortmo ha un costo lineare in media 
# in media ? 
# proprieta :nel caso peggiore  n  append () consecutivamente costano complessivamente O(n) 
'''
** LA COMPLESSITA' TEMPORALE CALCOLA IL CASO PEGGIORE DEL PROGRAMMA NON IN MEDIA **
*
* QUINDI L'ALGORITMO PRECEDENTE HA COMPLESSITA'  TEMPORALE O(N)
* NEL CASO PEGGIORE 
*
''' 


#La complessità temporale è **O(n)** perché l'algoritmo itera su tutti gli elementi della lista `a` 
# (di dimensione `n`) e per ciascun elemento esegue operazioni costanti: calcola la condizione 
# `x**2 + y**2 <= r**2` e, se vera, aggiunge il nome del punto alla lista `b` usando `append()`,
# che ha costo medio **O(1)**. 
# Complessivamente, il costo è proporzionale al numero di elementi nella lista, quindi **O(n)**.

#===========================================================================================================================================================================================================================================================================

# HO UNA LISTA E' 

def trova_posizioni (a,v):
    '''
    Input : a una lista , v un valore 
    return : una lista di interi contenente le posizioni di v in a 
    
    
    - Ritorna una lista di interi che rappresentano le posizioni in cui `v` appare nella lista `a`.
    '''
    
    # n = len di a
    
    
    b = []  # Inizializza una lista vuota per memorizzare le posizioni di `v` in `a`.

    i = 0  # Inizializza un indice `i` per scorrere la lista `a`.

    # Si utilizza un ciclo `while` invece di un ciclo `for` per avere maggiore controllo sull'indice.
    while i < len(a):  # Il ciclo continua finché `i` è minore della lunghezza della lista `a`.
        # il while ha costo costante di O(1)
        '''
        se questo ciclo  ha tempo lineare solo se la condizio'''
        
        if a[i] == v:  # Controlla se l'elemento nella posizione `i` della lista `a` è uguale a `v`.
            b.append(i)  # Se sì, aggiunge l'indice `i` alla lista `b`.
            '''append siccome ha un costo costante di quando aggiunge nella lista e la media del costo e' O(1) '''
        i += 1  # Incrementa l'indice `i` per passare all'elemento successivo nella lista.
    
    return b  # Ritorna la lista `b`, contenente tutte le posizioni in cui `v` appare in `a`.

'''
complessita' temporale : nel caso peggiore dove la memoria e' piena il costo sara lineare ossia O(n) ossia itera costantemente su n oggetti nel programma

le operazioni costose e non costose in una struttura di dati, come un array dinamico. 
Le operazioni costose, come la riallocazione della memoria quando l'array è pieno, richiedono tempo elevato (O(n)) 
perché comportano la copia di tutti gli elementi in un nuovo array più grande. 
Tuttavia, queste operazioni sono rare


'''



# Esempio di utilizzo della funzione
a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]  # Una lista di numeri
p = trova_posizioni(a, 6)  # Trova tutte le posizioni del valore `6` nella lista `a`

print('Stampa la lista delle posizioni:', p)  # Stampa le posizioni trovate

#======================================================================================================================================================================================================================================


a = [ ('A', 2,7), ('B',3, -1), ('C', 0, 1), ('D', -2,-2) ]
r = 2.9

# n = len(a)

# creare una lista che contiene i nomi dei punti in a a distanza al 
# più r da (O, 0,0)

b = []

for nome, x, y in a:
    if x**2+y**2 <= r**2:
        b.append(nome) # tempo costante "in media" O(1)
    
print(b)

# complessità temporale è O(n) in media?
#
# proprietà: nel caso peggiore n append() consecutivi
#    costano complessivamente O(n)
# 
# quindi l'algoritmo precedente ha complessità temporale O(n)
# nel caso peggiore

# In[]

def trova_posizioni(a, v):
    '''
    Input: a una lista, v un valore
    Return: una lista di interi contenente le posizioni di v in a
    '''
    
    # n = len(a)
    
    b = []
    
    i = 0
    # questo cliclo nel caso peggiore va O(n)
    
    while i < len(a): # O(1) 
        
        
        if a[i] == v: # O(1) perché indicizzazione ha costo costante
            # ha costo costante perche' nelle liste e l'iterazione e costante di O(1)
            
            b.append(i)
        i += 1
        
        # e' lineare perche' esegue n volte le operazioni,
        # pero' un volta eseguito questo ciclo piu' volte ha sempre un tempo costante 
    return b

    # complessità temporale O(n) nel caso peggiore



a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
p = trova_posizioni(a, 6)
print(p)
#--------------------------------------------------------------------------------------------------------------------------------

# In[]




# Definizione di una lista di numeri
a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]  # Lista contenente numeri interi

# Calcolo della lunghezza della lista
n = len(a)  # La funzione `len(a)` restituisce il numero di elementi nella lista `a`. In questo caso, n = 13.

# Iterazione sulla lista `a` utilizzando un ciclo `for`
# Il ciclo `range(n)` genera una sequenza di numeri da 0 a `n-1`, corrispondenti agli indici validi di `a`.
for i in range(n):
    # `i` rappresenta l'indice corrente della lista `a`.
    # Utilizziamo `a[i]` per accedere all'elemento della lista alla posizione `i`.
    print(a[i])  # Stampa l'elemento di `a` corrispondente all'indice `i`

#LA FUNZIONE RANGE CREA INTERNAMENTE UN LISTA  CHE VA DA 0 A N-1 
# USANDO QUESTO CODICE FARO' IN MODDO CHE IL PROGRAMMA SIA PIU' COMPATTO  



#-----------------------------------------------------------------------------------------------------------------------------------
# VERSIONE TROVA FUNZIONE CON IL FOR 
def trova_posiz(a, v):
    """
    Funzione per trovare tutte le posizioni di un valore specifico in una lista.
    
    Parametri:
    ----------
    a: list
        La lista in cui cercare il valore `v`.
    v: qualsiasi tipo
        Il valore da cercare nella lista `a`.

    Ritorno:
    --------
    list
        Una lista contenente tutte le posizioni (indici) in cui `v` appare nella lista `a`.
    """

    b = []  # Inizializza una lista vuota `b` per memorizzare gli indici in cui `v` appare nella lista `a`.

    # Iterazione sulla lista `a` utilizzando un ciclo `for` con un intervallo definito da `len(a)`
    for i in range(len(a)):
        # L'istruzione `if` controlla se l'elemento alla posizione `i` di `a` è uguale a `v`.
        if a[i] == v:  
            # Se la condizione è soddisfatta, aggiunge l'indice `i` alla lista `b`.
            b.append(i)  # `append()` aggiunge un nuovo elemento alla fine della lista `b`.

    return b  # Ritorna la lista `b` contenente tutti gli indici trovati.


a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8,5]  # Lista contenente numeri interi
p = trova_posiz (a,5)

print(p)

#-------------------------------------------------------------------------------------------------------------------------------------------------

a = 'programmazione dei compilatori '

# n = len(a)


b = ' '

# Itera su ogni elemento della sequenza `a`

for x in a: 
    
    # Controlla se il carattere `x` è una vocale (sia maiuscola che minuscola)
    
    if x in 'aeioAEIOU':  # qui il costo e' O(1), perche' esegue operazioni costanti 
            # esegue sempre allo stesso costo di tempo la funzione che sono al massimo 10 volte 
        
        # Se `x` è una vocale, aggiunge un asterisco '*' alla stringa `b`
        b += '*'  
    
    # Controlla se il carattere `x` è un numero compreso tra '0' e '9'
    # Se `x` è un numero, aggiunge il simbolo `#` alla stringa `b`
    
    elif x >= '0' and x <= '9':  # ricerca in modo costante tra la posizione tra 0 a 9 della lista 
        # quindi e' O(1)
        # questa funzionepero' copia la stinga precedente e' la sostituisce, tutto cio' richiede un costo 
        # il costo complessivo sara' dato dalla somma complessiva ossia 1+2+3+n 
        
        #quindi in questo elif : il costo e' costante ed e' n+1 perche' ogni volta che esegue un operazione,
        #la esegue n volte, incrementendo sempre di 1
        
        # fancenddo cosi'  la somma totale delle operazioni e' data da 
        
        #  n ∑ /i = 1   = i = 1 +2+3+...+ (n-2)+ (n-1) +n
        # facenddo come qui sopra sommando : i valori 1 + n, 2 + (n-1) e + 3 + (n-2) tutti loro daranno come risultato
        # n+1 perche' sono simmetrici, avro' quindi diverse coppie formate da elementi speculari n/2(n+1) e O(n²)
         # teta O(n²) , I COSTO DELL'ALGORITMO E' QUADRATICO 
        
        '''# Usi di Θ(N²):
        # - Si usa per descrivere il comportamento preciso dell'algoritmo.
        # - Indica che N² rappresenta sia un limite superiore che inferiore, 
        # quindi il tempo di esecuzione è strettamente proporzionale a N².

        # Differenza Chiave tra O(N²) e Θ(N²):
        # - O(N²): Limite superiore (crescita massima). Può crescere più lentamente di N².
        # - Θ(N²): Limite superiore e inferiore (crescita esatta). Cresce esattamente come N².
        '''
        
        b += '#'  
    
    # Se il carattere `x` non è né una vocale né un numero
    
    else:  
        # Aggiunge uno spazio vuoto ' ' alla stringa `b`
        b += ' '  

 # NUMERO DI OPERZAZIONI  = 1 + 2+..... +(N-2)+ (n-1)+n IN Theta(N²)
 # quindi la complessita' temprale  e' quadratica  
 
 
 
print(a)
print(b)




''' qui sopra elif ogni volta che esegue la ricerca: '''

# Calcolo della complessità per `b = b + 'c'`
# ------------------------------------------
# Ogni volta che si esegue l'operazione `b = b + 'c'`, viene effettuata una copia completa 
# della stringa `b`, e poi viene aggiunto il nuovo carattere `'c'`.
# Se `b` ha lunghezza `i`, l'operazione richiede **i operazioni** per copiare tutti i caratteri 
# della stringa esistente.
# Se ripetiamo questa operazione **n** volte (dove `n` è il numero di iterazioni), il costo totale sarà:
# 
# 1 + 2 + 3 + ... + n
#
# ------------------------------------------

# Somma totale delle operazioni
# -----------------------------
# La somma dei primi **n numeri interi** si calcola con la formula della somma aritmetica:
#
#   n/∑ /i=1 --- i (da 1 a n) = (n * (n + 1)) / 2
#
# Questo è il costo totale in termini di operazioni necessarie.
#
# Costo dominante:
# ----------------
# L'operazione cresce quadraticamente rispetto al numero di iterazioni, quindi la complessità temporale è **O(n²)**.

# ------------------------------------------
# Rappresentazione visuale:
# -------------------------
# Somma cumulativa delle operazioni:
# - Ogni iterazione aggiunge un costo crescente:
#     1 + 2 + ... + (n-1) + n
#
# Crescita della stringa:
# - Alla prima iterazione: b = 'c' (1 operazione),
# - Alla seconda iterazione: b = 'cc' (2 operazioni),
# - Alla terza iterazione: b = 'ccc' (3 operazioni),
# - E così via, fino alla lunghezza finale **n**.

# ------------------------------------------
# Conclusione:
# ------------
# La complessità dell'operazione `b = b + 'c'` ripetuta **m** volte è **O(m²)**.
# Questo succede perché ogni concatenazione di stringhe implica la copia completa di tutte 
# le iterazioni precedenti, portando a una crescita quadratica del costo totale.


''' E TETA DI O(N) PERCHE': 
# -----------
# La formula rappresenta il numero totale di operazioni necessarie per concatenare la stringa `b` 
# usando l'operazione `b = b + 'c'` per m iterazioni. 
# La complessità temporale risultante è quindi **O(n²)**.
'''

'''# Perché la complessità temporale è Θ(n²)
# ---------------------------------------
# Quando usiamo l'operazione `b = b + 'c'` in un ciclo, ad ogni iterazione la stringa `b` 
# viene **copiata interamente** prima di aggiungere il nuovo carattere `'c'`. 
# Questo accade perché le stringhe in Python sono **immutabili**:
# - Ogni modifica a una stringa crea una **nuova stringa** e copia l'intera stringa precedente.

# Analisi del ciclo
# -----------------
# Supponiamo di eseguire l'operazione `b = b + 'c'` per `n` iterazioni:
# - Alla **prima iterazione**, `b` è vuota, quindi la concatenazione richiede **1 operazione**.
# - Alla **seconda iterazione**, `b` contiene un carattere, quindi la concatenazione richiede **2 operazioni**.
# - Alla **terza iterazione**, `b` contiene 2 caratteri, quindi la concatenazione richiede **3 operazioni**.
# - E così via, fino all'**n-esima iterazione**, dove la concatenazione richiede **n operazioni**.

# Somma totale delle operazioni
# -----------------------------
# Il numero totale di operazioni eseguite è dato dalla somma:
# 1 + 2 + 3 + ... + n
# Questa somma può essere calcolata con la formula della somma dei primi `n` numeri interi:
#    Somma totale = (n * (n + 1)) / 2
#
# perche' fa n**2 e n+1 ed lo stesso e sse faccio la formula con n+2 che farebbe n**2  e n+2  ed e' sempre n**2 la forma dominante 


# La parte dominante di questa formula è il termine quadratico `n²`, quindi il costo totale è **Θ(n²)**.

# Differenza tra O(n²) e Θ(n²)
# ----------------------------
# - **O(n²)**: Indica il limite superiore della complessità. Questo significa che il tempo di esecuzione 
#   **non sarà mai peggiore** di `n²`.
# - **Θ(n²)**: Indica che il tempo di esecuzione è **esattamente quadratico**, ossia rappresenta sia il limite superiore
#   che il limite inferiore della complessità.

# Conclusione
# -----------
# L'operazione di concatenazione `b = b + 'c'` in un ciclo comporta un costo crescente (da 1 a `n`), 
# e quindi la somma totale è proporzionale a `n²`. Per questo motivo, la complessità temporale dell'algoritmo è **Θ(n²)**.
'''


#-------------------------------------------------------------------------------------------------------------------------------

# ogni volta che una stringa che e' imutabile viene modificata,viene copiata in una nuova stringa
# tutto cio' pero' ha un costo e tale non e' ottimale perche' richiede piu' tempo, per evitare cio'
# usiamo 'append' per far si che il costo della funzione sia lineare e non quadratica, creando pero' una lista 



a = 'pr0grammaz10ne de1 c4lc0lator1'

# n = len(a)

# Stampa a ed sottolineare con * le vocali e con # le
# cifre decimali
#
# Esempio
#
# pr0grammaz10ne de1 c4lc0lator1
#   #  *  * ## *  *#  #  # * * #

# Inizializza una lista vuota `b` che verrà usata per memorizzare i simboli corrispondenti ai caratteri in `a`
b = []

# Scorre ogni carattere della sequenza `a` usando un ciclo `for`
for x in a: 
    
    # Controlla se il carattere `x` è una vocale (sia maiuscola che minuscola)
    if x in 'aeiouAEIOU':  # Questa operazione ha complessità O(1) perché verifica l'appartenenza a una stringa fissa
        
        b.append('*')  # Se `x` è una vocale, aggiunge l'asterisco `*` alla lista `b`
    
    # Se il carattere `x` non è una vocale, controlla se è un numero
    
    elif x >= '0' and x <= '9':  # Questa operazione ha complessità O(1) perché effettua un confronto tra caratteri
        b.append('#')  # Se `x` è un numero, aggiunge il simbolo `#` alla lista `b`
    
    # Se il carattere `x` non è né una vocale né un numero
    
    else: # avra' un costo costante ogni volta che controlla che le opz. sopra non sono verificate quindi sara' O(1)
        
        b.append(' ')  # Aggiunge uno spazio `' '` alla lista `b`  , 
        # avra' un costo costante ogni volta che aggiunge uno spzio alla lista 


print(a)# Stampa la lista `a` originale


print(''.join(b))# Stampa la lista `b` che contiene i simboli corrispondenti ai caratteri in `a`
# questa operzazione qui sopra contiene una lista con n caratteri tanti quanti sono le stringhe
# quanti i caratteri della stringa, tale ha un costo linerare in n quindi e' di O(n)
# qualsiasi ddato e' un oggetto , join il costo e' quello della dimensione deta dalle dimensioni di b 


 



'''# Il metodo `join` in Python serve a unire gli elementi di una lista (o di un'altra sequenza) in una singola stringa,
# utilizzando una stringa separatore specificata.

# Spiegazione di `print(''.join(b))`:
# -----------------------------------
# 1. `b` è una lista:
#    - La lista `b` contiene i caratteri o stringhe generati durante il ciclo.
#    - Ad esempio, se `b = ['*', '#', ' ', '*', '#', ' ']`, è una lista di stringhe.

# 2. `''.join(b)`:
#    - La stringa vuota (`''`) è il separatore specificato.
#    - Il metodo `.join()` prende tutti gli elementi della lista `b` e li concatena in un'unica stringa, 
#      senza inserire nulla tra gli elementi (perché il separatore è vuoto).
#    - Risultato: Se `b = ['*', '#', ' ', '*', '#', ' ']`, `''.join(b)` restituisce la stringa `'*# *# '`.

# 3. `print(''.join(b))`:
#    - Stampa la stringa ottenuta dalla concatenazione degli elementi della lista `b`.
#    - Questa operazione è utile per ottenere un output leggibile o per creare una rappresentazione compatta dei dati.

# Esempio pratico:
# ----------------
# Se `b = ['*', '#', ' ', '*', '#', ' ']`:
# - Con il metodo `join` senza separatore:
#   ''.join(b) restituirà `'*# *# '`.
# - Con un separatore diverso (ad esempio uno spazio):
#   ' '.join(b) restituirà `'* #   * #  '`.

# Quando serve `join`:
# ---------------------
# Il metodo `join` è utile nei seguenti casi:
# 1. Creare una stringa a partire da una lista: Ad esempio, per trasformare una lista di caratteri in una parola o frase.
# 2. Ottimizzare concatenazioni multiple: Concatenare stringhe in una lista è più efficiente con `join` rispetto a fare ripetuti `+`.
# 3. Formattare un output personalizzato: Aggiungere separatori specifici (es. virgole, spazi) tra elementi.

# Conclusione:
# ------------
# In questo caso, `print(''.join(b))` serve a stampare la lista `b` come una singola stringa, combinando tutti i suoi elementi
# in un formato leggibile, senza separatori aggiuntivi.
'''
#__________________________________________________________________________________________________________________________________________

# capitalize ----> rende maiuscccccola la prima lettera 
# isalnum -----> che  che da True o False in base se contiene solo caratteri alfanumerici 
# join  concatena piu' stringhe tra di loro 
#c.join (['primo','seconddo']) --> unira' le due stringhe in unica 

#------------------------------------------------------------------------------------------------------------------------------------------------------
#in []

# n = len (a) 

a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8] 
# n = len(a)

b = a # il costo di quest'operazione O(1) perche' un aliasing O(1) ed non e' una copia 
# MA E' UN NOME ALTERNATIVO AD A e quindi potro' fare riferimento ad a mettendo b 


b[0] =100 # uscira' [100, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8] e quindi mi accorgo che modifica effettivaamente a 

print(a)

# lo slicing crea una sotto lista 
''' SE INVECE VOGLIO COPIARE UNA LISTA FACCIO: '''

c = a [:] # copia di a O(n) con costo lineare 
# facendo cosi' copiera' l'intera  lista 

# Costo dell'operazione
# ---------------------
# Operazione per elemento:
# - Copiare ogni elemento è un'operazione a costo costante O(1).
#
# Costo totale:
# - Per una lista di lunghezza `n`, sono necessarie `n` operazioni, una per ogni elemento.
# - Il costo totale è quindi O(n) (lineare) rispetto alla lunghezza della lista.

'''# Esempio
# -------
# Supponiamo che:
# a = [1, 2, 3, 4, 5]
# c = a[:]
#
# Python scorre ogni elemento di `a`:
# - Copia `1` nella nuova lista `c`.
# - Copia `2` nella nuova lista `c`.
# - Copia `3` nella nuova lista `c`.
# - Copia `4` nella nuova lista `c`.
# - Copia `5` nella nuova lista `c`.
#
# Il numero totale di operazioni è pari alla lunghezza di `a`, che è 5.

# Differenza rispetto ad altre operazioni
# ---------------------------------------
# c = a:
# - Qui non viene effettuata alcuna copia. `c` diventa semplicemente un riferimento alla stessa lista di `a`.
# - Costo: O(1) (solo un'assegnazione).
#
# c = a[:]:
# - Crea una nuova lista copiando tutti gli elementi di `a`.
# - Costo: O(n) (lineare rispetto alla lunghezza di `a`).

# Conclusione
# -----------
# L'operazione `c = a[:]` ha un costo lineare O(n) perché deve scorrere tutti gli elementi 
# della lista `a` per copiarli nella nuova lista `c`.
# Questo comportamento è necessario per creare una nuova lista distinta da `a`.

'''



print('ecco la lista copiata :',c) # stampa la lista copiata

a[1] = 200
print(b)
print(a)

print(id(a)) # id legge l'id unico di a, da quando nasce che sara' unico 
print(id(b)) # avranno lo stesso id perche' a e b sono la stessa cosa 

''' e quindi si nota che entrambi sono la stessa cosa, avendo un valore univoco unico '''
print(id(c)) # qui si notera' che id ha un ' indirizzo univoco diverso dagli altri 
#-------------------------------------------------------------------------------------------------------------------------------------

''' 
quindi  a --->>>  [3,0,4,9]
b= a  # sara un alias  ossia richioma a 
e si portra usare pure b per modificare a che sonbo la stessa cosa quindi --->  [3,0,4,9]

mentre c = a[:] copiera la lista e quindi sara' un altra  lista diversa ---->   [3,0,4,9]




'''


#------------------------------------------------------------------------------------------------------------------------------
#Es: 

# data una lista 

def del_item(a,v):
    '''
    input: a una lista : v un valore 
    return : None 
     
    Descrizione:
    - Elimina da `a` tutte le occorrenze del valore `v`.
    '''



  # Ciclo per iterare su ogni elemento della lista `a`
''' for e in a:  
        # Controlla se l'elemento corrente `e` è uguale al valore `v`
        if e == v:  
            # Qui si tenta di eliminare `e` con l'operazione `del(e)`, ma questo è concettualmente errato.
            # `e` è una variabile locale del ciclo e non una posizione o un riferimento diretto agli elementi della lista.
            del (e)  # Questo non elimina effettivamente l'elemento dalla lista.

    ''' # La funzione termina, ma la lista non viene modificata correttamente.

# Lista di esempio
a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8] 

# Chiamata della funzione per eliminare tutte le occorrenze del valore `1`
del_item(a, 1)

# Stampa della lista `a` dopo la chiamata della funzione
print(a)  # La lista rimarrà invariata a causa dell'errore logico sopra.
'''Facendo cio' risulta errato perche' andrebbe ad eliminare tutto :'''


#--------------------------------------------------------------------------------------------------------------------------------------------------
def del_item(a, v):
    '''
    input:
    - a: una lista
    - v: un valore da rimuovere dalla lista `a`

    return:
    - None (modifica direttamente la lista `a` in-place)

    Descrizione:
    - Elimina tutte le occorrenze del valore `v` dalla lista `a`.
    '''

    # Ciclo per iterare sugli indici della lista `a`
    '''for i in range(len(a)):  # Itera da 0 all'indice `len(a) - 1`
        # Controlla se l'elemento all'indice `i` è uguale a `v`
        if a[i] == v:  
            # Elimina l'elemento all'indice `i` dalla lista `a`
            del a[i]  # Modifica direttamente la lista `a`
            # Dopo questa eliminazione, gli indici degli elementi successivi si spostano indietro,
            # causando problemi nel ciclo.

    
'''
# Lista di esempio
a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]

# Chiamata della funzione per eliminare tutte le occorrenze del valore `1`
del_item(a, 1)

# Stampa della lista `a` dopo l'eliminazione
print(a)
#-----------------------------------------------------------------------------------------------------------------------------------------------



# Quando usare il ciclo `for` in Python
# -------------------------------------
# Il ciclo `for` in Python è efficace nei seguenti casi, purché non si modifichi la lista durante l'iterazione:

# 1. Iterazione su elementi senza modificare la lista:
#    - Il ciclo `for` è perfetto per leggere o eseguire operazioni sugli elementi della lista senza alterarne il contenuto.
#    - Esempio:
#        a = [1, 2, 3, 4]
#        for x in a:
#            print(x * 2)  # Moltiplica ogni elemento per 2 (solo in output)

# 2. Creazione di una nuova lista (senza alterare l'originale):
#    - Puoi usare il ciclo `for` per costruire una nuova lista a partire da quella originale, senza modificarla.
#    - Esempio:
#        a = [1, 2, 3, 4]
#        b = []
#        for x in a:
#            b.append(x * 2)  # Crea una nuova lista con elementi moltiplicati per 2
#        print(b)  # Output: [2, 4, 6, 8]

# 3. Raccolta di dati o esecuzione di operazioni cumulative:
#    - Usare il ciclo `for` per calcolare valori aggregati (ad esempio, somma o conteggio).
#    - Esempio:
#        a = [1, 2, 3, 4]
#        total = 0
#        for x in a:
#            total += x  # Somma tutti gli elementi
#        print(total)  # Output: 10

# 4. Filtrare dati senza alterare la lista:
#    - Il ciclo `for` è ottimo per filtrare elementi, costruendo una nuova lista con quelli desiderati.
#    - Esempio:
#        a = [1, 2, 3, 4, 5]
#        even_numbers = []
#        for x in a:
#            if x % 2 == 0:
#                even_numbers.append(x)  # Aggiunge solo i numeri pari
#        print(even_numbers)  # Output: [2, 4]

# 5. Stampare o analizzare dati:
#    - Se devi solo stampare, analizzare o verificare gli elementi della lista senza modificarli.
#    - Esempio:
#        a = [1, 2, 3, 4]
#        for x in a:
#            if x > 2:
#                print(f"Valore maggiore di 2: {x}")

# Quando evitare di usare il ciclo `for`
# --------------------------------------
# Non è ottimale usare il ciclo `for` nei seguenti casi:

# 1. Modifica della lista durante l'iterazione:
#    - Quando si rimuovono o aggiungono elementi alla lista durante l'iterazione.
#    - Problema: Modificare una lista provoca uno spostamento degli indici, portando a errori o comportamenti inattesi.
#    - Esempio:
#        a = [1, 2, 3, 4]
#        for i in range(len(a)):
#            if a[i] == 2:
#                del a[i]  # Dopo questa operazione, gli indici si spostano.

# Alternative per evitare problemi
# ---------------------------------
# 1. Utilizzo di una lista di comprensione:
#    - Soluzione elegante per creare una nuova lista filtrata.
#    - Esempio:
#        a = [1, 2, 3, 4]
#        a = [x for x in a if x != 2]  # Rimuove tutte le occorrenze di 2
#        print(a)  # Output: [1, 3, 4]

# 2. Iterazione inversa:
#    - Iterare sugli indici in ordine inverso evita problemi con lo spostamento degli elementi.
#    - Esempio:
#        a = [1, 2, 3, 4]
#        for i in range(len(a) - 1, -1, -1):  # Da ultimo elemento al primo
#            if a[i] == 2:
#                del a[i]  # Rimuove in sicurezza gli elementi

# Quando aggiungere un elemento è ottimale
# ----------------------------------------
# Aggiungere un elemento a una lista durante un ciclo è ottimale se si usa il metodo `append()`,
# che aggiunge un elemento in fondo alla lista senza alterare gli indici esistenti.
# Questo ha un costo medio di O(1) (amortizzato).
# Esempio:
#    a = [1, 2, 3]
#    for x in range(4, 7):
#        a.append(x)  # Aggiunge gli elementi 4, 5, 6 alla fine della lista
#    print(a)  # Output: [1, 2, 3, 4, 5, 6]

# Conclusione
# -----------
# Usa il ciclo `for` per leggere, analizzare o creare nuove liste a partire da una esistente.
# Evita di modificare la lista durante l'iterazione con `for` (ad esempio, rimuovendo elementi); 
# preferisci soluzioni come liste di comprensione o iterazioni inverse.
# Per aggiungere elementi, il metodo `append()` è ottimale e può essere usato senza problemi.

'''========================================================================================================================================='''
'''Quindi per rendere il programma piu' efficente usciamo un while '''
# ps. utiliza il for quando l'iterazione di una lista riamne invariata o aggiungi un elemento 
# MENTRE E' SCONSIGLIATO ACNHE PERCHE' E DIFFICILE CONTROLLARE L'INDICE QUANDO 
# CANCELLO UN ELEMENTO PERCHE' LO SPAZIO CANCELLATO DELL'ELEMENTO VERRA' 
# OCCUPATOP DALL'ELEMENTO CHE C'E ALLA SUA DESTRA, E QUINDI TUTTI GLI ELEMENTI ALLA SUA DESTRA 
# SCALERANNO DI UNA POSIZIONE A SINISTRA 
# IN QUESTO CASO NELLA POSIZIONE I LA POSIZIONE CHE HO CANCELLATO  EEEEE' ANDATA A FINIRE LA POSIZIONE CHE ERA IN I+1
# QUINDI NON DOVRO INCREMENTARE I, MA LO DEVO LASCIARE LI DOVE STA, AALTRIMENTI SE NON LO CAANCELLO ALLORA INCREMENTO 

# QUINDI L'INCREMENTO DI I NON DEVE ESSERE FATTO NECESSARIAMENTE OGNI VOLTA CHE ESEGUEO IL BOLOCCO DEL FOR 
# AA VOLTE VA FATTO ALTRE NO 
# VA FATTO SOLO SE L'ELEMENTO I NON E' DA CANCELLARE 

''' E' QUINDI CONSIGLIATO UN WHILE CHE HA UN CONTROLLO MAGLIORE SULL'INDICE '''  

def del_item(a, v):
    '''
    input:
    - a: una lista
    - v: un valore da rimuovere dalla lista `a`

    return:
    - None (modifica direttamente la lista `a` in-place)

    Descrizione:
    - Elimina tutte le occorrenze del valore `v` dalla lista `a`.
    '''
    
  # questa versione e' errata 
    '''for  i in range(len(a)): 
       
        if a[i] == v:  
           
            del a[i]  

    return '''
    
   # Inizializza le variabili `i` e `n`
    # `i` rappresenta l'indice corrente, inizializzato a 0.
    # `n` è la lunghezza della lista `a`, calcolata con `len(a)`.
      
    #i, n = 0, len(a) modo alterantivo 
    # while i < n: #i < len(a) #questo e' un modo alternativo 
    # Inizia un ciclo `while` che scorre la lista fino a quando l'indice `i` è minore della lunghezza della lista `n`.
    i = 0 
    while i < len(a):    
        # Controlla se l'elemento corrente `a[i]` è uguale al valore `v`.
        if a[i] == v:
            # Se il valore corrisponde, elimina l'elemento all'indice `i`.
            
            del (a[i]) # IL COSTO QUINDI E'O(N) PERCHE' LO POSSO RIMUOVERE N VOLTE  E QUINDI OTTENGO UN COSTO QUADRATICO 
            # PERCHE' LA CANCELLAZIONE PREVEDE LO SLITTAMENTO DI TUTTI I SUOI ELEMENTI CHE SONO ALLA DESTRA 
            # DELL'ELEMENTO CHE CANCELLO E QUINDI DEVO FARE N COPIE 
            # QUINDI UNA SINGOLA OPERAZIONE PUO' RICHEDERE N OPERAAZIONI 
            # QUINDI NEL CASO PEGGIORE SARA' O(N) OP.
            
            #Ad es: del cancella un elemento in posizione i, tutti quanti gli elementi che si trovano alla sua sinistra 
            # vengono scalati di una posizione, quindi voldire che il costo della cancellazione equivale 
            #      al costo di una traslazione di n-i di elementi a sinistra 
            ''' NEL CASO PEGGIORE IL COSTO E' LINEARE O(N)'''
            #----------------------------------------------------------------------------------------------
            
            # Nota: Dopo la rimozione, tutti gli elementi successivi si spostano indietro di un indice,
            # ma `i` non viene incrementato immediatamente, quindi controlla nuovamente l'indice `i`.
            
            # ps: n-1 va aggiungto solo quando metti len(a) insieme ad i 
            '''# poi bisogna scalare n perche' ho eliminato un elemento dalla lista, perche' lho eliminato e' sara' n-1 '''
            
            '''n -= 1  # Riduce la lunghezza virtuale della lista
            # Non incrementa `i` per controllare il nuovo elemento alla posizione `i`.'''
        
        else: # altrimenti incremento i 
            # non cancello solo i 
            # Se l'elemento non è uguale a `v`, passa al successivo incrementando `i`.
            i += 1

        # La funzione termina e restituisce la lista modificata `a`.
     

# Lista di esempio
a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]

# Chiamata della funzione per eliminare tutte le occorrenze del valore `1`
del_item(a, 1)

# Stampa della lista `a` dopo l'eliminazione
print('Ecco i valori aggiornati: ', a)

'''# Soluzione errata, range(len(a)) viene valutata soltanto la prima
# volta quindi la sequenza generata da range() dipenderà soltanto
# dal valore iniziale di len(a)'''
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

































































