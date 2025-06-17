

print(ord('a'), ord ('b')  )

print(ord('A'), ord ('B')  )

print(ord('0'), ord ('5')  )

print(chr(100))


#====================================================================================================================================

# da maiuscolo a minuscolo

c = str(input('inserisci il val di C :'))

if c >= 'A' and c <= 'Z': # c è maiuscolo
    #La condizione verifica se il carattere 'c' è una lettera maiuscola.
    # Questo avviene confrontando il valore Unicode (o ASCII) di 'c' con i valori delle lettere maiuscole 'A' e 'Z'.
    # 1. `c >= 'A'`: Controlla se il carattere 'c' è maggiore o uguale a 'A' (valore Unicode: 65).
    # 2. `c <= 'Z'`: Controlla se il carattere 'c' è minore o uguale a 'Z' (valore Unicode: 90).
    # Se entrambe le condizioni sono vere, significa che 'c' è una lettera maiuscola.
    '''# da maiuscolo a minuscolo '''
    delta = ord(c) - ord('A')  
# Calcola la "distanza" (o offset) tra il carattere 'c' e 'A' nella tabella Unicode/ASCII.
# Se 'c' è 'D', ad esempio:
# ord('D') restituisce 68, ord('A') restituisce 65.
# delta = 68 - 65 = 3.
# Questo offset rappresenta la posizione relativa di 'c' rispetto ad 'A'.

c_min = chr(ord('a') + delta)  
# Utilizza l'offset calcolato per determinare il carattere minuscolo corrispondente.
# Somma il valore Unicode di 'a' (97) all'offset per ottenere il carattere desiderato.
# Ad esempio:
# ord('a') = 97, delta = 3 → 97 + 3 = 100 → chr(100) restituisce 'd'.
# Quindi, se 'c' è 'D', il carattere minuscolo corrispondente sarà 'd'.

print(c_min)  
print (ord(c_min))
# Stampa il risultato, cioè il carattere minuscolo corrispondente a 'c'.

'''inserisci il val di C :D
d
100'''


#===========================================================================================================================================

# PROGRAMMA DELLA RADICE QUADRATA


# Chiede all'utente di inserire un numero intero e lo assegna alla variabile 'x'.
# La funzione `input` legge una stringa dall'input, e `int` la converte in un intero.
x = int(input('scrivi un num :'))

# Chiede all'utente di inserire un secondo numero intero e lo assegna alla variabile 'g'.
g = int(input('scrivi un secondo numero :'))

# Stampa il tipo della variabile 'g' per confermare che è un numero intero.
print(type(g))  # Output: <class 'int'>

# Avvia un ciclo `while` per approssimare la radice quadrata del numero `x` usando il metodo di Newton-Raphson.
# Il ciclo continua finché la differenza assoluta tra `g` e `x/g` è maggiore di una soglia (0.00001 in questo caso).

while abs(g - x/g) > 0.00001:  # La condizione valuta la precisione dell'approssimazione.
    print(g)  # Stampa il valore corrente di 'g' a ogni iterazione per osservare come evolve.
    
    # Aggiorna il valore di 'g' con la formula di Newton-Raphson:
    # `g` viene sostituito con la media tra `g` e `x/g`.
    # Questo passaggio riduce gradualmente l'errore tra `g` e la radice quadrata di `x`.
    g = (g + x/g) / 2
    
    # Stampa il tipo di 'g' dopo l'aggiornamento.
    # Poiché la divisione in Python restituisce sempre un numero di tipo float, il tipo di 'g' diventa `float` dopo la prima iterazione.
    print(type(g))  # Output: <class 'float'>

# Quando il ciclo termina, significa che la differenza tra `g` e `x/g` è inferiore o uguale a 0.00001.
# Stampa il valore finale di 'g', che è un'approssimazione della radice quadrata di `x`.
print(g)



#=================================================================================================================================

#LA FUNZIONE ' ABS '

'''
La funzione abs in Python serve a calcolare il valore assoluto di un numero. 
Il valore assoluto di un numero è la sua distanza dallo zero sulla retta numerica, indipendentemente dal segno.

'''

'''La funzione **`abs`** in Python serve a calcolare il **valore assoluto** di un numero.
Il valore assoluto di un numero è la sua distanza dallo zero sulla retta numerica, indipendentemente dal segno.
'''
### **Sintassi:**

