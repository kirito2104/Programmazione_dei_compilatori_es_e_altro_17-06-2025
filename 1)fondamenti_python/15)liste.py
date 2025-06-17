# 15 List
# - Collezioni di dati ordinate, indicizzate, modificabili e permettono duplicati.
# - Creare una lista con tipi uguali o mischiati.
# - Vediamo len(), type() e list().

# - Accedere agli elementi della lista: singolo, range, negativo.
# - Modificare elementi: singolo, range.
# - Inserire elementi con append(), insert(), extend().
# - Rimuovere elementi con remove(), pop(), del(), clear().
# - Ciclare elementi: for in, per indice, while e shorthand.
# - List comprehension.
# - Modificare l'ordine: ascendente, discendente, reverse.
# - Copiare una lista con copy().
# - Unire più liste insieme: +, append(), extend().


#---------------------------------------------------------------------------------------------------------------------------------------------

'''- Collezioni di dati ordinate, indicizzate, modificabili e permettono duplicati.'''
# laa lista e' una delle collezioni di dati piu' flessibili e' 


citta = ['napoli',"livorno",'Palermo'] # facendo cosi' si potranno mettere piu' stringhe in una sola riga,
#creando quindi una lista di stringhe , si puo anche fare una stringa con diversi elementi, anche un boolenan
# come qui sotto : 
c = [3,5,'ddd','k','s','sss',True]

''' quindi si potranno creare una liste con tipi uguali o mischiati.'''


#----------------------------------------------------------------------------------------------------------------------------------------------
'''    Vediamo len(), type() e list()    '''
# con type :

citta = ['napoli',"livorno",'Palermo']
c = [3,5,'ddd','k','s','sss',True]

# TYPE permette di mandare a schermo che tipo e' il contenuto della variabile 
print(type(citta))
# dira che e' una lista 

#---------------------------------------------------------------------------------------------------------------------------
''' Con LEN '''
# len controlla la lunghezza di un carattere 
x = ['napoli', 'livorno', 'Palermo'] 
c = [3, 5, 'ddd', 'k', 's', 'sss', True]

print(len(c))  # Questo stampa: 7 , controlla la lunghezzaa della lista

#len in questo caso controlla la lunghezza della lista, non all'interno di ogni stringa 
#-----------------------------------------------------------------------------------------------------------------------------

''' Ecco es con il comando LIST : " list(('milano','napoli','roma')) " '''

# IL CONMANDO LIST  SI PUO' :

Z = list(('napoli','livorno','Palermo')) # vanno usate le due parentesi tonde perche' e' dentro il costruttore list 

# facendo cosi' rimane sempre una lista, l'unica cosa che cambia e' che ci sono
# le parentesi e scritto list davanti 
 
print(type(Z)) #controlla de che tipo e' 

#--------------------------------------------------------------------------------------------------------------------------
# - Accedere agli elementi della lista: singolo, range, negativo.
#poi si puo accedere agli elementi della lista con

x = ['napoli', 'livorno', 'Palermo'] 
c = [3, 5, 'ddd', 'k', 's', 'sss', True]

#sigolo
print(x[0])  # facendo cosi' stampera' l'elemento 0 della lista x 

#modo negativo
print(x[-1]) # stampera gli elementi dell'ultima lista -1

#mntre cosi saara' con il range 
print(x[0:2]) #il range ha praticvamente un inizio ed una fine, parte dall'elemnto 0 e stampa fino al 1 (2)
#perche' parte da 0  quindi il primo sarebbe il num 0 e il primo , quindi stampera' napoli e livorno 

# si puo fare anche al contrario 
print(x[:2]) 
# o aanche in modo che preda in  num negativo quindi ripartira' dal primo 
print(x[:-2]) 

#-------------------------------------------------------------------------------------------------------------------------
'''Si puo' anche modificare una lista '''

# Creazione di una lista con tre elementi
x = ['napoli', 'livorno', 'Palermo']

# Modifica del primo elemento della lista (indice 0)
x[0] = 'Brescia'  # Sostituisce 'napoli' con 'Brescia'

# Stampa della lista aggiornata
print(x)  # Mostra: ['Brescia', 'livorno', 'Palermo']

#-------------------------------------------------------------------------------------------------------------------------
'''Con il range invece'''

# Creazione di una lista con tre elementi
x = ['napoli', 'livorno', 'Palermo', 'Roma', 'Milano']

