



#Esercizio

'''
Scrivere una funzione in Python che, data una lista binaria a, cioè contenente unicamente elementi in {0,1},
ordina la lista a. La funzione deve avere complessità temporale lineare in len(a) e complessità spaziale costante.
'''


#Esempio:

#Input:  [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
#Output:  [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]




lista = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]


'''
definizione della funzione per odrinare una lista 

'''




'''
Ecco alcuni consigli per aiutarti a scrivere il codice da zero senza copiarlo, mantenendo 
la complessità temporale O(n) e spaziale O(1):
'''

'''
1 Analizza il problema
'''
# - La lista contiene solo `0` e `1`.
# - Dopo l'ordinamento, tutti gli `0` devono essere a sinistra e tutti gli `1` a destra.
# - Non puoi usare funzioni di ordinamento O(n log n) come `sorted()` o `sort()`,
#   perché devi mantenere la complessità O(n).

# - Devi modificare la lista in-place, quindi non puoi creare nuove liste (complessità spaziale O(1)).

'''
2 Trova una strategia efficace
'''
# - **Conta gli `0`** : Scorri la lista una volta e conta quanti `0` ci sono.
# - **Sovrascrivi la lista**:
#   - Metti `0` nei primi `z` posti.
#   - Metti `1` nel resto della lista.
#
# > **Suggerimento:** Usa due passaggi sulla lista (uno per contare e uno per riscrivere)
#   per rispettare la complessità O(n).

'''
3 Evita gli errori comuni
'''
# ✔ **Non usare metodi di ordinamento predefiniti**, perché non sarebbero O(n).
# ✔ **Non creare nuove liste**, perché la memoria extra renderebbe la complessità spaziale O(n) invece di O(1).
# ✔ **Attento agli indici**: Quando modifichi la lista, assicurati di non accedere a posizioni fuori dall’intervallo.
# ✔ **Evita più cicli annidati**: Se usi due `for` annidati, finirai con O(n²), il che è sbagliato.

'''
4 Scrivi il codice mentalmente prima di programmarlo
'''
# - **Passo 1**: Conta quanti `0` ci sono in `a`.
# - **Passo 2**: Scrivi `0` nelle prime `z` posizioni.
# - **Passo 3**: Scrivi `1` nelle restanti posizioni.
# - **Passo 4**: Stampa il risultato e verifica se funziona con test diversi.
#
# > **Tecnica utile:** Prova a scriverlo su carta prima di passare a Python!

'''
5 Testa il codice con diversi input
'''
# Dopo averlo scritto, provalo con:
# - Una lista con solo `0`: `[0, 0, 0, 0]`
# - Una lista con solo `1`: `[1, 1, 1, 1]`
# - Una lista già ordinata: `[0, 0, 0, 1, 1, 1]`
# - Una lista con `0` e `1` mescolati in vari modi.
#
# Questo ti aiuterà a verificare che il tuo codice funzioni in tutti i casi.



def ordina_list_binaria (a):
     """
    l'idea è la seguente: sia z il numero di zeri in a.
    Allora è sufficiente modificare la lista inserendo 0
    nelle prime z posizioni e inserendo 1 nelle ultime
    len(a)-z posizioni
    """

     z = 0
     for l in a : 
        if l == 0:
            z += 1  #Incrementa il contatore degli 0
  
        # qui sopra ho ridefinito a e poi ho verificato che  fosse uguale a 0 se lo è incrementa di 1 
     k = 0
     #  questo ciclo inserisce 1 nelle posizioni restanti
     while z:  
        a[k] = 0  # Scrive 0 nella posizione k
        z = z - 1  # Riduce il numero di zeri da scrivere
        k = k + 1  # Sposta avanti l'indice k
     for j in range(k,len(a)):
        a[j] = 1 # Inserisce 1 nelle posizioni restanti


a = [0,0,0,1,1,0,0,1,1,1,0]


