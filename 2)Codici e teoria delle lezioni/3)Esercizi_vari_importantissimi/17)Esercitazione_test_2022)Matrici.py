
### *2) Python*

'''
Si scriva una funzione, denominata is_matrix, che riceva in input 
una lista di numeri e restituisca True se e solo se la lista può codificare
una matrice quadrata.
'''


### *Consigli per l'implementazione*



'''
. *Capire quando una lista può rappresentare una matrice quadrata*
q   - Una matrice quadrata ha dimensioni n x n, quindi la lunghezza della lista
   deve essere un quadrato perfetto (len(lista) == n^2 per qualche n intero).

2. *Implementazione del controllo*
   - Trovare la radice quadrata della lunghezza della lista (sqrt(len(lista))).
   - Verificare che sia un numero intero (int(sqrt(len(lista))) ** 2 == len(lista)).

3. *Restituire il valore corretto*
   - Se la condizione è soddisfatta, restituire True, altrimenti False.
   
   # *Esempio di codice*
   
    is_matrix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
   
   
'''
'''
def is_matrix(lst):
    
    n = int(len(lst) ** 0.5) # 0.5 sarebbe la radice quadrata
    
    for l in lst :
        if len(l) == n**2 # 
'''


''' 
✅ Versione con `len()` 
'''

def is_matrix(lst):
    '''
    Controlla se una lista di numeri può rappresentare una matrice quadrata.
    
    Il concetto di matrice quadrata implica che il numero di elementi nella lista deve essere un quadrato perfetto
    (es. 4 elementi → 2x2, 9 elementi → 3x3). Questa funzione verifica se una lista soddisfa questa condizione.
    
    :param lst: Lista di numeri
    :return: True se la lista è una matrice quadrata, False altrimenti
    '''
    # Verifica che `lst` sia effettivamente una lista, altrimenti restituisce False
    if not isinstance(lst, list):  
        return False

    # Ottiene la lunghezza della lista
    length = len(lst)  
    
    # Calcola la radice quadrata approssimata intera di `length`
    n = int(length ** 0.5)  

    # Controlla se il quadrato di `n` è uguale alla lunghezza,
    # garantendo che sia un quadrato perfetto
    '''return n * n == length  '''
    #Questa espressione verifica se il quadrato di n è uguale alla lunghezza della lista. 
    #Se la condizione è soddisfatta, Python restituisce automaticamente True; altrimenti,
    #restituisce False.

    #Ecco un modo poiu efficiente è specifico:
    
    if n * n == length:
        return True
    else:
        return False
    
'''
    Tuttavia, questo è ridondante perché l'espressione booleana 
    n * n == length restituisce già direttamente True o False.
    Quindi, il codice originale è più conciso ed efficiente.
'''
#############################################################################################
''' 
📌 Concetto di Ridondanza nel codice 
'''
# Probabilmente intendevi **ridondante**.
#
# **Ridondante** significa **superfluo** o **inutile**, nel senso che qualcosa viene ripetuto senza necessità.
#
# Nel caso del codice, scrivere esplicitamente:
#
# if n * n == length:
#     return True
# else:
#     return False
#
# è **ridondante** perché l'espressione `n * n == length` già restituisce un valore booleano (`True` o `False`).
#
# Quindi, la versione più concisa e diretta:
#
# return n * n == length
##############################################################################################
 


