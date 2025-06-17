#Esercizio 1: Creare una variabile chiamata nome e assegnargli un valore qualsiasi. Fatto
#ciò mandare a schermo la lunghezza della stringa,.

'''
nome= " pino "

print(len(nome)) # len(nome) permettera` di leggere la lunghezza della stringa, 
'''
# " len " legge quant'e` lunga

#______________________________________________________________________________________________________________________________________________________________________________________

# Esercizio 2: Mandare a schermo la variabile nome tutta in maiuscolo
'''
nome= " pino "

print(nome.upper() )''' #upper permettera` di stampare a schermo in maiuscolo
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Esercizio 3: Sostituire il carattere "a" contenuto nella variabile con "e" e stampare,.
'''
nome= " pino "

print(nome.replace("i","o"))''' #permette di sostituire le lettere


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Esercizio 4: Creare una variabile chiamata frase inserendoci la frase "ciao come stai?".,
#Dividere la frase in una lista di singole parole utilizzando il metodo split( e mandare a schermo il risultato
'''
nome= " pino "
frase = "ei ciaoooooo come va "
print(frase.split())
''' # il metodo "split"  permette di far in modo  che ogni frase sia divisa in una lista cosi` ['ei', 'ciaoooooo', 'come', 'va']
 # puo` essere utile per contare le parole in una frase 
 
 
#_______________________________________________________________________________________________________________________________________________________________________________________

#Esercizio 5: Stampare il numero di parole contenute nella frase mischiando il metodo
#split() per dividere e len() per contare



'''
nome = 'andre'  

frase = "ei ciaoooooo come va ggg" '''  # Stringa contenente una frase

# Utilizzo split() per dividere la stringa in una lista di parole separate dagli spazi

'''lista = frase.split() ''' # La lista risultante sarà: ['ei', 'ciaoooooo', 'come', 'va']

# Utilizzo di len() per calcolare il numero di elementi (parole) nella lista
'''print(len(lista))'''  # Stampa il numero di parole nella lista, ovvero 5

'''______________________________________________________________________________________________________________________________________________________________________---------------______'''

#Esercizio 6: Venticare se frase comincia con "Ciao" utilizzando il metodo startswith()
#e mandare a schermo il risultato booleano

'''
nome = 'andre'  

frase = "ei ciao come va ggg"  # Stringa contenente una frase

# Utilizzo split() per dividere la stringa in una lista di parole separate dagli spazi

lista = frase.split()


print (frase.startswitch('ciao'))'''   #startswitch dira` se c'e` nella frase, se non c'e` dira` false, in caso ci sia dira true ossia che e`presente

# startswitch verrifica che la stringa richiesta sia nella frase, se non c'e` rispondera` False, cerca esattamnte la stringa richiesta,
# creando la variabile lista e ponendola = a frase.split permette si che frase sia seperata a parole.

#Mentre '' print (frase.startswitch('ciao'))  '' facendo cosi` una  lettera Maiscola non viene riconosciuta 
#per renderlo compatibile bisogna fare 

'''nome = 'andre' 
lista = frase.split()

 
 # Definiamo la stringa 'frase' da verificare
frase = "Ciao, come stai?"  '''

# Confronta la stringa 'frase' (convertita in minuscolo) con la parola 'Ciao' (anch'essa convertita in minuscolo)
# .lower() rende entrambe le stringhe minuscole, mentre .startswith() verifica se 'frase' inizia con 'ciao'
 
'''print(frase.lower().startswith('Ciao'.lower()))'''  # Restituisce True se 'frase' inizia con 'ciao', False altrimenti

'''__________________________________________________________________________________________________________________________________________________________________________________________________________'''


#Esercizio 7: Creare la variabile cognome e nome_completo. Assegnare a quest'ultima Ia
# stringa concatenata tra nome e cognome e mandare a schermo,
'''
cognome = "Fazzini"
nome = "Andrea"
nome_completo = nome  + " " + cognome

print(nome_completo) '''

# Cio permette di concatenare le due tringhe separate 



'''__________________________________________________________________________________________________________________________________________________________________________________________________________'''


#• Esercizio 8: Creare la variabile età ed assegnarli in formato numero un valore casuale Mostrare a schermo il nome completo e l'età in una sola stringa di testo,

'''
cognome = "Fazzini"
nome = "Andrea"
nome_completo = nome  + " " + cognome
eta = 40
'''
#print(nome_completo + " " + eta) 
# non si concatenare perche` la variabile eta` non una stringa ma una variabile stringa quindi si fa:
# si fa mettendo eta tra parentesi e aggiungendo str per farlo diventare una stringa str(eta)

'''print(nome_completo + " " + str(eta)) '''



'''__________________________________________________________________________________________________________________________________________________________________________________________________________'''


#Esercizio 9: Mandare a schermo l'ultimo carattere della variabile frase in maiuscolo.

'''
cognome = "Fazzini"
nome = "Andrea"
nome_completo = nome  + " " + cognome
eta = 40

frase = "come stai ???"
print(frase [-1].upper)''' # facendo cosi`  permettera che l'ultimo valore diventi maiscolo concatendolo all'ultima lettera della frase 


'''__________________________________________________________________________________________________________________________________________________________________________________________________________'''


#Esercizio 10: Stampare gli ultimi 2 caratteri della stringa,
'''
cognome = "Fazzini"
nome = "Andrea"
nome_completo = nome  + " " + cognome
eta = 40

frase = "come stai ???"
print(frase [-2:].upper) ''' # facendolo con gli ultimi tre caratteri faro` [-2:] che significa da meno due in poi 




'''__________________________________________________________________________________________________________________________________________________________________________________________________________'''

#Esercizio 11: Stampare la sottostringa compresa tra il terzo ed quinto carattere.

'''
cognome = "Fazzini"
nome = "Andrea"
nome_completo = nome  + " " + cognome
eta = 40

frase = "come stai ?"
print(frase [2:5].upper) ''' # facendo cosi` faro` stampere dal 3 al 4 [2:5] perche i num partono da 0 , il 5 non sara compreso



'''__________________________________________________________________________________________________________________________________________________________________________________________________________'''

#Esercizio 12: Prendere i caratteri da inizio stringa fino a metã. Per trovare la metà dovrete usare len() e fare il casting ad intero,.

cognome = "Fazzini"
nome = "Andrea"
nome_completo = nome  + " " + cognome
eta = 40

frase = "ciao come stai"

# per far si che il valore non sia stampato a mano, si crea una nuova variabile ossia che permette di contare quanti caratteri ci sono  
meta_stringa = int(len(frase)/2)   # la lunghezza che ci interessa e` , lunghezza = 7 indice 0:6
 

# la meta stringa sara` uguale alla lunghezza e si mettera:  len che conta la frase 
#per far si che conti dall'inizio allla meta della frase bisogna : len(frase)/2 , diviso due (fuori)
#si mette in altrimenti uscirebbe 7.0 
#print(meta_stringa)


print (frase[0:meta_stringa]) # cio permettera di stampare a schermo la frse da 0 alla meta : che sara: ciao co
# bisogna inserire la frase e poi mettere dentro alla stinga da dove si vuole richiamare qui da 0: meta stinga.



'''__________________________________________________________________________________________________________________________________________________________________________________________________________'''

# Esercizio 13: Prendere i caratteri da metà stringa tino alla fine.
meta_stringa = int(len(frase)/2) 
print (frase[meta_stringa:])
# facendo cosi` prendera invece da 7 in poi ,(frase[0:meta_stringa:])

'''__________________________________________________________________________________________________________________________________________________________________________________________________________'''
