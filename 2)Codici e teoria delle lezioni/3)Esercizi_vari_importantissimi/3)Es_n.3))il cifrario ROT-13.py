
'''Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera
 del messaggio da cifrare viene sostituita con quella posta 13 posizioni 
 più avanti nell'alfabeto.

Scrivere una funzione in grado di criptare, usando il cifrario
 ROT-13 una stringa in input.

Nota: utilizzare l'alfabeto inglese (26 lettere) e per semplicità 
considerare solamente le lettere minuscole (no maiuscole o numeri).
'''
###################################################################################################################################

'''. Pianificazione generale (struttura del codice)
Prima di scrivere direttamente il codice, definisci uno schema mentale chiaro:

Cosa deve fare il programma?
Ricevere una stringa come input
Cifrare ogni lettera secondo la logica ROT-13
Restituire la stringa cifrata
Quali strumenti di programmazione usare?
Strutture dati: liste, stringhe
Funzioni: meglio separare la logica in funzioni riutilizzabili
Operazioni matematiche: utilizzerai gli indici delle lettere
2. Strategie di sviluppo
Passaggi da seguire mentalmente prima di scrivere il codice:

Mappare l'alfabeto

L'alfabeto inglese ha 26 lettere. Se una lettera si trova in una certa posizione n, la sua corrispondente in ROT-13 sarà (n + 13) % 26.
Convertire le lettere in numeri aiuta nel calcolo (es. usando il codice ASCII).
Convertire i caratteri

Ogni lettera minuscola ha un codice ASCII (ord('a') → 97, ord('z') → 122).
Devi applicare uno shift di 13 posizioni, facendo attenzione a rimanere nell’intervallo delle lettere minuscole.
Iterare sulla stringa

Per ogni carattere, verificare se è una lettera. Se sì, applicare la conversione ROT-13.
Se non è una lettera, lasciarlo invariato.
Restituire il risultato

Costruire una nuova stringa con i caratteri cifrati e restituirla.
3. Stile di programmazione consigliato
Chiarezza: usa nomi di variabili significativi (es. rot13_transform invece di r13).
Modularità: crea funzioni riutilizzabili, ad esempio:
Una funzione che trasforma una lettera
Una funzione che gestisce l'intera stringa
Evitare ripetizioni: sfrutta liste, dizionari o operazioni matematiche invece di scrivere troppi if.
Testare con casi semplici: prova prima con parole brevi (hello → uryyb) e poi con frasi più lunghe.
4. Prima di scriverlo sul compilatore
📌 Carta e penna: butta giù la logica senza codice!
📌 Scrivi i passaggi in pseudo-codice, ad esempio:

yaml
Copia codice
Per ogni carattere nella stringa:
    Se è una lettera minuscola:
        Convertire in numero (ASCII)
        Applicare ROT-13
        Convertire di nuovo in lettera
    Altrimenti:
        Lasciare invariato
Ricostruire la stringa e restituirla
📌 Solo dopo aver chiarito la logica, scrivilo nel compilatore!'''



# Certo! Ecco alcuni consigli strategici su come affrontare il problema senza usare il codice ASCII 
# e mantenendo autonomia nella scrittura del codice.

# ---
# 1. Pensa alla struttura logica prima di scrivere il codice
# 📌 Prima di scrivere una sola riga di codice, visualizza mentalmente o su carta come funzionerà 
# la trasformazione ROT-13 senza usare ord() e chr().
# 📌 Chiediti:  
#    - Come posso rappresentare l’alfabeto senza usare i codici numerici?  
#    - Quale struttura dati mi permette di trovare una lettera e sostituirla con la sua corrispondente?  

# 🔹 Possibile approccio → Usa una lista o una stringa con tutte le lettere dell’alfabeto.  

# ---
# 2. Creazione dell’alfabeto per la mappatura
# 🔍 Senza ASCII, devi trovare un modo alternativo per associare ogni lettera alla sua trasformata ROT-13.  

# 📌 Strategie possibili:  
# 1. Lista ordinata con tutte le lettere → trovare l’indice di una lettera e sostituirla con la lettera 13 posizioni avanti.  
# 2. Due stringhe parallele → una con l'alfabeto originale, l'altra con la versione "shiftata" (ROT-13).  
# 3. Dizionario di conversione → per un accesso rapido, puoi creare una "tabella di sostituzione" lettera per lettera.  

