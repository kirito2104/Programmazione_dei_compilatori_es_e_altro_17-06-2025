

# Scrivere una funzione in Python che, date due liste l1 e l2,
# restituisce una lista senza duplicati che è l'intersezione delle due liste l1 e l2.

'''
- controllare che le due liste e verificare se ci sono numeri uguali 
- appendere nella lista vuota cio' che e' uguale nelle due liste 

'''



def trova_uguaglianze_tra_le_due_lisste(list_a, list_b,risultato):  
    """
    Funzione che trova gli elementi comuni tra due liste e restituisce una lista senza duplicati.
    
    Parametri:
    list_a (list): Prima lista di numeri o elementi da confrontare.
    list_b (list): Seconda lista di numeri o elementi da confrontare.
    
    Ritorna:
    list: Lista contenente gli elementi comuni a entrambe le liste, senza duplicati.
    """
    
    # Creiamo una lista vuota per raccogliere gli elementi comuni (anche con duplicati)
    list_vuota = []

    # Primo ciclo: scorre tutti gli elementi di list_a
    for e1 in list_a:
        # Secondo ciclo: confronta ogni elemento di list_a con ogni elemento di list_b
        for e2 in list_b:
            if e1 == e2:  # Se troviamo un valore uguale nelle due liste
                list_vuota.append(e1)  # Aggiungiamo il valore a list_vuota (potrebbero esserci duplicati)

    # Creiamo una lista che conterrà gli elementi comuni senza duplicati
    risultato = []

    # Scorriamo gli elementi di list_vuota (che contiene gli elementi comuni con duplicati)
    for e in list_vuota:
        if e not in risultato:  # Se l'elemento non è già presente nella lista finale
            risultato.append(e)  # Lo aggiungiamo
    
    return risultato  # Restituiamo la lista filtrata senza duplicati
    
       
    
    
    
'''if risultato == e1 :
            return True
        else :
            risultato == e2
            return False
            '''



# Liste di input
list_a = [10, 2, 3, 2, 24, 5, 6, 7]
list_b = [10, 2, 3, 4, 5, 62, 1, 3, 7]

# Passiamo una lista vuota come terzo argomento
s = trova_uguaglianze_tra_le_due_lisste(list_a, list_b, [])

# 📌 Liste di input: queste sono le due liste di numeri che vogliamo confrontare
list_a = [10, 2, 3, 2, 24, 5, 6, 7]  # Lista 1 con alcuni numeri, alcuni ripetuti (es. 2)
list_b = [10, 2, 3, 4, 5, 62, 1, 3, 7]  # Lista 2 con alcuni numeri simili a list_a, ma con differenze

# 📌 Chiamata alla funzione `trova_uguaglianze_tra_le_due_lisste`
# Passiamo:
# 1️⃣ `list_a` → La prima lista con i numeri
# 2️⃣ `list_b` → La seconda lista con i numeri
# 3️⃣ `[]` → Una lista vuota che fungerà da contenitore per gli elementi comuni trovati
s = trova_uguaglianze_tra_le_due_lisste(list_a, list_b, [])

# 📌 Stampiamo il risultato in diversi modi

# 🔹 Modo 1: Stampa diretta della lista risultante
print("Numeri comuni tra le due liste:", s)  
# Esempio di output: Numeri comuni tra le due liste: [10, 2, 3, 5, 7]
# Qui Python stampa l'intera lista risultante con le parentesi quadre.

# 🔹 Modo 2: Stampiamo ogni numero comune su una riga separata
print("Elementi comuni uno per uno:")
for numero in s:  # Iteriamo sugli elementi della lista `s`
    print(numero)  # Stampiamo ogni numero su una nuova riga
# Esempio di output:
# Elementi comuni uno per uno:
# 10
# 2
# 3
# 5
# 7
# Questo metodo rende più leggibile il risultato, mostrando un numero alla volta.

