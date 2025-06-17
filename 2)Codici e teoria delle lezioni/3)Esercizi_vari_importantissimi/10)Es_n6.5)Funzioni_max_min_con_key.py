

#Esercizio 1 

'''
Scrivere una funzione Min in python che, data in input una lista a
e una funzione key, restituisce l'elemento e in a tale che 
key(e) = min(key(x) per x in a); 
se key è None, restitusce il minimo nella lista.
'''


# come prima cosa definisco la funzione identity all'interno della funzione MAx che restiruisce il valore (e) ossi SE STESSO
# POI DEFINISCO UN UN IF DOVE PONGO key  uguale a None  e poi un key
#poi definsico i due valori v_min con il valare della chive minima e poi r min  con il valore minimo 


"""
a = [('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5)]

funzione  Min (a,key=None):

    def identity(e):
        ritorna e 

    se key == None :
        key = identity 

    V_min = key(a[0]) 
    r_min = a[0]
    
    Per  e in a : 
        se key(e) < V_min 
            v_min, r_min = key(e), e  # Aggiorna sia il valore minimo che l'elemento corrispondente.



"""

def Min(a, Key=None):
    """
    Trova l'elemento con il valore minimo in una lista 'a' utilizzando una funzione di trasformazione 'Key' per il confronto.
    Se 'Key' è None, gli elementi vengono confrontati direttamente nel loro stato originale.
    """

    # Definiamo una funzione locale 'identita' che restituisce l'elemento stesso.
    # Questa funzione sarà utilizzata nel caso in cui l'utente non specifichi un criterio 'Key' per il confronto.
    def identita(e):
        return e  # Restituisce il valore inalterato dell'elemento.

    # Se l'utente non ha fornito una funzione 'Key', allora usiamo 'identita' come comportamento predefinito.
    # Questo significa che gli elementi verranno confrontati direttamente senza alcuna trasformazione.
    if Key is None:  
        Key = identita  # Assegniamo 'identita' come funzione predefinita per Key.
    
    # Inizializziamo la variabile 'v_min' con il valore trasformato (usando Key) del primo elemento della lista.
    # Questo sarà il valore con cui confronteremo gli altri elementi della lista.
    v_min = Key(a[0])

    # Inizializziamo 'r_min' con il primo elemento della lista, in modo che possa essere aggiornato
    # nel caso in cui troviamo un elemento con un valore minore.
    r_min = a[0]

    # Iteriamo attraverso tutti gli elementi della lista 'a'.
    for e in a:
        # Confrontiamo il valore trasformato dell'elemento attuale con il valore minimo registrato finora.
        if Key(e) < v_min:  
            # Se il valore dell'elemento attuale è inferiore al minimo registrato,
            # allora aggiorniamo sia 'v_min' che 'r_min'.
            v_min, r_min = Key(e), e  # Aggiorniamo il minimo attuale e l'elemento corrispondente.

    # Restituiamo l'elemento corrispondente al valore minimo trovato.
    return r_min  

def t1(e):
    """ 
    Funzione di trasformazione che estrae il secondo elemento di una tupla.
    Questa funzione sarà utilizzata come 'Key' per confrontare gli elementi della lista in base alla loro seconda componente.
    """
    return e[1]  # Restituisce il secondo elemento della tupla.

