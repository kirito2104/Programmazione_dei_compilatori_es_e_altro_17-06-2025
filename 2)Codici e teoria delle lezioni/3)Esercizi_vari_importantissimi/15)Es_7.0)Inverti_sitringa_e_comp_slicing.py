


#Scrivere una funzione in Python che, data una lista composta da interi e sottoliste annidate 
#(composte da interi e altre sottoliste), restituisce in output la somma di tutti gli interi.


def somma_liste_annidate(list_a):
    """
    Funzione ricorsiva per calcolare la somma di tutti gli interi presenti in una lista, 
    che può contenere sottoliste annidate di qualsiasi profondità.

    Parametri:
    - list_a: una lista contenente numeri interi e/o sottoliste (che a loro volta possono contenere interi e altre sottoliste).

    Ritorna:
    - La somma di tutti gli interi contenuti nella lista e nelle sue sottoliste annidate.
    """

    # Inizializzazione della variabile di accumulo della somma
    sum = 0  
    
    # Iterazione su ogni elemento della lista principale
    for a in list_a:  
        # Controllo se l'elemento attuale è un numero intero
        if type(a) is not list:
            # Se l'elemento è un intero, lo aggiungiamo direttamente alla somma
            sum += a  
        else:
            # Se l'elemento è una lista, chiamiamo la funzione ricorsivamente su quella lista
            # e sommiamo il valore restituito alla somma corrente.
            sum += somma_liste_annidate(a)
    
    # Dopo aver elaborato tutti gli elementi della lista (e delle sue sottoliste), restituiamo la somma totale
    return sum  

"""
la dimensione dell'input n è data dal numero degli elementi interi nella
lista ed in tutte le sottoliste annidate.
Complessità temporale:
    T(n) lineare in n 
Complessità spaziale:
    O(n) nel caso peggiore, cioà quando ci sono n livelli di
    annidamento
"""

"""
Analisi della complessità:

Dimensione dell'input (n): 
    - Il valore di n è determinato dal numero totale di elementi interi presenti nella lista, 
      compresi quelli contenuti in sottoliste annidate.

Complessità temporale:
    - In ogni chiamata della funzione, scansioniamo ogni elemento della lista una volta.
    - Se l'elemento è un numero intero, lo sommiamo in tempo O(1).
    - Se l'elemento è una sottolista, chiamiamo la funzione ricorsivamente su di essa.
    - Nel caso peggiore (tutti gli elementi sono distribuiti in sottoliste profonde), 
      visitiamo ciascun numero una sola volta, portando la complessità a O(n), dove n è il numero totale di interi.

Complessità spaziale:
    - Nel caso peggiore (ogni numero è contenuto in una sottolista annidata separata, es. [1, [2, [3, [4, ...]]]]), 
      il numero di chiamate ricorsive è proporzionale a n, quindi la complessità spaziale è O(n).
    - Nel caso medio, la profondità della ricorsione è inferiore a n, ma dipende dalla struttura della lista.
"""

# Definizione di una lista contenente interi e sottoliste annidate
lista_a = [1, 2, 5, [20, 3, 1, [40, 6, 3], 2, 5, 6], 5, [7, 8]]

# Stampa della somma di tutti gli elementi interi presenti nella lista e nelle sottoliste
print(somma_liste_annidate(lista_a))



###############################################################################################################################################################################################

#Qui è un esempio di come potresti implementare una funzione per invertire una 
#stringa in Python utilizzando la ricorsione e solo l'operazione di concatenazione 
#tra stringhe:
'''
def inverti_stringa(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + inverti_stringa(s[:-1])
'''
#Questa funzione prende una stringa come input e restituisce la sua inversione. Ad esempio, se la stringa è "hello", la funzione restituirà "olleh". La ricorsione è utilizzata per invertire la stringa di caratteri da un'estremità all'altra, concatenando i singoli caratteri alla fine della stringa.

#Per testare questa funzione, puoi eseguire il seguente codice:

#print(inverti_stringa("hello"))

#Questo stampa "olleh" sul terminale.







###################################################################################################################



'''
Scrivere una funzione in python che, data una stringa in input,
ritorna in output la stringa invertita. Fare questo usando la ricorsione 
e usando unicamente l'operazione di concatenazione tra stringhe.
'''
    
    # Base case: se la stringa è vuota, restituisce una stringa vuota
