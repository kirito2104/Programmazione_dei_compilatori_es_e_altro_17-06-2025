
"""
Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori
positivi, escluso sé stesso. Scrivere una funzione che verifichi se un numero è
perfetto oppure no.

"""

# Definiamo una funzione che verifica se un numero è perfetto
def Verifica_Num_Perfetto(n):
    '''
    La funzione accetta un numero intero n e verifica se è perfetto.
    Un numero perfetto è uguale alla somma dei suoi divisori (escluso sé stesso).
    Restituisce True se il numero è perfetto, False altrimenti.
    '''
    # Inizializziamo la variabile che terrà la somma dei divisori
    somma_divisori = 0
    
    # Inizializziamo il contatore che useremo per trovare i divisori
    i = 1 

    # Corretto il ciclo WHILE per scorrere da 1 fino a n//2
    while i <= n // 2:  # ✅ Corretta la condizione: prima era errata
        # Se i è un divisore di n, lo aggiungiamo alla somma
        if n % i == 0:  # n % i restituisce il resto della divisione. Se è 0, significa che i è divisore di n
            somma_divisori += i  # Aggiungiamo i alla somma dei divisori

        # Incrementiamo i per controllare il numero successivo
        i += 1  

    # Se la somma dei divisori è uguale a n, allora n è un numero perfetto
    if somma_divisori == n:
        return True  
    else:
        return False  

# Chiediamo all'utente di inserire un numero intero positivo
n = int(input("inserisci numero intero positiv: "))  

# Verifichiamo se il numero inserito è perfetto chiamando la funzione Verifica_Num_Perfetto()
if Verifica_Num_Perfetto(n):  # Se la funzione restituisce True...
    print("Il numero " + str(n) + " è un numero perfetto.")  
else:
    print("Il numero " + str(n) + " non è un numero perfetto.")  

''' Perché questa correzione?

in non è l'operatore corretto → doveva essere <= per confrontare i con n//2.
n/2 restituisce un float → n // 2 assicura che il valore sia un intero (divisione intera).
I divisori di n sono sempre ≤ n//2, quindi non serve iterare fino a n-1.
'''

###################################################################################################################
'''
Perché usiamo str(n)?
In Python, non puoi concatenare direttamente una stringa e un numero intero (int), perché genererebbe un errore:

Esempio errato:
n = 6
print("Il numero " + n + " è perfetto.")  # ❌ ERRORE: TypeError: can only concatenate str (not "int") to str

Per risolvere questo problema, bisogna convertire n in una stringa con str(n), in modo che Python possa unirlo al resto del testo:

Esempio corretto:
print("Il numero " + str(n) + " è perfetto.")  # ✅ Funziona perfettamente
'''

'''
🔹 Analisi della concatenazione nella stampa del risultato:

print("Il numero " + str(n) + " è un numero perfetto.")

🔸 Parte 1: "Il numero " → È una stringa normale.
🔸 Parte 2: str(n) → Converte il numero n in una stringa, es. str(6) → "6".
🔸 Parte 3: " è un numero perfetto." → È un'altra stringa normale.

Concatenazione finale:
"Il numero " + "6" + " è un numero perfetto."

Risultato finale (se n = 6):
Il numero 6 è un numero perfetto.
'''

# Verifica se il numero è perfetto e stampa il risultato
if Verifica_Num_Perfetto(n):  # Se la funzione restituisce True...
    print("Il numero " + str(n) + " è un numero perfetto.")  
else:
    print("Il numero " + str(n) + " non è un numero perfetto.")  

'''
🔹 Alternative più pulite:
Se vuoi un metodo più leggibile e moderno, puoi usare f-string, che evita l'uso di +:

print(f"Il numero {n} è un numero perfetto.")  # ✅ Più pulito e leggibile

💡 Output se n = 6:
Il numero 6 è un numero perfetto.

Le f-string (f"...") permettono di inserire variabili direttamente dentro la stringa, senza bisogno di str() o +.
Funzionano con qualsiasi tipo di dato.
'''

'''
🔹 Conclusione:
✅ Concatenazione (+) → Unisce stringhe, ma serve str(n) per i numeri.
✅ Problema senza str(n) → Non puoi unire stringhe e numeri direttamente.
✅ Migliore alternativa → Usa f-string per scrivere codice più leggibile.
'''





'''spiegami questo esercizio come svolgerlo imn modo che pero'  non me lo svolgi , che pero', riesca a farlo,( dammi anche vai sugerrimenti per riuscire nell'intento ) '''










'''INIZIO

DEFINISCI funzione èNumeroPerfetto(n)
    INIZIALIZZA sommaDivisori = 0

    PER ogni numero i da 1 a n//2 FARE
        SE i è divisore di n ALLORA
            Aggiungi i a sommaDivisori
        FINE SE
    FINE PER

    SE sommaDivisori è uguale a n ALLORA
        RESTITUISCI VERO
    ALTRIMENTI
        RESTITUISCI FALSO
    FINE SE

FINE FUNZIONE
🔹 Come migliorare nella scrittura dello pseudocodice?
Inizia sempre con carta e penna

Prima di scrivere codice, prova a strutturarlo in pseudocodice.
Pensa ai passi necessari senza distrarti con la sintassi.
Pratica con esercizi semplici

Scrivi pseudocodice per problemi facili, come trovare un massimo in un array o sommare numeri.
Leggi pseudocodici di altri

Studia esempi online per capire diversi stili.
Trasforma lo pseudocodice in codice vero

Una volta scritto, prova a convertirlo in un linguaggio di programmazione.

'''





