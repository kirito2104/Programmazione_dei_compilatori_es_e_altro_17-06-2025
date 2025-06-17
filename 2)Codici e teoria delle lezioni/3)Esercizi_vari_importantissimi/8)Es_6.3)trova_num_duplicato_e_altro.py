



### **Passaggi per risolvere l'esercizio:**
'''
1. **Analizza il problema**
   - Devi individuare i numeri che compaiono più di una volta nella lista.
   - L'output deve contenere solo i numeri duplicati, **senza ripetizioni**.

2. **Pensa a una strategia**
   - Come puoi contare quante volte appare ogni numero?
   - Come puoi evitare di ripetere i numeri nell'output?

3. **Considera diversi approcci**
   - **Utilizzare un dizionario (dict):** Puoi contare le occorrenze di ogni numero.
   - **Usare un insieme (set):** Puoi tenere traccia dei numeri già visti e di quelli duplicati.

4. **Scegli una struttura dati efficace**
   - Un **dizionario** potrebbe aiutarti a memorizzare la frequenza di ogni numero.
   - Un **set** potrebbe essere utile per evitare duplicati nell'output.

5. **Scrivi la funzione passo per passo**
   - Definisci la funzione e accetta una lista come argomento.
   - Itera sulla lista per trovare i numeri duplicati.
   - Raccogli i risultati in una nuova lista senza ripetizioni.
   - Restituisci la lista dei duplicati.

6. **Testa con più esempi**
   - Prova con liste diverse, inclusi numeri negativi e ripetizioni varie.
   - Assicurati che l'output non abbia duplicati.

7. **Ottimizza il codice**
   - Il tuo codice può essere scritto in modo più efficiente?  
   - Riesci a ridurre il numero di iterazioni?  
   - Quale metodo è più veloce se la lista è molto grande?

💡 **Extra sfida:**  
- Modifica il codice in modo che funzioni anche con liste contenenti **stringhe** (es. `["a", "b", "a", "c", "b"] → ["a", "b"]`).
- Fai in modo che l'ordine degli elementi duplicati nell'output sia lo stesso dell'input originale.

Prova a scrivere il codice e dimmi se incontri difficoltà! 🚀

'''

#Esercizio
#Scrivere una funzione in Python che, date una lista di interi, genera un'altra lista contenente solamente gli elementi duplicati.

#Esempio:

#Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
#Output : output_list = [20, 30, -20, 60]
#Input :  list = [-1, 1, -1, 8]
#Output : output_list = [-1]





num_lista =[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]



"""
funz : lista 
    



"""


def trova_duplicati(num_lista):
    
    i = 0 
    for i in range(len(num_lista)): # facendo cosi' : PRENDERA UN RANGE DI NUMERI E LI LEGGERA, SCORRENDO LA LISTA 
        for j in range(i + 1,len(num_lista)): 
            if num_lista[i] == num_lista[j]:
                print(f"lista[i] e' un duplicato")     
         






#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Esercizio
#Scrivere una funzione in Python che, date una lista di interi, genera un'altra lista contenente solamente gli elementi duplicati.

#Esempio:

#Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
#Output : output_list = [20, 30, -20, 60]
#Input :  list = [-1, 1, -1, 8]
#Output : output_list = [-1]

'''
 tuo codice usa due cicli for annidati (O(n^2)) per trovare i duplicati.
 Questo può essere migliorato con un dizionario o un set per ridurre 
 il tempo di esecuzione a O(n).
Attualmente confronti ogni elemento con tutti quelli successivi,
ma potresti usare un unico passaggio per contare le occorrenze.
'''




# Definizione della funzione per trovare i numeri duplicati in una lista
def trova_duplicato(numeri):
    """
    Funzione che trova tutti i numeri duplicati in una lista di interi.
    
    Parametri:
    numeri (list): Lista di numeri interi fornita in input.

    Restituisce:
    list: Una lista contenente tutti i numeri che compaiono più di una volta.
    """

    n = len(numeri)  # Determina la lunghezza della lista di numeri
    duplicati = []  # Inizializza una lista vuota per memorizzare i numeri duplicati

    # Primo ciclo per iterare sugli elementi della lista
    for i in range(n):
        k = i + 1  # Definisce l'indice successivo per il confronto
        
        # Secondo ciclo per confrontare ogni elemento con quelli successivi
        for j in range(k, n):
            # Se il numero nella posizione i è uguale al numero nella posizione j
            # e non è già presente nella lista dei duplicati, allora lo aggiunge
            if numeri[i] == numeri[j] and numeri[i] not in duplicati:
                duplicati.append(numeri[i])  # Aggiunge il numero alla lista dei duplicati

    return duplicati  # Restituisce la lista dei numeri duplicati