'''abs(x)
'''

##- **`x`**: Può essere un numero intero, un numero in virgola mobile (float), o un numero complesso.
#- **Ritorna:**
 # - Il valore assoluto di un numero intero o float.
  #- Il **modulo** di un numero complesso.


### **Esempi di utilizzo:**

#1. **Numeri interi:**
''' python
   print(abs(10))   # Output: 10
   print(abs(-10))  # Output: 10
  '''

#2. **Numeri in virgola mobile:**
  
''' print(abs(3.14))    # Output: 3.14
   print(abs(-3.14))   # Output: 3.14
   '''

#3. **Numeri complessi:**
''' Per i numeri complessi, `abs` restituisce il **modulo**, calcolato come:
   
   \text{modulo} = \sqrt{\text{reale}^2 + \text{immaginaria}^2}'''

 
''' print(abs(3 + 4j))  # Output: 5.0 (perché √(3² + 4²) = 5)
   print(abs(-1 - 1j)) # Output: 1.4142135623730951 (perché √((-1)² + (-1)²) ≈ 1.414)
   
'''
 



# **Perché si usa `abs` nel codice?**
#Nel contesto di calcoli come il metodo di Newton-Raphson (radice quadrata):

''' while abs(g - x/g) > 0.00001: '''

#- **Scopo:** Assicurarsi che la differenza tra l'approssimazione corrente (`g`)
# e quella ideale (`x/g`) sia **positiva** e confrontabile con una soglia (in questo caso, `0.00001`).
#- **Valore assoluto:** Evita che un risultato negativo (ad esempio, `g - x/g < 0`)
# interferisca con la logica del confronto.



### **Quando usare `abs`?**
#1. **Elaborazione numerica:**
   #- Per ignorare il segno nei calcoli matematici.
   #- Per misurare la distanza tra due numeri.

#2. **Condizioni di arresto nei cicli:**
   #- Controllare che una differenza (come in un'iterazione) sia minore di una soglia specifica.

#3. **Gestione dei numeri complessi:**
   #- Per ottenere il modulo di un numero complesso.


#===========================================================================================================================================
def sqrt1 (x =int(input("scrivi il primo num :")), g = int(input('scrivi il secondo num : ')) ): 

    g, c = x/2, 0  
    # Inizializza due variabili:
    # - `g`: rappresenta l'approssimazione iniziale della radice quadrata di `x`.
    # Viene impostata come metà di `x` per avere un punto di partenza ragionevole.
    # - `c`: è un contatore che tiene traccia del numero di iterazioni effettuate nel ciclo `while`.

    eps, c_max = 0.00000000000001, 1000
    # Definisce due parametri di controllo:
    # - `eps`: è la soglia di tolleranza per determinare quando 
    # l'approssimazione è sufficientemente precisa. Più piccolo è `eps`, maggiore sarà la precisione richiesta.
    # - `c_max`: è il numero massimo di iterazioni che il ciclo 
    # può eseguire. Questo evita cicli infiniti in caso di mancata convergenza.

    while abs(g - x/g) > eps and c < c_max:
        # Condizione del ciclo:
        # 1. `abs(g - x/g) > eps`: Controlla che la differenza assoluta tra `g` (approssimazione attuale) 
        # e `x/g` (valore teorico) sia maggiore della soglia `eps`.
        #    Se la differenza è minore o uguale a `eps`, significa che la precisione desiderata è stata raggiunta.
        # 2. `c < c_max`: Verifica che il numero di iterazioni non abbia superato 
        # il limite massimo. Questo garantisce che il ciclo termini anche se l'approssimazione non converge.
        
        c = c + 1
        # Incrementa il contatore `c` di 1 per tenere traccia delle iterazioni effettuate.

        g = (g + x/g) / 2
        # Aggiorna il valore di `g` usando la formula di Newton-Raphson:
        # - `g`: approssimazione attuale.
        # - `x/g`: valore calcolato usando l'approssimazione corrente.
        # La media tra `g` e `x/g` fornisce una nuova stima della radice 
        # quadrata, migliorando progressivamente l'approssimazione.
    print('ecco il nummm', g)
    # Stampa il valore finale di `g`, che rappresenta l'approssimazione della radice quadrata di `x`.
    # Se il ciclo termina perché la precisione `eps` è raggiunta, 
    # questo valore sarà molto vicino alla radice quadrata reale.