# '''
# 1. Comprendi il problema
# '''
# L'obiettivo è scrivere una funzione che inverta una stringa utilizzando solo la ricorsione e la concatenazione.
# Questo significa che NON possiamo usare slicing con [::-1] o metodi di Python come .reverse() o reversed().

# '''
# 2. Pensa al caso base
# '''
# Ogni funzione ricorsiva deve avere un caso base per fermare la ricorsione.
# Il caso base più semplice è quando la stringa è vuota ("") o ha un solo carattere.
# In entrambi i casi, la stringa è già "invertita", quindi possiamo restituirla direttamente.

# '''
# 3. Scomponi il problema in sottoproblemi
# '''
# Se abbiamo una stringa "hello", dobbiamo trovare un modo per ottenere "olleh" ricorsivamente.
# Un modo per farlo è prendere il primo carattere della stringa e spostarlo alla fine, ripetendo il processo per il resto della stringa.

# '''
# 4. Definisci la relazione ricorsiva
# '''
# Possiamo ridurre il problema eliminando il primo carattere e invertendo il resto della stringa.
# Poi possiamo concatenare il primo carattere alla fine del risultato ottenuto.
# Per esempio, con "hello":
#  - Primo carattere: 'h'
#  - Restante stringa: "ello"
#  - Invertiamo "ello" → "olle"
#  - Concatenando: "olle" + "h" → "olleh"

# '''
# 5. Segui il flusso di esecuzione
# '''
# Analizziamo passo dopo passo cosa succede con la stringa "abc":
#  - "abc" → primo carattere 'a', resto "bc"
#  - "bc" → primo carattere 'b', resto "c"
#  - "c" → caso base, ritorna "c"
#  - Torniamo indietro concatenando: "c" + "b" → "cb"
#  - "cb" + "a" → "cba"
#  - Risultato finale: "cba"

# '''
# 6. Testa con diversi input
# '''
# Verifichiamo con diversi casi:
#  - "" (stringa vuota) → ""
#  - "a" → "a"
#  - "abcd" → "dcba"
#  - "racecar" (palindromo) → "racecar"
#  - "12345" → "54321"

# '''
# 7. Pensa ai limiti della ricorsione
# '''
# Se la stringa è molto lunga, possiamo incorrere in un errore di stack overflow.
# Questo perché ogni chiamata ricorsiva occupa memoria nello stack.
# Una soluzione alternativa potrebbe essere un approccio iterativo o l'uso della tail recursion optimization (se supportata da Python, che purtroppo non la implementa direttamente).
'''
def inverti_stringa(s):
    # Caso base: se la stringa è vuota o ha un solo carattere, restituiscila
    if len(s) <= 1:
        return s
    
    # Chiamata ricorsiva: inverti la parte rimanente della stringa e aggiungi il primo carattere alla fine
    return inverti_stringa(s[1:]) + s[0]
'''
'''
# Esempi di test
print(inverti_stringa("hello"))  # Output: "olleh"
print(inverti_stringa("abc"))    # Output: "cba"
print(inverti_stringa(""))       # Output: ""
print(inverti_stringa("a"))      # Output: "a"
print(inverti_stringa("racecar")) # Output: "racecar"

'''
#Ecco l'esercizio svolto : 
# Invertire una stringa usando la ricorsione e concatenazione tra stringhe

def inverti_stringa_basic(s):
    """
    Funzione ricorsiva per invertire una stringa usando l'operazione
    di concatenazione tra stringhe.
    
    Parametri:
    s (str): La stringa da invertire.
    
    Ritorna:
    str: La stringa invertita.
    """
    
    # Caso base: se la stringa è vuota, restituisce il primo carattere
    if len(s) == 1: 
        return s[0]  # Attenzione: qui c'è un errore, perché s[0] non esiste se s è vuota
    
    else:
        # Chiamata ricorsiva rimuovendo il primo carattere della stringa
        reversed = inverti_stringa_basic(s[1:])
        
        # Aggiunge il primo carattere della stringa alla fine della parte invertita
        reversed += s[0]
    
    # Restituisce la stringa invertita
    return reversed
    '''
    modo alternativo :
     
    # Passo ricorsivo:
    # 1. Invertiamo la parte rimanente della stringa (escludendo il primo carattere)
    # 2. Aggiungiamo il primo carattere alla fine del risultato
    return inverti_stringa(s[1:]) + s[0]
    
    '''
    
    
