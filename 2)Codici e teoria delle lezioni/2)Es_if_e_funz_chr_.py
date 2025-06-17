#Ecco il codice estratto :

a = '   programmazione dei  calcolatori '

i = 0 # indice 
# calcolare il numero di spazi in 'a' a partire dalla posizione 'i'
spaces_from_i = 0

#while a[i + spaces_from_i] == ' ' and i + spaces_from_i < len(a):
# facendo cosi' risulta sbagliato 
# perche la condizione e' dopo
#avendo a che fare con un and, ogni volta che si vuole accedere ad una sequenza 
# bisogna accertarsi che l'indice sempre che l'indice sia all'interno del range ammessibile


'''viene utilizzato per iterare su una sequenza (come una lista, una stringa o una tupla)
  finché l'indice i è minore della lunghezza di quella sequenza. Questo controllo garantisce 
  che il ciclo non vada oltre i limiti della sequenza, evitando errori come IndexError.

Dettaglio del controllo
len(a): Restituisce la lunghezza della sequenza a, ovvero il numero totale di elementi.
i < len(a): Verifica che l'indice i sia inferiore alla lunghezza della sequenza. Quando i raggiunge la lunghezza della sequenza, significa che tutti gli elementi sono stati visitati, quindi il ciclo termina.
Esempio
Ecco un esempio pratico:

python
Copia codice
a = [10, 20, 30, 40, 50]  # Una lista con 5 elementi
i = 0  # Indice iniziale

while i < len(a):  # Continua finché l'indice i è minore della lunghezza della lista
    print(a[i])  # Stampa l'elemento corrente della lista
    i += 1  # Incrementa l'indice di 1 per passare all'elemento successivo
Perché è importante?
Evitare errori: Se non controllassimo la lunghezza della sequenza, potremmo cercare di accedere a un indice non valido, causando un errore.
Accesso sequenziale: Questo controllo permette di visitare ogni elemento della sequenza esattamente una volta.
Cosa accade quando i == len(a)?
Quando i raggiunge il valore di len(a):

La condizione i < len(a) diventa falsa.
Il ciclo while termina e il controllo passa al codice successivo.
  '''
while i < len(a): # una volta che i va fuori la lunghezza dell'indice di a, esce fuori 
  
  while i + spaces_from_i < len(a) and a[i + spaces_from_i] == ' ' : #si fa cosi' risparmiamo una variaabile 
        # - Controlla se il carattere nella posizione `i + spaces_from_i` è uno spazio (`' '`).
    # - Se lo è, incrementa il contatore `spaces_from_i`.
        
        # Incrementa il contatore `spaces_from_i` per ogni spazio trovato consecutivamente.
    spaces_from_i += 1
    spaces = spaces_from_i 
    # Sposta `i` in avanti di `spaces_from_i + 1` per passare oltre gli spazi contati.
  i += spaces_from_i + 1

    # Stampa il numero di spazi consecutivi trovati.
print('ecco i riss. e di :', spaces_from_i)

#-----------------------------------------------------------------------------------------------------------------------------

# **Cosa fa questo codice?**

#1. **Inizializzazione della stringa `a`:**
'''
   a = ' programmazione dei  calcolatori '
   '''
   #- La stringa `a` contiene spazi iniziali, intermedi e finali.
   #- Il compito è contare quanti spazi consecutivi ci sono a partire dall'indice `i` (inizialmente `0`).

#2. **Inizializzazione della variabile `spaces_from_i`:**
'''
   spaces_from_i = 0
   '''
   #- Questa variabile tiene il conto degli spazi consecutivi trovati a partire dalla posizione `i`.

#3. **Ciclo `while`:**
'''
   while a[i + spaces_from_i] == ' ':
       spaces_from_i += 1
   '''
  # - Controlla se il carattere nella posizione `i + spaces_from_i` è uno spazio (`' '`).
  # - Se lo è, incrementa il contatore `spaces_from_i`.
  # - Il ciclo si interrompe non appena incontra un carattere che non è uno spazio.

