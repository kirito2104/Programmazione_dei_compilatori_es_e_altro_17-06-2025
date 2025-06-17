



# Ordinare date 



#print(sorted(a))

# la funzione key che sul dominio  che gli elementi degli iterabili, qui e' una funz.
# che  prende in input gli elementi della nostra lista e gli ritorna il valore  

'''
*il parametro key di sorted e' utilizzato per attribuire il valore agli elemnti nei confronti 
* la posizione di e1 e e2 viene stabilito in base a key(e1) < key(e2)
*
*
'''
a = ['09-12-2024','10-12-2022','08-10-2023']

# sara' una funzione che prende un elemento 

def f(e):
    '''
    retutn #una tupla della forma (yyyy,mm,gg)
    

    Parameters
    ----------
    e :una stringa della forma 'dd-mm-yyyy'

    Returns
    -------
    una tupla della forma ('yyyy', 'mm', 'gg')

    '''
    
    return (e[6:], e[3:5], e[:2])
    # oppure return e.split('-')[::-1]

print(sorted(a, key=f))

#=============================================================================================================================================================================================================================================================
# In[stesso problema risolto senza utilizzo parametro key]

# Lista `a` contiene una serie di date in formato stringa (gg-mm-aaaa).
a = ['09-12-2024', '10-12-2022', '08-10-2023']
# Lista `b`, inizialmente vuota, verrà utilizzata per memorizzare le date modificate e ordinate.
b = []

# Itero su ogni elemento della lista `a` utilizzando un ciclo `for`.
for e in a:
    # Uso il metodo `split('-')` per dividere ogni data in tre parti (giorno, mese e anno),
    # basandomi sul separatore `-`. Ad esempio, '09-12-2024' diventa ['09', '12', '2024'].
    # Con `[::-1]`, inverto l'ordine della lista risultante (da [gg, mm, aaaa] a [aaaa, mm, gg]).
    b.append(e.split('-')[::-1])  
    # Dopo aver aggiunto la data invertita alla lista `b`, ordino la lista `b` in base ai valori invertiti.
    # `b.sort()` riordina la lista in modo crescente. Dato che le date sono in formato [aaaa, mm, gg],
    # il confronto tra le date funziona correttamente per ottenere l'ordine cronologico.
    b.sort()

# Stampo il contenuto della lista `b`. Ora contiene le date invertite e ordinate in ordine cronologico.
print(b)

'''
Il metodo `split()` in Python è utilizzato per dividere una stringa in una lista di sottostringhe,
basandosi su un delimitatore specificato (se non specificato, lo spazio è il delimitatore predefinito).

**Sintassi:**
    string.split(separator, maxsplit)

**Parametri:**
1. `separator` (opzionale): Il delimitatore che verrà utilizzato per dividere la stringa. Se non specificato,
   il metodo utilizzerà uno o più spazi come delimitatore.
   - Se il separatore è una stringa vuota (`''`), si genera un errore.
2. `maxsplit` (opzionale): Il numero massimo di divisioni da eseguire. Dopo aver raggiunto questo numero,
   il resto della stringa sarà lasciato intatto come ultima parte della lista. Il valore predefinito è -1,
   che indica che non ci sono limiti al numero di divisioni.

**Valore di ritorno:**
Il metodo restituisce una lista contenente le sottostringhe risultanti dalla divisione della stringa originale.

**Comportamento con delimitatori:**
- Se il delimitatore non è presente nella stringa, la stringa originale verrà restituita come un unico elemento nella lista.
- Se la stringa è vuota, restituisce una lista vuota.

**Esempi di utilizzo:**

1. Divisione basata su spazi (default):
    ```python
    testo = "Python è un linguaggio potente"
    risultato = testo.split()
    print(risultato)
    # Output: ['Python', 'è', 'un', 'linguaggio', 'potente']
    ```

2. Divisione con un delimitatore specifico:
    ```python
    testo = "uno,due,tre,quattro"
    risultato = testo.split(',')
    print(risultato)
    # Output: ['uno', 'due', 'tre', 'quattro']
    ```

3. Divisione con limite (`maxsplit`):
    ```python
    testo = "uno due tre quattro"
    risultato = testo.split(' ', 2)  # Dividi al massimo due volte
    print(risultato)
    # Output: ['uno', 'due', 'tre quattro']
    ```

4. Comportamento con delimitatori multipli:
    ```python
    testo = "    Python    è   fantastico   "
    risultato = testo.split()
    print(risultato)
    # Output: ['Python', 'è', 'fantastico']
    # Nota: Spazi multipli consecutivi vengono trattati come un unico delimitatore.
    ```

5. Uso senza separatore:
    ```python
    testo = ""
    risultato = testo.split()
    print(risultato)
    # Output: []
    # Una stringa vuota restituisce una lista vuota.
    ```

**Nota importante:**
- Il metodo `split()` non modifica la stringa originale ma restituisce una nuova lista.
- Per operazioni più avanzate, come dividere stringhe con caratteri multipli come delimitatori,
  è consigliabile usare il modulo `re` (espressioni regolari).

**Esempio con modulo `re` per più delimitatori:**
    ```python
    import re
    testo = "uno,due;tre.quattro"
    risultato = re.split(r'[;,.]', testo)  # Dividi su ';', ',' o '.'
    print(risultato)
    # Output: ['uno', 'due', 'tre', 'quattro']
    ```

**In sintesi:**
Il metodo `split()` è uno strumento molto versatile per lavorare con stringhe e dividerle in parti più gestibili.
Può essere utilizzato per tokenizzare testo, analizzare dati o separare valori basati su delimitatori specifici.
'''