print(inverti_stringa_basic("programmazione")) 
"""
Sia n la lunghezza della stringa.
Complessità temporale: O(n**2), in quanto vengono fatte n chiamate ricorsive
e all'interno di ogni chiamata ricorsiva avviene un'operazione di slicing
(come l'analisi temporale del massimo ricorsivo visto a lezione).
Complessità spaziale: O(n**2) per lo slicing.
"""
    
#Tale programma qui sopra non è molto efficiente per stringhe lunghe,e la complessita' è O(n^2).

# Ecco un esempio migliore qui sotto :

def reversed_recursive_maybe_better(s, i=0):
    """
    Funzione ricorsiva per invertire una stringa, utilizzando un indice `i`
    per scorrere la stringa da sinistra a destra invece di creare nuove 
    sottostringhe come nella versione precedente.

    Parametri:
    - s (str): La stringa da invertire.
    - i (int): Indice dell'elemento attuale che verrà spostato alla fine 
      della stringa invertita. Il valore predefinito è 0 (inizio della stringa).

    Ritorna:
    - str: La stringa invertita.
    """

    # Caso base: se l'indice ha raggiunto l'ultimo carattere della stringa, 
    # restituisce quel carattere perché non ci sono più caratteri da elaborare.
    
    if i == len(s) - 1: # iniz quindi dall'ultimo carattere della stringa
        
        return s[i]  

    else:
        # Chiamata ricorsiva avanzando di un indice per costruire la parte invertita della stringa
        reversed = reversed_recursive_maybe_better(s, i + 1)

        # Aggiunge il carattere corrente `s[i]` alla fine della stringa invertita parziale.
        reversed += s[i]

        # Restituisce la stringa invertita costruita fino a questo punto
        return reversed

'''
#  cio che cambia fondamente: e che ho inizilizzato un puntatore a 0 e poi faccio un
# ciclo if dove scorrere la stringa fino all'ultimo carattere, partendo dall'ultimo carattere.
 # e ritorna ritorna la stringa.
#Else invece chiama sé stessa avanzando di un indice (i+1), permettendo alla ricorsione
# di spostarsi verso la fine della stringa.

Aspetta il risultato della chiamata successiva senza fare nulla finché 
non viene raggiunto il caso base.

Quando il caso base viene raggiunto, la funzione comincia a concatenare i caratteri
in ordine inverso mentre torna indietro nella catena di chiamate.
🔥 Differenza chiave rispetto alla prima versione
In inverti_stringa_basic(s), ogni chiamata crea una nuova sottostringa con s[1:],
che è un'operazione costosa perché genera una copia della stringa ad ogni passo.

In reversed_recursive_maybe_better(s, i), invece: 
✔️ Non viene mai creata una nuova sottostringa: si lavora direttamente sugli indici.
✔️ Si evita l'operazione costosa di s[1:], riducendo l'overhead di memoria.


'''
print(reversed_recursive_maybe_better("programmazione")) 
"""
La versione con indice permette di evitare la creazione di nuove sottostringhe,
riducendo il numero di copie e riducendo il costo cumulativo.
Questo migliora la performance del programma per stringhe lunghe,
e la complessità viene ridotta a O(n).

E' possibile notare che la versione con indice è più efficiente rispetto 
alla versione precedente, che non è molto efficiente per stringhe lunghe.

"""

