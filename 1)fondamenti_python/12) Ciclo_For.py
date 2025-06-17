# IL CIClo FOR

# Il ciclo For varia DDAL WWHILE PER QUESTIONE di sintassi per iterazione di una sequenza, mentre nel while abbiamo
# una conddizione che possiamo dare noi, nel For abbiamo iteriamo una sequenza, una lista di valoi che possiamo mandarre
# a schermo o modifica, con il for possiamo passare questi valori  velocemente uno dopo l'altro.


lista_citta = ['milano', 'roma', 'napoli'] 

for citta in lista_citta:# qui nel for diamo nome singolo di un insieme di cose 
    #in lo uso per concatenare le due stringhe 
    print(citta)

'''facendo cosi, stampera' piu' facilmente una lista, creando prima una nuova variabile ossia 'citta' per poi concatenarla
    a 'list_citta', per poi stampare a schermo le citta, (per ogni elemento in collezione ddi eelementi fai qualcosa)
Facenddo cosi manddara' a schermo un insieme di elemnrti definiti in una lista in questo caso '''


#---------------------------------------------------------------------------------------------------------------------------

# con una stringa il for si comporta 


stringa= 'anguria'

for lettera in stringa : # facendo cosi' crea un nuovo elemento per poi concatenarlo alla stringa 
    print(lettera) # facendo cosi' stampera anguria in caratteri, ossia ogni lettera a capo

#---------------------------------------------------------------------------------------------------------------------------
# con range invece in For

# Il Range e' un generatore, si comporta come una lista che va da 0 a al numero che si mettere,
# la cosa che cambia e che vengono generati quando ci serrvo come nel caso qui sotto in x che va da 0 a 5 perche sono 6
# il range ddi 6 valori 

for x in range(6):
    print(x)
#cosi si crea unanuova variabile valida solo nel for e poi si concatena in range dove stampa dei valori da 0 a 5,

#-------------------------------------------------------------------------------------------------------------------------

# come nel while si puo usare ELSE 
#AD ES :
    
for x in range(6):
    print(x)
else: 
    print('ho finito ')
# una volta che haa finito di stampare il range stampa a schermo, ho finito 
#--------------------------------------------------------------------------------------------------------------------------

# si puo anche mettere l'if al suo interno 

for x in range(6):
    if x == 3 :
        break # Una volta che il range arriva a tre esce completamente al programma e non scende nel else 
    print(x)
else :
    print('ho finito ')
    
#---------------------------------------------------------------------------------------------------------------------------

# Con continue nel For , continue una volta che arriva a 3 salta l'iterazione di 3 e va avanti 


for x in range(6):
    if x == 3 :
     continue # con continue saltera' il vaalore 3 una volta che arriva la, per poi ripartire e leggere l'else 
    print(x)
else :
    print('ho finito ')
    
#----------------------------------------------------------------------------------------------------------------------------
# Nel for si possono anche avere diversi loop 

# si possono anche creare multipli for, possono essere utili per creare una tabella a e b con colonne e righe
#ogni riga   

for riga in range (6):
    for colonna in range (6):
        print("(" + str (riga)  + ":" + str(colonna) + ")" ) # cio' permette di stampare righe e colonne di una lsita 
        # di elementi stampati in questo caso una lista da 0 a 6  
        
else:
    print ("ho finito")

#UNa volta che ha stampatole colonne e righe richieste stampa cio che ce scritto nell'else 

    

    
    


