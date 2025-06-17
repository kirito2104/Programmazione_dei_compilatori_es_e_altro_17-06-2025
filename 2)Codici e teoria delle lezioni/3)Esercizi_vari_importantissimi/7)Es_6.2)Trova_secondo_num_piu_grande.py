






#Esercizio
#Scrivere una funzione in Python che, data una lista di numeri, 
# restituisce il secondo numero più grande all'interno della lista.

#Esempio:

#Numeri:  [30, 20, 20, 30, 30, 20]
#Secondo numero più grande:  20


#ecco lo psudo codice del codice : 


'''
# Definizione della funzione per trovare il secondo numero più grande in una lista

def trova_il_numero_piu_grande(numeri):

    # Controlla se la lista ha meno di due elementi
    if len(numeri) < 2:
        print("Riprovare, il codice è errato")  # Stampa un messaggio di errore
        
        return  # Esce dalla funzione per evitare errori successivi

    # Inizializza le variabili per il massimo e il secondo massimo
    pr_max_num = -1  # Il numero più grande trovato finora
    sec_max_num = -1  # Il secondo numero più grande trovato finora

    # Itera attraverso la lista dei numeri
    for num in numeri:  # ⚠️ Era scritto "numero", ma dovrebbe essere "numeri"
    
        if num > pr_max_num:  # Se il numero corrente è maggiore del massimo trovato finora
            sec_max_num = pr_max_num  # Il vecchio massimo diventa il secondo massimo
            pr_max_num = num  # Aggiorna il massimo con il nuovo numero più grande
        elif num > sec_max_num and num != pr_max_num:  # Se è maggiore del secondo massimo e diverso dal primo massimo
            sec_max_num = num  # Aggiorna il secondo massimo

    # Controlla se il secondo massimo è stato aggiornato
    if sec_max_num != -1:  # ⚠️ Qui mancava il valore di confronto
        return sec_max_num  # Restituisce il secondo numero più grande
    else:
        print("Non esiste un secondo numero più grande")  # Stampa un messaggio se non c'è un secondo massimo

        stampa ("non esite un secondo piu' grande ") 
'''


'''
# Per arrivare a scrivere un codice come quello che hai condiviso senza fare copia e incolla,
# segui questi passaggi logici e prova a implementarlo da solo.

# ----------------------------------------------------
# DRITTE PER COSTRUIRE IL CODICE DA ZERO 🚀
# ----------------------------------------------------

# 1. Gestisci il caso in cui la lista ha meno di due elementi
#    - Se la lista ha meno di due numeri, restituisci un messaggio di errore.

# 2. Inizializza due variabili per il massimo e il secondo massimo
#    - Imposta `largest` (il numero più grande) e `second_largest` (il secondo più grande) 
#      a un valore molto basso, ad esempio `-1` o `float('-inf')`.

# 3. Scorri la lista una sola volta (evita di ordinare la lista)
#    - Usa un ciclo `for` per iterare attraverso ogni numero della lista:
#      - Se il numero attuale è maggiore di `largest`, aggiorna sia `largest` che `second_largest` 
#        (spostando il vecchio `largest` in `second_largest`).
#      - Altrimenti, se il numero è maggiore di `second_largest` ma minore di `largest`, 
#        aggiorna solo `second_largest`.

# 4. Verifica se `second_largest` è stato aggiornato
#    - Se `second_largest` è rimasto al valore iniziale (ad esempio `-1` o `float('-inf')`), 
#      significa che non esiste un secondo numero più grande, quindi restituisci un messaggio appropriato.

# ----------------------------------------------------
# DOMANDE GUIDA PER IMPLEMENTARLO DA SOLO 💡
# ----------------------------------------------------

# 1. Come faccio a verificare se ci sono abbastanza numeri nella lista?
#    (Suggerimento: usa `len(numbers) < 2`).

# 2. Come posso inizializzare due variabili per tenere traccia del massimo e del secondo massimo?

# 3. Come aggiorno le variabili `largest` e `second_largest` all'interno di un ciclo `for`?

# 4. Come assicuro che `second_largest` non sia uguale a `largest`?

# 5. Cosa faccio se alla fine del ciclo `second_largest` non è cambiato?

# ----------------------------------------------------
# SFIDA PER TE 🎯
# ----------------------------------------------------

# 1. Scrivi il codice da solo seguendo i passaggi sopra.
# 2. Testalo con diverse liste, ad esempio:
#    - [10, 20, 30] → Dovrebbe restituire 20
#    - [30, 30, 30] → Dovrebbe restituire un messaggio che non esiste un secondo numero più grande
#    - [5] → Dovrebbe restituire un messaggio che non ci sono abbastanza numeri nella lista

# ----------------------------------------------------
# CONSIGLIO FINALE 💡
# ----------------------------------------------------

# Prova a scrivere il codice senza guardare quello che hai fornito! 
# Se hai difficoltà, posso darti suggerimenti mirati senza darti direttamente la soluzione. 💪🚀


'''