# 📌 Cosa evitare?  
# 🚫 Evita di scrivere tanti if separati per ogni lettera (if lettera == 'a': return 'n'...), perché è inefficiente e poco scalabile.  

# ---
# 3. Strategia di sostituzione
# 📌 Come gestire la trasformazione di ogni carattere?  
# - Trova il modo più efficiente per cercare la lettera originale e trovare la corrispondente in ROT-13.  
# - Se il carattere non è una lettera (spazi, punteggiatura, ecc.), come lo gestisci?  
#   - Soluzione: puoi controllare se è nella lista di lettere e, se non lo è, lasciarlo invariato.  

# 🔍 Possibile metodo:  
# 1. Scorri ogni lettera della stringa.  
# 2. Se la lettera è presente nella lista dell’alfabeto, trova la sua posizione.  
# 3. Usa quella posizione per trovare la lettera corrispondente nell’alfabeto ROT-13.  
# 4. Se il carattere non è una lettera, lascialo così com’è.  

# ---
# 4. Struttura del codice
# 📌 Prima di scrivere il codice, butta giù uno schema:  

# 1. Definire l’alfabeto normale e quello trasformato con ROT-13.
# 2. Creare una funzione che prende una stringa come input.
# 3. Iterare ogni carattere della stringa:
#    - Se è una lettera, sostituirla con quella corrispondente in ROT-13.
#    - Se non è una lettera, lasciarlo invariato.
# 4. Restituire la stringa trasformata.

# ---
# 5. Migliorare il codice
# Una volta scritto il codice base, puoi pensare a come migliorarlo:
# - Performance: Qual è il metodo più veloce per trovare una lettera e sostituirla? (Lista, stringa, dizionario?)  
# - Leggibilità: Il codice è chiaro e comprensibile? I nomi delle variabili sono descrittivi?  
# - Test: Prova diverse frasi per vedere se il cifrario funziona con ogni caso possibile (lettere diverse, spazi, numeri...).  

# ---
# 6. Cose da provare
# Dopo aver scritto la versione base, sperimenta con queste variazioni:  
# ✅ Supportare lettere maiuscole oltre a quelle minuscole.  
# ✅ Aggiungere una funzione di decodifica (ROT-13 è simmetrico: se cifri una stringa due volte, ottieni l’originale).  
# ✅ Ottimizzare la ricerca della lettera, per renderla più veloce (ad esempio, confrontando dizionario vs lista vs stringa).  

# ---
# 🎯 Obiettivo finale: Arrivare a un codice chiaro e funzionante, scritto in modo indipendente seguendo un processo logico ben definito. 🚀


'''Come posso rappresentare l'alfabeto senza usare i codici numerici?
Quale struttura dati mi permette di trovare una lettera 
e sostituirla con la sua corrispondente?
'''

#1. Concetto di ROT-13
#ROT-13 è un cifrario a sostituzione fissa dove ogni
# lettera dell'alfabeto viene sostituita con quella che si
# trova 13 posizioni dopo.
#Poiché l'alfabeto inglese ha 26 lettere, applicare un
# cambio di 13 posizioni significa che:

#La prima metà delle lettere (a-m) viene spostata nella seconda metà (n-z).
#La seconda metà (n-z) viene riportata nella prima (a-m).

'''
funz. ror_13 (testo)

testo_cifrato = ""

for c in testo_normale 
    if c deve essere uguale a " "
        accumolo testo cifrato += " " (ps e lo accumula qui )
    ELSE : 
        i =0 
        While c e' diverso da alfabeto[i] 
             testo_cifrato aggiungi a alfabeto_citrato[i]
        return alfabeto cifrato
'''



alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_cifrato = "nopqrstuvwxyzabcdefghijklm"

