
#RISPONDI AI SEQUENTI QUESITI:


'''
Domanda 1 (Spazio occupato da una struttura in Python)
'''

# Testo della domanda:
# Sia `n` un intero positivo, assumendo che `c` sia una opportuna costante,
# qual è lo spazio occupato dalla struttura `d` definita nel seguente frammento di codice?

#```python

# Frammento di codice:

'''
a, d = [], {}

for i in range(n):
    a.append(i)
    d[i] = a
    
'''

# Opzioni di risposta:
# 1. circa `c*n`  | -> questa è la risposta giusta.
# 2. circa `n**c`
# 3. circa `c*n**2` 
# 4. circa `c*n+(n**2)/2`
# 5. circa `c*(n**2)/2` 
###################################################################################################

# 1. **Analizza la struttura dei dati usata nella domanda 1:**
#    - Considera quanto spazio occupano le strutture di dati in Python.
#    - La lista `a` cresce linearmente, ma viene assegnata più volte al dizionario `d`.
# Capisci come questa crescita impatta sulla memoria.
################################################################
'''
Ecco perchè è la risposta 1 è la risposta piu' giusta per la domanda 1:

# Risposta 1: La risposta giusta per la domanda 1 è circa `c*n`,
# che significa che lo spazio occupato dalla struttura `d` è proporzionale alla dimensione
# dello input `n`. Questo spazio viene utilizzato per memorizzare gli elementi nella lista 
# `a` e nel dizionario `d`.
'''

#La lista a viene creata vuota e cresce con n elementi, quindi il suo spazio occupato è O(n).
#Il dizionario d ha n chiavi, e ogni chiave punta alla stessa lista a.
#Il dizionario memorizza solo riferimenti alla lista, non copie della lista stessa.
#Gli elementi del dizionario occupano solo spazio per le chiavi e i riferimenti, 
# non per il contenuto della lista.
#Dove stava l'errore nel pensare che fosse O(n²)?
#L'errore sta nel supporre che ogni assegnazione d[i] = a creasse una copia della lista.
# Ma in Python, il dizionario memorizza solo un riferimento alla stessa lista a,
# quindi non cresce quadraticamente.

#Se invece avessimo scritto d[i] = a[:], allora d[i] avrebbe contenuto una copia di a per ogni i, 
# e allora lo spazio occupato sarebbe stato O(n²).
#Ma dato che non c'è copia, lo spazio totale occupato è O(n).

'''Risultato finale
✅ Risposta corretta: la prima opzione (~c*n)
❌ Errore iniziale: pensare che il dizionario memorizzasse copie della lista invece di riferimenti.
'''
#####################################################################################################
'''
Domanda 2 (Complessità temporale della funzione `f(a)`)
'''

# Testo della domanda:
# Qual è la complessità temporale di `f(a)`?

#```python

# Frammento di codice:

def f(a):
    d = {}  # Inizializzazione di un dizionario vuoto
    c = 0
    for x in a:  # Primo ciclo che scorre tutti gli elementi di `a`
        if x in d:  # Controlla se `x` è già presente nel dizionario
            c += 1
        else:
            d[x] = None  # Aggiunge `x` al dizionario
            print(d)
            print(d)
    return c


# Opzioni di risposta:
# 1. Lineare nel caso medio
# 2. Quadratica nel caso medio
# 3. Quadratica sempre
# 4. Quadratica nel caso peggiore  ----> QUESTA è LA RISPOSTA CORRETTA. PERCHè DOPO IL FOR SCORRE DI NUOVO LA LSITA E QUINDI ESEGUE N**2 OPERAZIONI DI RICERCA
# 5. Lineare nel caso peggiore
# ---------------------------------------------------------------------
'''
Consigli per rispondere correttamente
'''

# 2. **Calcola la complessità temporale nella domanda 2:**
#    - Capisci quanto tempo impiega la ricerca in un dizionario Python (`x in d`).
#    - Analizza il comportamento del codice in caso di input con molteplici duplicati.
#    - Considera il caso peggiore e medio.

#########################################################################################################################################################################################################

'''ECCO PERCHè QUESTA �� LA RISPOSTA CORRETTA:'''
# '''
# La risposta corretta è la **quarta opzione**: **"Quadratica nel caso peggiore"**.

# '''
# Step-by-step della complessità temporale
# '''