# Modifica di un range di elementi (dal primo al secondo elemento, escluso il terzo)
x[0:2] = ['Brescia', 'Firenze']  # Sostituisce 'napoli' e 'livorno' con 'Brescia' e 'Firenze'

# Stampa della lista aggiornata
print(x)  # Mostra: ['Brescia', 'Firenze', 'Palermo', 'Roma', 'Milano']

'''si puo fare anche al contrario o in negativo  '''
# x[:-2] = ['Brescia', 'Firenze'] # nel caso in cui si metta solo un valore ne restuira solo uno 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - Inserire elementi con append(), insert(), extend().

# LA FUNZIONE " APPEND " VIENE USATA PER ACCODARE DEGLI ELEMENTI SU UNA LISTA 
# QUINDI " x.ppend " aggiungera breschia alla lista x in fondo 
# parte da sintra e appende all'ultimo l'elemento detto  

xr = ['roma', 'napoli','fiugi','genova','rimini']
 
xr.append("brescia")  
 
print(xr)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# - Inserire elementi con append(), insert(), extend().

# LA FUNZIONE " INSERT " VIENE USATA PER AGGIUNGERE UN ELEMENTO NELLA LISTA, PERO' BISOGNA DIRE IN CHE POSIZIONE DELLA LISTA DEVE ANDARE
# usando il metodo inset aggiungera ad una lista un elemento cosi'  " xr.insert(1,"brescia") "
#ed aggiungera nella posizione 1 brescia sensa eliminare napoli 

xr = ['roma', 'napoli','fiugi','genova','rimini']
 
xr.insert(1,"brescia")  #qui scelgo la posizione di dove deve essere inserito brescia
 
print(xr)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# LA FUNZIONE " exetend() " VIENE USATA  PER AGGIUNGERE UNA LISTA AD UN'ALTRA LISTA 

# " xr.extend(y) " PERMETTERA DI AGGIUNGERE LA LISTA Y ALLA LISTA XR 

#['roma', 'napoli', 'fiugi', 'genova', 'rimini', 'bologna', 'udine'] E LA LISTA DIVENTARA' COSI' 


xr = ['roma', 'napoli','fiugi','genova','rimini']

y = ['bologna','udine']

xr.extend(y) 

print(xr)
print(y)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - Rimuovere elementi con remove(), pop(), del(), clear()

# CON IL METODO " remove() " permette di rimuovere singolarmente un un determinato elemento della lista 
# In quest'esempio con tale funa " xr.remove('roma') " 
# e la lista diventera' ['napoli', 'fiugi', 'genova', 'rimini', 'bologna', 'udine']


xr = ['roma', 'napoli','fiugi','genova','rimini']

xr.remove('roma') 

print(xr)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CON IL METODO " pop " servira' per rimuovere  un determinato elemento da noi rischiesto in questo caso eliminero' roma 
# quindi qui eliminera roma ossia l'elemnto 0 , si possono rimuove anche piu'elementi  
# se a pop non viene scritto nulla eliminera' l'ultimo elemento in fondo ossia cosi' xr.pop()
# mentre cosi' si dira cosa si vuol rimuovere


xr = ['roma', 'napoli','fiugi','genova','rimini']

xr.pop(1) # rimuovera' l'elemento 1 

print(xr)

# pop in poche parole e' l'append della rimozione 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Mentre il metodo ' del ' che rimuove un singolo elemento cosi' :
# ' del xr[0] '  ed eliminera' roma dalla lista 
# si puo usare del anche da solo cosi' " del x " ed eliminera tutta la lista x

xr = ['roma', 'napoli','fiugi','genova','rimini']

del xr[0]

print(xr)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# LA FUNZIONE " clear " invece pulira' la rista rimuovendo tutto cio che c'e' al suo interno cosi' [] rimandendo solo con le quadre vuote 

# " x.clear() " cio' rimuovera' tutto dalla lista xr, pulira tutta la lista  

xr = ['roma', 'napoli','fiugi','genova','rimini']

xr.clear() # pulira' tutto cio che c'e' dentro xr 

print(xr)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - Ciclare elementi: for in, per indice, while e shorthand.

# In questo ciclo for  creo una variabile citta e la concateno ad f , poi la stampo a schermo  

 
f = ['milano','genoca','firenze', 'napoli','pisa']

for citta in f: # finche' ci sono citta in f , le stampa a schermo 
    print(citta)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Spiegazione del funzionamento:
Lista h:

Contiene 5 elementi: 'milano', 'genova', 'firenze', 'napoli', 'pisa'.
range(len(h)):