#4. **Stampa del risultato:**
'''python
   print(spaces_from_i)
   '''
  # - Dopo il ciclo, il programma stampa il numero di spazi consecutivi a partire dall'indice `i`.



# **Cosa cambia con la casistica?**

#La casistica si riferisce alla posizione iniziale (`i`) e al contenuto della stringa `a`.
# Cambia il risultato del programma in base a:

#1. **Posizione `i`:**
   #- Se `i = 0`, il programma conta gli spazi all'inizio della stringa.
  # - Se `i` è impostato a una posizione diversa, il programma conterà gli spazi
  # consecutivi a partire da quella posizione.

#2. **Contenuto di `a`:**
  # - Se la stringa `a` non contiene spazi consecutivi dopo la posizione iniziale `i`, il risultato sarà `0`.
  # - Se ci sono più spazi consecutivi, il risultato sarà pari al numero di spazi.


# **Esempi di comportamento**

# Caso 1: `a = ' programmazione dei  calcolatori '` e `i = 0`
#- **Stringa:** `' programmazione dei  calcolatori '`
#- **Posizione iniziale:** `i = 0`
#- **Spazi consecutivi:** 1 (solo lo spazio iniziale).

'''**Output:**

1
'''

# Caso 2: `a = ' programmazione dei  calcolatori '` e `i = 19`
#- **Stringa:** `' programmazione dei  calcolatori '`
#- **Posizione iniziale:** `i = 19` (dove iniziano gli spazi consecutivi dopo "dei").
#- **Spazi consecutivi:** 2.
'''
**Codice modificato:**
i = 19
spaces_from_i = 0
while a[i + spaces_from_i] == ' ':
    spaces_from_i += 1
print(spaces_from_i)
'''

#**Output:**
#2

# Caso 3: Nessuno spazio consecutivo a partire da `i`
#- Se `i` punta a una posizione senza spazi consecutivi, il ciclo non viene eseguito e il risultato sarà `0`.



# **Vantaggi del codice**
#- **Efficienza:** Conta gli spazi consecutivi senza dover scorrere l'intera stringa.
#- **Flessibilità:** Può essere adattato per contare spazi da una posizione arbitraria.

#------------------------------------------------------------------------------------------------------------------------------
a = ' programmaaaaazioni dei compilatori LLLL'
vocali = 0 

i = 0 


'''Cosi'  e' come sara' il codice sensa l'if '''


# Supponiamo che 'a' sia una sequenza (ad esempio una stringa o una lista).
# Questo codice conta i gruppi consecutivi di vocali in 'a' e si sposta oltre di conseguenza.

while i < len(a):  # Finché l'indice i è minore della lunghezza di 'a', il ciclo continua.
    vocali_i = 0  # Inizializza un contatore per il numero di vocali consecutive a partire da i.

    # Questo ciclo interno esplora le vocali consecutive a partire dalla posizione i.
    while i + vocali_i < len(a) and a[i + vocali_i] in 'aeiou':  
        # Controlla:
        # 1. Che l'indice corrente (i + vocali_i) non vada fuori dai limiti della sequenza.
        # 2. Che l'elemento corrente in 'a' sia una vocale (appartenente a 'aeiou').
        vocali_i += 1  # Incrementa il contatore per ogni vocale trovata.

    # Dopo aver contato le vocali consecutive, memorizza il numero nel contatore 'vocali'.
    vocali = vocali_i  

    # Sposta l'indice 'i' avanti di vocali_i + 1.
    # Si sposta oltre il gruppo di vocali consecutive e salta un ulteriore elemento.
    i += vocali_i + 1  

# Stampa il numero di vocali consecutive trovate nell'ultimo gruppo analizzato.
print('ecco i ris. e di :', vocali_i)  # Nota: sembra esserci un errore di battitura su 'vocaali_i'.

#----------------------------------------------------------------------------------------------------------------------------------