#=====================================================================================================================

#FUNZIONI 
# sono delle parte di codice che possono essere riutilizzate 
#sono delle sotto programmi che possono essere riusate 

'''sqrt significa l'approssimazione della radice quadrata di un numero utilizzando il metodo di Newton-Raphson.'''

def sqrt(x=int(input("scrivi il primo num: "))):
    
    g, c = x / 2, 0  
    # `g`: Approssimazione iniziale della radice quadrata (metà di `x`).
    # `c`: Contatore per il numero di iterazioni.

    eps, c_max = 0.00000000000001, 1000
    # `eps`: Tolleranza per determinare la precisione.
    # `c_max`: Limite massimo di iterazioni per evitare cicli infiniti.

    while abs(g - x / g) > eps and c < c_max:
        # Continua finché la differenza tra `g` e `x/g` è maggiore di `eps` 
        # e il numero di iterazioni è inferiore a `c_max`.

        c = c + 1  # Incrementa il contatore.
        g = (g + x / g) / 2  # Migliora l'approssimazione con Newton-Raphson.

    print('ecco il num ', g)
    # Stampa l'approssimazione finale della radice quadrata.
   
# stampa questo funz 

sqrt()

#------------------------------------------------------------------------------------------------------------------------------

#CON IL RETURN IL PROGRAMMA CAMBIERA', PERCHE AGGIUNGENDOLO POTRO' RESTITUIRE IL VALORE FINALE DELLA FUNZIONE 
#IN QUESTO CASO DELLA RADICE QUADRATA 



'''sqrt significa l'approssimazione della radice quadrata di un numero utilizzando il metodo di Newton-Raphson.'''

def sqrt(x=int(input("scrivi il primo num: "))):
    
    g, c = x / 2, 0  
    # `g`: Approssimazione iniziale della radice quadrata (metà di `x`).
    # `c`: Contatore per il numero di iterazioni.

    eps, c_max = 0.00000000000001, 1000
    # `eps`: Tolleranza per determinare la precisione.
    # `c_max`: Limite massimo di iterazioni per evitare cicli infiniti.

    while abs(g - x / g) > eps and c < c_max:
        # Continua finché la differenza tra `g` e `x/g` è maggiore di `eps` 
        # e il numero di iterazioni è inferiore a `c_max`.

        c = c + 1  # Incrementa il contatore.
        g = (g + x / g) / 2  # Migliora l'approssimazione con Newton-Raphson.

    print('ecco il num ', g)
    # Stampa l'approssimazione finale della radice quadrata.
   
    return g # Levando il retutn il ' ris ' sara' uguale a None 


ris = sqrt(3)
 
#------------------------------------------------------------------------------------------------------------------------------
def sqrt(x,eps, c_max):
    
    g, c = x / 2, 0  
    # `g`: Approssimazione iniziale della radice quadrata (metà di `x`).
    # `c`: Contatore per il numero di iterazioni.

   
    # `eps`: Tolleranza per determinare la precisione.
    # `c_max`: Limite massimo di iterazioni per evitare cicli infiniti.

    while abs(g - x / g) > eps and c < c_max:
        # Continua finché la differenza tra `g` e `x/g` è maggiore di `eps` 
        # e il numero di iterazioni è inferiore a `c_max`.

        c = c + 1  # Incrementa il contatore.
        g = (g + x / g) / 2  # Migliora l'approssimazione con Newton-Raphson.

    print('ecco il num ', g)
    # Stampa l'approssimazione finale della radice quadrata.
   
    return g # Levando il retutn il ' ris ' sara' uguale a None 


ris = sqrt(20,0.000000000000000001 , 1000 )

print('qusto e il ris :',ris)

# SI puo' anche fare : 
# ris = sqrt (20 , c_max =100 ,esp = 0.1234 )
# cio permette si di migliorare, il cod delle vaeriabili 


