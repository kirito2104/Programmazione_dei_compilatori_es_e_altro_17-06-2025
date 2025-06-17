

# Esercizio 1: Scrivi un programma che chiede all'utente di inserire un numero
# intero. Continua a chiedere all'utente di inserire un numero finché non viene
# inserito un numero pari.

while True:  # Avvia un ciclo infinito che continuerà a ripetersi finché non viene interrotto.
    numero = int(input('inserisci un numero intero:'))  # Chiede all'utente di inserire un numero intero e lo converte in un valore di tipo int.
    
    if numero % 2 == 0:  # Controlla se il numero è pari. 
         #Un numero è pari quando il resto della divisione per 2 è uguale a 0.
       
        break  # Se il numero è pari (la condizione è vera), il ciclo si interrompe grazie all'istruzione 'break'.
    else:
        print('numero dispari, rifare')  # Se il numero è dispari (la condizione è falsa), stampa un messaggio per chiedere all'utente di riprovare.

'''questo programma avvia un ciclo infinito che finche' la condizione posta nell' if non e'  vera ossia che il numero 
e pari, ritorna sopra e lo richiede , con break permette nel caso in cui e' vera interrompe il programma   
'''


#----------------------------------------------------------------------------------------------------------------------------
#Esercizio 2: Scrivi un programma che stampa i numeri da 1 a 100.

numero = 1 

while numero <= 100:
   print(numero)
   numero += 1 

'''facendo cosi' stampaera' i numeri fino a 100'''

#-----------------------------------------------------------------------------------------------------------------------------------

#Esercizio 3: Scrivi un programma che chiede all'utente di inserire un numero
#intero. Continua a chiedere all'utente di inserire un numero finché non viene
#inserito un numero multiplo dj 3

while True :
    numero = int (input('inserire unmultiplo di 3 :'))
    if numero % 3 == 0: # a differenza di prima l differenza e' che cambia il multiplo ossia 3
        break # permette di interrompere il programma, quando il multiplo e'stato trovato
    else :
        print('numero non multiplo di 3, rifare') 

'''cio' permettera'    '''
#-----------------------------------------------------------------------------------------------------------------------------------


#Esercizio 4: Scrivi un programma che chiede al'utente di inserire una
#parola. Continua a chiedere all'utente di inserire una parola finché la parola
#inserita non è "ciao",

flag = True  # Inizializza una variabile booleana 'flag' a True, utilizzata per controllare l'esecuzione del ciclo.
while flag:  # Avvia un ciclo 'while' che continua finché 'flag' è True.
    flag = False  # Imposta 'flag' a False all'inizio del ciclo, per evitare loop infiniti se non viene cambiato successivamente.
    parola = input('inserisci parola ')  # Richiede all'utente di inserire una parola.

    if parola == 'ciao':  # Controlla se la parola inserita è uguale a 'ciao'.
        break  # Se la parola è 'ciao', interrompe l'esecuzione del ciclo usando 'break'.
    else:
        print('la lettera non e ciao, inserire una nuova parola')  # Se la parola non è 'ciao', stampa un messaggio per chiedere un nuovo input.
        flag = True  # Reimposta 'flag' a True per continuare l'esecuzione del ciclo.



#-----------------------------------------------------------------------------------------------------------------------------------


#Esercizio 5. Scrivi un/ programma che stampa i numeri pari da 1 a  100.

numero = 1  # Inizializza la variabile 'numero' con il valore 1

while numero <= 100:  # Avvia un ciclo 'while' che continua finché 'numero' è minore o uguale a 100
    if numero % 2 == 0:  # Controlla se 'numero' è pari. Un numero è pari se il resto della divisione per 2 è uguale a 0
        print(numero)  # Se 'numero' è pari, viene stampato a schermo
    numero += 1  # Incrementa il valore di 'numero' di 1 a ogni iterazione


#------------------------------------------------------------------------------------------------------------------------------------
#Esercizio 6: Scrivi un programma che chiede all'utente di inserire una
#lettera. Continua a chiedere all'utente di inserire una lettera finché Ia lettera
#inserita non è una vocale.