def Rot13_basic(testo_normale):
    
    
    testo_cifrato= ""
    for c in testo_normale: #pongo c uguale a testo normale, quindi richiamo c come se fosse testo normale 
        if c == " ": # se c e' e' uguale " "
            testo_cifrato += " "
            # Questa riga di codice qui sopra:

            # if c == ' ':  # Se c è uno spazio
            #     testo_cifrato += " "
            # serve a mantenere gli spazi invariati nella stringa cifrata.
            # ---
            # Cosa succede esattamente?
            # 1. Durante l'iterazione sulla stringa di input, il carattere corrente
            # è assegnato alla variabile `c`.
            # 2. Il codice verifica se `c` è uno spazio (`' '`).
            # 3. Se la condizione è vera, lo spazio viene aggiunto direttamente
            # alla variabile `testo_cifrato`, senza modificarlo.

            # ---
            # Perché è necessario?
            # ROT-13 si applica solo alle lettere dell'alfabeto inglese, quindi:
            # - Le lettere vengono cifrate.
            # - Gli altri caratteri (spazi, numeri, simboli) devono rimanere invariati.

            # 📌 Esempio di comportamento:
            # input: "hello world"
            # output: "uryyb jbeyq"
            # Lo spazio tra `"hello"` e `"world"` rimane invariato, mentre 
            # le lettere vengono cifrate.

            # ---
            # Alternative e miglioramenti
            # Se vuoi generalizzare la condizione per lasciare invariati tutti
            # i caratteri non alfabetici, potresti usare:

            # if c not in alfabeto:
            #     testo_cifrato += c # Mantieni qualsiasi carattere che non è una lettera

            # 📌Questo evita di dover gestire separatamente numeri, punteggiatura e spazi.

            # ---
            # Conclusione
            # ✅ La riga `if c == ' ': testo_cifrato += " "` è utile per mantenere 
            # gli spazi invariati nella stringa cifrata.  
            # ✅ Se vuoi estendere il controllo ad altri caratteri non alfabetici,
            # puoi verificare direttamente se `c` non è una lettera e lasciarlo invariato.    
        else:  # Questo blocco viene eseguito solo se 'c' è una lettera presente nell'alfabeto (cioè non è uno spazio o un simbolo)
    
            i = 0  # Inizializza la variabile 'i' a 0. Questa sarà usata come indice per scorrere la stringa 'alfabeto'.
            while c != alfabeto[i]:  # Continua a scorrere l'alfabeto fino a trovare la lettera 'c'.
                i += 1  # Incrementa l'indice 'i' per passare alla lettera successiva nell'alfabeto.
                '''
                # Una volta che il ciclo 'while' trova la corrispondenza tra 'c' e un carattere in 'alfabeto',
                # 'i' rappresenta la posizione esatta della lettera 'c' all'interno della stringa 'alfabeto'.
                '''
            testo_cifrato += alfabeto_cifrato[i]  # Aggiunge al testo cifrato la lettera corrispondente in 'alfabeto_cifrato'.
            # Questo funziona perché 'alfabeto_cifrato' è una versione trasformata (ROT-13) di 'alfabeto', quindi:
            # Se 'c' è in posizione 'i' in 'alfabeto', la lettera in 'alfabeto_cifrato[i]' è la sua versione cifrata.

        # Dopo aver processato tutti i caratteri della stringa di input, restituisce il testo completamente cifrato.
    return testo_cifrato  # Restituisce la stringa cifrata finale, contenente tutte le lettere trasformate e i caratteri invariati.

'''
alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher   = "nopqrstuvwxyzabcdefghijklm"

def Rot13_basic(plaintext):
    """
    Questa funzione utilizza due liste per associare ad ogni carattere
    dell'alfabeto il carattere con cui sostituirlo per ottenere la stringa
    cifrata
    """
    ciphertext = ""
    for c in plaintext:
        if c == " ":
            ciphertext += " "
        else:
            i = 0
            while c != alphabet[i]:
                i += 1
            ciphertext += cipher[i]
    return ciphertext
'''

s = input("scriviuna lettera da sostituire con Rot-13:")


c = Rot13_basic(s)

print(c)


##===================================================================================================================================================

# Ecco una versione con meno commenti : 


alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_cifrato = "nopqrstuvwxyzabcdefghijklm"

def Rot13_basic(testo_normale):
    """
    Funzione che applica il cifrario ROT-13 a una stringa di input.
    Per ogni lettera minuscola, la sostituisce con la lettera corrispondente 13 posizioni dopo.
    Gli spazi e i caratteri non alfabetici restano invariati.
    """
    
    testo_cifrato = ""  # Inizializza la stringa che conterrà il testo cifrato
    
    for c in testo_normale:  # Scansiona ogni carattere della stringa input
        if c == " ":  # Se il carattere è uno spazio, lo mantiene invariato
            testo_cifrato += " "
        else:
            i = 0  # Inizializza un indice per cercare la lettera nell'alfabeto
            while c != alfabeto[i]:  # Trova la posizione della lettera nell'alfabeto originale
                i += 1  
            testo_cifrato += alfabeto_cifrato[i]  # Sostituisce la lettera con la corrispondente cifrata
    
    return testo_cifrato  # Restituisce il testo cifrato

