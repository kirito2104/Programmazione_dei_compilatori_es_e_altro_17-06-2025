





# ---
# 
# ## **2. Analisi della complessità per ogni istruzione**
# 
# | Istruzione                     | Complessità | Note |
# |--------------------------------|-------------|------|
# | `d = {}`                        | O(1) | Creazione di un dizionario vuoto |
# | `c = 0`                         | O(1) | Assegnamento semplice |
# | `for x in a:`                   | O(n) | Il ciclo viene eseguito per ogni elemento di `a` |
# | `if x in d:`                    | O(1) **(caso medio)** / O(n) **(caso peggiore)** | Controllo presenza nel dizionario |
# | `c += 1`                        | O(1) | Incremento semplice |
# | `d[x] = None`                   | O(1) **(caso medio)** / O(n) **(caso peggiore)** | Inserimento nel dizionario |
# | `print(d)`                      | O(n) | Dipende dal numero di elementi in `d`, ma non incide molto sul costo totale |
# 
# ---
# 
# ## **3. Caso Medio: Complessità Lineare O(n)**
# Nella maggior parte dei casi:
# - L’operazione `x in d` è **O(1)** perché i dizionari Python usano **hash table**.
# - L'operazione `d[x] = None` è **O(1)**.
# 
# Il ciclo principale viene eseguito `n` volte, quindi la complessità totale è **O(n)**.
# 
# ---
# 
# ## **4. Caso Peggiore: Complessità Quadratica O(n²)**
# Nel peggiore dei casi:
# - Se ci sono molte **collisioni di hash**, l'operazione `x in d` potrebbe dover 
# **scansionare una lista interna** all'interno della tabella hash, portando la ricerca a **O(n)** per elemento.
# - Se `x in d` diventa O(n), e viene eseguito per ogni elemento in `a`, la complessità totale diventa **O(n) * O(n) = O(n²)**.
# 
# Un caso in cui il peggiore scenario può verificarsi:
# - Se la funzione viene eseguita su un **input molto grande** con **molti elementi con lo stesso hash** 
# (es. con hash mal distribuiti, cosa che può accadere raramente nei dizionari Python).
# 
# ---
# 
# ## **5. Risposta Corretta**
# La tua scelta **"Quadratica nel caso peggiore"** è **giusta** perché:
# ✅ Nel **caso medio**, la complessità è **O(n)**.  
# ✅ Nel **caso peggiore**, a causa delle collisioni hash, può diventare **O(n²)**.  
# ❌ Non è "Quadratica sempre", perché il caso medio è **solo O(n)**.  
# 
# ---
# 
# ## **6. Conclusione**
# Hai risposto correttamente perché **la funzione è quadratica solo nel caso peggiore** 
# quando ci sono **molte collisioni di hash nel dizionario**. In media, invece, è lineare.
# 
# **Risposta corretta:**
# ✔ **Quadratica nel caso peggiore** ✅  
# ❌ **Quadratica sempre** è sbagliato, perché la maggior parte delle volte è **lineare**.



########################################################################################################################################################
#°° ECCO DEGLI ESEMPI SIEGATI CON LE VARIE COMPLESSITà :
'''
### **Casistiche comuni e come riconoscere la complessità dello spazio e del tempo**
'''

# La complessità dello **spazio** e del **tempo** occupato da una struttura dati dipende 
# da come vengono allocati, memorizzati e processati gli elementi.

# La complessità temporale misura il numero di operazioni eseguite in funzione della dimensione 
# dell'input.

# La complessità spaziale misura la quantità di memoria utilizzata in funzione dell'input.
# Vediamo diverse casistiche con esempi e come riconoscerle.

'''
## **1 Strutture lineari - O(n)**
'''

# 📌 **Regola**: Se una struttura cresce con la dimensione dell'input e ogni elemento è memorizzato
# o processato una sola volta, lo spazio e il tempo sono lineari.

'''
### **Esempio 1: Lista di `n` elementi**
'''
# Creazione di una lista con n elementi

'''
a = [i for i in range(n)]
'''
# ✔ **Analisi**:
# - **Spazio**: La lista `a` contiene `n` elementi, quindi occupa **O(n)** memoria.
# - **Tempo**: La creazione della lista richiede un'iterazione su `n`, quindi **O(n)**.

'''
### **Esempio 2: Scansione di una lista**
'''
# Iterazione su una lista
'''

a = [i for i in range(n)]
for elem in a:
    print(elem)
    
'''

# ✔ **Analisi**:
# - **Spazio**: La lista `a` occupa **O(n)** spazio.
# - **Tempo**: L'iterazione su tutti gli `n` elementi richiede **O(n)** tempo.

'''
## **2 Strutture quadratiche - O(n²)**
'''

# 📌 **Regola**: Se ogni elemento genera o contiene un'altra struttura di dimensione `O(n)`,
# il totale può diventare **O(n²)**.