# ecco il codice :


def trova_il_numero_piu_grande(numeri):

    # Controlla se la lista ha meno di due elementi
    if len(numeri) < 2:
        print("Riprovare, il codice è errato")  # Stampa un messaggio di errore
        
        return  # Esce dalla funzione per evitare errori successivi

    # Inizializza le variabili per il massimo e il secondo massimo
    pr_max_num = -1  # Il numero più grande trovato finora
    sec_max_num = -1  # Il secondo numero più grande trovato finora

    # Itera attraverso la lista dei numeri
    for num in numeri:  # ⚠️ Era scritto "numero", ma dovrebbe essere "numeri"
    
        if num > pr_max_num:  # Se il numero corrente è maggiore del massimo trovato finora
            sec_max_num = pr_max_num  # Il vecchio massimo diventa il secondo massimo
            pr_max_num = num  # Aggiorna il massimo con il nuovo numero più grande
        elif num > sec_max_num and num != pr_max_num:  # Se è maggiore del secondo massimo e diverso dal primo massimo
            sec_max_num = num  # Aggiorna il secondo massimo

    # Controlla se il secondo massimo è stato aggiornato
    if sec_max_num != -1:  # ⚠️ Qui mancava il valore di confronto
        return sec_max_num  # Restituisce il secondo numero più grande
    else:
        print("Non esiste un secondo numero più grande")  # Stampa un messaggio se non c'è un secondo massimo

        #stampa ("non esite un secondo piu' grande ") 



numeri =[20,30,40,20,20,20,30,30]



sec_max_num = trova_il_numero_piu_grande(numeri)

print("numeri",numeri)
print("ecco il secondo num piu' grande:", sec_max_num)


#===============================================================================================================================================================================================================
#=============================================================================================================================================================================================================================
#===========================================================================================================================================================================================================================
'''
MENTRE NEL CASO IN CUI IL PROGRAMMA QUI SOPRA LO SI VOGLIA ESEGUIRE INSERENDO DEI NUMERI BISOGNERA' FARE COME QUI SOTTO : 
'''


# Utilizzo della struttura `try-except`, della funzione `map()` e del metodo `.split()`

# 🔹 STRUTTURA `try-except`
# La struttura `try-except` viene usata per intercettare e gestire gli errori in modo che il programma non si interrompa bruscamente.
# Se all'interno del blocco `try` si verifica un errore, l'esecuzione passa al blocco `except`, che gestisce l'errore.

try:
    # L'utente inserisce una stringa di numeri separati da spazi
    # La funzione `input()` prende l'input dell'utente sotto forma di stringa
    # Il metodo `.split()` divide la stringa in una lista di sottostringhe
    # `map(int, ...)` converte ogni sottostringa in un intero
    numeri = list(map(int, input("Inserisci una lista di numeri separati da spazio: ").split()))
    
    # Chiamata a una funzione ipotetica che trova il secondo numero più grande
    risultato = trova_il_numero_piu_grande(numeri)
    
    # Se la funzione restituisce un valore valido, lo stampiamo
    if risultato is not None:
        print("Il secondo numero più grande è:", risultato)

# 🔹 ECCEZIONE `ValueError`
# Se l'utente inserisce un valore non numerico, il `map(int, ...)` genera un `ValueError`.
# In questo caso, viene eseguito il blocco `except`, che stampa un messaggio di errore.
except ValueError:
    print("Errore: Assicurati di inserire solo numeri separati da spazio.")

# 🔹 DETTAGLIO SU `map()`
# La funzione `map()` applica una funzione a ogni elemento di un iterabile (es. una lista)
# Nel nostro caso, `map(int, lista_di_stringhe)` converte ogni elemento della lista in un numero intero.
# Il risultato di `map()` è un oggetto iterabile, che viene poi convertito in lista con `list()`.

# Esempio dettagliato:
# Supponiamo che l'utente inserisca: "10 20 30"
#
# Passaggi:
# 1. `input()` riceve la stringa "10 20 30"
# 2. `.split()` la trasforma in lista: ["10", "20", "30"]
# 3. `map(int, ...)` converte ogni elemento in intero: [10, 20, 30]
# 4. `list(map(...))` finalizza la lista trasformata

# 🔹 METODO `.split()`
# `.split()` divide una stringa in una lista di sottostringhe basandosi su un separatore.
# Se non viene specificato alcun argomento, lo spazio viene usato come separatore predefinito.

# Esempio pratico:
stringa = "10 20 30"
lista = stringa.split()
print(lista)  # Output: ["10", "20", "30"]

# 🚀 Vantaggi di questa struttura:
# - Programma più robusto: evita crash dovuti a input errati
# - Conversione diretta dell'input in numeri senza bisogno di iterazioni manuali
# - Maggiore leggibilità e compattezza del codice
















