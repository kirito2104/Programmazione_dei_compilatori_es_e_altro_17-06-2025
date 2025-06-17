#esempi :
'''
Per contare gli spazi in una stringa in Python, puoi usare il metodo `.
count()` oppure iterare manualmente attraverso i caratteri della stringa. 
Ti mostro alcune opzioni:
'''


### **Metodo 1: Usare `.count(' ')`**
'''
Il metodo più semplice è utilizzare `.count()` per contare quante volte il 
carattere spazio (`' '`) appare nella stringa.
'''

testo = "Questa è una stringa con degli spazi."
# Conta il numero di spazi nella stringa
numero_spazi = testo.count(' ')
print("Numero di spazi:", numero_spazi)


#### **Output:**

#Numero di spazi: 6


### **Metodo 2: Iterare manualmente sui caratteri**
''' Puoi iterare sulla stringa e verificare manualmente se un carattere è uno spazio (`' '`). '''

testo = "Questa è una stringa con degli spazi."

# Inizializza un contatore
numero_spazi = 0

# Itera su ogni carattere della stringa
for carattere in testo:
    if carattere == ' ':  # Controlla se il carattere è uno spazio
        numero_spazi += 1

print("Numero di spazi:", numero_spazi)


#### **Output:**

#Numero di spazi: 6


### **Metodo 3: Usare una List Comprehension**
''' Puoi utilizzare una list comprehension per creare una lista di spazi e contare la sua lunghezza. '''

testo = "Questa è una stringa con degli spazi."
# Conta gli spazi usando una list comprehension
numero_spazi = len([c for c in testo if c == ' '])
print("Numero di spazi:", numero_spazi)


'''
**Output:**

Numero di spazi: 6
'''


### **Metodo 4: Usare `filter()`**
'''Puoi usare la funzione `filter()` per selezionare solo gli spazi e poi contare quanti ne trovi. '''

testo = "Questa è una stringa con degli spazi."
# Filtra solo gli spazi e conta quanti ce ne sono
numero_spazi = len(list(filter(lambda c: c == ' ', testo)))

filter(lambda c: c == ' ', testo)

#filter():
'''
La funzione filter() serve per "filtrare" gli elementi di un iterabile (come una stringa o una lista).
Prende in ingresso due argomenti:
Una funzione che restituisce True o False per ogni elemento.
Un iterabile (in questo caso, la stringa testo).
Restituisce un iteratore che contiene solo gli elementi per cui la funzione restituisce True.
lambda c: c == ' ':
'''

'''
Questa è una funzione anonima (lambda) che verifica se un carattere (c) è uno spazio (' ').
Per ogni carattere della stringa testo, questa funzione restituisce:
True se il carattere è uno spazio (' ').
False altrimenti.
Esempio: Se testo = "a b c", il filtro produce un iteratore contenente solo gli spazi: ['','']
'''
#list(filter(lambda c: c == ' ', testo))

#list():

'''
Converte l'iteratore restituito da filter() in una lista.
La lista risultante conterrà solo gli spazi trovati nella stringa testo.
'''

# Esempio: Se testo = "a b c", il risultato sarà:


#[' ', ' ']
#len(list(...))

#len():
'''
Calcola la lunghezza della lista creata in precedenza, ovvero il numero di spazi presenti nella stringa.
Esempio: Per testo = "a b c", la lunghezza della lista [' ', ' '] è 2.
'''


print("Numero di spazi:", numero_spazi)

'''
**Output:**

Numero di spazi: 6

'''

''' **Quando scegliere un metodo?** '''

# - **Metodo 1 (`.count(' ')`)**: Quando vuoi una soluzione semplice e diretta.
#- **Metodo 2 (loop manuale)**: Se vuoi avere più controllo o contare altre cose insieme.
#- **Metodo 3 (list comprehension)**: Se preferisci uno stile più funzionale e compatto.
#- **Metodo 4 (`filter()`)**: Se vuoi combinare funzioni funzionali con il conteggio.





