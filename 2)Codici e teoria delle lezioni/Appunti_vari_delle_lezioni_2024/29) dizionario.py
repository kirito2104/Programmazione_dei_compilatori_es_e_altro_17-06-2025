def disegna_punti_su_retta(a):
    # Funzione di ordinamento basata sul secondo elemento di ciascuna tupla
    def t1(e):
        return e[1]

    n = len(a)  # Lunghezza della lista di input

    # Ordinamento della lista in base al secondo valore di ciascuna tupla
    b = sorted(a, key=t1)  # Complessità temporale O(n log n), complessità spaziale O(n)

    # Estrazione del valore minimo e massimo dalla lista ordinata
    lx, rx = b[0][1], b[-1][1]

    # i rappresenta l'indice nel vettore b del prossimo punto da stampare
    i = 0  
    for p in range(lx, rx + 1):  # Scorre lungo il range di valori da lx a rx
        # Controlla se il valore corrente coincide con il secondo elemento di una tupla
        if i < n and p == b[i][1]:
            print(b[i][0], end='')  # Stampa il primo elemento della tupla
            i += 1  # Passa alla prossima tupla
        else:
            print('*', end='')  # Stampa un asterisco se non corrisponde a nessuna tupla

    # Complessità: tempo O(n log n + m) nel caso peggiore, dove m è il numero di elementi stampati
    # Complessità spaziale: O(n)

# Esempio di input
a = [('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5)]

# Chiamata alla funzione
disegna_punti_su_retta(a)


'''
 Spiegazione di complessità temporale e spaziale:

- **Complessità temporale** si riferisce a quanto tempo impiega 
un algoritmo a completare la sua esecuzione in relazione alla dimensione dell'input. 
In questo caso, la complessità temporale dell'algoritmo è \( O(n \log n + m) \) 
nel caso peggiore, dove \( n \) è la dimensione dell'input `a` e \( m \) 
è la lunghezza dell'output generato (dato da `rx - lx + 1`). Questo significa che 
l'algoritmo impiega tempo proporzionale al costo di ordinamento (\( O(n \log n) \))
più il tempo necessario per generare l'output.

- **Complessità spaziale** si riferisce alla quantità di memoria 
utilizzata da un algoritmo in relazione alla dimensione dell'input. 
In questo esempio, la complessità spaziale è \( O(n) \), poiché 
l'algoritmo crea una copia dell'array di input `a` e lo ordina.
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#In [dizionario]

a= [ 9,2 , 1 , 8 , 4] # l'insieme 

b = [ 1,7 , 0 ,8 ,2]

# un algoritmo che trovi a intersezione b 
# ovvero  c = [1,2,8]

c= []

for e in a :
    if e in a :
        c.append(e)      
print(c)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#In []

#complessita' temporale (n**2)
# assumiamo len (a) == len (b) di valore n 
# alog 2
a.sort()
b.sort()

print (a)
print (b)
    
i , j = 0,0

while i < len (a) and j < len (b):
    if a[i] == a [j]:
        c.append(a[i])
        i += 1
        j+= 1
    elif a [i] < b[j]:
        print()
    else:
        j+= 1
print (c)


# Complessità: tempo O(n log_2 n + m) nel caso peggiore,
    # spazio O(n) per via del metodo  
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------

# Dizionari

# mapping tra chiavi e valori (k, v)

# d contiene (k0, v0), (k1, v1),...

# proprietà: le chiavi sono univoche ki != kj se i != j

# operazioni: dato un dizionario

# ricerca: k è una chiave del dizionario

# lettura: data una chiave k voglio conoscere il valore associato a k

# l'aggiornamento : k, v


# se k e' una chiave ne viene aggiornato, il valore a v

# altrimenti (k,v) viene aggiunta al dizionario

#cancellazione  :


#se k e' una chiave , elina la coppia (k, v)   
# altrimenti Errore

d = {}  # dizionario vuoto
d = {5: 'cinque', 'uno': 1.0, 'due': (1, 2)}  # inizializzazione di un dizionario con chiavi e valori

print(d, len(d))  # stampa il dizionario e la lunghezza (numero di coppie chiave-valore)

print(5 in d)  # verifica se la chiave 5 è presente nel dizionario (True o False)
print('5' in d)  # verifica se la stringa '5' è presente come chiave nel dizionario (False)

print(d['uno'])  # stampa il valore associato alla chiave 'uno'
# print(d[1])  # Genererebbe un IndexError perché 1 non è una chiave del dizionario

d['uno'] = 'UNO'  # aggiorna il valore associato alla chiave 'uno'
print(d)  # stampa il dizionario aggiornato

d[10] = '2x5'  # aggiunge una nuova coppia chiave-valore (10: '2x5') al dizionario
print(d)

del(d['uno'])  # rimuove la coppia chiave-valore con la chiave 'uno'
print(d)  # stampa il dizionario aggiornato

# del(d['12'])  # Genererebbe un IndexError perché la chiave '12' non è presente nel dizionario
print(d)


'''
### Complessità temporale
- **Accesso (lettura)**: \(O(1)\) nel caso medio e migliore, poiché i dizionari in Python utilizzano tabelle hash che 
consentono di accedere rapidamente al valore associato a una chiave. Tuttavia, nel caso peggiore (molto raro), 
l'accesso può essere \(O(n)\) quando c'è un elevato numero di collisioni.
- **Inserimento**: \(O(1)\) nel caso medio, poiché l'inserimento di un elemento nel dizionario comporta 
il calcolo dell'hash della chiave e il posizionamento del valore appropriato. Nel caso peggiore,
l'inserimento può essere \(O(n)\) se si verificano troppe collisioni.
- **Ricerca**: \(O(1)\) nel caso medio e migliore per la ricerca di una chiave. 
Come per l'accesso e l'inserimento, nel caso peggiore può essere \(O(n)\).
- **Cancellazione**: \(O(1)\) nel caso medio per rimuovere un elemento dal dizionario.
Come per le altre operazioni, nel caso peggiore può essere \(O(n)\).

### Complessità spaziale
- **Memorizzazione**: \(O(n)\), dove \(n\) è il numero di elementi presenti nel dizionario. 
La memoria necessaria dipende dalla quantità di chiavi e valori che il dizionario contiene.

In sintesi, i dizionari in Python sono altamente efficienti per le operazioni di accesso, 
inserimento e cancellazione, con complessità temporali medie costanti \(O(1)\) grazie all'uso delle tabelle hash. 
Tuttavia, possono essere meno efficienti nel caso peggiore a causa delle collisioni.
 '''   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