'''
### **Esempio: Matrice quadrata e doppio ciclo**
'''
# Creazione di una matrice quadrata
def matrix(n):
    # Creazione di una matrice quadrata n x n inizializzata con zeri
    # Questo utilizza una list comprehension: per ogni riga (n righe), crea una lista con n zeri
    matrix = [[0] * n for _ in range(n)]  

    # Doppio ciclo annidato per iterare su ogni elemento della matrice
    # range(n) restituisce una sequenza di numeri interi da 0 a n-1
    # Nel ciclo esterno 'i' rappresenta l'indice di riga
    for i in range(n):
        # Nel ciclo interno 'j' rappresenta l'indice di colonna
        for j in range(n):
            # L'elemento nella posizione (i, j) viene aggiornato con la somma degli indici di riga e colonna
            # Questo significa che la diagonale principale avrà sempre numeri pari (i+j con i==j → 2*i),
            # e gli altri elementi aumentano con la distanza dalla posizione (0,0)
            matrix[i][j] = i + j
    '''
    # Per evitare n^2 bisogna mettere il for non sotto al altro for ma staccato,
    # questo permette di evitare che i due for avvengano in parallelo e che il tempo diventa n^3.
    
    '''
    # Restituisce la matrice risultante
    return matrix
print(matrix(3))
# Output:
# [[0, 1, 2],
#  [1, 2, 3],
#  [2, 3, 4]]


# ✔ **Analisi**:
# - **Spazio**: La matrice ha `n × n` elementi, quindi occupa **O(n²)** memoria.
# - **Tempo**: Ogni elemento viene elaborato una volta, ma il doppio ciclo comporta **O(n²)** operazioni.

'''
## **3 Strutture cubiche - O(n³)**
'''

# 📌 **Regola**: Se ogni elemento ha una struttura di O(n²) e viene visitato in tre cicli annidati,
# il totale diventa O(n³).

'''
### **Esempio: Matrice tridimensionale**
'''
# Creazione di una matrice tridimensionale
'''
cube = [[[0] * n for _ in range(n)] for _ in range(n)]

# Triplo ciclo annidato
for i in range(n):
    for j in range(n):
        for k in range(n):
            cube[i][j][k] = i + j + k
'''
# ✔ **Analisi**:
# - **Spazio**: La matrice tridimensionale contiene `n × n × n` elementi, quindi **O(n³)**.
# - **Tempo**: Ogni elemento viene aggiornato in un triplo ciclo, risultando in **O(n³)** operazioni.

'''
## **4 Strutture logaritmiche - O(log n)**
'''

# 📌 **Regola**: Se la struttura divide ripetutamente i dati in due parti, il tempo è spesso **O(log n)**.

'''
### **Esempio: Ricerca binaria**
'''
# Funzione per ricerca binaria
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ✔ **Analisi**:
# - **Spazio**: La ricerca binaria non utilizza memoria aggiuntiva, quindi **O(1)**.
# - **Tempo**: L'intervallo di ricerca si dimezza a ogni iterazione, risultando in **O(log n)** operazioni.

'''
## **5 Strutture quasi lineari - O(n log n)**
'''

# 📌 **Regola**: Se l'algoritmo richiede ordinamenti o altre operazioni che combinano una scansione
# lineare con divisioni logaritmiche, il tempo può essere **O(n log n)**.

'''
### **Esempio: Merge Sort**
'''
# Implementazione di Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ✔ **Analisi**:
# - **Spazio**: Merge Sort utilizza spazio addizionale per le liste suddivise, quindi **O(n)**.
# - **Tempo**: Ogni divisione dimezza il problema e richiede una ricombinazione lineare, 
# risultando in **O(n log n)**.

'''
## **6 Strutture sommate - O(n + m)**
'''

# 📌 **Regola**: Se il problema coinvolge due strutture di dimensioni diverse,
#               la complessità è la somma dei loro contributi.

'''
### **Esempio: Unione di due liste**
'''
# Unione di due liste
def merge_lists(list1, list2):
    return list1 + list2

# ✔ **Analisi**:
# - **Spazio**: La lista risultante ha dimensione `n + m`, quindi **O(n + m)**.
# - **Tempo**: La concatenazione richiede la copia di entrambi gli array, quindi **O(n + m)**.


##############################################################################################


## ** 7  Strutture costanti - O(1)**
'''

# 📌 **Regola**: Se la dimensione della struttura è indipendente dall'input e 
# le operazioni avvengono in tempo fisso, lo spazio e il tempo sono costanti **O(1)**.

'''
### **Esempio: Accesso a un elemento di un array**
'''
# Accesso diretto a un elemento di una lista
a = [1, 2, 3, 4, 5]
x = a[2]

# ✔ **Analisi**:
# - **Spazio**: La lista `a` è di dimensione fissa, quindi **O(1)**.
# - **Tempo**: L'accesso a un elemento in un array indicizzato è istantaneo, quindi **O(1)**.

'''

## **78��� Strutture esponenziali - O(2^n)*
    # **Regola**: Se l'algoritmo richiede ordinamenti o altre operazioni 
    # che combinano una scansione lineare con divisioni esponenziali, 
    # il tempo può essere **O(2^n)**.
 
'''   
## **Come riconoscere la complessità dello spazio e del tempo?**
'''

# 1. **Osserva le dimensioni della struttura dati** → Se cresce con `n`, lo spazio è almeno **O(n)**.
# 2. **Conta i cicli annidati** → Se ci sono due cicli `for`, il tempo è **O(n²)**, se tre **O(n³)**, ecc.
# 3. **Verifica le divisioni di dati** → Se il problema si dimezza a ogni iterazione, 
#       il tempo è **O(log n)**.

# 4. **Guarda le operazioni costanti** → Se eseguite una sola volta indipendentemente da `n`,
# il tempo è **O(1)**.
# 5. **Differenzia tra operazioni sequenziali e parallele** → Se gli elementi vengono processati
#                                       contemporaneamente in più thread, il tempo potrebbe ridursi.