print('input:',a)

s = ordina_list_binaria(a)

print('output:',a)

### **Come Sommare e Capire la Complessità Temporale O(n)**
### Per analizzare la complessità temporale del codice, dobbiamo contare quante operazioni vengono eseguite **in funzione della dimensione della lista** `n`.

### ---

### **Passo 1: Identificare i Cicli**
### Nel codice ci sono **due cicli principali**:

### 1️⃣ **Primo ciclo: Conta gli zeri**  
### z = 0  # Inizializza il contatore degli 0
### for e in a:  
###     if e == 0:  
###         z += 1  # Conta quanti 0 ci sono nella lista

### 🔹 **Quante iterazioni?**  
### - Questo `for` scorre **tutta la lista `a` una volta**.
### - La dimensione della lista è `n`, quindi viene eseguito **O(n)** volte.

### ---

### 2️⃣ **Secondo ciclo: Scrive gli 0 nella lista**  
### k = 0  
### while z:  
###     a[k] = 0  
###     z -= 1  
###     k += 1  

### 🔹 **Quante iterazioni?**  
### - Il `while` viene eseguito **z volte**, dove `z` è il numero di `0` nella lista.  
### - Nel caso peggiore, tutti gli elementi di `a` sono `0`, quindi `z = n`.  
### - **Nel caso medio**, `z ≈ n/2`, ma la complessità resta **O(n)**, perché nel peggiore dei casi (tutti `0`), ci vogliono `n` operazioni.

### ---

### 3️⃣ **Terzo ciclo: Scrive gli 1 nella lista**  
### for j in range(k, len(a)):  
###     a[j] = 1  

### 🔹 **Quante iterazioni?**  
### - Questo ciclo scorre gli ultimi elementi della lista e scrive `1`.  
### - Poiché `k` è già stato incrementato `z` volte, rimangono `n - z` iterazioni.  
### - Anche questo ciclo nel caso peggiore può arrivare fino a **O(n)**.

### ---

### **Passo 2: Sommare le Complessità**
### Ogni operazione significativa è stata eseguita in:
### - **Primo ciclo:** `O(n)`
### - **Secondo ciclo:** `O(n)`
### - **Terzo ciclo:** `O(n)`

### **Sommando tutto:**
### \[
### O(n) + O(n) + O(n) = O(3n)
### \]

### ---

### **Passo 3: Regola di Semplificazione**
### 🔹 **Regola della notazione Big-O:**  
### - Quando si sommano più termini **O(n)**, si prende **il termine dominante**, ignorando le costanti.
### - **O(3n) si semplifica in O(n)** perché le costanti non contano nella notazione Big-O.

### ---

### **Conclusione**
### La complessità temporale **finale** del codice è **O(n)**, perché ogni elemento della lista viene visitato **al massimo una volta** in ciascun ciclo.  
### **Anche se ci sono più cicli, la somma delle iterazioni è proporzionale a `n`, quindi rimane lineare.** 🚀

'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





### **Come Riconoscere la Complessità Temporale di una Funzione** 🚀

### Determinare la **complessità temporale** di una funzione significa 
##  **stimare il numero di operazioni** che esegue in base alla grandezza dell'input `n`.  
### Ecco un metodo passo passo per **riconoscere e calcolare la complessità temporale** di una funzione.

### ---

### **1️⃣ Conta i Cicli e le Iterazioni**
### **Regola base**:
### - **Un ciclo `for` o `while` che scorre da `0` a `n` → O(n)**
### - **Un ciclo annidato (`for` dentro un `for`) → O(n²)**
### - **Un ciclo che dimezza `n` ogni volta (`n /= 2`) → O(log n)**

### 📌 **Esempi**:
### ```python
### # Complessità O(n) - scorre tutta la lista
### def linear_search(arr, x):
###     for e in arr:
###         if e == x:
###             return True
###     return False
### ```
### - **Motivo**: Il ciclo scorre al massimo `n` elementi → **O(n)**.