#========================================================================================================================================================================================================================


# Lista `a` contiene date in formato stringa nel formato 'gg-mm-aaaa'.
a = ['09-12-2024', '10-12-2022', '18-10-2023']

# Utilizzo di una list comprehension per creare la lista `b`.
# Per ogni elemento `e` nella lista `a`, si divide la stringa utilizzando `split('-')` basandosi sul carattere '-'.
# Questo produce una lista di sottostringhe (['gg', 'mm', 'aaaa']).
# Successivamente, l'operazione `[::-1]` inverte l'ordine degli elementi nella lista, trasformandola in [aaaa, mm, gg].
b = [e.split('-')[::-1] for e in a]

# La list comprehension sopra è equivalente al codice tradizionale seguente:
# b = []
# for e in a:
#     b.append(e.split('-')[::-1])
# - Si utilizza il metodo `split('-')` per dividere ogni data in componenti.
# - L'operazione `[::-1]` inverte l'ordine dei componenti (anno-mese-giorno).
# - Ogni risultato viene aggiunto alla lista `b`.

# Ora, la lista `b` contiene date invertite in formato lista, ad esempio:
# [['2024', '12', '09'], ['2022', '12', '10'], ['2023', '10', '18']]

# Ordina la lista `b` in ordine crescente basandosi sui componenti [aaaa, mm, gg].
# Poiché l'anno è al primo posto in ogni lista, l'ordinamento avviene correttamente in base all'anno, poi al mese, e infine al giorno.
b.sort()

# Stampa la lista `b` dopo l'ordinamento. Ora le date sono ordinate cronologicamente ma ancora in formato lista.
print(b)

# Itero attraverso ogni elemento della lista `b`.
# Per ogni elemento, che è attualmente una lista [aaaa, mm, gg], uso il metodo `join('-')` per ricostruire
# la stringa originale nel formato 'aaaa-mm-gg'.
for i in range(len(b)):
    b[i] = '-'.join(b[i])

# Ora `b` è una lista di date in formato stringa ('aaaa-mm-gg'), ordinate cronologicamente.
print(b)


#===================================================================================================================================================================================================================
# Nuovo esempio
# Lista `a` con date in formato 'gg-mm-aaaa'.
a = ['09-12-2024', '10-12-2022', '18-10-2023']

# Lista vuota `b` che verrà popolata successivamente (questo blocco di codice non viene effettivamente eseguito qui).
b = []

# Lista `a` viene svuotata.
c = []

# Itero attraverso ogni elemento della lista `b` (che è vuota al momento di esecuzione).
# Per ogni elemento in `b`, utilizzo `'-'.join(e)` per ricostruire la stringa nel formato originale ('gg-mm-aaaa').
# Ogni stringa ricostruita viene aggiunta alla lista `a`.
for e in b:
    c.append('-'.join(e))

# Poiché `b` è vuota, la lista `a` rimane vuota e viene stampata come lista vuota ([]).
print(a)












