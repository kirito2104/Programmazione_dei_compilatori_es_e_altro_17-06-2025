
#16 tuple

#- Collezioni di dati ordinate, indicizzate, non modificabili e permettono duplicati
#- Creare una tupla normale e con un valore, singole e mischiate
#- Vediamo len(), type() e tuple()

#- Accedere agli elementi della lista, singolo, range, negativo
#- Verificare se elemento esiste

#- Modificare e inserire elementi: non è possibile se non con escamotage
#- Inserire elementi con append(), insert(), extend()

#- Rimuovere elementi con escamotage oppure cancellare tutto con del()
#- Spacchettare una tupla (unpack) normale e con *

#- Ciclare elementi

#- Unire tuple con join()

#- Metodi count() e index()

# verificare se un elemento esiste 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# le tuple  sono :

# collezioni di dati ordinate indicizate non modificabili ma permettono duplicati ,

# la cosa che cambia dalle liste  e che non possiamo modificare una tupla , una volta che e' stata creata 

#una tupla si crea con le parentesi ()


x = ('roma', 'tivoli','guidonia','firenze', 'milano', 'napoli') 

#possiamo avere anche molteplici valori come: 
y = ('milano', True , 43,0)

print(type(y)) # e dira' che e una tupla 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# mentre cosi dira che e' una stringa siccome manca una virgola 
# quindi aggiungendo la virgola si potra mettere solo un valore 


y = ('milano') # mettendo una virgola diventera' una tupla 

print(type(y)) # dira che e' una stringa siccome c'e' un solo valore 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Usando len leggera la lunghezza  della tupla 

y = ('milano','roma','malta') # mettendo una virgola diventera' una tupla 

print(len(y)) #legge la lunghezza della tupla che sara' di tre 


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ecco un altro modo per creare una tupla 


x = tuple(("milano", "roma", "napoli"))

print(x)

''' Spiegazione del codice:
tuple():

La funzione tuple() è utilizzata per creare una tupla.
Qui, una tupla viene creata a partire da una sequenza (in questo caso, un'altra tupla ("milano", "roma", "napoli")).
Il risultato sarà la stessa tupla, poiché la sequenza di partenza è già una tupla. '''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#- Accedere agli elementi della lista, singolo, range, negativo

x = ('roma', 'tivoli','guidonia','firenze', 'milano', 'napoli') 

print(x[0]) #facendo cosi accedero solo a firenze , stampandolo a schermo 


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
x = ('roma', 'tivoli','guidonia','firenze', 'milano', 'napoli') 

print(x[0:3]) # stampera' da 0 a 3 


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#facendo cosi' stampera in modo negativo 

x = ('roma', 'tivoli','guidonia','firenze', 'milano', 'napoli') 

print(x[1:-3]) # facendo cosi' stampera da 1 a -3 

# ossia partira' dall'ultimo per poi ripartire dal primo , quando e negativo 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
x = tuple(('milano','pisa','napoli'))

if 'milano' in x :
    print('ok')
# facendo cosi' verifica che ci sia 'milano' nella tupla 
# NEL CASO IN CUI NON CI SIA NULLA DI CIO' CHE E STATO CHIESTO ALL'IF DI VERIFICARE , NON RESTIURA' NULLA

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#- In una Tupla non e' possibile modificare e inserire elementi: non è possibile se non con escamotage

x = ('milano','pisa','napoli')

y = list(x)# facendo cosi' traformero' in una lista la tupla che diventera' una lista cosi :
#['milano', 'pisa', 'napoli']
y [0] = 'venezia ' #facendo cosi' modifichera' la lista e diventera': ['venezia ', 'pisa', 'napoli']


print(y)# mostrera' la nuova lista mutata 



#--------------------------------------------------------------------------------------------------------------------------------------------------------------

# qui converto , sia x che y per poi, levare 'milano', l'unico modo per modificare una tupla e' cosi' 


