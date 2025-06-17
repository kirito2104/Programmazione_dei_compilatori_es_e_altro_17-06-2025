# Ottimo che me lo chiedi Piero! Ti spiego in modo semplice **cos'è la complessità spaziale**, 
# **a cosa serve** e **come si calcola** — così non te lo scordi più 😉

# ----------------------------------------------------------
# 🧠 COSA SIGNIFICA "COMPLESSITÀ SPAZIALE"?
# La **complessità spaziale** misura **quanta memoria (RAM)** serve a un algoritmo per 
# funzionare in base alla dimensione dell’input.
# In parole semplici: **quanta roba serve salvare in memoria mentre il programma gira**.
# ----------------------------------------------------------

# ----------------------------------------------------------
# 🎯 A COSA SERVE?
# Serve a:
# - Ottimizzare programmi che girano su dispositivi con **poca RAM**.
# - Evitare algoritmi che consumano troppa memoria su input grandi.
# - Capire **quanto "pesante" è un algoritmo**, non solo in termini di tempo ma anche di spazio.
# ----------------------------------------------------------

# ----------------------------------------------------------
# 🔍 COME SI CALCOLA?
# Si conta **la quantità di variabili o strutture dati create durante l’esecuzione** 
# in funzione dell'input.
#
# ✨ Due casi:
# 1. **Spazio extra fisso → `O(1)` (costante)**  
#    - Usi solo variabili semplici (`i`, `j`, contatori, flag...).
#    - NON dipende dalla lunghezza dell’input.
#
# 2. **Spazio extra proporzionale all’input → `O(n)` o altro**  
#    - Usi **liste, set, dict** che crescono con l’input.
#    - Esempio: costruisci una lista di output lunga quanto `n` → `O(n)`
# ----------------------------------------------------------

# ----------------------------------------------------------
# ✅ NEL TUO CASO:
def intersezione(L1, L2):
    i, j = 0, 0           # → variabili scalari → spazio costante
    risultato = []        # → output, quindi non conta nello spazio supplementare

# - `i` e `j` sono variabili → **spazio costante**
# - `risultato` cresce, ma è **l’output**, quindi **non conta** se ti riferisci allo spazio **supplementare**
# - Non usi strutture extra → **complessità spaziale = `O(1)`**
#
# 📌 Se però **consideri anche l’output**, allora diventa `O(k)` dove `k` è il numero di elementi comuni tra `L1` e `L2`.
# ----------------------------------------------------------

# ----------------------------------------------------------
# 🧮 Riepilogo:

# | Tipo di spazio            | Cosa significa            | Esempio                     | Complessità |
# |---------------------------|---------------------------|-----------------------------|-------------|
# | Fisso (costante)          | Solo variabili scalari    | `i = 0`, `j = 0`            | `O(1)`      |
# | Proporzionale all'input   | Lista, dizionario, ecc.   | `output = list(n)`          | `O(n)`      |
# | Dipende da output         | Output cresce con i dati  | `output = [x for x in L1]`  | `O(k)`      |
# -----------------------------------------------------------------------------------------------------

#####################################################################################################################################################
############################################################################################################################################################


# Certo Piero! Ecco altri **casi tipici di complessità spaziale**, spiegati in modo **conciso, preciso** e con esempi pratici:

# ------------------------------------------------------------------
# 🟢 `O(1)` – **Spazio Costante**
# 🔹 Definizione: la memoria usata **non cresce** con l’input.
# 📦 Esempio: solo variabili scalari (int, bool...).

def somma(L):
    tot = 0
    for x in L:
        tot += x
    return tot

# ✅ Solo `tot` → **O(1)**

# ------------------------------------------------------------------
# 🔵 `O(n)` – **Lineare**
# 🔹 Definizione: spazio usato cresce **proporzionalmente** alla dimensione dell’input.
# 📦 Esempio: copi input, costruisci lista o dict grandi quanto `n`.

def copia_lista(L):
    return L[:]  # nuova lista grande quanto L

# ✅ Output di dimensione `n` → **O(n)**

# ------------------------------------------------------------------
# 🟠 `O(log n)` – **Logaritmica**
# 🔹 Definizione: usi memoria extra che cresce **logaritmicamente** rispetto all’input.
# 📦 Esempio: ricerca binaria ricorsiva.

def ricerca_binaria(L, x, inizio, fine):
    # Caso base: se l'intervallo è vuoto, l'elemento non è presente
    if inizio > fine:
        return False

    # Calcola l'indice centrale dell'intervallo corrente
    mid = (inizio + fine) // 2

    # Se l'elemento centrale è quello cercato, restituisci True
    if L[mid] == x:
        return True

    # Se l'elemento cercato è più piccolo, cerca nella metà sinistra
    elif x < L[mid]:
        return ricerca_binaria(L, x, inizio, mid - 1)

    # Altrimenti cerca nella metà destra
    else:
        return ricerca_binaria(L, x, mid + 1, fine)


# ✅ Stack di chiamate profondo `log n` → **O(log n)**

# ------------------------------------------------------------------
# 🔴 `O(n²)` – **Quadratica**
# 🔹 Definizione: memoria cresce **al quadrato** dell’input (tipico in tabelle 2D).
# 📦 Esempio: matrice `n x n`.

def matrice_z(n):
    return [[0]*n for _ in range(n)]

# ✅ Crea matrice `n×n` → **O(n²)**

# ------------------------------------------------------------------
# 🟣 `O(2^n)` – **Esponenziale**
# 🔹 Definizione: spazio cresce **esponenzialmente** con l’input.
# 📦 Esempio: algoritmi bruteforce o ricorsione senza memoization.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# ✅ Stack cresce come `2^n` → **O(2^n)** (spazio e tempo)

# ------------------------------------------------------------------
# 📌 Nota: se usi **memoization**, puoi passare da `O(2^n)` a **O(n)**, 
#         ma usi più spazio (per la cache).

# **tabella riassuntiva** dei casi più comuni di **complessità spaziale**, 
# con definizione, esempio e nota chiave:

# ------------------------------------------------------------------
# 🧠 Tabella: Complessità Spaziale a Confronto
#
# | Complessità | Cosa significa                      | Esempio codice                           | Spazio usato                  |
# |-------------|-------------------------------------|---------------------------------------- -|-------------------------------|
# | `O(1)`      | Spazio costante                     | `tot = 0`                                | Solo variabili scalari        |
# | `O(n)`      | Spazio proporzionale all'input      | `copia = L[:]`                           | Lista lunga quanto l’input    |
# | `O(log n)`  | Cresce lentamente (ricorsione log)  | Ricerca binaria                          | Stack chiamate profondo log n |
# | `O(n²)`     | Spazio quadratico                   | `[[0]*n for _ in range(n)]`              | Matrice `n×n`                 |
# | `O(2^n)`    | Spazio esponenziale                 | `fibonacci(n)` senza memoization         | Ricorsione esplosiva          |

# ------------------------------------------------------------------
# 📌 Memoization:
# - Trasforma `O(2^n)` in `O(n)` in termini di tempo,
#   ma **richiede più memoria** per la **cache** → spesso `O(n)` spazio.

# ------------------------------------------------------------------
