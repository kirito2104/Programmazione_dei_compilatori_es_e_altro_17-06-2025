
# 18 dictionary

# - Collezioni di dati ordinate, modificabili ma non permettono duplicati
# - Creare un dict
# - Vediamo len(), type()

# - Accedere agli elementi con [], get(), keys(), values(), items(), controllare se chiave esiste
# - Modificare elementi con [] e update()
# - Aggiungere elementi con [] e update()
# - Rimuovere elementi con pop(key), popitem(), clear(), del

# - Ciclare elementi: key, values(), keys(), items()

# - Copiare dict con copy() e dict()
# - Dict annidati

'''Spiegazione:
Dizionari in Python:

Sono collezioni di coppie chiave-valore.
Ordinati (a partire da Python 3.7).
Modificabili.
Non permettono chiavi duplicate.
Operazioni di base:

Creazione: Puoi creare un dizionario con {} o usando dict().
Lunghezza e tipo: Usa len() per la lunghezza e type() per verificare il tipo.
Accesso agli elementi:

Usa [] o get() per accedere ai valori associati alle chiavi.
Usa keys(), values(), items() per iterare sulle chiavi, valori o coppie chiave-valore.
Modifica e aggiunta:

Puoi aggiungere o modificare elementi assegnando un valore a una chiave (d['chiave'] = valore).
Usa update() per aggiornare più elementi contemporaneamente.
Rimozione di elementi:

pop(key): Rimuove un elemento specifico.
popitem(): Rimuove l'ultima coppia aggiunta.
clear(): Rimuove tutti gli elementi.
del: Elimina un elemento specifico o l'intero dizionario.
Copia e dizionari annidati:

Usa copy() o dict() per creare una copia di un dizionario.
I dizionari possono contenere altri dizionari come valori (dizionari annidati).'''


#------------------------------------------------------------------------------------------------------------------------------------------------

#I dict si aprono sempre con le parentesi quadre, 
# I dict sono un insieme di copie , chiave e valore 
# a differenza della collezione dei dati , sono piu' descrittivi come qui sotto: 
# Ognuna delle coppie e' composta da chiave e valore , come qui sotto :
# la cosa utile e' che usando questo stampo andro ad usare, una lista con chiave e valore , in modo piu' oridnato 

persona  = {
    'nome ': 'luca', # 
    'cognome': 'Rossi',
    'eta': 23,
    # 'eta':224  # facendo cosi' dara' errore perche' non ammette chiavi con valori uguali e quindi dara' errore 
    'ddd': 23 # facendo cosi' non dira nulla perche' solo chiave non deve essere uguale 
}
# non ammettendo duplicati la chiave eliminra' casualmente il duplicato 

print(type(persona)) # type leggera' di che tipo e' la lista di dati : sossia un   dict


# - Collezioni di dati ordinate, modificabili ma non permettono duplicati

#---------------------------------------------------------------------------------------------------------------------------------------------

# - Accedere agli elementi con [], get(), keys(), values(), items(), controllare se chiave esiste

persona  = {
    'nome': 'luca', # 
    'cognome': 'Rossi',
    'eta': 23,
    # 'eta':224  # facendo cosi' dara' errore perche' non ammette chiavi con valori uguali e quindi dara' errore 
    'ddd': 23 # facendo cosi' non dira nulla perche' solo chiave non deve essere uguale 
}

print(persona['cognome']) # facendo cosi' mandera; a schermo solo il contenuto della chiave cognome 


#Con il metodo ' get ' invece fara' la stessa cosa e' DARA' A SCHERMO IL CONTENUTO DELLA CHIAVE NOME 

print(persona.get('nome'))

#-------------------------------------------------------------------------------------------------------------------------------
# la funz. ' keys ' 
#usando la funzione ' keys ' : ci permetttera' di trasformare tutte le chiavi in una lista a parte 

# la funzuione valus ----->>>>> crea una lista con tutti i valori delle chiavi di un dict 
# ad es prendera tutti i valori di persona e fara' una lista con tali 
#dell'esercizio qui sotto : ict_values(['luca', 'Rossi', 23, 23])      