#-------------------------------------------------------------------------------------------------------------------------------------------
#Esercizi
'''1)Si scriva un programma che conti e stampi quante volte compare il carattere  
(spazio) all'interno di una stringa legata alla variabile a. 
Il programma deve far uso soltanto dei costrutti Python fin qua studiati. 
Suggerimento: potrebbe essere utile un ciclo while che conta il numero di 
spazi consecutivi a partire da una posizione e che sia 'annidato' nel ciclo
principale che scorre i caratteri della stringa.
'''
string = 'a a a a a a a a a a a '
#stringa = string.count(' ')
count_spazzi = 0
count_letter = 0 
i = 0 

while i < len(string):
    if string[i] == (' ') :
        count_spazzi += 1 
       
    if string[i] == ('a') :
        count_letter += 1 
        
    i += 1 
print('Ecco quanti sono gli spazi:', count_spazzi)        
print('Ecco quanti sono le "a":', count_letter)
#se mettevo i print all'interno di ogni ciclo if , non varebbe stampato solo un volta i numeri di quanti sono 
# i spazzi e le 'a' ma avrebbe stampato ogni volta il print, fino ad arrivare alla fine dellaa stringa
# in poche parole inizializzava finche' non finisce la stringa 

#########################################################################################################################
# facendo come qui sotto sarebbe sbagliato siccome bisogna prima creare su 
# contatori nuovi che si incrementano  ogni volta cvhe controllano se c'e' ne e' nella stringa 
'''Incremento `i` alla fine dell'ultimo `if` (oppure del ciclo) perché il **valore 
di `i` rappresenta l'indice corrente** nella stringa, e deve progredire per passare 
al prossimo carattere. Questo è necessario per evitare che il programma si blocchi 
in un ciclo infinito o che analizzi ripetutamente lo stesso carattere.
'''
#Ecco perché è importante:



#**Funzione di `i` nel ciclo**
# 1. `i` è l'indice che rappresenta la posizione corrente del carattere nella stringa.
#2. Ad ogni iterazione del ciclo, `i` deve essere incrementato per passare al carattere successivo.
#3. Se non incrementi `i`, il ciclo si blocca (ciclo infinito) perché la condizione `i < len(string)` rimane sempre vera.


'''
### **Esempio senza incremento di `i`**
Consideriamo questo codice:
```python
string = 'a a a'
i = 0
count_spaces = 0
count_a = 0

while i < len(string):
    if string[i] == ' ':
        count_spaces += 1
    if string[i] == 'a':
        count_a += 1
    # i += 1 manca qui!
```

**Cosa succede:**
- `i` rimane sempre uguale a `0`.
- Il ciclo verifica sempre `string[0]` (`'a'`), aggiornando ripetutamente i contatori senza mai progredire.
- Il programma va in un ciclo infinito.

---

### **Correzione con incremento di `i`**
Con l'incremento, il codice scorre correttamente la stringa:
```python
string = 'a a a'
i = 0
count_spaces = 0
count_a = 0

while i < len(string):
    if string[i] == ' ':
        count_spaces += 1
    if string[i] == 'a':
        count_a += 1
    i += 1  # Passa al prossimo carattere
```

**Cosa succede ora:**
1. La prima iterazione analizza `string[0]` (`'a'`).
2. `i` viene incrementato a `1`, quindi la seconda iterazione analizza `string[1]` (`' '`).
3. Il ciclo continua finché tutti i caratteri sono stati analizzati.

---

### **Esempio concreto**
Per la stringa `'a a a'`:
- La lunghezza è 5.
- Iterazioni del ciclo:
  - Iterazione 1: `i = 0`, analizza `'a'`, incrementa `count_a`.
  - Iterazione 2: `i = 1`, analizza `' '`, incrementa `count_spaces`.
  - Iterazione 3: `i = 2`, analizza `'a'`, incrementa `count_a`.
  - Iterazione 4: `i = 3`, analizza `' '`, incrementa `count_spaces`.
  - Iterazione 5: `i = 4`, analizza `'a'`, incrementa `count_a`.
- `i` raggiunge 5 (uguale a `len(string)`) e il ciclo si interrompe.

---
'''
##**Perché non incrementare `i` nei singoli `if`?**
# Incrementare `i` solo all'interno dei blocchi `if` può portare a errori, perché `i` 
# non verrebbe sempre aggiornato. Ad esempio:

