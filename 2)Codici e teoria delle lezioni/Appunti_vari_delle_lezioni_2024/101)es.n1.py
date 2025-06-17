#2. **Scrivere una funzione Python che soddisfi la seguente specifica:**

#Per scrivere una funzione Python che verifica se due stringhe sono anagrammi,
# puoi confrontare se le lettere di entrambe le stringhe, una volta ordinate, 
# sono identiche. Ecco il codice completo e spiegato:

### Codice:

def anagramma(a, b):
    """
    Parametri:
        a, b: stringhe
    Return:
        True se e solo se a e b sono anagrammi
    """
    # Rimuove spazi e converte entrambe le stringhe in lettere minuscole
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()

    # Confronta le versioni ordinate delle due stringhe
    return sorted(a) == sorted(b)

'''
### Spiegazione:

1. **Rimozione degli spazi e conversione in minuscolo:**
   - Gli anagrammi sono insensibili alla maiuscole/minuscole e agli spazi.
   - `replace(" ", "")`: Rimuove eventuali spazi.
   - `lower()`: Converte la stringa in lettere minuscole.

2. **Ordinamento delle stringhe:**
   - `sorted(a)`: Ritorna una lista con i caratteri della stringa `a` ordinati in ordine alfabetico.
   - `sorted(b)`: Fa lo stesso per la stringa `b`.

3. **Confronto delle liste ordinate:**
   - Se le liste ordinate delle due stringhe sono identiche, allora le stringhe sono anagrammi.

---

### Esempio di utilizzo:
```python
print(anagramma("roma", "amor"))  # True
print(anagramma("Roma", "Amor"))  # True (ignora maiuscole/minuscole)
print(anagramma("roma", "ramo"))  # True
print(anagramma("roma", "roma ")) # True (ignora spazi)
print(anagramma("roma", "casa"))  # False
```

---

### Complessità:
1. **Tempo:**
   - Ordinare una stringa ha complessità \(O(n \log n)\), dove \(n\) è la lunghezza della stringa.
   - Complessivamente, la complessità temporale della funzione è \(O(n \log n)\).

2. **Spazio:**
   - La funzione utilizza spazio extra per immagazzinare le stringhe ordinate.

'''
#----------------------------------------------------------------------------------------------------------------------------------------
#Il codice che hai fornito contiene un errore nel modo in cui utilizza il metodo `get()`
# per i dizionari. Ecco il codice che hai condiviso, con l'errore evidenziato:
'''
### Codice originale con errore:
```python
def anagrammi(a, b):  # Definisco la funzione  
    da, db = {}, {}
    for x in a: 
        da[x] = da.get = da.get(x, 0) + 1  # ERRORE
    for x in b: 
        db[x] = da.get = da.get(x, 0) + 1  # ERRORE

    for x in da:
        if da[x] != db[x]:
            return False
```

### L'errore:

1. **Assegnazione errata al metodo `get`:**
   - Nella riga:
     ```python
     da[x] = da.get = da.get(x, 0) + 1
     ```
     - Stai assegnando `da.get = da.get(x, 0) + 1`.
     - Questo sostituisce il metodo `get` del dizionario con un valore numerico (es. `da.get = 1`),
     rendendo il metodo inutilizzabile nelle iterazioni successive.

   - Dopo la prima iterazione, quando il codice cerca di usare `da.get(x, 0)` di nuovo, genererà un errore,
   perché `da.get` non è più un metodo, ma un numero.

2. **Problema nella seconda iterazione:**
   - Quando il secondo ciclo (per `b`) tenta di usare `da.get`, il programma solleverà un'eccezione 
   poiché il metodo `get` è stato sovrascritto.

### Soluzione:

Rimuovi l'assegnazione errata e utilizza il metodo `get` correttamente. La riga corretta è:
```python
da[x] = da.get(x, 0) + 1
```
e per `b`:
```python
db[x] = db.get(x, 0) + 1
```

### Codice corretto:
```python
def anagrammi(a, b):  # Definisco una funzione che verifica se due stringhe sono anagrammi
    da, db = {}, {}

    # Conta le occorrenze di ciascun carattere nella stringa 'a'
    for x in a:
        da[x] = da.get(x, 0) + 1  # Usa correttamente il metodo `get`

    # Conta le occorrenze di ciascun carattere nella stringa 'b'
    for x in b:
        db[x] = db.get(x, 0) + 1  # Usa correttamente il metodo `get`

    # Confronta i due dizionari
    for x in da:
        if da[x] != db.get(x, 0):  # Confronta il numero di occorrenze di ciascun carattere
            return False

    return True  # Restituisce True se tutte le occorrenze corrispondono
```

---

### Differenza tra il codice corretto e quello con errore:
1. Nel codice corretto, il metodo `get` non viene sovrascritto. È usato per accedere ai valori nei dizionari.
2. Il codice con errore sovrascrive accidentalmente il metodo `get`, 
causando malfunzionamenti nelle iterazioni successive.

---

### Esempio di errore nel codice originale:
```python
da = {}
da[x] = da.get = da.get(x, 0) + 1  # Dopo questa riga, `da.get` non è più un metodo ma un numero.
```
Se provi a eseguire `da.get('a', 0)` dopo, otterrai un errore simile a:
```
TypeError: 'int' object is not callable
```

---

### Conclusione:
L'errore è dovuto alla sovrascrittura accidentale del metodo `get`. La soluzione è utilizzare il metodo `get` 
direttamente e non assegnarlo come valore.'''
#----------------------------------------------------------------------------------------------------------------------------------------