while True :
    lettera = input('inserisci una lettera: '). lower()  # Convertiamo in minuscolo per uniformità
    
    if lettera not in 'aeiou':  # Controlliamo se la lettera non è una vocale
        print("lettera torvovata")  # Stampiamo un messaggio se la lettera non è una vocale
        break    # Usciamo dal ciclo se la condizione è soddisfatta
    # Se l'input è una vocale
    else : # Messaggio per informare che l'input è una vocale
        print(" la lettera inserita non e` una vocale, riprova")
        
        
''' In quest'altro codice qui sotto ho aggiunto una parte dove controlla se nel programma c'e piu di una lettera, in caso lo sia richiede di inserirla nuovamente
        ho messo questa parte del codice sopra al controllo che non sia una vocale la lettera  '''

# Iniziamo un ciclo infinito che continuerà finché non si soddisfano le condizioni richieste
while True:
    # Chiediamo all'utente di inserire una lettera
    lettera = input("Inserisci una lettera: ").lower()  # Convertiamo in minuscolo per uniformità

    # Controlliamo se l'input contiene più di una lettera
    if len(lettera) > 1:
        # Messaggio di errore se l'input non è una singola lettera
        print("Hai inserito più di una lettera, riprova.")
        continue  # Ritorna all'inizio del ciclo per chiedere di nuovo

    # Controlliamo se la lettera non è una vocale
    if lettera not in 'aeiou':
        # Stampiamo un messaggio se la lettera non è una vocale
        print("Lettera trovata (non è una vocale).")
        break  # Usciamo dal ciclo se la condizione è soddisfatta

    # Se l'input è una vocale
    else:
        # Messaggio per informare che l'input è una vocale
        print("La lettera inserita è una vocale, riprova.")


# Dettagli sul funzionamento del codice:
'''
1. **Ciclo `while True`:**
   - Viene utilizzato per mantenere il programma attivo finché l'utente non soddisfa la condizione di uscita (`break`).
   
2. **`input()` e `.lower()`:**
   - Chiediamo all'utente di inserire una lettera. La convertiamo in minuscolo per garantire che il confronto non sia influenzato da lettere maiuscole.

3. **Controllo della lunghezza (`len(lettera) > 1`):**
   - Controlliamo se l'utente ha inserito più di una lettera. Se sì, mostriamo un messaggio di errore e usiamo `continue` per ripetere il ciclo.

4. **Controllo vocale (`lettera not in 'aeiou'`):**
   - Se la lettera non è una vocale, consideriamo che l'utente ha trovato una lettera valida e usciamo dal ciclo con `break`.

5. **Gestione delle vocali:**
   - Se l'input è una vocale, mostriamo un messaggio e chiediamo di riprovare.

### Esempio di output:
- **Input:** "a"  
  **Output:** "La lettera inserita è una vocale, riprova."

- **Input:** "bc"  
  **Output:** "Hai inserito più di una lettera, riprova."

- **Input:** "b"  
  **Output:** "Lettera trovata (non è una vocale)."  

'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Esercizio 7: Scrivi un programma che stampa i numeri multipli di 3 e 25
# compresi tra 1 e 1000.

# Inizializza la variabile 'numero' con il valore 1
numero = 1
# Ciclo while che continua finché 'numero' è minore o uguale a 1000
while numero <= 1000:
    # Controlla se 'numero' è divisibile sia per 3 che per 25
    if numero % 3 == 0 and numero % 25 == 0:
        # Stampa il numero se soddisfa entrambe le condizioni
        print(numero)
    # Incrementa il valore di 'numero' di 1 a ogni iterazione del ciclo
    numero += 1

# Stampa un messaggio finale dopo aver trovato tutti i numeri
print('Ecco i numeri')


'''Spiegazione:
Inizializzazione (numero = 1):

La variabile numero viene impostata a 1 come punto di partenza.
Ciclo while:

Il ciclo continua a iterare finché numero è minore o uguale a 1000.
Condizione if:

La riga if numero % 3 == 0 and numero % 25 == 0 verifica due cose:
Se il numero è divisibile per 3 (il resto della divisione per 3 è 0).
Se il numero è divisibile per 25 (il resto della divisione per 25 è 0).
Se entrambe le condizioni sono vere, il numero viene stampato.
Incremento (numero += 1):

Dopo ogni iterazione, il valore di numero viene incrementato di 1, in modo che il ciclo continui a esaminare i numeri successivi.
Messaggio finale:

Dopo che il ciclo while ha terminato (quando numero supera 1000), viene stampato il messaggio 'Ecco i numeri' per indicare che il programma ha completato l'elenco.'''


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Esercizio 8: Scrivi un programma che chiede all’utente di inserire un numero
# intero. Continua a chiedere all'utente di inserire un numero finché non viene
# inserito un numero intero compreso tra 1 e 100.



# Ciclo infinito che continua a eseguire il blocco finché non viene soddisfatta la condizione per uscire
while True: 
    # Chiede all'utente di inserire un numero intero e lo converte in un valore di tipo int
    numero = int(input('Inserisci numero intero: '))
    
    # Controlla se il numero inserito è compreso tra 1 e 100 (inclusi)
    if 1 <= numero <= 100:
        # Se il numero è valido, esce dal ciclo utilizzando il comando 'break'
        break
    else:
        # Se il numero non è valido, informa l'utente e lo invita a riprovare
        print('Riprova, numero non valido!')

'''Spiegazione:
Ciclo infinito while True:

Questo ciclo continuerà a eseguire il blocco di codice al suo interno fino a quando non viene eseguito un break per uscirne.
Input utente:

La funzione input() viene utilizzata per chiedere all'utente di inserire un numero intero.
Il valore inserito viene convertito in un numero intero utilizzando int().
Condizione if:

Il controllo 1 <= numero <= 100 verifica che il numero inserito sia compreso tra 1 e 100, inclusi entrambi i limiti.
Se la condizione è vera, il comando break interrompe il ciclo e il programma prosegue oltre il blocco while.
Blocco else:

Se il numero inserito non rientra nell'intervallo desiderato, viene stampato un messaggio di errore per informare l'utente che il numero non è valido, e il ciclo ricomincia.'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Esercizio 9: Scrivi un programma che chiede all'utente di inserire una
# parola. Continua a chiedere all'utente di inserire una parola finché la parola
# inserita non è lunga almeno 8 caratteri.

# qui controlla la lunghezza della parola inserita con len per poi , dirgli che deve essere ameno piu` di 8 caratteri
# Ciclo infinito che continua a eseguire il blocco finché non viene soddisfatta la condizione per uscire
while True: 
    # Chiede all'utente di inserire una parola
    parola = input('Inserire una parola di almeno 8 caratteri: ')
    
    # Controlla se la lunghezza della parola è maggiore o uguale a 8 caratteri
    
    if len(parola) >= 8:  # Usa la funzione len() per calcolare la lunghezza della parola
        ''' qui controlla la lunghezza della parola inserita con len per poi , dirgli che deve essere ameno piu` di 8 caratteri'''
        # Se la lunghezza è valida, esce dal ciclo utilizzando il comando 'break'
        break 
    else:
        # Se la lunghezza non è valida, informa l'utente che la parola è troppo corta
        print('La parola non è di almeno 8 caratteri, riprovare:')

        '''Spiegazione:
Ciclo infinito while True:

Il ciclo continua a eseguire il blocco finché non viene eseguito un break.
Input utente:

La funzione input() chiede all'utente di inserire una parola. Il valore inserito è una stringa.
Controllo lunghezza (if len(parola) >= 8):

La funzione len(parola) calcola la lunghezza della parola inserita.
La condizione verifica se la lunghezza è maggiore o uguale a 8 caratteri.
Se la condizione è vera, viene eseguito il break, e il ciclo termina.
Blocco else:

Se la condizione non è soddisfatta (cioè, la parola ha meno di 8 caratteri), viene stampato un messaggio per informare l'utente e il ciclo ricomincia.'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







 