"""
Analisi della Complessità:

- Sia n la lunghezza della stringa.
- Complessità temporale: O(n**2), perché ci sono n chiamate ricorsive 
    e ogni concatenazione `+=` crea una nuova stringa, causando 
    un costo cumulativo quadratico.
- Complessità spaziale: O(n**2), perché ogni chiamata mantiene 
    un riferimento all'intera stringa generata, 
    causando una crescita quadratica della memoria usata.

Perché è più efficiente rispetto a `inverti_stringa_basic`?

1. **Migliore gestione delle substringhe**:
   - `inverti_stringa_basic(s[1:])` crea una nuova sottostringa ad ogni chiamata,
     eliminando il primo carattere e causando un'allocazione 
     di memoria separata per ogni passaggio.
     
   - `reversed_recursive_maybe_better(s, i+1)` invece usa un **indice**
    per scorrere la stringa, evitando la creazione di nuove sottostringhe
    e riducendo il numero di copie.

2. **Minor overhead di slicing**:
   - Nella versione precedente, `s[1:]` genera una **nuova stringa** di lunghezza
    `n-1`, `n-2`, ..., `1`, 
     portando ad un costo cumulativo elevato (O(n²) solo per lo slicing).
   - Qui si evita del tutto il costo di slicing, gestendo tutto con un **indice `i`**, 
     il che riduce l'uso della memoria e migliora le performance.

Tuttavia, questa versione è ancora inefficiente a causa della concatenazione `+=`, 
che genera una nuova stringa ad ogni passo. La soluzione più ottimale userebbe una lista per 
accumulare i caratteri e poi unirli con `''.join()`, portando la complessità a O(n).
"""

def reversed_recursive_much_better(s, i=0):
    """
    Funzione ricorsiva ottimizzata per invertire una stringa.
    
    A differenza delle versioni precedenti, questa implementazione:
    - Converte la stringa in una lista per evitare costose operazioni di slicing e concatenazione.
    - Utilizza un indice `i` per navigare attraverso la lista.
    
    Parametri:
    - s (str | list): La stringa da invertire (convertita in lista all'inizio se necessario).
    - i (int): Indice dell'elemento attuale da processare (default: 0).

    Ritorna:
    - str: La stringa invertita.
    """

    # 1️⃣ **Controllo del tipo della stringa**
    if type(s) == str:  # Verifica se `s` è effettivamente una stringa
        list = []  # Creiamo una lista vuota per contenere i caratteri

        # **Conversione della stringa in una lista**
        # Per ogni carattere della stringa originale, lo aggiungiamo alla lista
        for c in s:
            list.append(c)  # Metodo più efficiente di concatenazione

        s = list  # Ora `s` è una lista di caratteri

    # 2️⃣ **Caso base della ricorsione**
    if i < len(s) - 1:  
        # Se l'indice `i` è minore della lunghezza della lista - 1, 
        # significa che ci sono ancora caratteri da elaborare.
        return s[i]  # Torna il carattere attuale (non corretto, vedi spiegazione sotto)

    else:
        # 3️⃣ **Chiamata ricorsiva**
        # Chiamiamo la funzione avanzando l'indice `i` di 1
        reversed = reversed_recursive_much_better(s, i + 1)

        # 4️⃣ **Costruzione della stringa invertita**
        reversed += s[i]  # Aggiungiamo il carattere corrente alla stringa costruita finora

        # 5️⃣ **Restituzione della stringa invertita**
        return reversed

# **Esecuzione della funzione**
print(reversed_recursive_much_better("programmazione"))    
         
            
"""
Sia n la lunghezza della stringa, dunque n è anche la lunghezza della
lista d'appoggio creata.
Complessità temporale: O(n), in quanto vengono fatte n chiamate ricorsive
e in ogni chiamata ricorsiva si effettuano un numero costante di operazioni.
Complessità spaziale: O(n+n)=O(n) dato che vengono aperti n frame dalle
chiamate ricorsive e viene mantenuta una lista ausiliaria contenente tutti i
caratteri della stringa.
"""
###############################################################################à
"""
🔍 **Analisi della Complessità**
---------------------------------------------------
Sia n la lunghezza della stringa.

🔹 **Complessità Temporale: O(n)**
- La conversione della stringa in lista richiede O(n).
- La funzione ricorsiva viene chiamata `n` volte, ciascuna con un numero costante di operazioni.
- Non eseguiamo slicing `s[1:]`, quindi evitiamo il costo O(n²).

🔹 **Complessità Spaziale: O(n)**
- Manteniamo una lista di `n` caratteri (O(n)).
- Ci sono `n` chiamate ricorsive, quindi `n` stack frame (O(n)).
- Complessivamente, O(n) + O(n) = **O(n)**.
---------------------------------------------------


"""

    





