''' 
🔍 Esempi di utilizzo 
'''
# Verifica di matrici quadrate e non
print(is_matrix([1, 2, 3, 4]))  # True (2x2)
print(is_matrix([1, 2, 3, 4, 5]))  # False (non è un quadrato perfetto)
print(is_matrix([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # True (3x3)
print(is_matrix("1234"))  # False (non è una lista)

''' 
📌 Cosa cambia rispetto alla versione senza `len()`? 
'''
# 1. Usiamo `len(lst)` per determinare la lunghezza della lista direttamente, invece di iterare.
#    - `len(lst)` ha complessità O(1), mentre iterare ha complessità O(n).
#    - Questo rende la funzione più efficiente e leggibile.
#
# 2. Abbiamo eliminato `math.isqrt()` e sostituito con `int(length ** 0.5)`.
#    - Questo calcolo permette di ottenere la radice quadrata senza dover 
#       importare il modulo `math`.
#    - Il valore viene poi convertito in intero per verificare la proprietà del quadrato perfetto.

''' 
📌 Cosa fa `sqrt()` e perché lo abbiamo tolto? 
'''
# - `sqrt()` è una funzione della libreria `math` che calcola la radice quadrata di un numero.
# - Qui usiamo direttamente `length ** 0.5`, che ha lo stesso effetto senza bisogno di importare `math`.

''' 
🔵 Differenza tra `sqrt()` e `** 0.5` 
'''
# | Metodo               | Descrizione |
# |----------------------|-------------|
# | `math.sqrt(x)`       | Restituisce la radice quadrata precisa di `x` (float). |
# | `x ** 0.5`           | Stessa cosa di `sqrt(x)`, ma senza importare `math`. |
# | `math.isqrt(x)`      | Restituisce la radice quadrata **intera** (arrotondata per difetto). |
# | `int(x ** 0.5)`      | Approssima la radice quadrata intera, ma con potenziali piccoli errori di precisione. |

''' 
✔ Perché abbiamo usato `int(length ** 0.5)` invece di `math.isqrt()`? 
'''
# - Evita l'importazione di `math`, mantenendo il codice più semplice.
# - Per liste di dimensioni ragionevoli, la precisione è sufficiente.
# - `math.isqrt()` è più sicuro per numeri molto grandi, ma qui non è necessario.

''' 
🔵 Quale versione è meglio usare? 
'''
# | Versione | Vantaggi | Svantaggi |
# |----------|---------|----------|
# | `len() + ** 0.5` | ✅ Semplice, ✅ Senza importare `math` | ⚠ Minimi errori di arrotondamento per numeri grandi |
# | `len() + math.isqrt()` | ✅ Più preciso, ✅ Più sicuro su numeri grandi | ⚠ Richiede importazione di `math` |

# Per una soluzione semplice, usa `len(lst) ** 0.5`.
# Se devi lavorare con numeri molto grandi, `math.isqrt(len(lst))` è più sicuro.

''' 
📊 Complessità Computazionale 
'''
# - `len(lst)` ha una complessità O(1), poiché restituisce la lunghezza in tempo costante.
# - L'operazione `length ** 0.5` è anch'essa O(1), dato che la radice quadrata è un'operazione costante.
# - Il controllo `n * n == length` ha complessità O(1).
# - Pertanto, l'intera funzione ha complessità **O(1)**, rendendola estremamente efficiente.

''' 
🚀 Ora hai tutte le informazioni per scegliere la soluzione migliore! 
'''

##################################################################################################
''' 
📌 Come partire da zero e strutturare la funzione 
'''
# 1. Definisci il problema: vuoi verificare se una lista rappresenta una matrice quadrata.
# 2. Controlla il tipo di input: la funzione deve accettare solo liste.
# 3. Calcola la lunghezza della lista.
# 4. Determina se la lunghezza è un quadrato perfetto.
# 5. Restituisci il risul
#### **Per il codice in Python (is_matrix)**

'''
Questa sezione fornisce una guida passo passo su come costruire la funzione `is_matrix` da zero:

1. **Definire il problema**: Prima di scrivere il codice, bisogna chiarire cosa si vuole ottenere.
In questo caso, l'obiettivo è verificare se una lista può rappresentare una matrice quadrata,
il che significa che il numero di elementi deve essere un quadrato perfetto.

2. **Controllare il tipo di input**: Poiché la funzione deve operare su liste di numeri,
la prima cosa da verificare è che l'input sia effettivamente una lista.
Se non lo è, si deve restituire `False`.

3. **Calcolare la lunghezza della lista**: Il numero di elementi nella lista determina se 
essa può essere disposta in una matrice quadrata. Questa informazione si ottiene con `len(lst)`.

4. **Determinare se la lunghezza è un quadrato perfetto**: Per verificare questa condizione, 
si calcola la radice quadrata della lunghezza e si verifica se il suo quadrato restituisce 
il numero originale. Se sì, la lista rappresenta una matrice quadrata.

5. **Restituire il risultato**: Dopo aver effettuato i controlli
e le operazioni necessarie, si restituisce `True` o `False` a seconda dell'esito della verifica.

Questa struttura aiuta a sviluppare la funzione in modo logico e organizzato,
'''







####################################################################################################################################

  # Testiamo la funzione
print(is_matrix([1, 2, 3, 4]))  # True (2x2)
print(is_matrix([1, 2, 3, 4, 5]))  # False (non è un quadrato perfetto)
print(is_matrix([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # True (3x3)
print(is_matrix("1234"))  # False (non è una lista)






















