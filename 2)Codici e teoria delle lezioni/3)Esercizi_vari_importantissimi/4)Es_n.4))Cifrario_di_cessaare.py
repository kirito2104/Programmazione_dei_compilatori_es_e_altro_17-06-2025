'''
Il **Cifrario di Cesare** è un cifrario a sostituzione **monoalfabetica**,
in cui ogni lettera del messaggio viene sostituita, nel testo cifrato,
con la lettera che si trova **K posizioni avanti** nell'alfabeto.
Il numero **K** è detto **chiave di cifratura**.

#### **Obiettivo**
1. Scrivere una funzione che, data in input la **chiave K** e una **stringa**,
restituisca la stringa **cifrata** secondo il Cifrario di Cesare con chiave **K**.
2. Scrivere una seconda funzione che, data in input la **chiave K**
e una **stringa già cifrata**, restituisca il **testo originale** decriptandolo con la stessa chiave.

#### **Vincoli**
- Utilizzare l'**alfabeto inglese** (26 lettere).
- Considerare **solo lettere minuscole** (senza maiuscole, numeri o caratteri speciali).

#### **Suggerimento**
Per risolvere l'esercizio in modo efficiente, è utile sfruttare **l'aritmetica modulare**,
come fatto nell'esercizio 3. 🚀

'''



alfabeto_ing = "abcdefghijklmnopqrstuvwxyz"  # Definizione dell'alfabeto inglese

# Definizione della funzione per il Cifrario di Cesare
def Cifrario_cesare(testo, k):  
    """
    Funzione che implementa il Cifrario di Cesare.
    
    Parametri:
    - testo (str): Il testo da cifrare.
    - k (int): La chiave di cifratura che indica di quante posizioni spostare ogni lettera nell'alfabeto.

    Funzionamento:
    - Per ogni lettera nel testo, la funzione la sposta di 'k' posizioni in avanti nell'alfabeto inglese.
    - Se il testo contiene spazi, questi vengono mantenuti invariati.
    - Se l'indice supera la lunghezza dell'alfabeto (26 lettere), si riavvolge grazie all'operatore modulo (%).
    
    Ritorna:
    - (str) Il testo cifrato.
    """
    
    scorrimento_testo = ""  # Stringa che conterrà il testo cifrato risultante

    
    
    for c in testo:  # Itera su ogni carattere della stringa input
        if c == " ":  
            # Se il carattere è uno spazio, lo mantiene invariato
            scorrimento_testo += " "  
        else:
            i = 0  # Inizializza un indice per trovare la posizione della lettera nell'alfabeto
            
            # Trova la posizione della lettera 'c' nell'alfabeto
            while c != alfabeto_ing[i]: 
                i += 1  # Incrementa 'i' fino a trovare il carattere
            
            # Calcola il nuovo indice della lettera cifrata, usando il modulo per mantenere il range 0-25
            index = (i + k) % 26  
            
            # Aggiunge la lettera cifrata alla stringa risultato
            scorrimento_testo += alfabeto_ing[index]  
            
    return scorrimento_testo  # Restituisce il testo cifrato


# Input dell'utente
s = input("Inserisci la stringa da cifrare: ")  # Chiede all'utente di inserire il testo da cifrare
k = int(input("Inserisci la chiave di cifratura (numero intero): "))  # Chiede la chiave di cifratura

# Chiamata alla funzione con i parametri forniti dall'utente
t = Cifrario_cesare(s, k)  

# Stampa il risultato della cifratura
print("Testo cifrato:", t)

#=========================================================================================================================================================================

#Seconda soluzione dell'esercizio : 


def decrypt_caesar(ciphertext, k):
    '''
    Funzione che decifra un testo cifrato con il Cifrario di Cesare.

    -------------------------------------------------------------------------
    A parte il cambio di nomi delle variabili, il codice della funzione 
    `decrypt_caesar` è IDENTICO a quello della funzione `Cifrario_cesare`, 
    tranne per un problema logico nell'uso della chiave di cifratura.
    
    -------------------------------------------------------------------------
    DIFFERENZE NELLE VARIABILI:
    - `testo` → `ciphertext`: indica che si tratta del testo cifrato da decifrare.
    - `scorrimento_testo` → `plaintext`: rappresenta il testo in chiaro (decifrato).
    - `alfabeto_ing` → `alphabet`: solo un cambio di nome per l'alfabeto.
    
    Questi cambiamenti sono solo di NOMENCLATURA e non alterano il funzionamento.

    -------------------------------------------------------------------------
    PROBLEMA NELLA LOGICA DI DECRITTAZIONE:
    La funzione ha un errore nel modo in cui tenta di decifrare il messaggio.

    COME FUNZIONA IL CIFRARIO DI CESARE:
    - Per CIFRARE, si sposta ogni lettera in avanti di `k` posizioni:
        indice nuovo = (indice originale + k) % 26
    - Per DECIFRARE, si dovrebbe fare il contrario, ovvero spostare INDIETRO di `k` posizioni:
        indice nuovo = (indice originale - k) % 26
    
    Ma nel codice di `decrypt_caesar`, la chiave `k` veniva sommata invece che sottratta.
    Questo lo rendeva una funzione che cripta anziché decriptare.

    SOLUZIONE PER CORREGGERE IL CODICE:
    La linea errata:
        index = (i + k) % 26
    Dovrebbe essere modificata in:
        index = (i - k) % 26

    -------------------------------------------------------------------------
    CONCLUSIONE:
    - La funzione originale **non decrittava il messaggio** ma eseguiva una cifratura.
    - L'UNICA modifica necessaria per renderla una vera funzione di **decrittazione** 
      è cambiare `+ k` in `- k`.
    - Il resto del codice è IDENTICO a quello della cifratura, tranne per i nomi delle variabili.

    Ora, con questa correzione, se cifri un testo con `Cifrario_cesare(testo, k)`, 
    potrai recuperarlo con `decrypt_caesar(testo_cifrato, k)`.
    '''

    plaintext = ""  # Stringa che conterrà il testo decifrato
    

    for c in ciphertext:  # Scorre ogni carattere del testo cifrato
        if c == " ":
            plaintext += " "  # Mantiene invariati gli spazi nel testo decifrato
        else:
            i = 0  # Inizializza l'indice per trovare la posizione della lettera
            while c != alphabet[i]:  
                i += 1  # Trova la posizione della lettera nell'alfabeto
            
            index = (i - k) % 26  # Sposta la lettera indietro di 'k' posizioni per la decifrazione
            
            plaintext += alphabet[index]  # Aggiunge la lettera decifrata al risultato finale

    return plaintext  # Restituisce il testo decifrato



alphabet = "abcdefghijklmnopqrstuvwxyz"  # Definizione dell'alfabeto


s = input("Inserisci la stringa da cifrare: ")  # Chiede all'utente di inserire il testo da cifrare
k = int(input("Inserisci la chiave di cifratura (numero intero): "))  # Chiede la chiave di cifratura

# Chiamata alla funzione con i parametri forniti dall'utente
t = decrypt_caesar(s, k)  

# Stampa il risultato della cifratura
print("Testo cifrato:", t)