# 🔹 Modo 3: Stampa formattata per un output più leggibile
# Usiamo `map(str, s)` per convertire ogni numero in una stringa
# Poi utilizziamo `', '.join(...)` per unirli con una virgola e uno spazio
print(f"I numeri comuni sono: {', '.join(map(str, s))}")
# Esempio di output: I numeri comuni sono: 10, 2, 3, 5, 7
# Questo metodo rende l'output più pulito e leggibile in una singola riga.

'''
Cosa fa ogni parte del codice?
*Definiamo le due liste di numeri (list_a e list_b).

-Contengono numeri casuali, alcuni ripetuti e altri unici.

*Chiamiamo la funzione trova_uguaglianze_tra_le_due_lisste() con una lista vuota [].

-La funzione trova gli elementi comuni tra list_a e list_b, eliminando i duplicati.

*Stampiamo il risultato in tre modi diversi:

-Direttamente come lista.
-Numero per numero, uno per riga.
-In una stringa ben formattata con i numeri separati da virgole

'''

'''
Cosa cambia?
Ora passiamo [] (una lista vuota) come terzo argomento nella chiamata alla funzione.
Questo risolve l'errore e il codice funziona senza modificare la definizione della funzione
'''



##################################################################################################################
#############################################################################################################################################

#Esercizio
#Scrivere una funzione in Python che, date due liste l1 e l2, 
#restituisce True se ogni elemento di l1 è contenuto anche in l2, False altrimenti.


# Liste di input
list_1 = [10, 2, 3, 2, 24, 5, 6, 7]
list_2 = [10, 2, 3, 4, 5, 62, 1, 3, 7]

'''
- dai un aaltro nome alla lista come  e1 
- crea un variabile dove lo poni uguale a True 

e una altra ugulae a False 

'''

def trova_uglianzze_True_e_false (list_1,list_2):
    
    for e1 in list_1:
        appoggio = False 
        for e2 in list_2:
            if e1 == e2 :
                appoggio = False 
                """
                l'istruzione *break* interrompe il ciclo nel quale viene chiamata:
                in questo caso, se e1 = e2, l'operazione break interrompe
                il ciclo for più interno (for e2 in l2)
                """
                break 
        """
        se e1 non è uguale a nessun elemento di l2,
        allora l2 non contiene tutti gli elementi di l1
        quindi è inutile controllare gli altri elementi di l1,
        ritorna False
        """
        if not appoggio:
            return False 
        """
        se il ciclo più esterno termina, allora tutti gli elementi di l1
        sono in l2, ritorna True
        """
    return True

# 📌 Chiamata alla funzione `trova_uglianzze_True_e_false`
# Questa funzione verifica la presenza degli elementi di `list_1` in `list_2`
# e restituisce un valore booleano (`True` o `False`) oppure una lista con gli elementi comuni.

# 🔹 Passiamo come argomenti:
# 1️⃣ `list_1` → La prima lista contenente i numeri da verificare.
# 2️⃣ `list_2` → La seconda lista, in cui cerchiamo le corrispondenze.

d = trova_uglianzze_True_e_false(list_1, list_2)  # Chiamata alla funzione con le due liste come input

# 📌 Stampiamo il risultato in diversi modi per una migliore leggibilità

# 🔹 Modo 1: Stampa diretta dell'output della funzione
print("Risultato della verifica:", d)
# Se la funzione restituisce `True` o `False`, vedremo un semplice valore booleano.
# Se invece restituisce una lista, vedremo gli elementi comuni tra `list_1` e `list_2`.

# 🔹 Possibile output:
# Se la funzione restituisce un valore booleano:
# "Risultato della verifica: True"  (se tutti gli elementi di `list_1` sono in `list_2`)
# "Risultato della verifica: False" (se almeno un elemento di `list_1` non è in `list_2`)

# Se la funzione restituisce una lista di numeri comuni:
# "Risultato della verifica: [10, 2, 3, 5, 7]"
 