La funzione len(h) restituisce la lunghezza della lista h, che in questo caso è 5.
range(len(h)) genera una sequenza di numeri da 0 a 4 (escluso 5), cioè gli indici della lista.
Ciclo for:

Il ciclo for i in range(len(h)): itera sui valori generati da range(len(h)), ovvero sugli indici della lista h.
Accesso agli elementi della lista:

Ad ogni iterazione, la variabile i rappresenta l'indice corrente.
h[i] accede all'elemento della lista corrispondente all'indice i.
print(h[i]) stampa l'elemento corrente della lista


'''

h = ['tropea', 'genova', 'firenze', 'napoli', 'pisa']  # Lista di stringhe (nomi di città)

for i in range(len(h)):  # i srabbe l'indice, qui itera gli indici della lista h
    print(h[i])  # Stampa l'elemento della lista corrispondente all'indice i

# quindi praticamente crea un renge di tot numeri della lista, len misura la grandezza della lista in questo caso , il range parte da 0 


'''Quando il codice viene eseguito, ecco cosa succede passo per passo:

Iterazione 1: i = 0, h[0] = 'milano', stampa: milano.
Iterazione 2: i = 1, h[1] = 'genova', stampa: genova.
Iterazione 3: i = 2, h[2] = 'firenze', stampa: firenze.
Iterazione 4: i = 3, h[3] = 'napoli', stampa: napoli.
Iterazione 5: i = 4, h[4] = 'pisa', stampa: pisa.'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

hx = ['tropea', 'genova', 'firenze', 'napoli', 'pisa']  # Lista di stringhe (nomi di città)

i = 0  # Inizializzazione della variabile indice

while i < len(hx):  # Ciclo while che continua finché l'indice i è minore della lunghezza della lista hx
    print(hx[i])  # Stampa l'elemento della lista hx corrispondente all'indice i
    i += 1  # Incrementa l'indice i di 1 per passare all'elemento successivo


'''Spiegazione dettagliata:
Lista hx:

Contiene 5 elementi: 'tropea', 'genova', 'firenze', 'napoli', 'pisa'.
Inizializzazione di i:

La variabile i è inizializzata a 0. Questo rappresenta l'indice corrente che verrà utilizzato per accedere agli elementi della lista.
Condizione del ciclo while:

while i < len(hx):
Il ciclo continua finché i è minore della lunghezza della lista hx (che è 5 in questo caso).
len(hx) restituisce il numero di elementi nella lista.
Corpo del ciclo while:

print(hx[i]): Stampa l'elemento della lista hx all'indice i.
i += 1: Incrementa il valore di i di 1 ad ogni iterazione, per passare all'elemento successivo.
Esecuzione passo per passo:

Iterazione 1: i = 0, hx[0] = 'tropea', stampa: tropea, poi i diventa 1.
Iterazione 2: i = 1, hx[1] = 'genova', stampa: genova, poi i diventa 2.
Iterazione 3: i = 2, hx[2] = 'firenze', stampa: firenze, poi i diventa 3.
Iterazione 4: i = 3, hx[3] = 'napoli', stampa: napoli, poi i diventa 4.
Iterazione 5: i = 4, hx[4] = 'pisa', stampa: pisa, poi i diventa 5.
Il ciclo si interrompe perché la condizione i < len(hx) non è più vera.'''


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# - List comprehension.
# ci permette di usare una sintassi ridotta, in merito alle liste, si basa tutta all'interno di due parentesi quadre 
# si stampa prima citta, la nuova variabile nel for , e poi concatena alla lista delle citta 

# ' != ' di verso da 

# Lista di città
lista_citta = ['tropea', 'genova', 'firenze', 'napoli', 'pisa'] 

# Ciclo che stampa le città nella lista diverse da 'roma'
# Questo codice è corretto solo se scritto così:
[print(citta) for citta in lista_citta if citta != 'roma']

'''prima di tutto manda a schermo citta' concatenata alla lista_ citta , solo se  citta e' diversa da 'roma' '''

# Commento:
# 1. La list comprehension scorre ogni elemento della lista 'lista_citta'.
# 2. La condizione 'if citta != "roma"' verifica se l'elemento corrente non è 'roma'.
# 3. La funzione `print(citta)` viene eseguita per le città che soddisfano la condizione.
# Nota: 'roma' non è presente in 'lista_citta', quindi tutte le città verranno stampate.