# Chiede all'utente di inserire numeri separati da virgola
numeri_input = input("Inserisci numeri separati da virgole: ")

# Converte la stringa di input in una lista di numeri interi
# Spiegazione:
# - `split(',')` divide la stringa in una lista separando gli elementi tramite la virgola
# - `map(int, ...)` converte ogni elemento della lista in un numero intero
# - `list(...)` trasforma l'oggetto map in una vera lista
numeri = list(map(int, numeri_input.split(',')))

# Chiama la funzione per trovare i numeri duplicati
s = trova_duplicato(numeri)

# Stampa la lista dei numeri duplicati trovati
print("Numeri duplicati:", s)


#pseudo codice :
'''
funzione trova_duplicati(numeri)
				n= len(numeri)
				duplicato= []
    Per	i in run range di n ossia i numeri
								k=i+=1 // qui incremento il i egli do un alias
        Per j in un range di numeri di (k,n)// k l'iteratore e n i numeri 
											se i numeri[i] == numeri[j] and numeri[i]( non devono essere duplicati) not in duplicati 
														poi appendo i numeri duplicati di numeri[i]	ossia i duplicati.append(numeri[i])
				Ritorna i  duplicati 
    
'''	

#===============================================================================================================================================================

#Es n.2

#Scrivere una funzione in python che, data una lista, rimuove da quest'ultima
# tutte le liste vuote contenute all'interno.

#Input: [3, 10, [], [], 4, [], 18]
#Output: [3, 10, 4, 18]
#Input: [3, 11, [4,3], [], 4, [1], 18]
#Output: [3, 11, [4,3], 4, [1], 18]


#psudocodice : 

"""
FUNZIONE (LISTA )
    
    TEMP = []
    FOR l IN LISTA   
        IF l != []
            TEMP.APPEND(L)
        i = 0 
        n = len(lista)
        while i < n
            temp = lista 
        i+=1
        // mentre qui eseguo ulterio covntrolli dove controllo la lunghezza della lista 
        // per vedere hanno la stessa lunchezza 
        
        while i < n 
            temp.del(lista[-1])
"""
'''
- CREARE UNA LISTA TEMPORAANEA DOVE APPENDO GLI ELEMNTI 
- CODIZ , VERIFICA SE E' DIVERSO DA [] 
    SE' UGULE A TEMP CHE E' UNA LISTA VUOTA 

-COPIA GLI ELEMENTI DA TEMPP A LISTA, MODIFICANDO LA LISTA ORIGINALE 
- APPENDO A TEMP LE PARTI DELLA LISTA DEI NUMERI 
- CREA UN INDICE PER FAR SCORRERE TEMP  

- USA UN WHILE CHE ITERA FINCHE LA SOLUZIONE IMPOSTA NON SI VERIFICA 
-  CONDIZIONE SARA' CHE SE I E MINORE DI LEN(TEMP)
- devo copiare ttemp sulla lista
- continua ad iterare finche' non ci sono piu' elemnti nella lista 
- poi una volta fatto cio rileggo la lista e gli elemnti trovati li calncello 
    gli ultimi elementi in fondo alla lista 
-   
'''
def cancella_liste_annidate(lista):
   def cancella_liste_annidate(lista):
    """
    Funzione che rimuove tutte le liste vuote da una lista principale.
    
    Parametri:
    lista (list): Lista che può contenere numeri e liste vuote ([]).

    Restituisce:
    list: La lista senza liste vuote.
    """

    tmp = []  # Lista temporanea per raccogliere solo gli elementi validi
    eliminati = []

    for l in lista:  # Itera sugli elementi di lista
        if l != []:  # Se l'elemento non è una lista vuota
            tmp.append(l)  # Aggiunge l'elemento a tmp
            
            '''Aggiungo un else per vede i valori eliminati '''
        else:
            eliminati.append(l)# Se è una lista vuota, la aggiunge agli eliminati
            
        n = len(lista)  # Numero di elementi nella lista
        i = 0  # Inizializza l'indice per iterare
        
        while i < n:  # Loop che dovrebbe modificare lista (ma è errato nel tuo codice)
            tmp = l  # Questo non ha effetto utile, lo manteniamo solo per correggerlo
            i += 1  # Incrementa `i` per evitare loop infinito
        
        while i < n:  # Questo loop cerca di rimuovere elementi ma è errato nel tuo codice
            del lista[-1]  # Se rimanessero elementi in più, li cancella
            i += 1  # Incrementa per evitare loop infinito

    return tmp, eliminati # Restituisce la lista senza liste vuote