# 1. **Ciclo `for x in a`**  
#    - Il ciclo scorre **tutti** gli elementi di `a`, quindi abbiamo **O(n)** iterazioni.

# 2. **Operazione `if x in d`**  
#    - L'operazione di ricerca `x in d` nel **caso medio** è **O(1)** 
#       perché il dizionario Python utilizza tabelle hash per memorizzare gli elementi.

#    - Tuttavia, **nel caso peggiore**, quando si verificano **collisioni hash**,
#       la ricerca potrebbe richiedere **O(n)** tempo.

# 3. **Caso peggiore: ricerca `O(n)`**  
#
# - Se tutte le chiavi inserite nel dizionario generano collisioni, 
#       ogni lookup (`x in d`) può diventare **O(n)** anziché **O(1)**.
#   
# - Poiché il ciclo `for` scorre su tutti gli elementi di `a`,
#   e nel caso peggiore ogni operazione di lookup nel dizionario è **O(n)**, 
#   il tempo totale diventa **O(n²)**.

# '''
# Perché non sono corrette le altre opzioni?
# '''

# 1. **Opzione 1: "Lineare nel caso medio" ❌**  
#    - Nel caso medio, la ricerca nel dizionario è **O(1)**,
#       quindi la complessità sarebbe **O(n)**.  

#    - Tuttavia, la domanda chiede **il caso peggiore**, quindi questa risposta è sbagliata.

# 2. **Opzione 2: "Quadratica nel caso medio" ❌**  
#    - Nel caso medio, il lookup in un dizionario avviene in **O(1)**,
#       rendendo la complessità complessiva **O(n)**.  
#    - Quadratica sarebbe solo nel caso peggiore, quindi questa risposta è errata.

# 3. **Opzione 3: "Quadratica sempre" ❌**  
#    - La complessità **non è sempre** quadratica, perché nel caso medio 
#        il lookup nel dizionario è O(1) e l'intero algoritmo è **O(n)**.  
#    - La quadratica avviene solo nel **caso peggiore**, quindi questa risposta è sbagliata.

# 4. **Opzione 4: "Quadratica nel caso peggiore" ✅**  
#    - Nel caso peggiore, il lookup nel dizionario diventa **O(n)** a causa delle collisioni hash.  
#    - Poiché il ciclo `for` scorre su **n** elementi, 
#       e ogni lookup nel caso peggiore è **O(n)**, la complessità totale è **O(n²)**.  
#    - **Questa è la risposta corretta.**

# 5. **Opzione 5: "Lineare nel caso peggiore" ❌**  
#    - Abbiamo visto che nel caso peggiore la ricerca nel dizionario diventa **O(n)**,
#       quindi l'intero algoritmo diventa **O(n²)**.  

#    - **Non può essere solo lineare nel caso peggiore, quindi è errato.**

# '''
# Conclusione
# '''
# - **Caso medio**: `O(n)`, perché la ricerca nel dizionario avviene in `O(1)`.
# - **Caso peggiore**: `O(n²)`, perché ogni lookup diventa `O(n)`, e il ciclo esegue `n` iterazioni.

# La risposta corretta è quindi **"Quadratica nel caso peggiore" (Opzione 4)**. 🚀



################################################################################################################################################################################################
'''
Domanda 3 (Algoritmo di ordinamento)
'''

# Testo della domanda:
# Si consideri il seguente frammento di codice dove `a` è una stringa di interi. Quale tra le affermazioni elencate è corretta?

#```python
# Frammento di codice:
def ff(a):
    # Inizializzazione del contatore
    c = 0
    n = len(a)

    # Ciclo for che scorre su tutta la lunghezza dell'array
    for c in range(n):  # O(n)
        i = 0
        # Ciclo while che dovrebbe scorrere i valori rimanenti, ma è mal definito
        while i < n - c:  # O(1) ❌ ERRORE QUI
            # Confronto tra elementi adiacenti nella lista (con indici negativi)
            
            if a[-i] < a[-i - 1]:  # O(1)
                # Scambio degli elementi
                a[-i], a[-i - 1] = a[-i - 1], a[-i]  # O(1)
            # Incremento dell'indice
            i += 1  # O(1)
    
    # Restituzione dell'array modificato
    return a  # O(1)



