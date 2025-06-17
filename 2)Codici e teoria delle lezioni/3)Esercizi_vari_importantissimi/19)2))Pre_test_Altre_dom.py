'''
# Domanda 1
'''
# Testo estratto:
# Si consideri il seguente frammento di codice: quale delle affermazioni è vera?

# Codice in C:
# int a[3] = {1, 0, -1};
# int *p;
# char *c;

# p = a;
# c = a;

# c++;
# p++;

# Opzioni:
# 1. *c < *p
# 2. *p == *c
# 3. c < p
# 4. a[p] == 0

'''
# Consigli per rispondere:
'''
# - Analizza come vengono inizializzati `p` e `c`. Entrambi puntano all'inizio dell'array `a`,
#   ma `p` è un `int*` e `c` è un `char*`.
# - Il puntatore `p` avanza di 4 byte (dimensione di un `int`), mentre `c` avanza di 1 byte (dimensione di un `char`).
# - Dopo l'incremento, `*p` legge il secondo elemento dell'array (`0`), mentre `*c` legge un byte della rappresentazione
#   binaria di `1` in memoria. Questo può portare a confronti non intuitivi.
###################################################################################################################################################################################################

''' 
Analisi del codice fornito
'''

# Dichiarazione delle variabili e inizializzazione dell'array

# Definizione di un array di tre elementi
#int a[3] = {1, 0, -1};

# Dichiarazione di due puntatori
#int *p;   # Puntatore a intero
#char *c;  # Puntatore a carattere

# Assegnazione degli indirizzi
#p = a;  # Il puntatore p punta all'inizio dell'array a
#c = a;  # Il puntatore c viene assegnato all'array a (conversione implicita da int* a char*)

# Incremento dei puntatori
#c++;  # Spostamento del puntatore c di 1 byte in avanti
#p++;  # Spostamento del puntatore p alla prossima posizione dell'array, avanzando di sizeof(int)

'''
Analisi del comportamento delle variabili p e c
'''

# 1. p = a;
#    - Il puntatore p viene inizializzato all'indirizzo di a[0].
#    - p ora punta a &a[0].

# 2. c = a;
#    - Il puntatore c è dichiarato come char*, ma gli viene assegnato un int*.
#    - Il compilatore accetta questa conversione con un warning.
#    - Ora c punta all'inizio dell'array a, ma viene interpretato come un puntatore a char.

# 3. c++;
#    - Poiché c è un char*, l'incremento di c avanza di 1 byte.
#    - Su molte architetture, un int occupa 4 byte, quindi c ora punta al secondo byte di a[0].

# 4. p++;
#    - Poiché p è un int*, l'incremento di p avanza di sizeof(int), tipicamente 4 byte.
#    - Ora p punta a a[1], che contiene il valore 0.

'''
Analisi delle risposte
'''

# 1. *c < *p
#    - *c è il valore del byte successivo al primo byte di a[0].
#    - *p è il valore di a[1], che è 0.
#    - Non possiamo garantire che *c sia inferiore a *p, perché dipende dalla rappresentazione in memoria.
#    - Questa affermazione non è necessariamente vera.

# 2. *p == *c
#    - *p è il valore di a[1], quindi 0.
#    - *c è il valore del secondo byte di a[0], che potrebbe non essere 0.
#    - Non è garantito che *p sia uguale a *c.
#    - Questa affermazione è errata.

# 3. c < p ✅
#    - Inizialmente, c e p puntavano allo stesso indirizzo.
#    - Dopo l'operazione c++, il puntatore c si è spostato di 1 byte in avanti.
#    - Dopo l'operazione p++, il puntatore p si è spostato di 4 byte in avanti.
#    - Poiché c è avanzato meno di p, il suo valore è ancora inferiore rispetto a p.
#    - Questa affermazione è vera.

# 4. a[p] == 0
#    - p punta a a[1], quindi a[p] significa a[a[1]].
#    - a[1] è 0, quindi a[p] sarebbe a[0].
#    - a[0] è 1, quindi questa affermazione è falsa.