'''
Questo approccio qui sopra non funziona 

input_lista= input("inserisci numeri : ")

lista = list(map(int,input_lista.split(",")))

s = cancella_liste_annidate(lista)

print(s)

'''

# === INPUT UTENTE ===
input_lista = input("Inserisci elementi separati da virgole (usa [] per liste vuote): ")
lista = []  # Inizializza una lista vuota che conterrà gli elementi trasformati

for item in input_lista.split(","):# Itera su ogni elemento della stringa divisa dalla virgola
   
    # 🔹 `item` è una variabile che rappresenta un singolo elemento della lista risultante da .split(",")
    # 🔹 .split(",") suddivide la stringa in più elementi separati da virgole
    # 🔹 Esempio:
    # Se input_lista = "3, 10, [], 20, []"
    # Dopo .split(","), avremo questa lista: ['3', ' 10', ' []', ' 20', ' []']
    # Ora `item` assumerà questi valori nel ciclo:
    # - Prima iterazione:  item = '3'
    # - Seconda iterazione: item = ' 10'
    # - Terza iterazione:   item = ' []'
    # - Quarta iterazione:  item = ' 20'
    # - Quinta iterazione:  item = ' []'
    '''Mentre se l'utente si sbaglia e' iserisce uno spazio in piu' servira' fare come qui sotto che: '''
    
    item = item.strip()  # 🔹 Rimuove eventuali spazi extra prima e dopo `item`
    # 🔹 Esempio:
    # - Se item = ' 10', dopo .strip() diventa '10'
    # - Se item = ' []', dopo .strip() diventa '[]'
    if item == "[]":# 🔹 Controlla se `item` è esattamente la stringa "[]"
        
        lista.append([])# 🔹 Se `item` è "[]", lo converte in una vera lista vuota [] e lo aggiunge a `lista`
        # 🔹 Esempio:
        # - Se item = "[]", allora lista.append([]) trasforma la stringa in una lista vuota
        # - Lista dopo questo passaggio: [3, 10, [], 20, []]
     
    else : 
         # 🔹 Tentativo di conversione di `item` in un numero intero
        try:    # nel caso in cui l'utente lo inserisca come una : 
            lista.append(int(item))  # 🔹 Converte `item` in un intero e lo aggiunge alla lista
            # 🔹 Esempio:
            # - Se item = "10", allora int(item) diventa 10 e viene aggiunto a `lista`
            # - Lista dopo questo passaggio: [3, 10, [], 20, []]
        except ValueError:
            lista.append(item)  # 🔹 Se `item` non è un numero, lo lascia come stringa e lo aggiunge a `lista`
            # 🔹 Esempio:
            # - Se item = "ciao", int(item) genererebbe un errore
            # - Il blocco `except` lo mantiene come stringa nella lista
            # - Lista finale: [3, 10, [], 20, [], 'ciao']

# === ESEMPIO DI RISULTATO DOPO IL CICLO FOR ===
# Se l'input era: "3, 10, [], 20, []"
# Il risultato finale in `lista` sarà: [3, 10, [], 20, []]
            

# === CHIAMATA ALLA FUNZIONE ===


# === CHIAMATA ALLA FUNZIONE PER LA PULIZIA DELLA LISTA ===
s, eliminati = cancella_liste_annidate(lista) 
''' Facendo cosi cio' che ho riportato all'interno della funzione alla fine che facevo ritornare i val eliminati  '''

# === Mostro gli elementi eliminati ===
print("\n📌 Elementi eliminati:", eliminati)  # Mostra gli elementi eliminati

# === STAMPA DEL RISULTATO ===
print("Lista pulita:", s)



#=========================================================================================================================

'''Versione piu' semplice con i dati gia' dati : '''

def empty_list(lista):
    tmp = []
    
    for e in lista:
        if e != []:
            tmp.append(e)
            
    i = 0
    while i < len(tmp):
        lista[i] = tmp[i]
        i += 1
        
    # i è la posizione del primo elemento da eliminare da a
    while i < len(lista):
        del(lista[-1])
    return tmp

lista = [3, 11, [4,3], [], 4, [1], 18]
s = empty_list(lista)

print(s)
