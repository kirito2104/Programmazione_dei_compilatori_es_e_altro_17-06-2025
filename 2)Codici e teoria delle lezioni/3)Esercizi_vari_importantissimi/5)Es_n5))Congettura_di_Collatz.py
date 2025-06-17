

# Esercizio 3: La Congettura di Collatz

'''
# La Congettura di Collatz è una congettura matematica tuttora irrisolta.
# Fu enunciata per la prima volta nel 1937 da Lothar Collatz, da cui prende il nome.

# La congettura riguarda il seguente algoritmo:
# 1. Si prende un intero positivo `n`.
# 2. Se `n == 1`, l'algoritmo termina.
# 3. Se `n` è pari, si divide per due → `n = n / 2`.
# 4. Se `n` è dispari, si moltiplica per `3` e si aggiunge `1` → `n = 3 * n + 1`.

# La congettura di Collatz asserisce che questo algoritmo giunge sempre a termine, 
# indipendentemente dal valore di partenza.
'''

# Obiettivo dell'esercizio:
'''
# Scrivere una funzione che, dato un intero `n` in input, restituisce il numero di 
# iterazioni necessarie affinché l'algoritmo termini, ovvero il numero di passaggi 
# richiesti affinché `n` diventi `1`.
'''

# Esempio di esecuzione:

'''
# Se `n = 6`, allora abbiamo la seguente successione:
# 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Numero totale di iterazioni = 8
'''


# Suggerimenti per risolvere l'esercizio:
'''
# - Definire una funzione `collatz(n)` che prende un intero `n` come input.
# - Inizializzare un contatore `count = 0` per contare il numero di iterazioni.
# - Usare un ciclo `while` che esegue l'algoritmo finché `n != 1`:
#   - Se `n` è pari, dividerlo per 2.
#   - Se `n` è dispari, moltiplicarlo per 3 e aggiungere 1.
#   - Incrementare il contatore `count` a ogni iterazione.
# - Alla fine, restituire `count` come numero di iterazioni totali.
'''


'''
=========================================================================================================================================================================
'''
##### **Consigli per risolvere l'esercizio senza aiuti** #####

# 1. **Comprendere la logica della Congettura di Collatz**  
#    - Si parte con un numero intero positivo `n`.
#    - Se `n == 1`, l'algoritmo si ferma.
#    - Se `n` è pari, lo si divide per 2 → `n = n / 2`.
#    - Se `n` è dispari, lo si moltiplica per 3 e si aggiunge 1 → `n = 3 * n + 1`.
#    - Il processo continua fino a raggiungere `n = 1`.
#    - L’obiettivo è contare il numero di passaggi (iterazioni) necessari per arrivare a `1`.

# 2. **Scomporre il problema in passi chiari**  
#    - Devi creare una funzione che accetta un numero `n`.
#    - Devi ripetere il processo di trasformazione fino a ottenere `n = 1`.
#    - Ad ogni passo, devi contare quante trasformazioni avvengono.
#    - Alla fine, restituisci il numero totale di iterazioni.

# 3. **Struttura generale dell’algoritmo**  
#    - Devi usare un **ciclo** per continuare a trasformare `n` finché non diventa `1`.
#    - Devi usare una **variabile contatore** per tenere traccia delle iterazioni.
#    - Devi usare una **struttura condizionale** (`if`) per decidere se `n` è pari o dispari.

##### **Pseudo-codifica dell’algoritmo** #####

# Definire la funzione `collatz(n)`, dove `n` è il numero iniziale
# Creare una variabile `count = 0` per tenere traccia del numero di iterazioni
# Finché `n` non è uguale a 1:
#     a. Se `n` è pari:
#         - Dividere `n` per 2
#     b. Altrimenti (se `n` è dispari):
#         - Moltiplicare `n` per 3 e aggiungere 1
#     c. Aumentare il contatore `count` di 1
# Restituire `count` come numero totale di iterazioni

##### **Esempio passo-passo per `n = 6`** #####