# Creazione di una tupla iniziale con tre elementi
x = ('milano', 'pisa', 'napoli') 
print(x)  # Stampa la tupla originale: ('milano', 'pisa', 'napoli')

# Conversione della tupla 'x' in una lista 'y'
y = list(x)

# Rimuove l'elemento 'milano' dalla lista 'y'
y.remove('milano')

# Converte nuovamente la lista 'y' in una tupla e la assegna a 'x'
x = tuple(y) # coverte y in una tupla  e la assrgna a x

# Stampa la nuova tupla aggiornata
print(x)  # Stampa: ('pisa', 'napoli')


'''### Spiegazione passo per passo:

1. **Creazione della tupla iniziale:**
   ```python
   x = ('milano', 'pisa', 'napoli')
   ```
   - Una tupla `x` con tre elementi è creata.
   - **Proprietà delle tuple:** Le tuple sono immutabili, quindi non è possibile modificare direttamente i loro elementi (es. rimuovere o aggiungere elementi).

2. **Stampa della tupla:**
   ```python
   print(x)
   ```
   - Viene stampata la tupla originale:
     ```
     ('milano', 'pisa', 'napoli')
     ```

3. **Conversione in lista:**
   ```python
   y = list(x)
   ```
   - La tupla `x` viene convertita in una lista `y` utilizzando `list(x)`.
   - La lista risultante è modificabile, a differenza della tupla.

4. **Rimozione di un elemento:**
   ```python
   y.remove('milano')
   ```
   - L'elemento `'milano'` viene rimosso dalla lista `y`.
   - La lista `y` ora contiene:
     ```python
     ['pisa', 'napoli']
     ```

5. **Conversione in tupla:**
   ```python
   x = tuple(y)
   ```
   - La lista `y` viene riconvertita in una tupla utilizzando `tuple(y)`.
   - La nuova tupla viene assegnata alla variabile `x`.

6. **Stampa della nuova tupla:**
   ```python
   print(x)
   ```
   - La nuova tupla, dopo la rimozione di `'milano'`, è stampata:
     ```
     ('pisa', 'napoli')
     ```

'''
### Riassunto:
#- Le tuple sono immutabili, quindi non si possono modificare direttamente.
#- Per rimuovere o modificare elementi, è necessario convertirle in liste, effettuare le modifiche desiderate e riconvertirle in tuple.
#- In questo caso, l'elemento `'milano'` è stato rimosso, e la tupla aggiornata è stata ricreata.

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#- UN ELEMENTO IN UNA 'tupla()'si puo' rimuovere elementi con escamotage oppure cancellare tutto con del()
# ossia convertirla in una lista per poi eliminare cio che si vuole e poi riconvertirla
'''
x = ('pisa','napoli','roma')

del x # facendo cosi' cancellera' tutta la tupla se si vuole , eliminare qualcosa nella tupla BISOGNA 

print(x)
'''
#staampera errore perche' x e' stata completamente eliminata

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# una tupla si puo' anche spacchettare, in piu' elemnti 
#- Spacchettare una tupla (unpack) normale e con *



citta = ('pisa','napoli','roma')

(x,y,z) = citta # facendo cosi spacchettero in diverse tuple, la tupla iniziale che diventera':
#pisa
#napoli
#roma


print(x)
print(y)
print(z)

#--------------------------------------------------------------------------------------------------------------------------------------------------------


citta = ('pisa','napoli','roma','venezia')

(x,y,*z) = citta # facendo cosi spacchettero in diverse tuple, la tupla iniziale che diventera':
#pisa
#napoli
# e ['roma',''venezia'] saranno separate diversamente , diventeranno parte di una lista 
print(x)
print(y)
print(z)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Mentre per ciclare le tuple :
#- Ciclare elementi
lista_citta = ('pisa','napoli','roma','venezia')

for citta in lista_citta :
    print(citta)
#facendo cio concatenero' la nuova variabile  nel for con lista_citta, per poi ciclarla e stampaarla a schermo con citta 
#--------------------------------------------------------------------------------------------------------------------------
# Creazione di una tupla contenente i nomi di alcune città
lista_citta = ('pisa', 'napoli', 'roma', 'venezia')