# la funz ' items() ' ----->>>>> ci andra' a creare una lista di tuple, con ogni coppia del dict
# e diventaara' cosi' ogni coppia  : dict_items([('nome', 'luca'), ('cognome', 'Rossi'), ('eta', 23), ('ddd', 23)])
# quindi in complessivo genera delle tuple con chiave e valore 

persona  = {
    'nome': 'luca', # 
    'cognome': 'Rossi',
    'eta': 23,
    # 'eta':224  # facendo cosi' dara' errore perche' non ammette chiavi con valori uguali e quindi dara' errore 
    'ddd': 23 # facendo cosi' non dira nulla perche' solo chiave non deve essere uguale 
}


x = persona.keys() # ci crea un lista apparte con tutte le chiavi cosi: dict_keys(['nome', 'cognome', 'eta', 'ddd'])
print(x)
x = persona.values()# crea una lista con solo i valori di ogni cxhiave sara' cosi : #dict_values(['luca', 'Rossi', 23, 23])
print(x)
x = persona.items() #crea piu' tuple con ogni sua coppia nel set : diventa cosi' : dict_items([('nome', 'luca'), ('cognome', 'Rossi'), ('eta', 23), ('ddd', 23)])
print(x)
#----------------------------------------------------------------------------------------------------------------------------------

'''Mentre per verificare se esistono faccio cosi': '''

print('nome' in persona ) # e ci dira' che e' vero 
print('bbfdd'in persona) # ci dira' False ossia che non esiste nel set 

#--------------------------------------------------------------------------------------------------------------------------------------

# - Modificare elementi con [] e update()

# per modificare un vaslore faccio cosi' : 
persona  = {
    'nome': 'luca', # 
    'cognome': 'Rossi',
    'eta': 23,

}
persona ['nome'] = 'Marco' # facendo cosi' ci modifichera il nome che diventera: Marco 

print(persona)

#Mentre usando update ,  che aggiorna il dict 
# si fa cosi'
persona.update({'nome':"anna"}) # facendo cosi' aggoiornera il nome e mettera' anna, aggiornando il dict 
# che diventa cosi: {'nome': 'anna', 'cognome': 'Rossi', 'eta': 23}

print(persona)

#-----------------------------------------------------------------------------------------------------------------------------------------------
# - Mentre per aggiungere elementi con [] e update()

# Creazione di un dizionario iniziale
dizionario = {
    "nome": "Mario", 
    "età": 30 
    
    }
# facendo cosi' :
# Aggiungere un elemento con []
dizionario["colore"] = "blue"  # Aggiunge una nuova coppia chiave-valore
print("Dizionario dopo aggiunta con []:", dizionario)
#--------------------------------------------------------------------------------------------------------------------------------------
# mentre con ()
# Aggiungere più elementi con update()

dizionario.update({"professione": "Ingegnere", "hobby": "calcio"})
print("Dizionario dopo aggiunta con update():", dizionario)

# Aggiornare un elemento esistente con []
dizionario["età"] = 31  # Aggiorna il valore della chiave "età"
print("Dizionario dopo aggiornamento con []:", dizionario)
#---------------------------------------------------------------------------------------------------------------------------------------
#mentre usando update():
# che a differenza aggiorna gli elemnti del dizionario 

# Aggiornare più elementi con update()
dizionario.update({"hobby": "tennis", "città": "Milano"}) # se non si vuole modificare, e si mette quind una chiave che non e
# esiste nel dizionario, andra' ad aggiornare il dizinario 


print("Dizionario dopo aggiornamento con update():", dizionario)


#------------------------------------------------------------------------------------------------------------------------------
#mentre per eliminare una chiave 
## - Rimuovere elementi con pop(key), popitem(), clear(), del

# Creazione di un dizionario iniziale
dizionario = {"nome": "Mario",
    "età": 30,
    "città": "Roma", 
    "hobby": "calcio"
              }
print("Dizionario iniziale:", dizionario)