# Vediamo come si evolve la sequenza e come contiamo le iterazioni:
# 1. `n = 6`  (pari)   → `n = 6 / 2 = 3`, iterazioni = 1  
# 2. `n = 3`  (dispari)→ `n = 3 * 3 + 1 = 10`, iterazioni = 2  
# 3. `n = 10` (pari)   → `n = 10 / 2 = 5`, iterazioni = 3  
# 4. `n = 5`  (dispari)→ `n = 5 * 3 + 1 = 16`, iterazioni = 4  
# 5. `n = 16` (pari)   → `n = 16 / 2 = 8`, iterazioni = 5  
# 6. `n = 8`  (pari)   → `n = 8 / 2 = 4`, iterazioni = 6  
# 7. `n = 4`  (pari)   → `n = 4 / 2 = 2`, iterazioni = 7  
# 8. `n = 2`  (pari)   → `n = 2 / 2 = 1`, iterazioni = 8  

# Numero di iterazioni totali = **8**.

##### **Suggerimenti per scrivere il codice** #####

# - Usa un **ciclo `while`** per ripetere il processo finché `n != 1`.
# - Usa un **contatore (`count`)** per registrare il numero di passaggi.
# - Usa un **`if`** per controllare se `n` è pari o dispari.
# - Assicurati che la funzione restituisca il valore corretto.

# 💡 **Ora puoi provare a scriverlo senza guardare codice di esempio!** 🚀


'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

#Esercizio 3 

'''
La Congettura di Collatz è una congettura matematica tuttora irrisolta. 
Fu enunciata per la prima volta nel 1937 da Lothar Collatz, da cui prende il nome.

La congettura riguarda il seguente algoritmo:

- Si prende un intero positivo `n`.
- Se `n == 1`, l'algoritmo termina.
- Se `n` è pari, si divide per due; altrimenti si moltiplica per `3` e si aggiunge `1`.

La congettura di Collatz asserisce che questo algoritmo giunge sempre a termine, 
indipendentemente dal valore di partenza.

Scrivere una funzione che, dato un intero `n` in input, restituisce il numero di iterazioni 
necessarie affinché l'algoritmo termini, cioè dopo quante iterazioni risulta `n = 1`.
'''

#Esempio: per `n = 6`, allora abbiamo la successione:

#6, 3, 10, 5, 16, 8, 4, 2, 1

#Dunque l'algoritmo termina dopo `8` iterazioni.

#questo e' lo psudo codice :
'''
def conggettura di Collatz ( n ):
     n = int (input("inserisci numero da verificare ))
    iterazioni  = 0 
    while n > 1  : 
         se n%2 == 0 e' possitivo
            print("il num e' positivo ) 
            n=n//2
        altrimenti : 
            n = 3*n+1
        stampa (n,end=" ,")
        iterazioni +=1
        print("")
    return iterazioni 
    
'''

##### **Perché è stato usato `end=' '` invece di `break` e perché c'è il `print("")`?** #####

'''
# 1 **Perché `end=' '` invece di `break`?**
# '''
# - La differenza tra `end=' '` e `break` è che hanno funzioni completamente diverse:
#   - `end=' '` viene usato in `print()` per controllare la formattazione dell'output, evitando di andare a capo dopo ogni numero stampato.
#   - `break` invece interrompe l'esecuzione del ciclo `while` o `for`.

'''- Se avessimo usato `break`, il codice si sarebbe fermato immediatamente dopo la prima iterazione! '''
# - Con `end=' '`, il programma continua a stampare i numeri della sequenza di Collatz sulla stessa riga.

##### **Esempio di comportamento** #####

# Con `end=' '`:
# for i in range(5):
#     print(i, end=' ')
# Output:
# 0 1 2 3 4 
# (Tutti i numeri vengono stampati sulla stessa riga con uno spazio tra di loro.)

# Se avessimo usato `break`:
# for i in range(5):
#     print(i)
#     break
# Output:
# 0
# (Il ciclo si ferma subito dopo aver stampato `0` perché `break` interrompe l'esecuzione.)

''' `end=' '` è usato per formattare l'output, mentre `break` interromperebbe il ciclo prematuramente, cosa che non vogliamo. '''

'''
# 2**Perché c'è il `print("")`?**
'''
# - Il comando `print("")` viene usato per stampare una riga vuota alla fine dell'output.
''' - Il suo scopo è quello di: '''
#   1. **Andare a capo dopo aver stampato tutta la sequenza**, evitando output disordinati.
#   2. **Separare l'output da eventuali altre stampe successive**, migliorando la leggibilità.

'''
##### **Esempio di comportamento** #####
# '''

# Senza `print("")`:
# print(6, end=' ')
# print(3, end=' ')
# print(10, end=' ')
# print("Fine del programma")
# Output:
# 6 3 10 Fine del programma
# (La frase "Fine del programma" appare subito dopo il numero 10, senza andare a capo.)

