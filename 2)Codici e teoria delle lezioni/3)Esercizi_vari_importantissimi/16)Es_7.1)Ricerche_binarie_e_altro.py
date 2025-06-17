

'''
Esercizio
Scrivere una funzione in Python che, data una lista di numeri interi
distinti non negativi ordinati in modo crescente, restutisce
il più piccolo elemento non negativo mancante in essa.
Se non ci sono elementi mancanti, restituisce -1.

Esempio:

Input: [0,1,2,3,4,5,7,9,11]
Output: 6
Input: [1,2,3,5,7,9,20]
Output: 0
Input: [0,1,2,3,4,5]
Output: -1

'''
def ricerca_esculdendo_i_numeri_con_meno(numeri):
    """
    Funzione che cerca il **primo elemento non negativo** in una lista di numeri ordinati
    utilizzando la ricerca binaria.
    
    ⚠️ Il nome della funzione non è appropriato: non ordina una lista, ma effettua una ricerca.

    Parametri:
    - numeri (list[int]): Lista di numeri interi ordinati.

    Ritorna:
    - int: L'indice del primo numero **non negativo** nella lista.
    """

    n = len(numeri)  # 1️⃣ Salviamo la lunghezza della lista `numeri`
    
    # 2️⃣ Inizializziamo gli indici per la ricerca binaria:
    lx, rx = 0, n - 1  # `lx` è l'inizio della lista, `rx` è la fine della lista
    
    # 3️⃣ **Ricerca binaria per trovare il primo numero non negativo**
    while lx <= rx:
        # 🟢 **Calcolo dell'indice centrale** 🟢
        # Si usa la formula `(lx + rx) / 2` per trovare il centro dell'intervallo
        cx = int((lx + rx) // 2)

        # 4️⃣ **Condizione per aggiornare i puntatori**
        if cx == numeri[cx]:  
            # 📌 Se l'indice `cx` è uguale al valore `numeri[cx]`,
            # significa che stiamo ancora nella parte dei numeri negativi o ordinati male.
            lx = cx + 1  # 🔼 Spostiamo `lx` verso destra (escludendo `cx` stesso)

        else:
            # 📌 Altrimenti, significa che dobbiamo restringere la ricerca verso sinistra.
            rx = cx - 1  # 🔽 Spostiamo `rx` verso sinistra

    # 5️⃣ Quando il ciclo termina, `lx` sarà l'indice del primo elemento non negativo
    return lx  if lx < len(numeri) else -1  # Se `lx` è fuori dai limiti, nessun numero è >= 0




"""
🔍 **Analisi della Complessità**
---------------------------------------------------
Sia `n` la lunghezza della lista.

🔹 **Complessità Temporale: O(log n)**
- L'algoritmo utilizza **ricerca binaria**, dimezzando lo spazio di ricerca a ogni iterazione.
- Invece di scansionare tutti gli `n` elementi, eseguiamo circa `log₂(n)` passi.

🔹 **Complessità Spaziale: O(1)**
- Non viene usata memoria aggiuntiva significativa, solo variabili `lx`, `rx` e `cx`.

-----------------------------------=----------------
"""
"""
❓ **Perché esce 0 quando compiliamo?**
----------------------------------------

🔹1 La funzione sta cercando un valore `cx` tale che `cx == numeri[cx]`, 
      ma **nessun elemento della lista soddisfa questa condizione**.

🔹 2 Durante tutto il ciclo, `lx` non viene mai modificato perché 
      **la condizione `cx == numeri[cx]` non è mai vera**.

🔹 3 Quando il ciclo `while` termina, la funzione restituisce `lx`, 
      e dato che `lx` è sempre rimasto `0`, alla fine il valore di ritorno è **0**.

----------------------------------------

📌 **Esempio di esecuzione:**
Lista in input: `[1, 2, 6, 7, 10, 11, 13]`

- lx parte da `0`, rx parte da `6`.
- Si calcola `cx = (0 + 6) // 2 = 3` → `cx != numeri[cx]` (3 != 7), quindi `rx = 2`
- Si calcola `cx = (0 + 2) // 2 = 1` → `cx != numeri[cx]` (1 != 2), quindi `rx = 0`
- Si calcola `cx = (0 + 0) // 2 = 0` → `cx != numeri[cx]` (0 != 1), quindi `rx = -1`

🔹 **A questo punto, il ciclo termina e `lx` è ancora 0.**
🔹 **Quindi la funzione stampa 0.** 🎯

"""



numeri =[0,1,2,3,4,5,7,9,11]
nume =[0,1,2,3,4,5]
# **Esempio di utilizzo**
print(ricerca_esculdendo_i_numeri_con_meno(numeri))  
print(ricerca_esculdendo_i_numeri_con_meno(nume))  
"""
Sia n la lunghezza della lista.
Complessità temporale: O(log n)
Complessità spaziale: O(1)
"""

"""
📌 Riassunto dettagliato della funzione e dei suoi output
La funzione ordina_lista_in_ord_crescente(numeri) cerca un indice cx tale
che cx == numeri[cx] in una lista ordinata.
Se non trova nessun numero che soddisfa questa condizione, 
restituisce il primo indice (lx) dove tale condizione avrebbe dovuto verificarsi.

🔢 Analisi dei casi di output
Caso 1: [0,1,2,3,4,5,7,9,11] → Output 6
✅ Fino a 5, gli indici corrispondono ai valori.
⚠️ Il 6 manca nella sequenza, quindi la funzione restituisce 6, ovvero il primo indice dove 
l'uguaglianza indice == valore non è più rispettata.

Caso 2: [1,2,3,5,7,9,20] → Output 0
✅ Il primo elemento è 1, quindi già numeri[0] ≠ 0.
📌 La funzione capisce subito che la sequenza è sbagliata dall'inizio e restituisce 0.

Caso 3: [0,1,2,3,4,5] → Output -1
✅ Tutti gli elementi rispettano indice == valore.
📌 Non c'è nessuna interruzione nella sequenza, 
quindi la funzione arriva fino alla fine e restituisce -1.
"""




####################################################################################################################################àààààààààààààààà



# #In una lista c'è un intruso: osvaldo.

#Scrivi una funzione in Python che data una lista di elementi, tra cui sottoliste annidate, 
#ritorna True se trova osvaldo, False altrimenti


lista = ['cioa', ['mare', 'cane', ['osvaldo', 'ragno']], 'uomo', ['panda', 'cane']]


def trova_intruso(lista):
    """
    Funzione ricorsiva per cercare se l'elemento 'osvaldo' è presente all'interno di una lista.
    
    La funzione esplora la lista principale e, nel caso in cui un elemento sia una sotto-lista,
    richiama sé stessa ricorsivamente per esplorare anche il contenuto della sotto-lista.

    Parametri:
    - lista (list): Una lista contenente elementi misti (stringhe, numeri, o sotto-liste).

    Ritorna:
    - bool: True se 'osvaldo' è presente in qualsiasi livello della lista, False altrimenti.
    """

    # 1️⃣ **Iteriamo su ogni elemento della lista**
    for i in lista:

        # 2️⃣ **Caso base: Se troviamo 'osvaldo', restituiamo subito True**
        if i == 'osvaldo':
            return True  # 🔴 **A questo punto la funzione si ferma immediatamente**

        # 3️⃣ **Caso ricorsivo: Se l'elemento è una lista, esploriamola ricorsivamente**
        elif isinstance(i, list):  
            # 🔹 `isinstance(i, list)` verifica se `i` è una lista.
            # 🔹 Se sì, richiamiamo la funzione su `i` stessa per cercare dentro la sotto-lista.
            if trova_intruso(i):  
                return True  # 🔴 **Se una chiamata ricorsiva trova 'osvaldo', fermiamo tutto e restituiamo True**

    # 4️⃣ **Se abbiamo finito di scansionare tutta la lista e le eventuali sotto-liste senza trovare 'osvaldo', restituiamo False**
    return False  # 🔴 **Questo accade solo se 'osvaldo' non è stato trovato da nessuna parte**

# la complessità Temporale: O(n), dove n è il numero di elementi nella lista
# la complessità Spaziale: O(n), dove n è il numero di elementi nella lista




# **Esempio di utilizzo**

print(trova_intruso(lista))  # Output: True


# ### **Come calcolare la complessità della funzione `trova_intruso(lista)`?**  
#
# La complessità della funzione dipende da **due fattori principali**:
# 1. **Il numero totale di elementi (n) nella lista e nelle sue sotto-liste.**
# 2. **La profondità massima della ricorsione (d), cioè quanto sono annidate le sotto-liste.**
#
# ---

# ## **🔹 Complessità Temporale (Time Complexity)**
# La funzione **esplora ogni elemento della lista una sola volta**, e quando incontra una sotto-lista, richiama sé stessa per scansionarla.  
# Questo significa che:
# - Nel **caso peggiore**, ogni elemento della lista deve essere visitato una volta.
# - Se la lista ha **n elementi totali** (inclusi quelli nelle sotto-liste), il tempo di esecuzione sarà **O(n)**.
# - Se `'osvaldo'` viene trovato presto, la funzione si ferma immediatamente e può essere più veloce (**best case O(1)**).
#
# 📌 **Caso Peggiore (Worst Case - O(n))**  
# - `'osvaldo'` è l'ultimo elemento della lista o non esiste.  
# - La funzione deve attraversare tutti i **n** elementi prima di restituire `False`.
#
# 📌 **Caso Migliore (Best Case - O(1))**  
# - `'osvaldo'` è il **primo elemento** della lista, quindi la funzione lo trova subito e termina.
#
# ### **📝 Formula Generale della Complessità Temporale**
# T(n) = O(n)
# perché ogni elemento viene **visitato una sola volta**.
#
# ---

# ## **🔹 Complessità Spaziale (Space Complexity)**
# La complessità spaziale è determinata da **quanta memoria viene utilizzata dalla ricorsione**.
#
# 1. **Nel caso più semplice** (lista senza sotto-liste):  
#    - L'uso della memoria è **O(1)** perché non ci sono chiamate ricorsive.
#
# 2. **Nel caso peggiore** (lista profondamente annidata):  
#    - Se la lista ha `d` livelli di sotto-liste, la funzione effettua una chiamata ricorsiva per ciascun livello, quindi la memoria utilizzata sarà **O(d)**.
#
# 📌 **Caso Migliore (Best Case - O(1))**  
# - `'osvaldo'` è trovato subito → **non vengono fatte chiamate ricorsive**.
#
# 📌 **Caso Peggiore (Worst Case - O(d))**  
# - `'osvaldo'` si trova **alla massima profondità** della lista, quindi la funzione deve scendere fino a **d livelli di annidamento** prima di terminare.
#
# ### **📝 Formula Generale della Complessità Spaziale**
# S(n) = O(d)
# dove **d è la profondità della lista**.
#
# ---

# ## **🔍 Esempi Pratici di Complessità**
# | **Lista in Input**            | **n (elementi totali)** | **d (profondità)** | **Tempo O(n)** | **Spazio O(d)** |
# |--------------------------------|----------------------|-----------------|---------------|--------------|
# | `['osvaldo']`                     | 1                 | 1               | **O(1)**      | **O(1)**     |
# | `['mario', 'osvaldo', 'luigi']`   | 3                 | 1               | **O(2)** (trova `'osvaldo'` presto) | **O(1)** |
# | `['mario', ['osvaldo'], 'luigi']` | 3                 | 2               | **O(3)**      | **O(2)**     |
# | `[ ['a'], ['b'], ['c'], ['osvaldo'] ]` | 4            | 2               | **O(4)**      | **O(2)**     |
# | `[ [[[[[['osvaldo']]]]]] ]`            | 1            | 6               | **O(1)** (perché trova subito) | **O(6)** |

# ---

# ## **🔑 Conclusione**
# - **Complessità temporale**: **O(n)** nel caso peggiore, **O(1)** nel migliore.
# - **Complessità spaziale**: **O(d)**, dove **d** è la profondità delle sotto-liste.
#
# 🚀 **Se vuoi migliorare la funzione, potresti usare un approccio iterativo con una pila (stack) per evitare la ricorsione profonda!**




########################################################################################################################################################################################


# ### **🔍 Differenza tra `type()` e `isinstance()` in Python**
# Entrambe le funzioni, `type()` e `isinstance()`, vengono utilizzate per controllare 
# il tipo di una variabile, ma funzionano in modo diverso. Vediamo in dettaglio le differenze. 🚀

# ---
# ## **🔹 `type()`**
# 📌 **Controlla esattamente il tipo di un oggetto**, restituendo il suo tipo.  
# 📌 **Non considera le sottoclassi**, quindi un oggetto di una sottoclasse 
#     non viene riconosciuto come appartenente alla classe madre.

# ### **✅ Esempio di `type()`**
x = 5
print(type(x) == int)  # ✅ True

y = 5.5
print(type(y) == int)  # ❌ False

z = True
print(type(z) == bool)  # ✅ True

# Creiamo una classe personalizzata che eredita da `list`
class MiaLista(list):
    pass

m = MiaLista()
print(type(m) == list)  # ❌ False → perché `type(m)` è `MiaLista`, non `list`

# 🔹 `type()` restituisce il tipo esatto dell'oggetto, quindi non riconosce `MiaLista` 
#     come un `list`, anche se lo eredita.

# ---
# ## **🔹 `isinstance()`**
# 📌 **Verifica se un oggetto appartiene a un tipo specifico o a una sua sottoclasse**.  
# 📌 **Supporta il concetto di ereditarietà**, quindi può riconoscere anche le sottoclassi.

# ### **✅ Esempio di `isinstance()`**
x = 5
print(isinstance(x, int))  # ✅ True

y = 5.5
print(isinstance(y, int))  # ❌ False

z = True
print(isinstance(z, int))  # ✅ True → perché in Python `bool` è una sottoclasse di `int`!

# Creiamo una classe personalizzata che eredita da `list`
m = MiaLista()
print(isinstance(m, list))  # ✅ True → perché `MiaLista` eredita da `list`

# 🔹 `isinstance(m, list)` restituisce **True** perché `MiaLista` è una sottoclasse di `list`.

# ---
# ## **🔑 Differenza chiave tra `type()` e `isinstance()`**
# | **Funzione**  | **Controlla il tipo esatto?** | **Riconosce sottoclassi?** | **Uso consigliato** |
# |--------------|-----------------|-----------------|-----------------|
# | `type(obj) == some_type`     | ✅ Sì | ❌ No | Quando vuoi un confronto esatto tra tipi |
# | `isinstance(obj, some_type)` | ✅ Sì | ✅ Sì | Quando vuoi verificare se un oggetto è di un tipo o di una sua sottoclasse |

# ---
# ## **🛠️ Quando usare `type()` e quando `isinstance()`?**
# ✅ **Usa `type()`** quando vuoi confrontare un oggetto con un tipo esatto e vuoi evitare 
#     effetti dovuti all'ereditarietà.  
# ✅ **Usa `isinstance()`** quando vuoi verificare se un oggetto appartiene a un tipo o a 
#     una sua sottoclasse (più flessibile).  

# ### **Esempio pratico:**

def controlla_tipo(valore):
    if isinstance(valore, (int, float)):  # Può essere int o float
        print("È un numero")
    else:
        print("Non è un numero")

controlla_tipo(10)       # ✅ Output: È un numero
controlla_tipo(3.14)     # ✅ Output: È un numero
controlla_tipo("ciao")   # ❌ Output: Non è un numero

# 🚀 **In sintesi: `isinstance()` è più potente e flessibile rispetto a `type()` nella maggior parte dei casi!**

















#####################################################################################################################################################################################################

'''
Scrivere una funzione in Python che, data una lista a di numeri ordinati in
modo non decrescente ed un numero k restituiscela posizione della prima occorrenza del numero k
in a e la  la posizione dell'ultima occorrenza di k in a. Se k non è in a, ritorna -1.

Esempio:
Input: a = [1, 3, 4, 4, 4, 4, 5, 7, 7, 7, 7, 10, 10, 12, 12, 15, 17],
       k = 4
Output:  prima occorrenza: posizione 2; ultima occorrenza: posizione 5

'''
def Ricerca_bin_right(a, k):
    '''
    Questa funzione cerca la posizione dell'ultima occorrenza del numero k in una lista ordinata a.
    
    **ATTENZIONE:**
    Il codice contiene errori logici e non funzionerà correttamente.
    
    Parametri:
    - a: lista ordinata in modo non decrescente (elementi possono ripetersi)
    - k: numero da cercare
    
    Ritorna:
    - Indice dell'ultima occorrenza di k in a, oppure -1 se k non è presente
    '''
    N = len(a)  # Calcola la lunghezza della lista (non usato nel codice)
    
    lx, rx = 0, len(a) - 1  # Inizializza i limiti della ricerca binaria
    
    while lx < rx:  # Continua finché il limite sinistro non supera quello destro
        cx = int((lx + rx) / 2)  # Trova l'indice centrale

        if cx < k:  # qui controlliamo se il numero centrale è minore di k
            
            # Se l'elemento centrale fosse minore di k, dovremmo cercare a destra
            lx = cx - 1  
        
        elif k == a[cx] and (cx == 0 or a[cx - 1] < k):
            # Questa condizione è malformata e mancano le istruzioni!
            return cx  # Qui dovrebbe esserci un `return cx`
        
        else:
            # Se a[cx] > k, dobbiamo cercare a sinistra
            lx = cx + 1 
    
    return -1  # Se non troviamo k, restituiamo -1

'''
Funzione:
Scopo: Cerca la prima occorrenza del numero k nella lista a usando ricerca binaria.
Input: Una lista ordinata a e un numero k.
Output: L'indice della prima occorrenza di k, oppure -1 se k non è nella lista.
Passaggi chiave:
Si inizializzano i limiti della ricerca binaria (lx = 0, rx = len(a) - 1).
Si entra in un ciclo finché lx non supera rx:
Si calcola l'indice centrale cx.
Se a[cx] è minore di k, significa che k deve trovarsi a destra, quindi si aggiorna lx = cx + 1.
Se a[cx] è uguale a k e preceduto da un numero diverso da k, allora è la prima occorrenza → si ritorna cx.
Se a[cx] è maggiore di k, k deve trovarsi a sinistra, quindi si aggiorna rx = cx - 1.
Se il ciclo finisce e k non è stato trovato, si restituisce -1.
'''





#----------------------------------------------------------------

def binary_search_right(a, k):
    """
    Questa funzione cerca la posizione dell'**ultima occorrenza** dell'elemento k in una lista ordinata a.
    Anche questa utilizza la **ricerca binaria** con una complessità di O(log n).

    Parametri:
    - a : lista ordinata in modo non decrescente
    - k : numero da cercare

    Ritorna:
    - Indice dell'**ultima occorrenza** di k in a
    - Se k non è presente, restituisce -1
    """

    lx, rx = 0, len(a) - 1  # Inizializza i limiti della ricerca binaria

    while lx <= rx:
        cx = int((lx + rx) / 2)  # Calcola l'indice centrale

        if k < a[cx]:  
            # Se k è minore dell'elemento centrale, dobbiamo cercare nella parte sinistra
            rx = cx - 1  

        elif k == a[cx] and (cx == len(a) - 1 or a[cx + 1] > k):
            # Se l'elemento centrale è uguale a k e non è seguito da un altro k, lo abbiamo trovato
            return cx  

        else:
            # Se l'elemento centrale è minore di k, oppure k è presente dopo, cerca a destra
            lx = cx + 1  

    return -1  # Se non troviamo k, restituiamo -1
'''
Funzione:
Scopo: Cerca l'ultima occorrenza del numero k nella lista a usando ricerca binaria.
Input: Una lista ordinata a e un numero k.
Output: L'indice dell'ultima occorrenza di k, oppure -1 se k non è nella lista.
Passaggi chiave:
Si inizializzano i limiti (lx = 0, rx = len(a) - 1).
Si entra nel ciclo finché lx non supera rx:
Si calcola l'indice centrale cx.
Se a[cx] è maggiore di k, allora k deve essere a sinistra, quindi si aggiorna rx = cx - 1.
Se a[cx] è uguale a k e seguito da un numero diverso da k, allora è l'ultima occorrenza → si ritorna cx.
Se a[cx] è minore di k, significa che dobbiamo cercare a destra, quindi lx = cx + 1.
Se il ciclo finisce e k non è stato trovato, si restituisce -1.
'''


#----------------------------------------------------------------

def first_last_occurrence(a, k):
    """
    Questa funzione trova la **prima e l'ultima occorrenza** di k nella lista ordinata a.
    Per farlo, usa due ricerche binarie:
    - **binary_search_left** per trovare la prima occorrenza
    - **binary_search_right** per trovare l'ultima occorrenza

    Parametri:
    - a : lista ordinata in modo non decrescente
    - k : numero da cercare

    Ritorna:
    - Una tupla contenente (indice della prima occorrenza, indice dell'ultima occorrenza)
    - Se k non è presente, restituisce -1
    """

    # Trova la prima occorrenza di k usando binary_search_left
    first = binary_search_left(a, k)
    # Trova l'ultima occorrenza di k usando binary_search_right
    last = binary_search_right(a, k)

    # Se la prima ricerca ha restituito -1, significa che k non è nella lista
    if first == -1:
        return -1

    return first, last  # Ritorna la posizione della prima e dell'ultima occorrenza


# Esempio di utilizzo
a = [1, 3, 4, 4, 4, 4, 5, 7, 7, 7, 7, 10, 10, 12, 12, 15, 17]
k = 4

print(first_last_occurrence(a, k))  # Output: (2, 5)


# Funzione:
# Scopo: Restituisce la prima e l'ultima posizione di k nella lista.

# Input:
# - Una lista ordinata `a`
# - Un numero `k`

# Output:
# - Una tupla contenente (prima_occorrenza, ultima_occorrenza)
# - Oppure `-1` se `k` non è presente

# Passaggi chiave:
# 1. Chiama `binary_search_left(a, k)` per trovare la prima occorrenza.
# 2. Chiama `binary_search_right(a, k)` per trovare l'ultima occorrenza.
# 3. Se la prima occorrenza restituisce `-1`, significa che `k` non è nella lista, quindi restituisce `-1`.
# 4. Altrimenti, restituisce una tupla `(prima_occorrenza, ultima_occorrenza)`.

''' 🔹 Complessità Temporale '''

# 📈 Analisi della Ricerca Binaria
# La ricerca binaria funziona dividendo l'elenco a metà ad ogni passo.
# Supponiamo di avere una lista con `n` elementi.
# Ogni iterazione dimezza lo spazio di ricerca:

# Iterazione | Numero di elementi da esaminare
# --------------------------------------------
# 1          | n / 2
# 2          | n / 4
# 3          | n / 8
# ...        | ...
# k          | 1 (ferma quando c'è un solo elemento)

# L'equazione che descrive quante iterazioni servono per ridurre il numero di elementi a 1 è:
# n / 2^k = 1

# Risolvendo per `k`:
# k = log₂(n)

# Quindi la ricerca binaria ha una complessità temporale di **O(log n)**.

''' 🔹 Analisi della Complessità delle Funzioni '''

# - `binary_search_left(a, k)`  → O(log n)
#   (La ricerca binaria dimezza lo spazio di ricerca a ogni iterazione)
# - `binary_search_right(a, k)` → O(log n)
#   (Stessa logica della funzione precedente)
# - `first_last_occurrence(a, k)` → O(log n) + O(log n) = O(log n)
#   (Chiama due ricerche binarie, ma log n + log n = O(log n))

''' ⚡ Confronto con una Ricerca Lineare '''

# - Una ricerca lineare **O(n)** analizzerebbe ogni elemento dell'array uno per uno.
#   Per una lista con **1.000.000** elementi, nel peggiore dei casi richiederebbe **1.000.000** di confronti.
# - La ricerca binaria **O(log n)**, invece, dimezzando a ogni passo, farebbe solo:

# log₂(1.000.000) ≈ 20 operazioni

# 👉 **Molto più veloce!** 🚀

''' 🔥 Conclusione '''

# ✅ Il codice sfrutta la ricerca binaria per trovare rapidamente la prima e l'ultima occorrenza di un numero in una lista ordinata.
# ✅ La complessità è **O(log n)**, molto più efficiente di **O(n)** per liste grandi.
# ✅ Utile per grandi dataset, risparmiando tempo rispetto a una scansione lineare.





# ------------------------------------------------------------------------------------------------------------
# questa e' una versione alternativa con un po' di modifiche dopo elif 


def Ricerca_bin_right(a, k):
    '''
    parametri : data una lista a di numeri ordinati in modo non decrescente 
    
    ed un numero k che restituisce la posizione della prima occorrenza del numero k che e' in a
    poi la posizione dell'ultima occorrenza di k in a.
    
    ritorna : Se k non e' in a, ritorna -1.
    '''
    N = len(a)
    
    lx, rx = 0 , len(a) - 1
    
    while lx <= rx :# lx se e' minore di rx: 
        cx = int(( lx + rx )/2)
        if cx <= k : #Se l'elemento centrale è minore di k, la ricerca deve proseguire sulla destra.
            lx = cx - 1 
        elif k == a[cx] and(cx == 0 or a[cx - 1] < k) : # Se l'elemento centrale è uguale a k
            return cx                                        #e non è la prima occorrenza
        else: # altrimenti, la ricerca deve proseguire sulla sinistra.
             rx = cx + 1
    
    return -1

def binary_search_left(a, k):
    lx, rx = 0, len(a) - 1

    while lx <= rx:
        cx = int((lx + rx) / 2)
        if k > a[cx]:
            lx = cx + 1
        elif k == a[cx] and (cx == 0 or a[cx - 1] < k):
            return cx
        else:
            rx = cx - 1

    return -1




def first_last_occurrence(a, k):
    # usando binary_search_left, troviamo la prima occorrenza di k
    first = binary_search_left(a, k)
    # usando binary_search_right, troviamo l'ultima occorrenza di k
    last = binary_search_right(a, k)

    # se k non è in a (cioè le ricerche binarie restituiscono -1), allora
    # si restituisce -1
    if first == -1:
        return -1

    return first, last


a = [1, 3, 4, 4, 4, 4, 5, 7, 7, 7, 7, 10, 10, 12, 12, 15, 17]
k = 4

print(first_last_occurrence(a, k))