'''Cosi e' come sara' il codice con l'if '''
#facendo cosi' avranno delle ritondanze, possono essere sostituite per semplificare il codice 


# Inizializza la stringa 'a' che verrà analizzata.
# Questa stringa contiene parole con lettere, spazi e diverse vocali.
a = ' programmaaaaazioni dei compilatori LLLL'

# Inizializza il contatore 'vocali' a 0.
# Questo contatore servirà a tenere traccia del numero totale di vocali presenti nella stringa.
vocali = 0  

# Inizializza l'indice 'i' a 0 per iniziare a esaminare la stringa dal primo carattere.
i = 0  

# Avvia un ciclo 'while' che si ripete finché 'i' è minore della lunghezza della stringa 'a'.
while i < len(a):  
    # Controlla se il carattere corrente (a[i]) è una vocale.
    # La condizione verifica se il carattere è uno tra 'a', 'e', 'i', 'o', 'u'.
    if a[i] in 'aeiou':
        # Se il carattere è una vocale, incrementa il contatore 'vocali' di 1.
        vocali += 1  
    
    # Incrementa l'indice 'i' di 1 per passare al carattere successivo.
    i += 1  

# Dopo aver terminato l'analisi della stringa, stampa il numero totale di vocali trovate.
# 'vocali' contiene il risultato finale del conteggio.
print('ecco i ris. e di :', vocali)


#----------------------------------------------------------------------------------------------------------------------------------

# ci sono diverse forme dell'if tra cui l'elif 


'''
if cod 0 
  blocco0 
elif cod1
  blocco1
elif cod2
  blocco3 
else 
  blocco default 
  
# si puo anche fare :
if  cod0 
    blocco0
else:
    blocco1
if cod0 
  blocco0
elif cod1:
  blocco1
  
  
'''
# elif serve una  volta che il programma si bloccato prende in considerazione l'opzione dopo 

#--------------------------------------------------------------------------------------------------------------------------

# Inizializza la stringa 'a', che verrà analizzata per contare il numero di vocali.
# Questa stringa contiene parole e caratteri, alcuni dei quali sono vocali.
a = 'programmazioooneee dei compliatori'

# Inizializza il contatore 'vocali' a 0.
# Questo contatore tiene traccia del numero totale di vocali trovate nella stringa.
vocali = 0  

# Avvia un ciclo 'for' per iterare su ogni carattere della stringa 'a'.
# Ogni carattere della stringa viene assegnato alla variabile 'x' in ogni iterazione.
for x in a:
    # Controlla se il carattere corrente ('x') è una vocale.
    # La condizione verifica se 'x' è uno dei caratteri nella stringa 'aeiou'.
    if x in 'aeiou':
        # Se il carattere è una vocale, incrementa il contatore 'vocali' di 1.
        vocali += 1  

# Dopo che il ciclo 'for' ha analizzato tutti i caratteri della stringa, stampa il numero totale di vocali trovate.
print('ecco le vocali :', vocali)



#================================================================================================================================
#Es  1.3

a = 'programmazioooneee dei compliatori447790'

# stampa a ed evidenzia con * le vocali e con # le 
#  cifre decimali 
#
# pr0grammazione del compilatori 
# # * * ## * *# # # * * #
#

# Inizializza la stringa vuota 'b'.
# Questa stringa verrà utilizzata per costruire una rappresentazione modificata di 'a',
# dove vocali, numeri e altri caratteri saranno sostituiti rispettivamente con '*', '#', e spazi doppi.
b = ''  