# Con `print("")`:
# print(6, end=' ')
# print(3, end=' ')
# print(10, end=' ')
# print("")
# print("Fine del programma")
# Output:
# 6 3 10 
# Fine del programma
# (Ora la frase "Fine del programma" appare su una nuova riga, migliorando la leggibilità.)

'''
##### **🔍 Conclusione** #####
'''

# - **`end=' '`** è usato per stampare i numeri della sequenza sulla stessa riga con spazi tra di loro, invece di andare a capo dopo ogni numero.
# - **`break` non avrebbe senso in questo contesto**, perché fermerebbe il ciclo immediatamente.
# - **`print("")`** viene usato per andare a capo alla fine, migliorando la formattazione dell'output.


'''
=====================================================================================================================================================================
==========================================================================================================================================================================
'''

#Esecuzione esercizio 3 
'''
La Congettura di Collatz è una congettura matematica tuttora irrisolta. 
Fu enunciata per la prima volta nel 1937 da Lothar Collatz, da cui prende il nome.
'''
#La congettura riguarda il seguente algoritmo:

#- Si prende un intero positivo `n`.
#- Se `n == 1`, l'algoritmo termina.
#- Se `n` è pari, si divide per due; altrimenti si moltiplica per `3` e si aggiunge `1`.
'''
La congettura di Collatz asserisce che questo algoritmo giunge sempre a termine, 
indipendentemente dal valore di partenza.

Scrivere una funzione che, dato un intero `n` in input, restituisce il numero di iterazioni 
necessarie affinché l'algoritmo termini, cioè dopo quante iterazioni risulta `n = 1`.
'''

#Esempio: per `n = 6`, allora abbiamo la successione:

#6, 3, 10, 5, 16, 8, 4, 2, 1

#Dunque l'algoritmo termina dopo `8` iterazioni.



# ''' Definizione della funzione per la Congettura di Collatz '''
def Congettura_di_collatz(n):
    
    # ''' Inizializzazione della variabile contatore '''
    # Questa variabile tiene traccia del numero di iterazioni necessarie
    # per ridurre il numero `n` a 1 seguendo la sequenza di Collatz.
    iterazioni = 0 

    # ''' Ciclo per generare la sequenza di Collatz '''
    # Continua ad eseguire le operazioni finché `n` non diventa 1.
    while n > 1:
        
        # ''' Controllo se il numero è pari '''
        if n % 2 == 0:
            # Se `n` è pari, lo dividiamo per 2
            # Usiamo `//` per assicurarci che il risultato sia un numero intero.
            n = n // 2  
        else:  
            # ''' Caso in cui il numero è dispari '''
            # Se `n` è dispari, applichiamo la regola `3n + 1`
            n = 3 * n + 1  
        
        # ''' Stampa il valore corrente della sequenza '''
        # Usiamo `end=" , "` per stampare i valori sulla stessa riga, separati da una virgola.
        print(n, end=" , ")  

        # ''' Incremento del contatore delle iterazioni '''
        # Ad ogni passaggio, aumentiamo il numero di trasformazioni effettuate.
        iterazioni += 1  

    # ''' Restituzione del numero totale di iterazioni '''
    # Questo valore indica quante volte è stato modificato `n` prima di raggiungere `1`.
    return iterazioni  


# ''' Richiesta dell'input all'utente '''
# Viene richiesto un numero intero positivo da verificare con la Congettura di Collatz.
n = int(input("Inserisci un numero da verificare: "))

# ''' Chiamata della funzione e memorizzazione del risultato '''
# La funzione viene eseguita sul numero inserito, e il numero di iterazioni viene memorizzato in `s`.
s = Congettura_di_collatz(n)

# ''' Stampa del risultato finale '''
# Dopo aver stampato la sequenza, viene mostrato il numero totale di iterazioni necessarie.
print('\nNumero di iterazioni: ', s)














#questo e' lo psudo codice :
'''
def conggettura di Collatz ( n ):
     n = int (input("inserisci numero da verificare ))
    iterazioni  = 0 
    while n > 1  : 
         se n%2 == 0 e' possitivo
            print("il num e' positivo ) 
            n=n//2
        altrimenti : 
            n = 3*n+1
        stampa (n,end=" ,")
        iterazioni +=1
        print("")
    return iterazioni 
    
'''