'''python
while i < len(string):
    if string[i] == ' ':
        count_spaces += 1
        i += 1  # Incrementa solo se c'è uno spazio
    if string[i] == 'a':
        count_a += 1
        i += 1  # Incrementa solo se c'è una 'a'
'''

#**Problemi:**
# - Se `string[i]` non è né `' '` né `'a'`, `i` non viene incrementato e il ciclo si blocca su quel carattere.



# **Soluzione corretta: Incremento alla fine**
#Incrementare `i` alla fine del ciclo garantisce che il programma 
#analizzi tutti i caratteri, indipendentemente dal loro valore:
'''
while i < len(string):
    if string[i] == ' ':
        count_spaces += 1
    if string[i] == 'a':
        count_a += 1
    i += 1  # Incrementa sempre, indipendentemente dagli if
'''

# **Conclusione**
#Incrementare `i` alla fine è una **pratica sicura e standard** per evitare che il ciclo si blocchi o 
#che vengano ignorati caratteri non corrispondenti alle condizioni `if`.



'''
# Ciclo principale per scorrere ogni carattere della stringa
i = 0  # Inizializza l'indice
while i < len(string):  # Scorri tutti i caratteri della stringa
    
    if string[i] == (' '):# Entra nel ciclo e controlla se il  carattere corrente è uno (' ') spazio
        i+= 1 
        print ('ecco quanti sono i spazzi : ',i )
    if string[i] == ('a'):# Entra nel ciclo e controlla se il  carattere corrente è una 'a'
        i+=1
        print ('ecco quanti sono le a  : ',i )
'''
# questa versione qui sotto e' sbaglita perche' conforntando i che e' un numero con una stringa non ha senso 
'''   
while i == string :
    i +=1
    if i.count == (' '):
        print('Ecco qunti sono gli spazi ',i)
    if i.count == ('a'):
        print('Ecco qunti sono le a :',i)        

'''
'''Uso sbagliato di while: Non stavi scorrendo correttamente la stringa con un indice.
Uso sbagliato di .count: Il metodo .count deve essere applicato a una stringa, non a un intero.
Nessuna variabile contatore: Non stavi accumulando i risultati in variabili per il conteggio.
'''















#----------------------------------------------------------------------------------------------------------------------------------------
#''' Modificare il codice precedente facendo in modo che il programma conti il numero '''
#di vocali minuscole all'interno della stringa. 
#Risolvere il problema usando l'operatore in di seguito descritto.

'''Siano x e y due stringhe, x in y vale True se e solo se la stringa x è sottostringa di y. Ad esempio

    'yt' in 'Python'
vale True mentre

    'a' in 'Python'
    'yht' in 'Python'
valgono False
'''





string = 'a a a a a a a a a a a A A '
#stringa = string.count(' ')
count_spazzi = 0
count_letter = 0 
i = 0 
count_maiuscole = 0 
while i < len(string):
    if string[i] == (' ') :
        count_spazzi += 1 # Conta gli spazi
       
    if string[i] == ('a') :
        count_letter += 1  # Conta le 'a'
    
    if string[i] in ('A') :
        count_maiuscole +=1 #Conta le " A "
    
    i+= 1 # Incrementa i per passare al prossimo carattere
    
   
    
