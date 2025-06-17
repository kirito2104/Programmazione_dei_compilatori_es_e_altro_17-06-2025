
# Esercizio 1: 
# Creare una lista di numeri interi e stampare solo gli elementi che sono divisibili per 3.

# Esercizio 2: 
# Creare una tupla di stringhe e stampare solo le stringhe di lunghezza pari.

# Esercizio 3: 
# Creare un set e una lista di numeri interi.
# Stampare solo i numeri che sono presenti sia nel set che nella lista.

# Esercizio 4: 
# Creare un dizionario in cui le chiavi sono stringhe e i valori sono numeri interi.
# Stampare solo le coppie chiave-valore in cui il valore è maggiore di 5.

# Esercizio 5: 
# Creare una lista_di_tupla, in cui ogni tupla contiene due stringhe.
# Stampare le tuple in cui la prima stringa inizia con la lettera 'a'.

# Esercizio 6: 
# Creare un set_di_tuple in cui ogni tupla contiene due numeri interi.
# Stampare le tuple in cui la somma dei due numeri è pari.





#-----------------------------------------------------------------------------------------------------------------------------
# Esercizio 2: 
# Creare una tupla di stringhe e stampare solo le stringhe di lunghezza pari.

tupla_parolaa =('gino','Ginevra','alessio','pino')


for i in tupla_parolaa :
    if len(i) % 2 == 0 : # mettendo len controlleraa' la lunghezza della stringa 
        #e la divera' per due se e' para verraa stampaata 
        print(i)



#-----------------------------------------------------------------------------------------------------------------------------

# Esercizio 3: 
# Creare un set e una lista di numeri interi.
# Stampare solo i numeri che sono presenti sia nel set che nella lista.


# Creazione di un set di numeri
lista_set__numeri = {2, 3, 56, 6, 4, 5, 8, 14, 22}

# Creazione di una lista di numeri
lista_num = [5, 9, 78, 43, 6, 8, 10, 43, 24, 8, 66]

# Iterazione sugli elementi del set
for set in lista_set__numeri:  # Il nome della variabile 'set' è sconsigliato perché è una parola chiave in Python.
    # Controlla se l'elemento del set è presente nella lista
    if set in lista_num:
        # Stampa i numeri che si trovano sia nel set che nella lista
        print('Ecco i numeri:', set)



#---------------------------------------------------------------------------------------------------------------------------------------------------
# Esercizio 4: 
# Creare un dizionario in cui le chiavi sono stringhe e i valori sono numeri interi.
# Stampare solo le coppie chiave-valore in cui il valore è maggiore di 5.


list_dizionario = {
    'num1 :': 8 ,
    'num2 :' : 78 ,
    'num3 :' : 24 ,
    'num4 :': 42 ,
    'num5 :': 3 ,
    
}

for chiave, valore in list_dizionario.items() : # qui creo due variabile, dove definisco, la chiave e il valore 
    # usando items() su list_dizionario, assegnera' alle chiavi e al contenuto di esse, 
    #le vartiabili concatenate 
    if valore > 5 : # In questo If verifico che il valore sia maggiore di 5, se non lo e' non stampa nulla
        print("ecco i numri maggiori di 5:",chiave, valore )
    elif valore < 5 : # in caso sia minore, dira' che e' un val minore di 5 
        print('questo valore e minore di 5 : ',chiave,valore)
    else :
        print('il valore non e un numero' )
     
#---------------------------------------------------------------------------------------------------------------------------------
# Esercizio 5: 
# Creare una lista_di_tupla, in cui ogni tupla contiene due stringhe.
# Stampare le tuple in cui la prima stringa inizia con la lettera 'a'.

# Creazione di una lista di tuple, dove ogni tupla contiene due stringhe
lista_tupla = [('gi', 'Gino'), ('giacomo','luigi'), ('adamo', 'testo') , ('ai')]



# Iterazione su ogni tupla nella lista
for tupla in lista_tupla:
    # Controlla se la prima stringa nella tupla inizia con la lettera 'a'
    if tupla[0][0] == 'a':
        print('Ecco le stringhe che iniziano con "a":', tupla)
        '''
Questa condizione verifica solo il primo carattere della prima stringa della tupla (tupla[0][0]). 
"giacomo", invece, inizia con la lettera 'g', quindi non soddisfa il controllo.'''

       
''' # Commentato perché non necessario o non pertinente al contesto
    elif len(tupla) >= 2:  # Questo controllo non è valido: ogni tupla in lista_tupla ha sempre 2 elementi
        print('Queste stringhe hanno più di 2 elementi:', tupla)'''
        
#-----------------------------------------------------------------------------------------------------------------------------------

# Esercizio 6: 
# Creare un set_di_tuple in cui ogni tupla contiene due numeri interi.
# Stampare le tuple in cui la somma dei due numeri è pari.

# Creazione di un set di tuple, dove ogni tupla contiene due numeri interi
set_di_tuple = {(1, 2), (4, 6), (54, 76), (44, 64)}

# Iterazione su ogni tupla presente nel set
for tupla in set_di_tuple:
    # Somma i due numeri nella tupla e verifica se la somma è pari
    if (tupla[0] + tupla[1]) % 2 == 0:  # La somma è pari se il resto della divisione per 2 è uguale a 0
        # Stampa le tuple in cui la somma dei due numeri è pari
        print('Ecco i numeri con somma pari:', tupla)




































