# Opzioni di risposta:
# 1. Ordina gli elementi di `a` dal più piccolo al più grande in tempo lineare nel caso migliore ---> QUESTA E' LA RISPOSTA è sbagliata 
# 2. Ordina gli elementi di `a` dal più grande al più piccolo in tempo quadratico nel caso peggiore
# 3. Ordina gli elementi di `a` dal più piccolo al più grande in tempo quadratico nel caso peggiore
# 4. Il programma ha un comportamento indefinito e complessità temporale quadratica ---> QUESTA E' LA RISPOSTA CORRETTA
# 5. Ordina gli elementi di `a` dal più grande al più piccolo in tempo lineare nel caso migliore
#---------------------------------------------------------------------
# # 3. **Analizza il comportamento dell'ordinamento nella domanda 3:**
#    - Verifica se il codice sta implementando un algoritmo simile a Bubble Sort.
#    - Identifica se il codice ha un comportamento anomalo.
#    - Controlla il numero di iterazioni che esegue nei vari scenari.
# ###############################################################################################################################################
''' # Ecco perchè QUESTA E' LA RISPOSTA CORRETTA: '''


# La complessità del programma nel caso migliore è O(n^2), perché il ciclo `while` all'interno
# del ciclo `for` viene eseguito al più `n` volte. Questo porta alla complessità totale O(n^2).
# La risposta corretta è quindi "Ordina gli elementi di `a` dal più grande al più piccolo in tempo quadratic nel caso peggiore".

'''
Errore nell'analisi della complessità
'''
# Il tuo errore principale è nel considerare il `while` come O(1). In realtà,
# il ciclo `while i < n - c` non è costante, ma dipende da `n`!

# Vediamo perché:
# - Il ciclo for esterno esegue n iterazioni (range(n), quindi va da 0 a n-1).
# - Il ciclo while esegue iterazioni che dipendono da c:
#     - nella prima iterazione (c = 0) il ciclo while scorre fino a n
#     - nella seconda (c = 1) fino a n-1, e così via fino all'ultima iterazione.

'''
Riformuliamo la complessità correttamente
'''
# - Il for esegue `n` iterazioni.
# - Il while all'interno esegue, nel caso peggiore:
#     - `n` iterazioni la prima volta
#     - `n-1` iterazioni la seconda volta
#     - `n-2` iterazioni la terza volta
#     - ...
#     - Fino ad arrivare a 1 iterazione.

# Quindi, il numero totale di operazioni è dato dalla somma:
# n + (n-1) + (n-2) + ... + 1 = (n(n+1))/2 = O(n^2)

# **Dunque, la complessità nel caso peggiore è `O(n²)`, non O(n).**

'''
Il secondo errore: comportamento del codice
'''
# Analizziamo cosa fa il codice:
# 1. Il ciclo for scorre da `c = 0` a `n-1`.
# 2. Il ciclo while scorre sugli elementi della stringa `a` da destra a sinistra,
# cercando di confrontare e scambiare gli elementi.

# 3. Il problema principale è nell'accesso agli elementi: `a[-i]` e `a[-i - 1]`
# non funzionano correttamente con `i = 0`, portando a un errore di accesso agli indici.

# Dunque, il codice **non funziona correttamente** e può portare a un comportamento indefinito.

'''
Quale opzione è corretta?
'''
# Ora che sappiamo che:
# - La complessità è `O(n²)`, non `O(n)`.
# - Il codice ha problemi con gli indici negativi.

# L'opzione corretta è:
# **4. Il programma ha un comportamento indefinito e complessità temporale quadratica** ✅

'''
Dove hai sbagliato?
'''
# 1. **Hai considerato erroneamente il ciclo `while` come `O(1)`,
# invece è variabile e porta a `O(n²)`.**

# 2. **Non hai notato che l'accesso agli indici negativi (`a[-i]`)
# può portare a errori di esecuzione.**
# 3. **Hai scelto un'opzione che presupponeva che l'algoritmo 
# fosse corretto e funzionasse in `O(n)`, mentre in realtà ha un comportamento errato.**


###########################################################################################################################################à
'''
Domanda 4 (Struttura dati `dict` in C)
'''

# Testo della domanda:
# Sia `d` un `dict` implementato in C come visto a lezione 
# (le definizioni delle strutture sono riportate nel codice seguente). 
# Assumendo che un `d_item` occupi `c` byte ed un puntatore `p`
# byte, quanto vale `sizeof(d)`