print('Ecco quanti sono gli spazi:', count_spazzi)        
print('Ecco quanti sono le "a":', count_letter)
print('Ecco quanti sono le Maiuscole :', count_maiuscole)

'''
Nel ciclo while,se incremento  due volte ' i ': una volta dopo 
il primo controllo su ' ' (spazio) e una volta dopo il controllo su 'A' (maiuscola). 
Questo comporta un errore nel salto di caratteri, poiché stai aumentando i due volte 
per ogni iterazione, saltando così dei caratteri nella stringa.
'''
# quindi per risolvere il problema bisogna incrementare i solo una volta ossia alla fine
#perche ogni volta che scorre l'indice controlla nei vari if , se 
# le condizioni poste sono tali 


#----------------------------------------------------------------------------------------------------------------------------------------
#######Esercizio: Conta consonanti, vocali e caratteri speciali
#Scrivi un programma che prenda in input una stringa e:

#Conti quante vocali (a, e, i, o, u) sono presenti.
#Conti quante consonanti sono presenti.
#Conti quanti caratteri non alfabetici (come spazi, numeri o simboli) sono presenti.
#Suggerimento
#Usa un ciclo per scorrere ogni carattere della stringa.
#Puoi usare l'operatore in per verificare se un carattere è una vocale.
##Usa il metodo .isalpha() per verificare se un carattere è alfabetico

print('---------------------------------------------------')
count = 0 
count1 = 0
count2 = 0 
count3 = 0 

string1 = ['ieirocsdsfdadffgfg', '==-98133@!$#*(^)aa','gAddfhgfd','iiiiOOOO']
#stringa = string.count(' ')

count_spazzi = 0
count_letter = 0 

count_vocali = 0
count_consonanti = 0
count_speciali = 0

i = 0 
count_maiuscole = 0 
while i < len(string1):
    string = string1[i] # Prende la stringa corrente dalla lista
    j = 0  # Inizializza l'indice per scorrere i caratteri della stringa
    while j < len(string):
        char = string[j]
        if char == (' ') :
            count_spazzi += 1 # Conta gli spazi
            
        if char in 'a' :
            count_letter += 1  # Conta le 'a'
    
        if char in ('A') :
            count_maiuscole +=1 #Conta le " A "
        if char in 'AeiuoaEIOU': # controlla che nella string1 ci siano le vocali poste e conta quate sono 
            count_vocali += 1
        elif char.isalpha(): # controlla quante consonanti ci sono
            count_consonanti +=1
        # isalpha controlla e' un metodo che controlla se ci sono lettere dell'alfabeto ee conta quante 
        #Il metodo .isalpha() verifica se tutti i caratteri 
        #di una stringa sono lettere dell'alfabeto (sia maiuscole che minuscole) e restituisce:   
        #controlla solo le lettere dell'alfabeto 
        
        elif not char.isalnum():# controlla che ci siano caratteri speciali 
            #diversi dalle lettere e' numeri, infaatti metto not per negare e' stampare 
            #isalum cotrolla sia lettere che numeri a differenza di 'isalpha'
            count_speciali +=1
            
        j+=1 # Incrementa l'indice per il prossimo carattere
    i += 1  # Passa alla prossima stringa nella lista
  
  
  
#Usa .isalnum():
#Quando vuoi verificare che una stringa contenga solo lettere e numeri (senza spazi o simboli).
#Ad esempio, per validare username, password o identificatori.
    
print('Ecco quanti sono gli spazi:', count_spazzi)        
print('Ecco quanti sono le "a":', count_letter)
print('Ecco quanti sono le Maiuscole.. :', count_maiuscole)

print('Ecco quanti sono le vocali .. :', count_vocali)

print('Ecco quanti sono le consonnti  .. :', count_consonanti)
print('Ecco quanti sono i caratteri speciali  .. :', count_speciali)


#----------------------------------------------------------------------------------------------------------------------------

#facendo come qui sotto risultera' sbagliato perche':