'''
Conclusione
'''

# La risposta corretta è "c < p" perché, dopo gli incrementi,
# l'indirizzo contenuto in c è inferiore a quello contenuto in p.

##################################################################################################################################################################################################################

'''
# Domanda 2
'''
# Testo estratto:
# Qual è la lunghezza di `a` al termine del seguente frammento di codice?

# Codice in C:
# char a[] = "programmazione";
# char b[] = "algoritmo";
# int i;

# for (i = 0; b[i] != '\0'; i++)
#     a[i] = b[i];

# Opzioni:
# 1. 10
# 2. 9
# 3. 14
# 4. 15

'''
# Consigli per rispondere:
'''
# - La stringa originale `a` ha lunghezza 14 (`"programmazione"` più `\0`).
# - Il `for` sovrascrive i primi 9 caratteri con quelli di `b`, 
#   lasciando il resto invariato.
# - La terminazione `\0` potrebbe essere copiata solo se `b` è più corta di `a`.
######################################################################################################################ààà
'''
### **Spiegazione passo dopo passo**
'''

# 1. L'array `a` viene inizializzato con la stringa "programmazione",
# che in memoria occupa **14 caratteri** (incluso il terminatore `\0`).

# 2. L'array `b` viene inizializzato con la stringa "algoritmo",
# che in memoria occupa **10 caratteri** (incluso il terminatore `\0`).

# 3. Il ciclo `for` itera fino a che il carattere corrente di `b`
# non è il terminatore `\0`:

#    - `b` ha **9 caratteri validi** più `\0`, quindi il ciclo copierà **9 caratteri** 
#       da `b` a `a`.

# 4. Dopo la copia, il contenuto di `a` diventa `"algoritmozione\0"`,
#       ma la sua lunghezza rimane **14 caratteri**.

'''
### **Errore nella tua risposta**
'''

# - Hai scelto **9**, probabilmente pensando che `a` venga troncato alla lunghezza di `b`.
# - Tuttavia, la lunghezza di `a` **non cambia** perché l'array è
#   già stato dichiarato con 14 caratteri.
# - Il contenuto di `a` cambia, ma la sua dimensione in memoria rimane invariata.

'''
### **Differenza tra la tua scelta e la risposta corretta**
'''

# | Risposta | Significato | Corretta? |
# |----------|------------|-----------|
# | **9** (tua scelta) | Pensavi che `a` diventasse lungo quanto `b` | ❌ Sbagliato |
# | **14** (risposta giusta)
# | `a` mantiene la lunghezza originale di 14, cambiando solo alcuni caratteri 
#                                                                    | ✅ Corretto |

'''
### **Conclusione**
'''

# La dimensione di un array dichiarato **non cambia** con l'assegnazione di nuovi valori.
# Il ciclo copia solo alcuni caratteri, ma la lunghezza dell'array rimane invariata.






################################################################################################################



'''
# Domanda 3
'''
# Testo estratto:
# Quanto vale `c` al termine del seguente frammento di codice?

# Definizione della lista e del dizionario vuoto
# La lista `a` contiene numeri interi, alcuni dei quali ripetuti.
a = [3, 2, 5, 4, 5, 6, 7, 6, 7, 5]
d = {}  # Dizionario che terrà traccia dei numeri già visti

# Inizializzazione della variabile contatore `c`
c = 0

# Iterazione sugli elementi della lista
for x in a:
    if x in d:  # Se `x` è già presente nel dizionario, è un duplicato
        c += 1  # Incrementiamo il contatore `c`
    else:
        d[x] = None  # Aggiungiamo `x` al dizionario

# Opzioni:
# 1. 3
# 2. 4
# 3. 1
# 4. 10
# 5. 7

'''
# Consigli per rispondere:
'''
# - Il dizionario `d` memorizza i numeri già visti.
# - `c` viene incrementato quando un valore è già presente in `d`.
# - Conta le occorrenze ripetute di ogni numero in `a` per determinare il valore finale di `c`.
################################################################################################################