s = input("Scrivi una frase da cifrare con ROT-13: ")
#print(Rot13_basic(s))  # Applica la funzione e stampa il risultato


#questo e' cio che restituira'
'''
scriviuna lettera da sostituire con Rot-13:cebtenzznmvbar qrv pnypbyngbev
programmazione dei calcolatori
'''


###################################################################################################################################################################
#mentre nell'altra versione era cosi:

'''
# Il ciclo `while` non è stato modificato, ma il codice successivo cambia il modo 
# in cui viene applicata la trasformazione ROT-13.

# 🔹 Differenza principale
'''
# 🔍 Vecchio metodo (decrittazione)

'''
while c != alphabet[i]:  # Scansiona l'alfabeto per trovare la posizione di 'c'
    i += 1  


👉 Poi, usava questa logica per decriptare ROT-13:
'''

'''
index = (i - 13) % 26  # Sottraeva 13 per tornare indietro nel cifrario
plaintext += alphabet[index]


📌 Qui il codice applicava la decrittazione (cioè tornava alla lettera originale).

---
'''

# 🔍 Nuovo metodo (cifratura)
'''
index = (i + 13) % 26  # Aggiunge 13 posizioni invece di sottrarle
ciphertext += alphabet[index]  # Prende la lettera cifrata
'''

'''
📌 Qui il codice sta cifrando e NON decriptando.

💡 Cosa cambia?
- Nel primo caso (-13), si sta decriptando (tornando alla lettera originale).
- Nel secondo caso (+13), si sta cifrando (applicando ROT-13).

---
'''
# 🔹 Confronto pratico

# Vecchio metodo (decrittazione)
'''
alfabeto = "abcdefghijklmnopqrstuvwxyz"
c = "o"  # 'o' è una lettera cifrata

i = alfabeto.index(c)  # Trova la posizione di 'o'
index = (i - 13) % 26  # Sottrae 13 per tornare indietro
plaintext = alfabeto[index]  # Trova la lettera originale

print(plaintext)  # Output: 'b' (se la frase era "oryyb", il risultato sarà "hello")
'''

# ✅ Risultato: Decripta la stringa riportandola al testo originale.


# Nuovo metodo (cifratura)
'''
alfabeto = "abcdefghijklmnopqrstuvwxyz"
c = "b"  # 'b' è una lettera normale

i = alfabeto.index(c)  # Trova la posizione di 'b'
index = (i + 13) % 26  # Aggiunge 13 per cifrare
ciphertext = alfabeto[index]  # Trova la lettera cifrata

print(ciphertext)  # Output: 'o' (se la frase era "hello", il risultato sarà "uryyb")
'''

# ✅ Risultato: Cifra la stringa applicando ROT-13.



#  Conclusione
'''
#📌 Se fai `+13`, stai cifrando con ROT-13.
#📌 Se fai `-13`, stai decriptando un testo cifrato con ROT-13.
#📌 Poiché ROT-13 è simmetrico, applicando `+13` su una stringa già cifrata, la riporti al testo originale.

#🚀 Ora sai come trasformare il codice tra cifratura e decifratura! 🚀

'''





##===================================================================================================================================================
'''
Esercizio 1
Scrivere una funzione che, data in input una stringa criptata
usando il cifrario ROT-13, decripta la stringa e restituisce in output
la stringa decriptata.

Esempio: data in input la stringa

cebtenzznmvbar qrv pnypbyngbev
la funzione deve restituire in output la stringa

programmazione dei calcolatori
Nota: utilizzare l'alfabeto inglese (26 lettere) e per semplicità
considerare solamente le lettere minuscole (no maiuscole o numeri).

Suggerimento: è sufficiente fare qualche modifica al codice scritto
per risolvere l'esercizio 3.

'''

#1. Definire l’alfabeto normale e la sua versione cifrata ROT-13.
#2. Creare una funzione che accetta una stringa in input.
#3. Iterare ogni carattere della stringa:
#   - Se è una lettera, sostituirla con la corrispondente in ROT-13.
#   - Se non è una lettera, lasciarla invariata.
#4. Restituire il testo trasformato.

