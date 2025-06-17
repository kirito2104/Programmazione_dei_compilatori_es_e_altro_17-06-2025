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
string = 'a a a a a a a a'
#stringa = string.count(' ')
i = 0 
#while i in stringa :
    #if :

for ge in string :
    while i in ge :
        i += 1
    if ge == 'a':
        ge.count(' ')
    print















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