''' 
### **Analizziamo il codice Python fornito per determinare il valore finale di `c`**
'''

'''
### **Analisi del codice e comportamento passo-passo**
- `a` è una lista contenente valori interi con alcuni duplicati: `[3, 2, 5, 4, 5, 6, 7, 6, 7, 5]`.
- `d` è un dizionario vuoto che verrà usato per memorizzare i numeri già visti.
- `c` è inizializzato a 0 e viene incrementato ogni volta che troviamo un valore già presente nel dizionario.
'''

'''
### **Iterazioni del ciclo**
| Iterazione | `x`  | `d` dopo iterazione  | `c`  |
|------------|------|----------------------|------|
| 1          | 3    | `{3: None}`          | 0    |
| 2          | 2    | `{3: None, 2: None}` | 0    |
| 3          | 5    | `{3: None, 2: None, 5: None}` | 0    |
| 4          | 4    | `{3: None, 2: None, 5: None, 4: None}` | 0    |
| 5          | 5    | `{3: None, 2: None, 5: None, 4: None}` | 1 (5 è già in `d`) |
| 6          | 6    | `{3: None, 2: None, 5: None, 4: None, 6: None}` | 1 |
| 7          | 7    | `{3: None, 2: None, 5: None, 4: None, 6: None, 7: None}` | 1 |
| 8          | 6    | `{3: None, 2: None, 5: None, 4: None, 6: None, 7: None}` | 2 (6 è già in `d`) |
| 9          | 7    | `{3: None, 2: None, 5: None, 4: None, 6: None, 7: None}` | 3 (7 è già in `d`) |
| 10         | 5    | `{3: None, 2: None, 5: None, 4: None, 6: None, 7: None}` | 4 (5 è già in `d`) |
'''

# Il valore finale di `c` è 4

'''
### **Analisi delle possibili risposte**
1. **Risposta 1 (`c = 3`)** ❌  
   - Questo valore è errato perché ci sono **4** duplicati nell'array (`5, 6, 7, 5`), non 3.
  
2. **Risposta 2 (`c = 4`)** ✅  
   - Questo valore è corretto: ci sono **4 duplicati** che fanno incrementare `c`.

3. **Risposta 3 (`c = 1`)** ❌  
   - Questo valore è errato perché `c` viene incrementato 4 volte, non 1.

4. **Risposta 4 (`c = 10`)** ❌  
   - Questo valore è errato perché `c` non viene incrementato per ogni elemento, ma solo per quelli già visti.

5. **Risposta 5 (`c = 7`)** ❌  
   - Questo valore è errato perché `c` è incrementato solo per i numeri duplicati, non per tutti i numeri visti.
'''

'''
### **Conclusione**
**La risposta corretta è la numero 2 (`c = 4`)** perché il codice conta quanti numeri sono già apparsi precedentemente nell'array. 
In questo caso, i numeri `5`, `6`, `7` e `5` sono ripetuti, portando `c` a `4`.
'''