'''##################################################################################################################################################'''
# Ecco alcuni consigli strategici per scrivere l'algoritmo da zero, 
# senza copiare il codice, ma sviluppandolo in modo autonomo. 🚀

# ---
# 1️⃣ Capisci bene cosa deve fare l'algoritmo
# 📌 Obiettivo:
# - L'algoritmo prende in input una stringa cifrata con ROT-13.
# - Deve decriptarla, restituendo il testo originale.
# - ROT-13 è simmetrico, quindi applicare di nuovo ROT-13 a un testo cifrato 
#   lo riporta al testo originale.

# 📌 Vincoli:
# - Lavoriamo solo con lettere minuscole.
# - Gli spazi devono essere mantenuti invariati.
# - Dobbiamo trovare la lettera cifrata, calcolare la posizione originale 
#   e ricostruire il testo.

# ---
# 2️⃣ Struttura logica da seguire
# Prima di scrivere il codice, prova a buttare giù un ragionamento su come funzionerà.
# 📌 Passaggi principali:
# 1. Definire l'alfabeto (una stringa con le 26 lettere).
# 2. Scorrere ogni carattere del testo cifrato.
# 3. Gestire gli spazi (se un carattere è uno spazio, lo lasci invariato).
# 4. Trovare la posizione della lettera nell'alfabeto.
# 5. Sottrarre 13 posizioni per tornare al testo originale.
# 6. Aggiungere la lettera decriptata al risultato finale.
# 7. Restituire il testo decriptato.

# ---
# 3️⃣ Strategie di sviluppo
# 💡 Domande da porsi prima di scrivere il codice:
# - Come posso trovare la posizione di una lettera nell'alfabeto?
#   📌 Soluzione: Scorrere l'alfabeto con un ciclo `while` oppure usare `.index()`.
# - Come posso tornare indietro di 13 posizioni?
#   📌 Soluzione: `(indice + 13) % 26` per ROT-13.
# - Come gestire spazi e altri caratteri?
#   📌 Soluzione: Se un carattere non è nell'alfabeto, lo aggiungo direttamente al testo decriptato.

# ---
# 4️⃣ Scrivere l'algoritmo in pseudo-codice
# Prima di scrivere il codice, butta giù uno schema logico:

# 1. Creare una stringa con le lettere dell'alfabeto.
# 2. Creare una variabile `testo_in_chiaro` per il risultato finale.
# 3. Per ogni carattere nel testo cifrato:
#    - Se è uno spazio, aggiungerlo a `testo_in_chiaro`.
#    - Altrimenti:
#       - Trovare la sua posizione nell'alfabeto.
#       - Calcolare la posizione originale sottraendo 13 posizioni.
#       - Aggiungere la lettera decriptata al risultato finale.
# 4. Restituire il testo decriptato.

# ---
# 5️⃣ Consigli per migliorare l'algoritmo
# ✅ Usa `index()` invece di un `while` per trovare la posizione della lettera più velocemente.
# ✅ Gestisci eventuali errori nel caso in cui il testo contenga caratteri non previsti.
# ✅ Testa il codice con più esempi per verificare che la decriptazione sia corretta.
# ✅ Se vuoi rendere il codice più leggibile, aggiungi qualche commento chiaro e diretto.

# ---
# 🎯 Conclusione
# 🚀 Ora hai tutti gli strumenti per scrivere l'algoritmo in autonomia!
# 📌 Segui i passaggi logici e scrivi il codice passo dopo passo.
# 📌 Testalo con diverse stringhe cifrate per verificare che funzioni correttamente.

# 🔍 Buona programmazione! 🚀





alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_cifrato = "nopqrstuvwxyzabcdefghijklm"

def decrypt_rot13(testo_cifrato):
    """
    Questa funzione utilizza l'artimetica modulare:
    https://it.wikipedia.org/wiki/Aritmetica_modulare
    """
    lettura_testo = "" 
    for c in testo_cifrato:
        if c == " ":
            lettura_testo += " "
        else : 
            i = 0 
            while c != alfabeto[i]:
                '''La funzione .index() serve per trovare direttamente la posizione di 
                un elemento in una stringa o lista, senza dover usare un ciclo while. 
                Ti spiegherò come arrivarci da solo e come semplifica il codice.
                '''
                i+=1
            index = ( i +13)%26
            lettura_testo += alfabeto_cifrato 
    return lettura_testo
   
s = input('scrive testo da decifrare: ')