def anagrammi(a, b):  # Definisco una funzione che verifica se due stringhe sono anagrammi
    # Creazione di due dizionari vuoti per contare le occorrenze dei caratteri
    da, db = {}, {}

    # Conta le occorrenze di ciascun carattere nella stringa 'a'
    for x in a:
        da[x] = da.get(x, 0) + 1  # Usa `get(x, 0)` per ottenere il valore corrente o 0 se il carattere non esiste
        #0 (1) in media 
    # Conta le occorrenze di ciascun carattere nella stringa 'b'
    for x in b:
        db[x] = db.get(x, 0) + 1  # Usa `get(x, 0)` per ottenere il valore corrente o 0 se il carattere non esiste
        #0 (1) in media
        
    # Confronta i due dizionari
    for x in da:  # Itera sui caratteri del primo dizionario
        if da[x] != db.get(x, 0):  # Confronta il numero di occorrenze di ciascun carattere
            return False  # Se c'è una discrepanza, le stringhe non sono anagrammi

    # Se non ci sono discrepanze, restituisce True
    return True
a = 'AABCDAABD'
b = 'BABCADADA'
print(anagramma(a,b))

'''
### Spiegazione dettagliata:

1. **Definizione della funzione:**
   ```python
   def anagrammi(a, b):
   ```
   - La funzione `anagrammi` accetta due stringhe `a` e `b` come input e restituisce `True` se sono anagrammi, altrimenti `False`.

2. **Creazione dei dizionari:**
   ```python
   da, db = {}, {}
   ```
   - `da` e `db` sono dizionari vuoti che verranno utilizzati per contare le occorrenze dei caratteri rispettivamente in `a` e `b`.

3. **Conteggio delle occorrenze in `a`:**
   ```python
   for x in a:
       da[x] = da.get(x, 0) + 1
   ```
   - Per ogni carattere `x` nella stringa `a`, aggiorna il dizionario `da`:
     - `da.get(x, 0)` restituisce il valore corrente associato al carattere `x` o `0` se il carattere non esiste nel dizionario.
     - Incrementa il valore di `da[x]` di 1.

4. **Conteggio delle occorrenze in `b`:**
   ```python
   for x in b:
       db[x] = db.get(x, 0) + 1
   ```
   - Fa lo stesso per la stringa `b`, aggiornando il dizionario `db`.

5. **Confronto dei dizionari:**
   ```python
   for x in da:
       if da[x] != db.get(x, 0):
           return False
   ```
   - Itera su ogni carattere `x` nel dizionario `da`.
   - Confronta il numero di occorrenze del carattere `x` in `da` e in `db`:
     - `db.get(x, 0)` restituisce il valore di `x` in `db` o `0` se il carattere non esiste.
   - Se c'è una discrepanza, restituisce `False`, poiché le stringhe non sono anagrammi.

6. **Restituisce `True`:**
   ```python
   return True
   ```
   - Se tutti i caratteri corrispondono in numero, le stringhe sono anagrammi, quindi restituisce `True`.

---

### Esempio di utilizzo:
```python
print(anagrammi("roma", "amor"))  # True
print(anagrammi("roma", "amore"))  # False
print(anagrammi("roma", "mora"))  # True
print(anagrammi("roma", "ramo"))  # True
```
'''
### Output:

'''
True
False
True
True
'''


'''
### Complessità:
1. **Tempo:**
   - Conta i caratteri di entrambe le stringhe: \(O(n)\), dove \(n\) è la lunghezza della stringa più lunga.
   - Confronta i dizionari: \(O(n)\).
   - Complessivamente: \(O(n)\).

2. **Spazio:**
   - Due dizionari utilizzati per il conteggio: \(O(u)\), dove \(u\) è il numero di caratteri unici.

Se hai domande o vuoi ulteriori chiarimenti, fammi sapere! 😊
        
'''

#Ecco la continuazione del calcolo:


# Cancellare a[1] dalla lista a coda 
# Il costo per cancellare un elemento da una lista è proporzionale alla distanza dell'elemento dalla fine della lista
# (n - 1) * c dove n = len(a), c è una costante 

# Costo medio = somma di tutti i costi / n
# Somma dei costi per cancellare ciascun elemento:
# costo di a[1] + costo di a[2] + ... + costo di a[n-1]

# Per espandere:
# c * n + c * (n - 1) + c * (n - 2) + ... + c

# Fattorizziamo la costante c:
# c * (n + (n - 1) + (n - 2) + ... + 1)

# La somma dei numeri da 1 a n è una progressione aritmetica: 
# Somma = n * (n + 1) / 2

# Quindi, il costo totale è:
# c * (n * (n + 1) / 2)

# Costo medio = costo totale / n
# Costo medio = [c * (n * (n + 1) / 2)] / n
# Costo medio = c * (n + 1) / 2


### Conclusione:
#Il costo medio per cancellare un elemento in una lista Python utilizzando `del()` è:

#\[
#\text{Costo medio} = \frac{c \cdot (n + 1)}{2}
#\]

#- **`c`**: Una costante che dipende dall'implementazione della lista.
#- **`n`**: La lunghezza della lista.

#Questa formula tiene conto del fatto che cancellare un elemento all'inizio della lista è più costoso rispetto
#a cancellare un elemento alla fine, poiché richiede lo spostamento degli elementi successivi.