################################################################################################################
#Domanda 4:
'''Sia a una lista Python di n interi e b una lista concatenata implementata 
in C avente gli stessi elementi di a.
Siano A(p) e B(p) i costi dell'operazione di inserimento, rispettivamente 
in a e b, di un nuovo elemento in posizione p.
Quale delle seguenti affermazioni è vera?
'''
...
#Opzioni:
'''
B(p) <= A(p)
B(p) è in O(p) ✅ (risposta corretta)
A(p) <= B(p)
A(p) è in O(p) ❌ (risposta errata selezionata da te)
Perché hai sbagliato?
Hai scelto la risposta 4. A(p) è in O(p), ma la risposta corretta è la 2. B(p) è in O(p).

'''
'''
#Analisi del problema:

a è una lista Python, quindi è implementata internamente come un array dinamico.
Inserire un elemento in posizione p richiede lo spostamento di tutti
gli elementi successivi, il che ha costo O(n) nel caso peggiore.
b è una lista concatenata in C:
Per inserire un elemento in posizione p, bisogna percorrere p nodi 
per raggiungere la posizione corretta, il che ha costo O(p).
Errore nella tua scelta:

Hai scelto A(p) è in O(p), ma questo è sbagliato perché l'inserimento
in una lista Python non ha complessità O(p), bensì O(n) nel caso medio e peggiore.
La risposta corretta è B(p) è in O(p), perché per una lista concatenata 
bisogna attraversare p nodi prima di poter effettuare l'inserimento.
Risultato corretto:
✔️ La lista concatenata ha costo O(p) per l'inserimento in posizione p, 
quindi la risposta giusta era la numero 2.


# '''
# Consigli per rispondere:
# '''
# - L'inserimento in una lista Python (`list`) richiede uno spostamento degli elementi, 
# quindi può essere O(n).
# - In una lista concatenata, il costo dell'inserimento dipende dalla posizione 
# `p`, ma in media è più efficiente.
##############################################################################################################################

# Ecco il testo della domanda estratto dall'immagine:
#
# ---
#
# Domanda:
# Sia `n` un intero positivo maggiore di 1876. Si consideri il valore di `c` al termine del seguente frammento di codice in **C**:
#
# ```c
# int c = n;
# for (int i = 0; i < n; i++) {
#     c -= 1;
#     i += 1;
# }
# ```
#
# Opzioni:
# 1. `c == (n/2 - 1)`  
# 2. `c == (n/2 + 1)`  
# 3. `c == n`  
# 4. `c == n/2` ❌ *(risposta errata selezionata da te)*  
# 5. `c == 0`  
#
# Risposta corretta: ✅ `c == n/2`
#
# ---
#
# Perché hai sbagliato?
# Hai selezionato la risposta 4 (`c == n/2`), ma la risposta corretta è la 3 (`c == n/2`).  
# In realtà, questa tua risposta è corretta, quindi sembra che tu abbia indicato proprio la risposta giusta e il sistema l'abbia valutata correttamente.
#
# Tuttavia, per capire bene il funzionamento del codice, analizziamolo:
#
# ---
#
# Analisi del codice passo per passo
#
# 1. **Inizializzazione:**  
#    - `c` parte con il valore `n`.  
#    - `i` viene inizializzato a `0`.  
#
# 2. **Esecuzione del ciclo:**  
#    - La condizione `i < n` è verificata, quindi si entra nel corpo del ciclo.  
#    - `c -= 1` decrementa `c` di 1.  
#    - `i += 1` incrementa `i` di 1 (oltre all'incremento di `i++` nella condizione del `for`).  
#
# 3. **Come si comporta `i`?**  
#    - Ogni iterazione del ciclo **incrementa `i` di 2** (una volta nel `for` e una volta con `i += 1`).  
#    - Questo significa che `i` non va da `0` a `n` con passi di `1`, ma con passi di **2** (`0, 2, 4, ..., n-2` o `n-1`).  
#    - Di conseguenza, il ciclo **si esegue circa `n/2` volte**.  
#
# 4. **Come si comporta `c`?**  
#    - `c` parte da `n` e viene decrementato di `1` a ogni iterazione.  
#    - Poiché il ciclo si esegue **circa `n/2` volte**, `c` alla fine sarà **n - n/2 = n/2**.  
#
# ---
#
# Conclusione: perché la risposta 3 (`c == n/2`) è corretta?
# - Il ciclo si esegue **circa `n/2` volte**.  
# - Ogni iterazione decrementa `c` di `1`, quindi il valore finale di `c` è **n/2**.  
# - Questo corrisponde alla risposta **`c == n/2`**.
#
# ---
#




'''
# Consigli per rispondere:
 '''
# - Il ciclo `for` incrementa `i` due volte per iterazione (`i++` e `i += 1`), quindi si esegue circa `n/2` volte.
# - `c` viene decrementato una volta per ogni iterazione.
# - Il valore finale di `c` dipende dal numero di iterazioni totali del ciclo.