print(decrypt_rot13(s))  
   
#######################################################################################################################################################################################
  
#ecco come funziona la dunzione index :
'''
La funzione `.index()` in Python trova la posizione di un elemento all'interno di una stringa 
o lista e restituisce l'indice corrispondente.

---

🔹 Come funziona `index()` con le stringhe

📌 Esempio 1: Trovare la posizione di un carattere in una stringa
'''
alfabeto = "abcdefghijklmnopqrstuvwxyz"
lettera = "g"

posizione = alfabeto.index(lettera)  # Trova la posizione della lettera "g"
print(posizione)  # Output: 6

'''
📌 Cosa succede?
- La stringa è indicizzata da 0:
  
  a b c d e f g h i j k l m n o p q r s t u v w x y z
  0 1 2 3 4 5 6 7 8 9 10 ...

- "g" è alla posizione 6 → `.index("g")` restituisce 6.

---

📌 Esempio 2: Trovare la posizione di una lettera in una parola
'''
parola = "programmazione"
indice = parola.index("m")  # Trova la posizione della prima 'm'
print(indice)  # Output: 6

'''
📌 Perché?
- La prima "m" appare nella posizione 6 (partendo da 0).

---

🔹 `index()` con le liste

📌 Esempio 3: Trovare un numero in una lista
'''
numeri = [10, 20, 30, 40, 50]
posizione = numeri.index(30)  # Trova l'indice di 30
print(posizione)  # Output: 2

'''
 La lista è:

  [10, 20, 30, 40, 50]
   0   1   2   3   4

- Il valore `30` si trova in posizione 2.

---

📌 Esempio 4: Trovare la prima occorrenza di un elemento ripetuto
'''
frutta = ["mela", "banana", "pera", "banana", "arancia"]
indice = frutta.index("banana")  # Trova la PRIMA "banana"
print(indice)  # Output: 1

'''
📌 Cosa succede?
- Ci sono due "banana" nella lista (indice 1 e indice 3).
- `.index("banana")` restituisce solo la prima occorrenza (1).

---

🔹 Errori comuni con `index()`

📌 Errore: L'elemento non esiste
'''
numeri = [10, 20, 30, 40]
# print(numeri.index(100))  # ERRORE: 100 non è nella lista

'''
⚠ Python genera un `ValueError` se l'elemento non è presente nella lista o stringa.
✅ Soluzione: Usa un controllo prima:
'''
if 100 in numeri:
    print(numeri.index(100))
else:
    print("Elemento non trovato")

'''
---

🔹 Usare `.index()` per ROT-13

Ora capiamo come `.index()` può sostituire il ciclo `while` per trovare la posizione di una lettera.

📌 Versione con `while`
'''
alfabeto = "abcdefghijklmnopqrstuvwxyz"
c = "r"
i = 0

while c != alfabeto[i]:  # Cerca la posizione di "r"
    i += 1

print(i)  # Output: 17

'''
📌 Problema:
- Il ciclo `while` deve scorrere tutto l'alfabeto fino a trovare `c`.
- Se `c = "z"`, il `while` farà 26 iterazioni.

✅ Sostituire con `.index()`
'''
alfabeto = "abcdefghijklmnopqrstuvwxyz"
c = "r"

i = alfabeto.index(c)  # Trova la posizione di "r" direttamente
print(i)  # Output: 17

'''
📌 Vantaggi:
✅ Più veloce 🚀
✅ Codice più pulito
✅ Nessun ciclo inutile

---

🔹 Conclusione
- `.index()` restituisce la posizione del primo elemento trovato in stringhe o liste.
- Alternativa più veloce rispetto a un `while` che scansiona carattere per carattere.
- Se l'elemento non esiste, dà errore, quindi puoi verificare prima con `if elemento in lista`.

🚀 Ora prova a sostituire i tuoi `while` con `.index()` per migliorare le prestazioni del tuo codice! 🚀
'''
   

''' testo_in_chiaro = ""
    for c in testo_cifrato:
        if c == " ":
            testo_in_chiaro += " "
        else:
            i = 0
            while c != alfabeto[i]:
                i += 1
            index = (i + 13) % 26
            testo_in_chiaro += alfabeto[index]
    return testo_in_chiaro
'''

s = input("Scrivi una frase da cifrare con ROT-13: ")
print(Rot13_basic(s))  # Applica la funzione e stampa il risultato




