# La struttura generale di una list comprehension:
# [espressione for item in lista if condizione]
# 1. 'espressione': l'operazione o il valore da aggiungere alla lista risultante.
# 2. 'for item in lista': scorre ogni elemento della lista.
# 3. 'if condizione': filtra gli elementi per includerli solo se la condizione è vera.
# Risultato: crea una nuova lista (o in questo caso esegue azioni come 'print') per gli elementi che soddisfano la condizione.



#[ espressione for item in lista if condizione == True ]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Definizione della lista di città
lista_citta = ["udine", "roma", "napoli", "venezia"]

# List comprehension per stampare tutte le città nella lista che non sono "roma"
[print(citta) for citta in lista_citta if citta != "roma"]
# Spiegazione:
# 1. Itera su ogni elemento della lista `lista_citta`.
# 2. Controlla se l'elemento corrente (citta) è diverso da "roma" (`if citta != "roma"`).
# 3. Se la condizione è vera, stampa l'elemento.
# NOTA: Questo costrutto genera output sulla console ma non restituisce una nuova lista.

# List comprehension per creare una nuova lista con "milano" al posto di ogni elemento che non è "roma"
x = ["milano" for citta in lista_citta if citta != "roma"]
# Spiegazione:
# 1. Itera su ogni elemento della lista `lista_citta`.
# 2. Controlla se l'elemento corrente (citta) è diverso da "roma".
# 3. Se la condizione è vera, aggiunge la stringa "milano" alla nuova lista.
# 4. Se la condizione è falsa (cioè per "roma"), l'elemento viene ignorato.

# Stampa la nuova lista
print(x)
# Output atteso: ['milano', 'milano', 'milano']
# Spiega che tutti gli elementi diversi da "roma" vengono sostituiti con "milano".

# Commento sulla struttura generale delle list comprehension
# [espressione for item in lista if condizione == True]
# Spiegazione:
# 1. `espressione`: Operazione da eseguire sull'elemento o valore da aggiungere alla lista risultante.
# 2. `for item in lista`: Itera su ogni elemento della lista originale.
# 3. `if condizione`: Filtra gli elementi, includendoli solo se la condizione è vera.


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - Modificare l'ordine: ascendente, discendente, reverse.

# il metodo ' SORT() '

# ORDINA UNA LISTA DI ELEMENTI SIA NUMERICAMENTE CHE ALFABETICAMENTE, NUMERICAMENTE DAL PIU`  PICCOLO AL PIU GRANDE
# RIORDINA LA NOSTRA LISTA 


lista_citta = ['udine', 'roma','livorno','pisa','ANCONA','BARI', 'BOLOGNA']


lista_citta.sort() # questo metodo ordinera` alfabeticamente in questo caso la lista in modo ordinato 

print(lista_citta)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

''' SI PUO ANCHE FARE L'INVERSO QUINDI  ORDINERA' DALL' PIU' GRANDE AL PIU PICCOLO  NUMERICAMENTE E ALFABETICAMENTE AL CONTRARIO '''


# IL MOTODO ' REVERSE ' SI USA PER INVERTIRE L'ORIDINAMENTO 
# ' lista_citta.sort(reverse = True ) 'la funzione reverse funziona cosi' invertira l'ordine quindi non partira' piu da a la lista ordinata 


lista_citta = ['udine', 'roma','livorno','pisa','ANCONA','BARI', 'BOLOGNA']


lista_citta.sort(reverse = True) # questo metodo reverse ordinera` alfabeticamente al contraio in questo caso la lista iniziera diversamente da su  

print(lista_citta)

#['udine', 'roma', 'pisa', 'livorno', 'BOLOGNA', 'BARI', 'ANCONA'] cosi e come sara' ordinata la lista 


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# - Copiare una lista con copy().


c =['malta','sicilia', 'sardegna','vulcano','gozo']


y = c # y fa un riferimento ad c , e poi quindi succesivamente sotto modifica la posizione 0 con 'new york' 
# quindi praticamente non la sto a copia ma faccio riferimento ad c 

y[0] = 'new york ' # modifica la posizione 0 di c 

print(c)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# METODO ' COPY() '

# Mentre nel caso in cui si voglia copiare una lista bisognera' usare il metodo copy 

xr =['malta','sicilia', 'sardegna','vulcano','gozo']

y = xr.copy() # FACENDO COSI' COPIERA LA LISTA XR PER POI AGGIUNGERLA ALLA LISTA Y 

y[0] = 'new york ' # modifica la posizione 0

print(y)

#['new york ', 'sicilia', 'sardegna', 'vulcano', 'gozo'] questo sara' cio che comparira' a schermo copiera la lista xr


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Definizione della lista originale
x = ["udine", "bari", "napoli", "ancona"]