###################################################################################################################################################àà
'''
 Domanda 6
# '''
# Testo estratto:
# Qual è il costo temporale del bubble sort su una lista `b` ottenuta aggiungendo un elemento `e` all'inizio di una lista `a` già ordinata?

# Opzioni:
# 1. O(1)
# 2. O((n+1)^2)
# 3. O(n)
# 4. O(n^2)
# 5. O(n log n)

'''
# Consigli per rispondere:
'''
# - Il bubble sort ha una complessità di O(n^2) nel caso generale.
# - Se il nuovo elemento `e` è minore di tutti gli elementi, deve essere spostato fino in fondo.
# - Questo può portare a una complessità temporale di O(n^2), sebbene in alcuni casi particolari possa essere più efficiente.

# Se hai bisogno di altre domande spiegate o ulteriori dettagli, fammelo sapere!

'''
Domanda 7
'''
# Testo estratto:
# La lista `a` contiene `n` tuple costituite da due elementi ciascuna.
# Il primo è un’etichetta che può valere `0` oppure `1`. Si vuole ordinare `a` in modo
# che le tuple con etichetta `0` precedano quelle con etichetta `1`. Qual è il costo temporale
# del miglior algoritmo che risolva il problema?

# Opzioni:
# 1. O(n^2)
# 2. O(n)
# 3. O(n log n)
# 4. O(1)
# 5. O(log n)

'''
Consigli per rispondere:
'''
# - Considera il problema come un caso speciale di ordinamento.
# - Poiché ci sono solo due valori possibili (0 e 1), è possibile risolvere il problema
#   in O(n) utilizzando un algoritmo di conteggio o una scansione della lista.

'''
Domanda 8
'''
# Testo estratto:
# Si consideri una lista `a` contenente `n` interi ordinati dal più piccolo al più grande.
# Si definisca `b` come:

# ```python
# b = [e] + a
# ```

# Qual è il costo temporale del bubble sort sulla lista `b`?

# Opzioni:
# 1. O(1)
# 2. O((n+1)^2)
# 3. O(n)
# 4. O(n^2)
# 5. O(n log n)

'''
Consigli per rispondere:
'''
# - Il bubble sort ha una complessità tipica di O(n^2).
# - Se il nuovo elemento `e` è più piccolo del primo elemento originale, potrebbe dover essere spostato attraverso tutta la lista.
# - Questo impatta negativamente sulle prestazioni, portando a una complessità di O(n^2).

'''
Domanda 9
'''
# Testo estratto:
# Qual è il costo temporale del miglior algoritmo per ordinare un array di `n` interi?

# Opzioni:
# 1. O(n^2)
# 2. O(n log n)
# 3. O(n)
# 4. O(1)
# 5. O(log n)

'''
Consigli per rispondere:
'''
# - Gli algoritmi di ordinamento più efficienti hanno complessità O(n log n), come quicksort e mergesort.
# - Esistono algoritmi O(n) solo in casi particolari, ad esempio per ordinamenti basati su conteggio (counting sort) quando i valori hanno un intervallo limitato.

'''
Domanda 10
'''
# Testo estratto:
# Sia `n` un intero positivo maggiore di 1876. Qual è il valore di `c` al termine del seguente frammento di codice?

# Codice in Python:
# ```python
# c = n
# for i in range(n):
#     c -= 1
#     i += 1
# ```

# Opzioni:
# 1. n // 2
# 2. n // 2 - 1
# 3. n // 2 + 1
# 4. n
# 5. 0

'''
Consigli per rispondere:
'''
# - Osserva l'incremento di `i`: il loop esegue `i += 1` all'interno, quindi `i` aumenta di 2 per iterazione.
# - Il ciclo non viene eseguito `n` volte, ma circa `n/2` volte.
# - `c` viene decrementato di 1 ad ogni iterazione, quindi il valore finale sarà circa `n/2`.

# Se hai bisogno di ulteriori chiarimenti, fammelo sapere!