# 1. Rimuovere un elemento specifico con pop(key)
# pop() rimuove la chiave specificata e restituisce il valore associato

valore = dizionario.pop("città") #qui ' pop ' eliminera' la chiave richiesta 



print("\nDizionario dopo pop('città'):", dizionario)
print("Valore rimosso con pop:", valore)

# 2. Rimuovere l'ultimo elemento aggiunto con popitem()
# popitem() rimuove e restituisce l'ultima coppia chiave-valore

ultima_coppia = dizionario.popitem()     # popitem eliminera' l'ultimo item della del dizionario ossia. l'ultima coppia 


print("\nDizionario dopo popitem():", dizionario)
print("Ultima coppia rimossa con popitem():", ultima_coppia)

# 3. Rimuovere tutti gli elementi con clear()
# clear() svuota completamente il dizionario

'''dizionario.clear() '''# clear() svuota completamente il dizionario''' ''''

print("\nDizionario dopo clear():", dizionario)

# 4. Rimuovere un elemento o l'intero dizionario con del
dizionario = {"nome": "Luigi", "età": 25, "città": "Napoli"}  # Ricreiamo un dizionario
print("\nDizionario ricreato:", dizionario)

# Rimuovere una chiave specifica con del
del dizionario["città"] # puo' eliminare tutto come anche un solo item 

print("Dizionario dopo del dizionario['città']:", dizionario)

# Rimuovere l'intero dizionario con del
'''del dizionario '''
# print(dizionario)  # Questo genera un errore perché il dizionario è stato eliminato


#----------------------------------------------------------------------------------------------------------------------------


persona  = {
    'nome ': 'luca', # 
    'cognome': 'Rossi',
    'eta': 23,
    # 'eta':224  # facendo cosi' dara' errore perche' non ammette chiavi con valori uguali e quindi dara' errore 
    'ddd': 23 # facendo cosi' non dira nulla perche' solo chiave non deve essere uguale 
}
# quindi facendo cosi stampera : le coppie insieme 


for x in persona :
    print(x)
    print(persona[x]) # facendo cosi' stampera' il contenuto dentro la chiave 
    
# facendo cosi' stampra nome, cognome e citta

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Dizionario che rappresenta una persona
persona = { 
    'nome': 'luca',  # Nome della persona
    'cognome': 'Rossi',  # Cognome della persona
    'eta': 23,  # Età della persona
    # Nota: in un dizionario, le chiavi devono essere uniche. Se aggiungi un'altra chiave 'eta', 
    # il valore verrà sovrascritto e non causerà un errore.
    'altro': 23  # Valori duplicati sono ammessi se le chiavi sono diverse.
}

# Ciclo per stampare tutti i valori del dizionario
for x in persona.values():  # Usa il metodo corretto .values()
    print(x)  # Stampa ogni valore del dizionario

'''for chiave in persona.keys: # qui facendo si' prendera' tutte le chiavi , invece dei valori , le chiavi  saranno mandate a schermo 
    print(chiave)
'''
# cio che uscira' sara' questo :
'''luca
Rossi
23
23
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
persona = { 
    'nome': 'luca',  # Nome della persona
    'cognome': 'Rossi',  # Cognome della persona
    'eta': 23,  # Età della persona
    # Nota: in un dizionario, le chiavi devono essere uniche. Se aggiungi un'altra chiave 'eta', 
    # il valore verrà sovrascritto e non causerà un errore.
    'altro': 23  # Valori duplicati sono ammessi se le chiavi sono diverse.
}

'''for chiave in persona.items:# trasformera ilcontenuto in una tupla 
    print(chiave)
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dizionario che rappresenta una persona
persona = { 
    'nome': 'luca',  # Nome della persona
    'cognome': 'Rossi',  # Cognome della persona
    'eta': 23,  # Età della persona
    # Nota: in un dizionario, le chiavi devono essere uniche. Se aggiungi un'altra chiave 'eta', 
    # il valore verrà sovrascritto e non causerà un errore.
    'altro': 23  # Valori duplicati sono ammessi se le chiavi sono diverse.
}