'''linguaggio c

#include <stdio.h>
// Frammento di codice:
struct d_item {  // definizione della struttura d_item
    char *k; // chiave associata al elemento
    float v; // valore associato al chiave
};
typedef struct d_item d_item; // definizione della struttura d_item

struct nodo { // struttura nodo
    d_item info; // elemento del dizionario
    struct nodo *succ; // puntatore al successivo nodo
};
typedef struct nodo nodo; // definizione della struttura nodo

struct dict {
    nodo **a;
    int m; // numero di liste (dimensione di a)
    int n; // numero di elementi nel dizionario
};
typedef struct dict dict;

'''
# Opzioni di risposta:
# 1. circa `p*d.m`
# 2. circa `c*d.n`
# 3. `O(n+m)`
# 4. `O(1)`

#-----------------------------------------------------------------------

'''
Consigli per rispondere correttamente
'''



# 4. **Analizza le strutture dati in C nella domanda 4:**
#    - Verifica la dimensione delle strutture dati.
#    - Comprendi la relazione tra liste concatenate e memoria allocata.
#    - Considera la dimensione di ciascun elemento (`d_item` e `nodo`).

#----------------------------------------------------------------------

''' # Ecco perchè QUESTA E' LA RISPOSTA CORRETTA, LA QUARTA RISPOSTA:'''
'''
La domanda riguarda la dimensione in memoria della struttura `dict` in C.
Vediamo perché la risposta corretta è la **4. `O(1)`**, 
mentre la tua scelta **2. `circa c*d.n`** è errata.
'''
'''
### **Analisi della struttura `dict`**
'''



'''
#### **1 Comprendiamo `sizeof(dict)`**
'''

# La funzione `sizeof(dict)` calcola la dimensione **statica** della struttura,
# ovvero lo spazio richiesto per i suoi campi diretti,
# **non** quello usato dinamicamente per i dati contenuti (elementi del dizionario).

# I campi della struttura `dict` sono:
# - `nodo **a` → **Puntatore a un array di puntatori** (`p` byte).
# - `int m` → **Intero** (tipicamente 4 byte).
# - `int n` → **Intero** (tipicamente 4 byte).

# **La dimensione di `dict` è quindi fissa, indipendentemente 
#   dal numero di elementi `n` o dalla dimensione `m`.**  

# 👉 **Questa è una caratteristica tipica di `O(1)`.**

'''
#### **2 Perché la risposta `circa c*d.n` è errata?**
'''

# La tua risposta suggerisce che la dimensione di `dict` dipenda 
# direttamente da `n`,
# ma **`dict` stesso non memorizza gli elementi del dizionario,
# bensì solo i puntatori alle liste che li contengono.**  
# Quindi, il **peso effettivo degli elementi `d_item` è dinamico e
# non influisce su `sizeof(dict)`**, che rimane costante.

'''
#### **3 Perché la risposta giusta è `O(1)`?**
'''

# La dimensione della struttura `dict` è **indipendente dal numero di elementi 
# `n` o di liste `m`**, quindi rimane **costante** rispetto 
#  alla crescita del dizionario.  
# **Questo è il motivo per cui la risposta corretta è `O(1)`.**

# ---

'''
### **Come migliorare e risolvere problemi simili?**
'''

# 1. **Distingui tra dimensione della struttura e dimensione dei dati contenuti.**
#    - `sizeof(dict)` misura **solo la memoria allocata per i campi diretti** della struttura.
#    - Se ti chiedessero la memoria occupata dagli elementi **inseriti**, dovresti considerare `n`.

# 2. **Riconosci quando la memoria cresce con `n` e quando è costante.**
#    - Se ci fosse una **lista direttamente dentro `dict`**, la dimensione sarebbe variabile (`O(n)`).
#    - Ma poiché abbiamo **solo puntatori a liste**, `sizeof(dict)` non cambia con `n`.

# 3. **Memorizza la regola generale per strutture con puntatori in C:**
#    - Un puntatore ha dimensione fissa (`O(1)`).
#    - Una struttura contenente solo puntatori ha dimensione costante (`O(1)`).
#    - Il contenuto puntato può essere dinamico e influenzare la memoria
#       usata **a runtime**, ma non `sizeof(struct)`.

# ---

# **Conclusione**
# - `sizeof(struct dict)` è **O(1)** perché la dimensione della struttura è costante.
# - La memoria effettivamente utilizzata dipende dai dati dinamici,
#   ma `sizeof()` misura solo la parte statica.

# - Riconoscere la complessità aiuta a ottimizzare il codice e comprendere
#   le prestazioni.