'''Il tuo codice è errato perché presenta alcuni problemi logici e sintattici che impediscono
il corretto funzionamento. Ecco i principali errori e come correggerli:
'''


# **1. Problema: Iterazione errata con `list[string]`**
#Il tuo codice include questa riga:

#while i < len(list[string]):

'''**Errore:**
- `string1` è una lista, quindi devi scorrere direttamente i suoi elementi.
- Non esiste `list[string]`, e usare `len(list[string])` genererà un errore.'''

'''**Correzione:**
Sostituisci con:
```python
while i < len(string1):

In questo modo, `i` scorre correttamente gli indici della lista `string1`.'''



### **2. Problema: Controllo errato delle vocali e consonanti**

'''if string[i] == ['aeiou']:
    count += 1
if string[i] == ['bcdfghjklmnpqwxyz']:
    count1 += 1
'''
'''**Errore:**
- `string[i]` è un carattere, mentre `['aeiou']` è una lista di stringhe.
- Non puoi confrontare un carattere con un'intera lista.
'''
#**Correzione:**
#Usa l'operatore `in` per verificare se il carattere è in una stringa:

'''if string[j] in 'aeiouAEIOU':  # Controllo per vocali
    count += 1
if string[j] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':  # Controllo per consonanti
    count1 += 1'''

# **3. Problema: Iterazione sui caratteri della stringa**
#Il ciclo `while` non scorre correttamente i caratteri della stringa attuale, 
#poiché ti manca un secondo indice per iterare sui caratteri all'interno di ogni stringa della lista `string1`.

'''**Correzione:**
Aggiungi un secondo ciclo interno per iterare sui caratteri:

while i < len(string1):  # Scorre le stringhe nella lista
    string = string1[i]  # Prendi la stringa corrente
    j = 0  # Inizializza l'indice per i caratteri della stringa
    while j < len(string):  # Scorre i caratteri della stringa
        # Operazioni sui caratteri
        j += 1
    i += 1'''


# **4. Problema: Variabile `char` non inizializzata**
#Il tuo codice non assegna alcun valore alla variabile `char`, il che potrebbe generare confusione.

#**Correzione:**
#Dichiarare esplicitamente `char` come il carattere corrente:

#char = string[j]


## **5. Problema: Mancanza del controllo dei caratteri speciali**
#Non hai implementato un controllo completo per i caratteri non alfabetici.

'''**Correzione:**
Usa `not char.isalnum()` per identificare i caratteri speciali:


if not char.isalnum():
    count3 += 1'''


## **Codice Corretto**

#Ecco il tuo codice corretto con le modifiche sopra:


'''# Inizializza i contatori
count = 0  # Contatore per le vocali
count1 = 0  # Contatore per le consonanti
count2 = 0  # Contatore per i caratteri speciali

# Lista di stringhe
string1 = ['ieirocsdsfdadffgfg', '==-98133@!$#*(^)']

# Indice per iterare sulla lista
i = 0

# Ciclo per ogni stringa nella lista
while i < len(string1):
    string = string1[i]  # Prendi la stringa corrente
    j = 0  # Inizializza l'indice per i caratteri della stringa
    while j < len(string):  # Scorri i caratteri della stringa
        char = string[j]  # Carattere corrente
        if char in 'aeiouAEIOU':  # Controllo per vocali
            count += 1
        elif char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':  # Controllo per consonanti
            count1 += 1
        elif not char.isalnum():  # Controllo per caratteri speciali
            count2 += 1
        j += 1  # Incrementa l'indice per il prossimo carattere
    i += 1  # Passa alla prossima stringa nella lista

# Stampa i risultati
print('Ecco quante sono le vocali:', count)
print('Ecco quante sono le consonanti:', count1)
print('Ecco quante sono i caratteri speciali:', count2)'''


### **Esempio di Output**

#Per la lista:

#string1 = ['ieirocsdsfdadffgfg', '==-98133@!$#*(^)']