# Creare una copia del dizionario
xr = persona.copy()  # Il metodo .copy() crea una copia indipendente del dizionario originale

# Stampare il dizionario copiato
print(xr)  # Output: {'nome': 'luca', 'cognome': 'Rossi', 'eta': 23, 'altro': 23}



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# usando dict



#Entrambi i metodi creeranno una copia superficiale del dizionario, ma dict() è un costruttore più generico.

#2. Quando usarli?
#.copy():

'''Usalo se hai già un dizionario e vuoi semplicemente copiarlo.
È più leggibile quando il tuo scopo è chiaramente copiare un dizionario.'''
# invece :
#dict():
    
'''
Usalo se stai creando un dizionario da un'altra struttura dati (ad esempio, una lista di tuple o un altro dizionario).
È più versatile perché può essere usato anche per creare un dizionario vuoto o trasformare dati.
'''#3. Esempio pratico:
#Con un dizionario:


originale = {'a': 1, 'b': 2}

# Copia usando .copy()
copia1 = originale.copy()
print(copia1)  # Output: {'a': 1, 'b': 2}

# Copia usando dict()
copia2 = dict(originale)
print(copia2)  # Output: {'a': 1, 'b': 2}
#Con una lista di tuple:


tuples = [('a', 1), ('b', 2)]

# Usa dict() per creare un dizionario
nuovo_dict = dict(tuples)
print(nuovo_dict)  # Output: {'a': 1, 'b': 2}

# .copy() non funziona qui perché non è un dizionario
# copia = tuples.copy()  # Genera un errore
'''4. Comportamento con dati mutabili (copia superficiale):
Entrambi creano una shallow copy (copia superficiale). Questo significa che se i valori nel dizionario originale 
sono oggetti mutabili (ad esempio liste o dizionari), entrambe le copie manterranno il riferimento agli stessi oggetti mutabili.
'''
#Esempio:

originale = {'a': [1, 2, 3], 'b': 42}

# Usando .copy()
copia1 = originale.copy()

# Usando dict()
copia2 = dict(originale)

# Modifica il valore della lista in 'a'
originale['a'].append(4)

'''
print(originale)  # Output: {'a': [1, 2, 3, 4], 'b': 42}
print(copia1)     # Output: {'a': [1, 2, 3, 4], 'b': 42}
print(copia2)     # Output: {'a': [1, 2, 3, 4], 'b': 42}
Se vuoi una deep copy (copia profonda), che duplichi anche i valori mutabili, devi usare il modulo copy:

python
Copia codice
import copy

copia_profonda = copy.deepcopy(originale)
Riepilogo delle differenze:
Metodo	Specifico per dizionari?	Copia superficiale?	Altri usi
.copy()	Sì	Sì	Solo per copiare un dizionario esistente
dict()	No	Sì	Può creare un dizionario da altre strutture dati

'''

person = {
    'nome': 'gino',
    'cognome' : 'ulisse',   
    'eta' : 23
}



x = dict(person) # facendo cosi' crea un nuovo dict (dizionario ) con tutti i valori di quello precedente 


print(x)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''' SI POSSONO ANCHE FARE DEI DICT ANNIDATI OSSIA DIZIONARI ALL'INTERNO CON ULTERIO INFORMAZIONI AL VALORE '''
# ECCO UN ES DI UN DICT ANNIDATO , APRENDO DELLE NUOVE QUDRE COME QUI SOOTO :



person = {
    'nome': 'gino',
    'cognome' : 'ulisse',   
    'eta' : 23 ,
    'INDIRIZZO': {
        'CAP': '00012',
        'CITTA': 'MILANO',
        'CIVICO': 43 
        }
}

print(person) # facendo cosi' stampera' la dict

# che sara' cosi' il dizionario :  {'nome': 'gino', 'cognome': 'ulisse', 'eta': 23, 'INDIRIZZO': {'CAP': '00012', 'CITTA': 'MILANO', 'CIVICO': 43}}

print(person['INDIRIZZO']['CIVICO']) # facendo cosi' stampera il civico dell'indirizzo annidato all'interno di persona  