# Definiamo una lista di tuple, in cui ogni tupla contiene una lettera e un numero.
a = [('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5)]

# Trova il valore minimo nella lista senza specificare una funzione 'Key'.
# Poiché non forniamo una funzione di trasformazione, il confronto avverrà direttamente tra le tuple.
print("Ecco il valore minimo:", Min(a))

# Trova il valore minimo utilizzando la funzione 't1' come 'Key'.
# Questo significa che il confronto verrà fatto sulla seconda componente della tupla, ovvero il numero associato alla lettera.
print("Il valore minimo basato sulla seconda componente:", Min(a, Key=t1))

    
print('###############################################################################')

'''

########################################################################################################################################################################################

'''
#funzione Max per trovare il massimo 

def Max(a, key=None):
    """
    Trova l'elemento massimo in una lista 'a' utilizzando 'key' per il confronto.
    Se 'key' è None, gli elementi vengono confrontati direttamente.
    """

    # Definiamo una funzione locale identity, usata solo all'interno di Max.
    # Questo mostra che in Python è possibile definire funzioni dentro altre funzioni.
    
    def identity(e):
        return e  # Restituisce l'elemento stesso (comportamento predefinito se 'key' non è fornita).

    if key is None:
        key = identity  # Se 'key' non è fornita, utilizza la funzione identity.

    v_max = key(a[0])  # Inizializza 'v_max' con il valore chiave del primo elemento.
    r_max = a[0]  # Inizializza 'r_max' con il primo elemento della lista.

    for e in a:
        # Confronta il valore chiave dell'elemento attuale con 'v_max'.
        if key(e) > v_max:
            v_max, r_max = key(e), e  # Aggiorna sia il valore massimo che l'elemento corrispondente.

    return r_max  # Restituisce l'elemento con il valore massimo, non solo il valore trasformato.

def t1(e):
    """ Estrae il secondo elemento della tupla per il confronto numerico. """
    return e[1]

# Lista di tuple contenenti una lettera e un numero.
a = [('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5)]

# Trova il massimo considerando direttamente le tuple.
print('Ecco il valore massimo:', Max(a))

# Trova il massimo basato sulla seconda componente della tupla.
print('Il valore massimo basato sulla seconda componente:', Max(a, key=t1))

"""
Cosa cambia con l'aggiunta di 'v_max'?

1. Separazione tra valore chiave e elemento massimo:
   - La funzione originale restituiva solo il valore massimo calcolato, il che poteva creare ambiguità
     se 'key' trasformava gli elementi (ad esempio, estraendo una parte di una struttura complessa come una tupla).
   - Ora 'v_max' tiene traccia del valore chiave massimo, mentre 'r_max' conserva l'elemento originale.

2. Restituzione dell'elemento originale:
   - 'v_max' viene usato solo per i confronti.
   - 'r_max' mantiene il riferimento all'elemento completo della lista.
   - Questo rende la funzione più versatile, perché restituisce l'intero elemento che ha generato il valore massimo,
     invece di restituire solo il valore numerico trasformato.

In sintesi:
Grazie a 'v_max', possiamo confrontare gli elementi in base ai loro valori trasformati senza perdere il riferimento 
all'elemento originale. Questo migliora la flessibilità della funzione e ne amplia le possibilità di utilizzo in contesti complessi.
"""



####################################################################################################################################################################################################


#Scrivere una funzione in python che, data una lista di interi in input, 
#esegue le seguenti operazioni:

#-rimuove i duplicati dalla lista in input (modificare la lista in input);
#-crea una tupla a partire dalla lista modificata;
#-restituisce l'elemento massimo e l'elemento minimo nella tupla;


'''
Esempio:

Input: [87, 45, 41, 65, 94, 41, 99, 94]

Lista modificata con duplicati rimossi: [87, 45, 41, 65, 99]

Si crea la tupla: (87, 45, 41, 65, 99)

Output: min: 41, max: 99
'''


"""
a = input("inserisci numeri:")
lista_numeri = list (map(int, a.split(',')))


funzione Modifiche_lista(a)
    # si rimuovono i duplicati dalla lista
    # in input (quindi dalla lista a)
   
    i = 0 
    elementi_visti =set()
    while i < len(a)
        j = i + 1
        while j < len(a)
            if a[i] == a[j]:
                del a[j]
            else :
                j += 1
        i += 1
     numbers_tuple = ()
    for e in a:
        # concatenazione di tuple, come le stringhe
        # mettendo la virgola dopo e, convertiamo
        # l'intero e in una tupla
        numbers_tuple += (e,)

    print(numbers_tuple)

    # restituiamo max e min nella tupla
    maximum = max(numbers_tuple)
    minimum = min(numbers_tuple)

    return maximum, minimum
        

complessita' O(n^2)


    
"""
def modifica_lista(a):
    """
    Funzione che rimuove i duplicati da una lista di interi, preserva l'ordine originale,
    crea una tupla dalla lista modificata e restituisce il valore minimo e massimo della tupla.

    Complessità:
    - Rimozione dei duplicati: O(n)
    - Conversione in tupla: O(n)
    - Calcolo di min e max: O(n)
    - Complessità totale: **O(n)** (efficiente rispetto a O(n²) del doppio ciclo `while` iniziale)
    """

    # Creazione di un insieme (set) per tracciare gli elementi già visti
    # Complessità: O(1) per ogni operazione di lookup (controllo "in" e aggiunta)
    elementi_visti = set()

    # Creazione di una nuova lista per mantenere solo i numeri unici, preservando l'ordine
    # Complessità: O(n), dato che iteriamo sulla lista una sola volta
    nuova_lista = []  

    for num in a:
        # Se il numero non è già stato visto, lo aggiungiamo alla nuova lista e al set
        if num not in elementi_visti:  
            nuova_lista.append(num)  # Operazione O(1) per l'aggiunta in lista
            elementi_visti.add(num)  # Operazione O(1) per l'aggiunta in set

    # Conversione della lista senza duplicati in una tupla
    # Complessità: O(n), poiché copia ogni elemento nella nuova struttura dati
    numbers_tuple = tuple(nuova_lista)  

    # Controlliamo se la tupla non è vuota per evitare errori con min() e max()
    if numbers_tuple:
        # Calcolo del valore massimo e minimo nella tupla
        # Complessità: O(n) ciascuna
        massimo = max(numbers_tuple)  
        minimo = min(numbers_tuple)  
    else:
        # Se la tupla è vuota, assegniamo None per gestire il caso limite
        massimo = minimo = None  

    # Restituzione dei valori minimo e massimo come tupla
    return minimo, massimo



