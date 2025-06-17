#- **Esercizio 1**:Creare una variabile paarola con un volore casuale.
# Mandare a schermo ciascuna lettera della parola.

parola = 'edoardo'
for lettura in parola :
   print(lettura)
#facendo cosi' stampa a schermo la stringa lettera per lettera 

#----------------------------------------------------------------------------------------------------------------------------
#- **Esercizio 2**: Creare una variabile `lista` con valori a scelta e mandarla a schermo con un ciclo for.

lista_citta = ['napoli',"livorno",'Palermo']

for citta in lista_citta :
    print(citta)
else: print(' ecco le citta')

# facendo cosi' stampera' a schermo la lista delle citta, concatenata alla nuova variabile citta'


lista = [7,39,90,0,234,35]

for valore in lista :
    print(valore)
else: print(' ecco i valori')
#qui stessa cosa , con numeri interi pero'

#------------------------------------------------------------------------------------------------------------------------------
#- **Esercizio 3**: Mandare a schermo solo i numeri pari nel `range()` tra 5 e 100 (non compreso).


for valore in range (5,100) : # facendo cosi' gli diro ddi fare un range da 5 a 100 ossiaa da 4 a99 
    if valore % 2 == 0 :
        print(valore)
else: print('ecco i valori nel range tra 5 e 100, pari') # mettenddo tab lo stamperebbe per ogi valore, 
    #ogni volta che fa il range stampi solo i valori pari 


#--------------------------------------------------------------------------------------------------------------------------------

#- **Esercizio 4**: Stampare con `print()` tutti i nomi delle celle di una scacchiera sapendo che 
# le righe sono numerate e le colonne nominate con lettere.
righe = range (1,9)
colonne = 'abcdefgh' #si poteva anche fare anche una stringa , cosi' ['a','b','c','d','e','f','g','h']

for colonna in colonne : # non va stampata la colonna, ma riga e colonna insieme come nel print qui sotto
    for riga in righe:
        print(colonna + str(riga))
    # print(riga) facendo cosi' stampera la riga sotto , bisogna unirle pero' come qui sopra 

'''Facendo cio stampera ad es a1,a2, b1,b2 '''

#-------------------------------------------------------------------------------------------------------------------------------
#- **Esercizio 5**: Creare una `lista = ["parola", "parola", ...]` inserendo un numero a piacere di parole. ]
# Mandare a schermo tutte le parole con lunghezza pari ed in aggiunta le singole vocali che le compongono.

list_parole =['rossi','luca','edoardo', 'marco', 'anna']

print('ecco le parole: ')
for parole in list_parole : #concatena le due variabili 
    if len(parole)% 2 == 0 : # facendo cio divideraa la lista sopra delle in due per poi restiure che sono pari, 
        #le parole che pari, stampandole poi qui sotto 
        #LEN misura la lunghezza della stringa 
        print(parole)
        for lettura in parole : # concateno la nuova variabile a parole, (quella creata precedentemente nel for)
            if lettura in 'aeiou':# facendo cosi' stamapera' anche le vocali che le compongono
                print(lettura)
#----------------------------------------------------------------------------------------------------------------------------
#- **Esercizio 6**: Creare due liste di numeri separate. Iterare la prima lista e mandare a schermo 
# i numeri solo se fanno parte anche della seconda.

# Definizione della prima lista di numeri
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 32]

# Definizione della seconda lista di numeri
list2 = [32, 3, 0, 4, 56, 42, 54, 12, 1, 2, 3, 4]

# Messaggio per indicare il risultato atteso
print('Manda a schermo i numeri solo se fanno parte anche della seconda')

# Iterazione attraverso gli elementi della prima lista
for valore in list1:
    # Verifica se l'elemento della prima lista è presente anche nella seconda
    if valore in list2:
        # Stampa del valore se si trova in entrambe le liste
        print(valore)