#======================================================================================================================================================
#------------------------------------------------------------------------------------------------------------------------------
def sqrt(x,eps = 0.001, c_max = 1000):
    
    g, c = x / 2, 0  
    # `g`: Approssimazione iniziale della radice quadrata (metà di `x`).
    # `c`: Contatore per il numero di iterazioni.

   
    # `eps`: Tolleranza per determinare la precisione.
    # `c_max`: Limite massimo di iterazioni per evitare cicli infiniti.

    while abs(g - x / g) > eps and c < c_max:
        # Continua finché la differenza tra `g` e `x/g` è maggiore di `eps` 
        # e il numero di iterazioni è inferiore a `c_max`.

        c = c + 1  # Incrementa il contatore.
        g = (g + x / g) / 2  # Migliora l'approssimazione con Newton-Raphson.

    print('ecco il num ', g)
    # Stampa l'approssimazione finale della radice quadrata.
   
    return g # Levando il retutn il ' ris ' sara' uguale a None 



# si puo' anche modificare cosi' la variabile che e' stata assegnata sopra :

print(sqrt(20,0.001 , 10 )) # si puo' anche modificare cosi' 

print(sqrt(20 )) # o cosi' 

print(sqrt(c_max =21, x = 20 )) # o anche soci' chiamando direttamnete il nome della variabile 
# si puo' anche non assegnare l'oridine quando richiami le variabili 



#------------------------------------------------------------------------------------------------------------------------------------

#palindromo funz.

a = '012Kayak210'
n = len(a)

i = 0

while i < n/2  and a[i] == a[n-1 - i ]:
    i+= 1
if a[i] != a[n-1-i ]:
    print('NON PALINDROMO')
else :
    print('E PALINDROMO ')

#TALE CODICE PERO' SE BISOGNA RITILIZZARLO, FACENDO COSI' NON SI PUO E' QUINDI SI UTILIZZA
# DICHIARANDO SOPRA LA FUNZ PALINDROMO E POI CI SI METTE AL SUO INTERNO , PIU' VARIABILI 
# iN QUESTO CASO METTO SOLO 'a'  DOVE SOTTO POI GLI ASSEGNO IL VALORE(POTREI FARLO ANCHE SOPRA )
# DOPO DI CHE LA COSA CHE CAMBIA PRINCIPALMENTE E' CHE IL PRINT NON E' EFFECIENTE SE SI VOLGIONO 
#RICHIAMARE I VALORI DELLA FUNZIONE, 
# E QUINDI PER FAR SI CHE VENGANO RESTITUITI, SI FA COSI:
''' if a[i] != a[n - 1 - i]:
        # Se il carattere corrente da sinistra (`a[i]`) non corrisponde al carattere corrente da destra
        # (`a[n-1-i]`), significa che la stringa non è un palindromo.
        return False
        # Restituisce `False` perché la stringa non è un palindromo.

    # Se il ciclo termina senza trovare disuguaglianze, la stringa è un palindromo.
    return True
    '''
# FACENDO COSI' FARO' SARA' EQUIVALENTE ALLA SOLUZIONE ELSE, QUI SFRUTTO IL FATTO CHE CON L'ISTRUZIONE RETURN CHIUDE LA FUNZ PER RESTITUIRE 
# IL VALORE. IL RETURN QUINDI CONTROLLA SE LA FUNZIONE E' VERA E' RESTITUISCE CHE E' 
# " return false " e la funz termina, nel caso in cui sia false restituisce che e' 
# " return True " 

# se non c'e' il return viene restituito il valore None (ossia valore nullo )

#====================================================================================================================================================
#Restituzione del valore (return):

'''La funzione restituisce True se la stringa è un palindromo, altrimenti False. 
Questo dà maggiore flessibilità rispetto al codice senza funzione, che stampa direttamente il risultato.
Separazione della logica e dell'output:
'''

'''
La funzione si occupa solo di verificare il palindromo.
La logica per stampare il risultato (E PALINDROMO o NON PALINDROMO) viene separata e gestita nel codice principale.
'''




#============================================================================================================================
# Definisce una funzione `palindromo` che verifica se la stringa `a` è un palindromo.
# Un palindromo è una stringa che si legge uguale da sinistra a destra e da destra a sinistra.