### ```python
### # Complessità O(n²) - due cicli annidati
### def bubble_sort(arr):
###     for i in range(len(arr)):       # O(n)
###         for j in range(len(arr)):   # O(n)
###             if arr[j] > arr[j + 1]:
###                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
### ```
### - **Motivo**: Il primo ciclo fa `n` iterazioni e per ogni iterazione il secondo ciclo fa altre `n` iterazioni → **O(n * n) = O(n²)**.

### ---

### **2️⃣ Identifica le Operazioni Dominanti**
### Se una funzione ha più parti con complessità diverse, la sua **complessità è determinata dalla parte più lenta**.

### 📌 **Esempio**:
### ```python
### def mixed_function(arr):
###     for i in range(len(arr)):  # O(n)
###         print(arr[i])
    
###     for i in range(len(arr)):  # O(n)
###         for j in range(len(arr)):  # O(n)
###             print(arr[i], arr[j])  # O(n²)
### ```
### - **Qui abbiamo**:
###   - Un ciclo **O(n)**.
###   - Un ciclo annidato **O(n²)**.
### - **La complessità totale è O(n²) perché è la più lenta e dominante.**

### ---

### **3️⃣ Osserva le Funzioni Ricorsive**
### 📌 **Regole per la complessità della ricorsione**:
### - **Se una funzione chiama sé stessa con `n-1` → O(n)**
### - **Se dimezza il problema a ogni chiamata → O(log n)**
### - **Se fa due chiamate per ogni livello → O(2ⁿ)** (es. Fibonacci)

### 📌 **Esempio O(n) (ricorsione lineare)**:
### ```python
### def factorial(n):
###     if n == 1:
###         return 1
###     return n * factorial(n-1)
### ```
### - **Ad ogni chiamata `n` diminuisce di `1`** → `O(n)`.

### 📌 **Esempio O(log n) (ricorsione che divide il problema a metà)**:
### ```python
### def binary_search(arr, left, right, x):
###     if left > right:
###         return -1
###     mid = (left + right) // 2
###     if arr[mid] == x:
###         return mid
###     elif arr[mid] > x:
###         return binary_search(arr, left, mid-1, x)
###     else:
###         return binary_search(arr, mid+1, right, x)
### ```
### - **Dimezza il problema ad ogni chiamata** → `O(log n)`.

### ---

### **4️⃣ Confronta le Complessità Comuni**
### | **Complessità** | **Tipico Caso d'Uso** | **Esempi** |
### |--------------|-------------------|-----------|
### | **O(1)** | Costante | Accesso a un array `arr[i]` |
### | **O(log n)** | Divisione a metà | Binary search |
### | **O(n)** | Un singolo ciclo | Scansione di un array |
### | **O(n log n)** | Algoritmi efficienti di ordinamento | Merge Sort, Quick Sort |
### | **O(n²)** | Doppio ciclo annidato | Bubble Sort, Selection Sort |
### | **O(2ⁿ)** | Ricorsione esponenziale | Fibonacci senza memoization |

### ---

### **5️⃣ Errori Comuni da Evitare**
### ❌ **Non confondere cicli sequenziali e annidati**  
### ```python
### for i in range(n):   # O(n)
###     print(i)
    
### for j in range(n):   # O(n)
###     print(j)
### ```
### ✅ Qui **non è** `O(n²)`, ma `O(n + n) = O(n)`, perché sono due cicli **indipendenti**.

### ---

### **Conclusione**
### 🔹 **Guarda i cicli**: Singolo → O(n), Doppio annidato → O(n²), Divisione a metà → O(log n).  
### 🔹 **Controlla le operazioni dominanti** e ignora i termini meno significativi.  
### 🔹 **Analizza la ricorsione**: Se `n` cala linearmente → O(n), Se si divide per `2` → O(log n).  
### 🔹 **Evita di confondere cicli separati con cicli annidati**.  