# Creazione di una copia della lista 'x'
y = list(x)

# Modifica del primo elemento della lista 'y'
y[0] = "new york"

# Stampa della lista originale 'x'
print(x)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# per unire  insieme piu liste  faccio : con il + o append o extend


x = ["udine", "bari", "napoli", "ancona"]

c =['malta','sicilia', 'sardegna','vulcano','gozo']


print(x + c)

# facendo cosi' uniro' la lista c alla lista x e' sara' cosi: ['udine', 'bari', 'napoli', 'ancona', 'malta', 'sicilia', 'sardegna', 'vulcano', 'gozo']
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# mettendo il ciclo invece come qui sotto 

# Definizione della lista originale 'x'
x = ["udine", "bari", "napoli", "ancona"]

# Definizione della lista 'c' (nuove città da aggiungere)
c = ['malta', 'sicilia', 'sardegna', 'vulcano', 'gozo']

# Iterazione su ogni elemento della lista 'c'
for citta in c:  # 'citta' rappresenta l'elemento corrente della lista 'c'
    x.append(citta)  # Aggiunge l'elemento corrente di 'c' alla lista 'x'

# Stampa della lista aggiornata 'x'
print(x)  # La lista 'x' ora contiene gli elementi originali più quelli di 'c'


# quindi sopra abbiamo appeso ogni citta' di y a citta per poi appendere x a citta 
# e quindi la lista sara' :  x = ["udine", "bari", "napoli", "ancona", "malta", "sicilia", "sardegna", "vulcano", "gozo"]



'''Spiegazione dettagliata:
Definizione della lista x:

La lista x contiene inizialmente quattro città: ["udine", "bari", "napoli", "ancona"].
Definizione della lista c:

La lista c contiene altre città o luoghi: ['malta', 'sicilia', 'sardegna', 'vulcano', 'gozo'].
Questi elementi verranno aggiunti a x.
Ciclo for:

Il ciclo itera su ciascun elemento della lista c. Ad ogni iterazione:
La variabile citta assume il valore dell'elemento corrente della lista c.
L'elemento corrente viene aggiunto alla lista x utilizzando il metodo .append().
Metodo .append():

Il metodo .append() aggiunge un singolo elemento alla fine della lista x.
Ad ogni iterazione del ciclo, un elemento di c viene aggiunto a x.
Stampa della lista x:

Dopo il ciclo, la lista x contiene sia i suoi elementi originali sia gli elementi aggiunti dalla lista c'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# con il metodo ' extend ' 

# Lista originale 'x' con alcune città
x = ["udine", "bari", "napoli", "ancona"]

# Un'altra lista 'y' con nuove città
y = ["milano", "venezia"]

# Estende la lista 'x' aggiungendo tutti gli elementi della lista 'y'
x.extend(y)

# Stampa la lista aggiornata 'x'
print(x)

# questo e cio uscira a schermo : ['udine', 'bari', 'napoli', 'ancona', 'milano', 'venezia']

''' Spiegazione di ciò che fa il codice:

Definizione della lista x:

La lista x contiene inizialmente quattro città:

python

["udine", "bari", "napoli", "ancona"]
Definizione della lista y:

La lista y contiene due nuove città:
python

["milano", "venezia"]
Metodo .extend():

x.extend(y) aggiunge tutti gli elementi di y alla lista x.
Non crea una nuova lista, ma modifica direttamente la lista x, concatenandola con y.
Dopo questa operazione, la lista x contiene i suoi elementi originali seguiti dagli elementi di y.
Stampa della lista aggiornata x:

La lista x aggiornata viene stampata con tutti gli elementi di x e y.
Esempio di output:
Se esegui il codice, l'output sarà:


['udine', 'bari', 'napoli', 'ancona', 'milano', 'venezia']
Differenza tra .extend() e .append():
.extend(y):

Aggiunge tutti gli elementi di y come singoli elementi alla lista x.
La lista x viene modificata per contenere anche gli elementi di y.
Risultato: ['udine', 'bari', 'napoli', 'ancona', 'milano', 'venezia'].
.append(y):

Aggiunge l'intera lista y come un singolo elemento alla lista x.
La lista x avrà una lista annidata.
Risultato: ['udine', 'bari', 'napoli', 'ancona', ['milano', 'venezia']].
Esempio con .append():


x.append(y)
print(x)
# Output: ['udine', 'bari', 'napoli', 'ancona', ['milano', 'venezia']]'''





