'''L'output sarà:

Ecco quante sono le vocali: 7
Ecco quante sono le consonanti: 14
Ecco quante sono i caratteri speciali: 12
'''

### **Cosa abbiamo corretto?**
#1. Scorrimento della lista di stringhe con il ciclo esterno.
#2. Scorrimento dei caratteri di ogni stringa con il ciclo interno.
#3. Uso corretto dell'operatore `in` per controllare vocali e consonanti.
#4. Identificazione dei caratteri speciali con `not char.isalnum()`.
#5. Aggiunta della variabile `char` per rendere il codice più leggibile.








'''
while i < len(list[string]):
    if string[i] == ['aeiou'] :
        count +=1
    if string[i] == ['bcdfghjklmnpqwxyz']:
        count1 +=1
    if string[i].isalpha():#.isalpha() per verificare se un carattere è alfabetico
        count3 += 1 
    
    i += 1

print ('ecco quante sono le vocali ',count)
print ('ecco quante sono le consonanti  ',count1)
print ('ecco quante sono i caratteri specili  ',count3)
'''

'''
Usa while se hai bisogno di controllare manualmente l'indice o interrompere il ciclo in condizioni particolari.
Usa for quando devi scorrere una sequenza in modo più semplice ed elegante.


'''





#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------


#Se usi il metodo **`.count()`** per contare vocali, consonanti e caratteri speciali, il programma diventa molto più semplice e compatto perché non è necessario iterare manualmente sulla stringa. Il metodo `.count()` conta direttamente le occorrenze di un carattere specifico in una stringa.



# **Soluzione con `.count()`**

#Ecco come utilizzare `.count()` per contare vocali, consonanti e caratteri speciali:


# Stringa da analizzare
string1 = 'Hello 123!@# World'

# Conta le vocali
vocali = sum(string1.count(v) for v in 'aeiouAEIOU')

# Conta le consonanti
consonanti = sum(string1.count(c) for c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

# Conta i caratteri speciali
speciali = sum(1 for c in string1 if not c.isalnum())

# Stampa i risultati
print("Vocali:", vocali)
print("Consonanti:", consonanti)
print("Caratteri speciali:", speciali)




## **Come funziona il codice?**

#1. **Conteggio delle vocali:**
  
'''sum(string1.count(v) for v in 'aeiouAEIOU')'''
   
  # - Usa una **list comprehension** per iterare su ogni vocale in `'aeiouAEIOU'` e somma le occorrenze di ciascuna vocale nella stringa `string1`.
  # - `string1.count(v)` conta il numero di volte che la vocale `v` appare nella stringa.

#2. **Conteggio delle consonanti:**
   
''' sum(string1.count(c) for c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ') '''
   #- Simile al conteggio delle vocali, ma itera su tutte le consonanti.

#3. **Conteggio dei caratteri speciali:**
'''
   sum(1 for c in string1 if not c.isalnum())
  '''
   #- Usa una **list comprehension** per contare ogni carattere che non è alfanumerico (cioè non è una lettera o un numero).



# **Esempio di Output**

#Per la stringa:
#string1 = 'Hello 123!@# World'

#Il programma stampa:
'''
Vocali: 3
Consonanti: 7
Caratteri speciali: 6
'''

# **Vantaggi di `.count()`**

#1. **Semplicità:**
   #- Non devi gestire manualmente cicli e condizioni.
   ####- Il codice è più compatto e leggibile.

#2. **Efficienza:**
   #- `.count()` è ottimizzato internamente in Python per trovare rapidamente le occorrenze di un carattere.



# **Quando usare `.count()`?**

#- **Usalo se devi contare caratteri specifici in una stringa.**
#- Tuttavia, `.count()` non è adatto se devi lavorare con stringhe complesse 
# o se devi fare controlli più dettagliati 
# (ad esempio, distinguere tra maiuscole e minuscole in modo condizionale).