#####################################################################################################################################################à



#esercizio
#Scrivere una funzione in Python che, date due liste l1 e l2 entrambe ordinate, 
# restituisce una lista che è l'intersezione delle due liste l1 e l2. La soluzione
# deve avere complessità temporale lineare in len(l1) + len(l2), e memoria supplementare costante, possibilmente.

#Nota: considerate le liste come insiemi, ovvero, non ci sono elementi ripetuti.


#Esempio:


'''
-PSUDOCODE:

definie le due liste 
- creare un iteratore per far scorrere la lista 
creo un for separato e rinomino l1 e l2  li faccio  scorrere  in parallelo 


'''
def intersect_sorted (l1,l2):
    
    raccoglimento_liste = []
    i = 0
    j = 0
    #for i,j in l1,l2: 
    while i < len(l1) and j < len(l2):
       # se i-esimo elemento di l1 e j-esimo
        # elemento di l2 sono uguali, allora
        # tale elemento appartiene alla intersezione
        # delle due liste
      
        if l1[i] == l2[j]:   
            raccoglimento_liste.append(l1[i])
            i += 1
            j += 1
            # se i-esimo elemento di l1 è minore di j-esimo elemento di l2
            # se l'i-esimo elemento di l1 è più piccolo
            # del j-esimo elemento di l2, allora, dato che la lista
            # l2 è ordinata, l'elemento i-esimo di l1 non si trova in l2,
            # dunque non fa parte dell'intersezione delle due liste.
            # Avanza l'indice i.
            ''' Nel caso in cui non esita un elemento in l1  che sia  in l2  verra  scritto 
            un  else che  avanza l'indice  j  per  non  perder  la  condizione  del  while  '''
        elif l1[i] < l2[j]: # qui verifico che l1 sia minore di l2
            i += 1 # qui incremento l'indice di l1
           
            '''
            # se il j-esimo elemento di l2 è più piccolo
            # del i-esimo elemento di l1, allora, dato che la lista
            # l1 è ordinata, l'elemento j-esimo di l2 non si trova in l1,
            # dunque non fa parte dell'intersezione delle due liste.
            # Avanza l'indice j.
            '''
            
        else: # qui verifico che l2 sia minore di l1
            j += 1 # qui incremento l'indice di l2
    return raccoglimento_liste       
    
    #complessità temporale O(n + m) nel primo cliclo n = len(l1) e m = len(l2)
    #complessità spaziale O(1) perchè   se il j-esimo elemento di l