def palindromo(a):
    n = len(a)  
    
    '''len(a):
La funzione integrata len() restituisce il numero 
di caratteri in una stringa. Nel caso della stringa a,
len(a) indica quanti caratteri contiene la stringa.'''

    # Calcola la lunghezza della stringa `a` e la salva nella variabile `n`.

   
    # Inizializza una variabile `i` a 0, che rappresenta l'indice corrente da cui si inizia il confronto.

    # Avvia un ciclo `while` che esamina i caratteri della stringa `a` dall'inizio e dalla fine:
    while i < n / 2 and a[i] == a[n - 1 - i]:
        # Condizione 1: `i < n/2` → Continua il ciclo finché `i` è nella prima metà della stringa.
        # Condizione 2: `a[i] == a[n-1-i]` → Verifica che il carattere all'indice `i` sia uguale
        # al carattere corrispondente dalla fine (`n-1-i`).
        
        i += 1
        # Incrementa l'indice `i` per passare al carattere successivo.

    # Dopo il ciclo, verifica se il confronto tra i caratteri è fallito:
    if a[i] != a[n - 1 - i]:
        # Se il carattere corrente da sinistra (`a[i]`) non corrisponde al carattere corrente da destra
        # (`a[n-1-i]`), significa che la stringa non è un palindromo.
        return False
        # Restituisce `False` perché la stringa non è un palindromo.

    # Se il ciclo termina senza trovare disuguaglianze, la stringa è un palindromo.
    return True
    # Restituisce `True` per indicare che la stringa è un palindromo.


# Testa la funzione `palindromo` con l'input '012Kayak210'.
# Nota: la stringa contiene numeri e lettere maiuscole/minuscole, quindi il confronto è case-sensitive.

print(palindromo('012Kayak210'))
# Stampa il risultato: `False`, perché '012Kayak210' non è un palindromo.


'''
La versione con def è più strutturata, riutilizzabile e separa la logica del controllo dal resto del programma.
Permette di estendere e migliorare il codice in modo semplice senza modificarlo pesantemente.
'''

#=======================================================================================================================================================

# A DIFFERENZA DI PRIMA CI SONO UN IF ED UN ELSE CHE FANNO IL CONTRARIO DELLA OPZIONEW PRECEDENTE :def palindromo(a):  

    # Definizione della funzione `palindromo`, che verifica se una stringa `a` è un palindromo.
    # Un palindromo è una stringa che si legge uguale da sinistra a destra e da destra a sinistra.
def PALINDROMO(a):
    n = len(a)  
    # Calcola la lunghezza della stringa `a` e la assegna alla variabile `n`.
    # Questo è necessario per determinare il numero di confronti da effettuare nel ciclo.

    i = 0  
    # Inizializza una variabile `i` a 0. Questa variabile sarà l'indice corrente utilizzato per
    # confrontare i caratteri dalla prima metà della stringa con quelli della seconda metà.

    while i < n/2 and a[i] == a[n-1-i]:  
        # Avvia un ciclo `while` che esegue due controlli:
        # 1. `i < n/2`: Continua il ciclo finché `i` è nella prima metà della stringa.
        # 2. `a[i] == a[n-1-i]`: Verifica che il carattere all'indice `i` sia uguale
        #    al carattere corrispondente dalla fine (`n-1-i`).
        # Se entrambe le condizioni sono vere, il ciclo continua.

        i += 1  
        # Incrementa il valore di `i` per passare al confronto del carattere successivo.

    if a[i] != a[n-1-i]:  
        # Dopo il ciclo, controlla se un confronto ha fallito:
        # Se il carattere corrente da sinistra (`a[i]`) non corrisponde al carattere corrente da destra
        # (`a[n-1-i`), la stringa NON è un palindromo.
        return False  
        # Restituisce `False` per indicare che la stringa non è un palindromo.

    else:  
        # Se il ciclo si conclude senza trovare disuguaglianze,
        # significa che tutti i caratteri corrispondono.
        return True  
        # Restituisce `True` per indicare che la stringa è un palindromo.
        
print(PALINDROMO('012Kayak210'))

#-------------------------------------------------------------------------------------------------------------------------------------------------


a = '0123456789'

print(a[-1]) # indica la posizione precedente 
print(a[1:7])  # slicing
print(a[:7])
print(a[1:])
print(a[:])
print(a[1:7:2]) # slicing con step
print(a[::-1])

# In[]

def palindromo_ingenua( a ):
    return a == a[::-1]





