# Ciclo for per iterare sugli indici della tupla
for i in range(len(lista_citta)):  # 'i' rappresenta l'indice della tupla
    #range parte daa 4 elementi quindi parte da 0 
    
    # Stampa l'elemento della tupla corrispondente all'indice 'i'
    print(lista_citta[i])

    '''Ecco il codice corretto con i commenti:

```python
# Creazione di una tupla contenente i nomi di alcune città
lista_citta = ('pisa', 'napoli', 'roma', 'venezia')

# Ciclo for per iterare sugli indici della tupla
for i in range(len(lista_citta)):  # 'i' rappresenta l'indice della tupla
    # Stampa l'elemento della tupla corrispondente all'indice 'i'
    print(lista_citta[i])
```

---

### Spiegazione passo per passo:
1. **Definizione della tupla:**
   ```python
   lista_citta = ('pisa', 'napoli', 'roma', 'venezia')
   ```
   - Una tupla contenente quattro città è creata. Le tuple sono ordinate e indicizzate.

2. **Uso di `range(len(lista_citta))`:**
   ```python
   range(len(lista_citta))
   ```
   - `len(lista_citta)` restituisce la lunghezza della tupla, ovvero `4`.
   - `range(4)` genera una sequenza di numeri da `0` a `3` (escluso `4`), che sono gli indici validi per accedere agli elementi della tupla.

3. **Ciclo `for`:**
   ```python
   for i in range(len(lista_citta)):
   ```
   - Il ciclo scorre ciascun indice della tupla, da `0` a `3`.
   - La variabile `i` rappresenta l'indice corrente.

4. **Accesso agli elementi della tupla:**
   ```python
   print(lista_citta[i])
   ```
   - Per ogni indice `i`, accede all'elemento corrispondente della tupla tramite `lista_citta[i]`.
   - L'elemento viene stampato.

---

### Output:
Il codice stamperà i nomi delle città uno per riga:
```
pisa
napoli
roma
venezia
```

---

### Nota:
In Python, un modo più "pythonic" per iterare sugli elementi di una tupla è direttamente sugli elementi stessi, senza accedere agli indici:

# Iterazione diretta sugli elementi della tupla
for citta in lista_citta:
    print(citta)
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Inizializzazione della variabile contatore 'i'
i = 0  

# Creazione di una tupla contenente i nomi di alcune città
lista_citta = ('pisa', 'napoli', 'roma', 'venezia')

# Ciclo while che itera finché 'i' è minore della lunghezza della tupla
while i < len(lista_citta):
    print(lista_citta)  # Stampa l'intera tupla ad ogni iterazione
    i += 1  # Incrementa la variabile contatore 'i' di 1
#----------------------------------------------------------------------------------------------------------------------------
#con le tuple si puo: 
#- Unire tuple con join()
# Creazione di una tupla contenente alcune città
lista_citta = ('pisa', 'napoli', 'roma', 'venezia')

# Creazione di una seconda tupla con altre città
lista_citta2 = ('genova', 'firemze')

# Concatenazione delle due tuple
y = lista_citta + lista_citta2
# Nota:
# L'operatore '+' consente di unire due tuple creando una nuova tupla.
# La tupla originale 'lista_citta' e 'lista_citta2' rimangono immutabili.

# Stampa della nuova tupla concatenata
print(y)
#---------------------------------------------------------------------------------------------------------------------------
#- Metodi count() e index()
#count conta 

# Creazione di una tupla contenente alcune città
lista_citta = ('pisa', 'napoli', 'roma', 'venezia')

# Creazione di una seconda tupla con altre città
lista_citta2 = ('genova', 'firemze')

x = lista_citta.count('pisa') # e dira' che la posizione 1 
# quindi questo codice conta a che posizione si trova quello richiesto  

print(x)
# verificare se un elemento esiste 






