#testiamo la funzione
#Input:
l1 =  [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
l2 =  [1, 3, 4, 6, 7, 10, 13, 22, 23, 24, 25, 26, 45, 69, 99, 121]
#Output:  [1, 3, 6, 7, 22, 23, 45, 99]


print("Input:")
print("l1 = ", l1)
print("l2 = ", l2)
print("Output: ", intersect_sorted(l1, l2))
    
    
'''
**Qual è la strategia migliore?**
- Dato che le liste sono **ordinate**, possiamo usare **due indici** (`i` per `l1` e `j` per `l2`) e **scorrerle in parallelo**.
- Se `l1[i] == l2[j]`, allora l'elemento è **nell'intersezione** e lo aggiungiamo al risultato.
- Se `l1[i] < l2[j]`, significa che `l1[i]` **non esiste in l2**, quindi possiamo **avanzare `i`**.
- Se `l2[j] < l1[i]`, significa che `l2[j]` **non esiste in l1**, quindi possiamo **avanzare `j`**.
- **Terminiamo** quando uno dei due indici esce dai limiti della lista.
'''










'''
Ecco alcuni **consigli e suggerimenti** per aiutarti a **scrivere il codice da solo senza copiarlo**,
rispettando la **complessità temporale O(n + m)** e la **complessità spaziale O(1)**.
'''

'''
### **1 Capisci il Problema**

- **Le liste sono già ordinate**: Questo è fondamentale perché ci permette di confrontarle in modo efficiente.
- **Vogliamo l'intersezione**: Dobbiamo trovare gli elementi **comuni** tra `l1` e `l2`.
- **Non ci sono elementi ripetuti**: Ogni valore compare al massimo una volta per lista.
'''


'''
### **2 Scegli una Strategia Efficiente**

✅ **Non usare operazioni O(n²)** (es. `for` annidati) → L'obiettivo è O(n + m).  
✅ **Non creare nuove strutture dati inutili** → La memoria deve essere **O(1)**.

**Qual è la strategia migliore?**
- Dato che le liste sono **ordinate**, possiamo usare **due indici** (`i` per `l1` e `j` per `l2`) e **scorrerle in parallelo**.
- Se `l1[i] == l2[j]`, allora l'elemento è **nell'intersezione** e lo aggiungiamo al risultato.
- Se `l1[i] < l2[j]`, significa che `l1[i]` **non esiste in l2**, quindi possiamo **avanzare `i`**.
- Se `l2[j] < l1[i]`, significa che `l2[j]` **non esiste in l1**, quindi possiamo **avanzare `j`**.
- **Terminiamo** quando uno dei due indici esce dai limiti della lista.
'''

'''
### **3 Evita gli Errori Comuni**

❌ **Non usare `for` annidati**, altrimenti la complessità diventa O(n × m).  
❌ **Non convertire le liste in set**, perché l'operazione `set(l1) & set(l2)` richiede memoria extra O(n).  
❌ **Non riordinare le liste**, perché sono già ordinate, quindi un `sort()` sarebbe uno spreco di tempo.
'''

'''
### **4 Scrivi un Piano per il Codice**

🔹 **Passo 1**: Crea una lista `result` per memorizzare l'intersezione.  
🔹 **Passo 2**: Usa due indici `i` e `j` per scorrere `l1` e `l2`.  
🔹 **Passo 3**: Confronta `l1[i]` con `l2[j]` e aggiorna gli indici di conseguenza.  
🔹 **Passo 4**: Quando una delle due liste finisce, interrompi il ciclo.  
🔹 **Passo 5**: Restituisci `result`.
'''

'''
### **5 Testa il Codice**
Dopo averlo scritto, prova a testarlo con:

✅ **Due liste con elementi in comune**  
✅ **Due liste senza elementi in comune**  
✅ **Una lista vuota e una non vuota**  
✅ **Liste con un solo elemento**  
'''

'''
Ora prova a scriverlo **senza guardare la soluzione!** 💻🔥  
Se trovi difficoltà, torna a questi suggerimenti e ripensa alla logica. 🚀
'''

########################################################################################################################################################################################################
########################################################################################################################################################################################

#Scrivere una funzione in Python che implementa l'algoritmo di ricerca binaria
#destra usando la ricorsione. In particolare dunque, data una lista 'a' 
#di numeri ordinati in modo non decrescente ed un numero 'k', la funzione 
#restituisce la posizione dell'occorrenza più a destra di 'k'in 'a'
#Se 'k' non è in 'a', ritorna -1.


''' 
creo una  che fa la ricerca binaria partendo da desto andando poi verso sinstra
creo poi lx e rx  e poi li divido creando un centro, poi faccio partire la ricrca verso destra 
 e poi verso sinistra 

prima di cio creo un cliclo dove se lx è minore di rx torna -1
  
'''
#ricerca binaria verso destra 

def ricerca_bin_right(a,k,lx,rx):
    
    if lx > rx:
        return -1 # Se lx ha superato rx, significa che k non è presente

    '''
    Perché lo usiamo?
        
        lx (indice sinistro) rappresenta la parte iniziale della porzione di lista che stiamo esplorando.
        rx (indice destro) rappresenta la parte finale della porzione di lista che stiamo esplorando.
        Se lx diventa maggiore di rx, significa che abbiamo esaurito la porzione 
        di lista da controllare, quindi k non è presente e dobbiamo restituire -1.
        
        🔹 In quali altri algoritmi potremmo trovare un controllo simile?

        Ricerca binaria classica (if lx > rx: return -1)
        Ricorsione per trovare il minimo/massimo in un array (if lx == rx: return a[lx])
        Divide et Impera (es. Merge Sort), quando dividiamo un array e dobbiamo gestire i casi limite.
    
    
    
    '''
    # Calcolo del punto centrale dell'intervallo attuale
    cx = (lx + rx) // 2  # Divide l'intervallo a metà usando la divisione intera

    # Controllo se l'elemento centrale è l'ultimo valore uguale a k nell'array
    if k == a[cx] and (cx == len(a) - 1 or a[cx + 1] > k):
        # Se il valore trovato è uguale a k e:
        # - È l'ultimo elemento dell'array (cx == len(a) - 1)
        # - Oppure l'elemento successivo è più grande di k (a[cx + 1] > k)
        # Significa che abbiamo trovato l'ultima occorrenza di k, quindi restituiamo cx
        return cx  

    # Se k è più piccolo dell'elemento centrale, cerchiamo nella metà sinistra
    if k < a[cx]:
        return ricerca_bin_right(a, k, lx, cx - 1)  
    # Ricorsione sulla parte sinistra dell'array, escludendo cx

    else:
         return ricerca_bin_right(a, k, cx + 1, rx)  
    # Se k è maggiore o uguale, cerchiamo nella parte destra dell'array
   
    
    
lista = [1,3,4,4,4,4,5,7,7,7,7,10,10,12,12,15,17]
k = 4
print("Input: ", lista, k)
print("Output: ", ricerca_bin_right(lista, k, 0, len(lista)-1))
    
"""
    Sia n la lunghezza della lista.
    Complessità temporale: O(log n)
    Complessità spaziale: O(log n) -> si vanno a creare log_2 n frames, uno per
    ogni chiamata ricorsiva (ci sono log_2 n chiamate ricorsive), e ogni frame
    occupa memoria costante.
    """
    
# creo come prima cosa due indici uno desto e sinistro uno destro , poi creo un ciclo dove se rx è maggiore si lx , ritorna -1

# poi creo un mezzo che sarebbe cx = (lx+rx)/2
#dopo di che creo un for dove  se k == a [cx] e deve essere ( cx  è nella meta di è (a)-1 o a [ cx+1] > k )
# se k == a [cx ] oppure è il centro è uguale al -1  o alla lista a [cx+1 un elemnto ]ed è maggiore di k 
# riotorna cx poi             
        


########################################################################################################################################################################################


### **Consigli per Scrivere il Codice da Solo**  



#Voglio aiutarti a **scrivere il codice da solo**, partendo dal **primo `if`**, senza copiarti la soluzione.
#Ti guiderò passo passo su **come ragionare** e **perché usare `if` in questo caso**.


'''
### **1 Capire il Problema**
'''
# ✔ Devi implementare **la ricerca binaria destra** (**rightmost binary search**) usando **la ricorsione**.
# ✔ Devi trovare **l’ultima posizione in cui compare `k` nella lista ordinata `a`**.
# ✔ Se `k` **non è presente**, devi restituire `-1`.
# ✔ La lista **è già ordinata**, quindi puoi sfruttare **la ricerca binaria (O(log n))** invece di una scansione lineare (O(n)).

'''
### **2 Perché Usiamo `if`?**
'''
# L'`if` serve a **gestire i casi base**, ovvero le condizioni in cui possiamo fermare la ricerca e restituire un risultato.
# Nella ricerca binaria ricorsiva, devi sempre avere **almeno un caso base** per evitare **ricorsioni infinite**.

'''
### **3 Primo `if`: Quando Smettere la Ricerca?**
'''
# Nel tuo codice, il primo `if` è questo:
# ```python
# if lx > rx:
#     return -1
# ```
# 🔹 **Perché lo usiamo?**  
# - `lx` (indice sinistro) rappresenta la parte iniziale della porzione di lista che stiamo esplorando.  
# - `rx` (indice destro) rappresenta la parte finale della porzione di lista che stiamo esplorando.  
# - Se `lx` diventa **maggiore** di `rx`, significa che **abbiamo esaurito la porzione di lista da controllare**, quindi **k non è presente** e dobbiamo restituire `-1`.
# 
# 🔹 **In quali altri algoritmi potremmo trovare un controllo simile?**  
# - **Ricerca binaria classica** (`if lx > rx: return -1`)
# - **Ricorsione per trovare il minimo/massimo** in un array (`if lx == rx: return a[lx]`)
# - **Divide et Impera** (es. Merge Sort), quando dividiamo un array e dobbiamo gestire i casi limite.


############################################################################################################################################################################################
#############################################################################################################################################################################################àà


'''
### **🔹 Passo 2: Trova l'Elemento Centrale**
'''
# Ora devi trovare l'elemento **a metà della lista**:
# ```python
# cx = int((lx + rx) / 2)  # Calcola l'indice centrale
# ```
# 💡 **Suggerimento per scriverlo senza guardare la soluzione**:  
# - La ricerca binaria divide sempre la lista a metà, quindi devi calcolare il **centro**.  
# - Usa `int((lx + rx) / 2)`, perché vogliamo un **indice intero**.

'''
### **🔹 Passo 3: Controlla Se Abbiamo Trovato `k`**
'''
# Dobbiamo verificare se **a[cx] == k** e se è **l'ultima occorrenza**:
# ```python
# if k == a[cx] and (cx == len(a) - 1 or a[cx + 1] > k):
#     return cx
# ```
# 💡 **Suggerimento per scriverlo senza guardare la soluzione**:  
# - Se **l'elemento al centro è `k`**, potrebbe essere una soluzione.  
# - Ma dobbiamo assicurarci che sia **l'ultimo `k`** presente, quindi controlliamo **se l'elemento dopo è diverso**.






'''
### **🔹 Passo 4: Decidi Dove Continuare la Ricerca**
'''
# - Se `k` è **più piccolo** di `a[cx]`, vuol dire che **tutte le sue occorrenze (se esistono) sono a sinistra** → Ricorriamo a sinistra (`rx = cx - 1`).
# - Se `k` è **più grande o uguale** a `a[cx]`, dobbiamo cercare **a destra** (`lx = cx + 1`), perché vogliamo **l'ultima occorrenza**.
# 
# ```python
# if k < a[cx]:
#     return binary_search_recursive_right(a, k, lx, cx - 1)
# else:
#     return binary_search_recursive_right(a, k, cx + 1, rx)
# ```
# 💡 **Suggerimento per scriverlo senza guardare la soluzione**:  
# - **Se `k < a[cx]`**, scendi a **sinistra** (`rx = cx - 1`).  
# - **Altrimenti**, vai a **destra** (`lx = cx + 1`), perché potresti trovare un altro `k` più avanti.

'''
### **5 Testa il Codice**
'''
# Dopo averlo scritto, prova a testarlo con:
# ✅ **Un numero presente una sola volta**  
# ✅ **Un numero che compare più volte** (per verificare che prendi l'ultimo)  
# ✅ **Un numero assente dalla lista** (per verificare che restituisce `-1`)  
# ✅ **Lista con un solo elemento**  

'''
### **🔥 Ora Prova a Scriverlo da Solo!**
'''
# Ti ho dato tutte le **dritte** e i **ragionamenti** necessari per costruire la funzione **senza copiarla**.
# Se trovi difficoltà, torna a questi punti e prova a ricostruire il codice pezzo per pezzo. 🚀💻