# Avvia un ciclo 'for' per iterare su ogni carattere della stringa 'a'.
# Ogni carattere della stringa viene assegnato alla variabile 'x' in ogni iterazione.
for x in a:
    # Controlla se il carattere corrente ('x') è una vocale (maiuscola o minuscola).
    # 'aeiouAEIOU' include tutte le vocali in entrambe le casse.
    if x in 'aeiouAEIOU':  
        b += '*'  # Sostituisce ogni vocale con un asterisco (*) e aggiunge il risultato a 'b'.
    
    # Controlla se il carattere corrente è un numero (digit).
    # Questo confronto funziona confrontando il valore ASCII dei caratteri tra '0' e '9'.
    # Alternativamente, si potrebbe usare `x in '0123456789'` per ottenere lo stesso risultato.
    
    elif x >= '0' and x <= '9':   # controllerebbe ogni volta ogni singolo indice 
        #(deve essere maggiore o uguale a 0  e minore di 9   )

        b += '#'  # Sostituisce ogni cifra numerica con un cancelletto (#) e lo aggiunge a 'b'.

    # Per tutti gli altri caratteri (consonanti, spazi, simboli, ecc.),
    # aggiunge due spazi alla stringa 'b' come rappresentazione.
    else:  
        b += '  '  # Sostituisce il carattere con due spazi e lo aggiunge a 'b'.

# Dopo aver elaborato l'intera stringa 'a', stampa l'originale e la stringa modificata 'b'.
print(a)  # Stampa la stringa originale.
print(b)  # Stampa la stringa modificata con sostituzioni.

#------------------------------------------------------------------------------------------------------------------------------------------------



# Usa la funzione ord() per ottenere il valore ASCII/unicode del carattere 'a'.
# ord() restituisce un intero che rappresenta il codice Unicode del carattere.
print(ord('a'), ord('b'))  # Stampa i codici ASCII/unicode dei caratteri 'a' e 'b'.

# Stampa i codici ASCII/unicode dei caratteri maiuscoli 'A' e 'B'.
# Nota che i codici delle lettere maiuscole sono diversi e più bassi rispetto alle lettere minuscole.
print(ord('A'), ord('B'))

# Stampa i codici ASCII/unicode dei caratteri numerici '0' e '1'.
# Anche i numeri rappresentati come caratteri hanno un codice specifico nel set ASCII/unicode.
print(ord('0'), ord('1'))

'''Cosa fa ord()?
La funzione ord() in Python restituisce il valore Unicode 
(o codice ASCII per i caratteri compresi tra 0 e 127) di un singolo carattere passato come argomento.'''

#Dettagli:
'''Ogni carattere ha un valore numerico associato secondo lo standard Unicode.
Questo valore numerico è chiamato codice del carattere o code point. '''
#Ad esempio:
#'a' → codice Unicode: 97
#'A' → codice Unicode: 65
#'0' → codice Unicode: 48



#====================================================================================================================
#Cosa fa chr()?
#La funzione chr() fa l'opposto di ord():

# ' Chr 'Restituisce il carattere associato al codice Unicode passato come argomento.
#chr() viene usato per convertire un numero intero in un carattere.

print(chr(97))  # Restituisce 'a'
print(chr(65))  # Restituisce 'A'
print(chr(48))  # Restituisce '0'



#=======================================================================================================================================

'''  Come vengono utilizzati ord() e chr()? '''
#Conversione tra caratteri e numeri:

#ord() viene usato per convertire un carattere in un numero intero.
#chr() viene usato per convertire un numero intero in un carattere.

#Operazioni sui caratteri:

'''Puoi fare operazioni matematiche sui caratteri trattandoli come numeri: '''
# Spostare una lettera avanti di una posizione nell'alfabeto
print(chr(ord('a') + 1))  # Output: 'b'

''' Verifica e confronto di caratteri: '''
#Sapendo che i caratteri hanno codici numerici ordinati, è possibile confrontarli facilmente:


print('a' > 'A')  # True perché il codice Unicode di 'a' (97) è maggiore di 'A' (65)

#Manipolazione di stringhe e cifre:

''' Puoi verificare se un carattere è una cifra controllando il suo codice: '''

def is_digit(char):
    return ord('0') <= ord(char) <= ord('9')  # True se il carattere è tra '0' e '9'

print(is_digit('5'))  # Output: True


#==============================================================================================================================


































  
  
  














