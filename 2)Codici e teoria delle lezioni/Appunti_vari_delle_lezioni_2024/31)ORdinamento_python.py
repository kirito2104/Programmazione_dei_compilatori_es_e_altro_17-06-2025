def f(e):
    '''
    Funzione di trasformazione per il parametro `key` in `sorted`.

    Parametri
    ---------
    e: str
        Una stringa nella forma 'dd-mm-yyyy'.

    Returns
    ---------
    tuple
        Una tupla nella forma ('yyyy', 'mm', 'dd'), dove:
        - Il primo elemento è l'anno.
        - Il secondo elemento è il mese.
        - Il terzo elemento è il giorno.
    '''
    # Slicing della stringa per ottenere 'yyyy', 'mm', e 'dd'
    return (e[6:], e[3:5], e[:2])  # Ordine cambiato per ordinare prima per anno, poi per mese, poi per giorno.

# Lista di date nella forma 'dd-mm-yyyy'
a = ['09-12-2024', '10-12-2022', '18-10-2023']

# Utilizzo della funzione `f` come chiave per ordinare la lista `a`
# La funzione `sorted` usa `key=f` per trasformare ogni elemento in una tupla ('yyyy', 'mm', 'dd') e poi ordina.
print(sorted(a, key=f))  # Stampa la lista ordinata in base all'anno, al mese e al giorno.

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Metodo alternativo per risolvere lo stesso problema senza l'utilizzo del parametro `key` di `sorted`.

# Lista di date nella forma 'dd-mm-yyyy'
a = ['09-12-2024', '10-12-2022', '18-10-2023']

# Inizializza una lista vuota per memorizzare le date trasformate
b = []

# Itera su ogni elemento della lista `a`
for e in a:
    # Divide ogni data in giorno, mese, anno usando `.split('-')`
    # `e.split('-')` restituisce una lista [dd, mm, yyyy].
    # Inverte l'ordine con `[::-1]` per ottenere [yyyy, mm, dd].
    b.append(e.split('-')[::-1])

# Ordina la lista `b` in base all'ordine naturale delle liste nidificate.
# Ogni elemento è una lista del tipo ['yyyy', 'mm', 'dd'].
# Python ordina queste liste comparando gli elementi uno alla volta nell'ordine lessicografico.
b.sort()

# Stampa la lista `b` ordinata.
# Il risultato sarà una lista ordinata in base all'anno, poi al mese, e infine al giorno.
print("Lista ordinata come liste nidificate:", b)

# Lista `c` per trasformare nuovamente le date in formato 'dd-mm-yyyy'
c = []

# Itera su ogni elemento della lista `b`
for i in range(len(b)):
    # `b[i]` contiene una lista del tipo ['yyyy', 'mm', 'dd']
    # Invertiamo di nuovo l'ordine degli elementi usando `'-'.join(b[i])`.
    # `'-'.join(b[i])` combina gli elementi della lista con '-' tra di loro, ripristinando il formato originale.
    b[i] = '-'.join(b[i])

# Stampa la lista trasformata, con le date ritornate nel formato originale ma ordinate.
print("Lista ordinata nel formato originale:", b)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# la list copresion , consente di creare una lista usando un unica stringa 

b = [ e.split('-')[::-1] for e in a  ]

# equivalente  
'''

b = []

for e in a:
    b.append(e.split('-')[::-1])

'''








