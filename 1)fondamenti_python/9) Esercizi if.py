
# Esercizio 1: Scrivere un programma che chieda all'utente di inserire un numero intero.
# Se il numero è pari, stampare "Il numero è pari", altrimenti stampare "Il numero è dispari".
# Prendere la risposta dell'utente assegnando alla variabile `numero` il metodo 
# input("inserire qui domanda per utente") con il giusto tipo di dato.


'''CREIAMO UNA VARIABILE DI NOME : NUMERO , L'ABBIAMO RESA UNA FUNZIONE INPUT, PER POI CASTARLA IN UN INTERO   '''

numero = int (input ('inserisci un numero intero:')) 

''' L'INPUT SERVE PER FAR SCRIVERE ALL'UNTENTE A SCHERMO CIO' CHE SI VUOLE CHIEDERE '''
#----------------------------------------------------------------------------------------------------------------------------------
''' POI CREO UN IF CHE '''
''' il resto tra la divisione e il numero deve essere 0 per essere pari, mentre se e' dispari e 1 o piu' '''

numero = int (input ('inserisci un numero intero:')) 

# come prima cosa dichiaro una variabile , poi mando in input, cio che deve essere stampato, e lo dichiaro come numero intero 
# bisogna subito convertirlo per evitare che sia una stringa
''' POI CREO UN IF CHE '''

if numero % 2 == 0 :    # IN QUESTO IF FACCIO UN DIVISIONE CHE RICHIEDE IL RESTO , E UNA VOLTA FATTA SE E' 0 SCENDE NELL'IF E STAMPA, CHE E' PARO
    #S E NON E' PARO SCENDE SOTTO NELL'ELSE 
    print('il num e paro ')
else :
    print('il nume disparo ')
    
    
    
    




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Esercizio 2: Chiedere all'utente di inserire un numero intero compreso tra 1 e 10.
# Se il numero inserito dall'utente è compreso in questo intervallo, stampare "Numero valido",
# altrimenti stampare "Numero non valido".


numero = int (input ('inserisci un numero intero , compreso tra 1 e 10 :')) # come prima cosa dichiaro una variabile , poi mando in input, cio che deve essere stampato, e lo dichiaro come numero intero 
# bisogna subito convertirlo per evitare che sia una stringa

#(<)minore
#(>) maggiore 
''' POI CREO UN IF CHE dove racchiudo numero tra 1 e 10 '''

if  1 <= numero <= 10 : # qui richiedo che il numero sia compreso tra 1 e 10  , quindi che 1 (sia minore o uguale ) a numero e che numero ( sia minore o ugule) a 10
     
    print ('il numero  e valido')
else :
    print (' non e` valido ')






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Esercizio 3: Chiedere all'utente di inserire una lettera.
# Se la lettera inserita è una vocale, stampare "La lettera è una vocale",
# altrimenti stampare "La lettera non è una vocale".

#(<)minore
#(>) maggiore 

lettera = (input(' inserire una lettera:  '))

# il metodo In viene usato per confrontare la stringa, i questo caso lettera  con "aeiou" 
# con lower permette anche se e minuscolo il carattere inserito , consentisce di leggerlo comunque 

if lettera.lower() in 'aeiou':   # cio' permette di controllare se la lettera e` una vocale o no, 
    #con il controllo apposito ossia il metodo ' in ' la stringa posta succesivamente ossia le vocali 
    #lower permette 
    print('La lettera è una vocale')
else :
    print ('La lettera non è una vocale')



'''
1. **`input()`**:
   - Utilizzato per ricevere un input dall'utente.
   - Qui stiamo chiedendo all'utente di inserire una lettera.

2. **`.lower()`**:
   - Metodo applicato alle stringhe che converte tutti i caratteri della stringa in minuscolo.
   - È utile per uniformare il confronto tra lettere maiuscole e minuscole.

3. **`in`**:
   - Operatore che verifica se un elemento è presente in una sequenza (come una stringa).
   - In questo caso, viene utilizzato per controllare se la lettera inserita dall'utente è presente nella stringa `consonanti` o `vocali`.
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Esercizio 4: Prendendo un numero come input, verificare se si tratta di un valore
# compreso tra 1 e 10, tra 11 e 50 oppure maggiore o uguale a 51.
# Se nessuna di queste tre opzioni si verifica, controllare se si tratta di 0 oppure di un numero negativo.
# Per ogni casistica, mandare a schermo un messaggio.

''' esempio dicome potrebbe essere '''
#(<)minore
#(>) maggiore
'''
if 1 <= numero <= 10:
    print("compreso tra 1 e 10")
elif 11 <= numero <= 50:
    print("compreso tra 11 e 50")
elif numero >= 51:
    print("maggiore di 51")
else:
    if numero ==  0:
        print("è zero")
    else:
        print("è negativo")
'''
#if 1 <= numero <= 10 and 11 <= numero <= 50 and numero >= 51:
''' potrebbe andare bene solo che con l'and servirebbero piu` variabili quindi si opta per spezzare cio facendo piu controlli '''
'''con un or si sarebbe potuto fa, ma anche cosi` :'''

numero = int(input(" inserire valore: "))


if 1 <= numero <= 10 : # nel primo solo i num compresi tra 1 e 10 
    print ('il numero e compreso tra 1 e 10') 
elif  11 <= numero <= 50 : # qui comprede solo i numeri compresi tra 1 e 50 
    print (" il numero e` compreso tra 11 e 50 ") 
elif numero >= 51: # qui chide se numero e maggiore o ugule a 51 
    print('il numero e` maggiore o ugule a 51 ')
 # in questi tre cicli ho fatto in modo che determinati numeri  sia compresi, e se restituisco una determinata risposta diversa , in base a cio che chiede l'utente 
if  numero == 0:
    print('il numero e` 0')
else :
    print('il nume e negativo ')  
    # queste due in caso siano minori  di 0 entrera` nell'if se no va oltre , questa e` l'opzione migliore
    
#elif numero == 0 or numero <= 1: print ('il nume e 0 o e negativo ')
# si puo anche fare cosi ma l'esercizio vuole che di a due risposte separate 

'''
if  numero == 0:
    print('il numero e` 0')
if  numero <= 1:
    print('il nume e negativo ')  
'''# puo andare bene ma in parte perche` comprederebbe anche lo 0 se e minore di 1

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Esercizio 5: Stiamo comprando una maglietta per regalarla ad un amico e sappiamo
# che il suo colore preferito è nero e la taglia è M, però apprezza anche magliette più larghe di una taglia.
# Creare quindi un programma che ricalchi il nostro ragionamento in negozio,
# mandando a schermo se abbiamo comprato o meno il regalo.
maglietta = 'nero' 
taglia = 'M'

# nella funzione qui sotto  gli pongo due condizioni con l'and
#con l'and le entrambe opzioni devono essere vere per far si che entri nell'if, se non sono vberificate 
# scende e va nell'else 
# nell'if si puo anche mettere all'interno di un and con piu' opzioni, 
#in questo programma infatti viene richiesto che la taglia della maglietta puo' essere anche 'l'
#quindi all'interno dell'and, metto anche or dove almeno un opzione deve essere verificata , per leggere l'if ,
# altrimenti va avanti   

if maglietta == 'nero' and (taglia == 'M' or taglia == 'L'): # qui controlla che le taglie siano M  o L , altrimenti non e' verificata 
    print ('il colore e nero')
else : 
    print(" non compro la maglietta ")




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Esercizio 6: Chiedere all'utente di inserire prima un numero e successivamente una lettera.
 Se l'utente ha inserito più di una lettera o il numero è negativo,
 mandare a schermo "Valori non validi". Nel caso in cui i valori siano validi, mandare a schermo "Ok".

se: il numero è minore di 10 e pari mentre la lettera una tra "m", "p" o ""

il numero è compreso tra 50 e 70 e la lettera non è una vocale

il numero inserito e minore o pari alla lunghezza -1 i alfabeto_inglese. Inoltre se il
numero e la lettera combaciano con indice e risultato di alfabeto_inglese, ad
esempio se inserisco come numero 5 e lettera f e scrivo
alfabeto_inglese[numero]== lettera (True perchè f è indice 5).
'''
 
numero = int(input('inserire un numero :'))
lettera = input("inserire lettera :")
alfabeto_inglese ='abcdefghijklmnopqrstuvwxyz'
#LEN CONTROLLA LA LUNGEZZA DEI CARATTERI DI LETTERA  

# in serve per unire due 
# IN QUESTO IF A DIFFERENZA DEGLI ALTRI ESERCIZI CONTROLLA CHE I NUMERI, NON SIANO NEGATIVI E CHE LA LETTERA NON SIA MAGGIORE DI 1
#SE LO SONO ENTRA NELL'IF, SE NON LO SONO VA NELL'ELSE E QUINDI SONO OK , CONTROLLA SOLO CHE NON SIANO NUM. NEGATIVI E LETTERE PIU GRANDI DI UN CARATTERE  

if numero < 0 or len(lettera)> 1 : # CONTROLLA CHE IL VALORE NON SIA NEGATIVO O CHE LA LUNGHEZZA DELLA LETTERA NON SIA PIU DI 1 CARATTERE
    print("Valori non validi")
else :
    if numero < 10 and numero % 2 == 0 and lettera.lower in 'mpz': 
        # qui controlla che il numero sia minore di 10 e poi viene diviso per 2 , se non e pari 
        #scende dall'if , se le lettere mpz e compreso in questo caso altrimenti scende 
        print('ok')
    elif  50 <= numero <= 70 and lettera not in 'aeiou': #(non essere aeiou )
        # qui controllaa che il numero sia compreso tra 50 e 70 , se non lo e' va avanti,
        # poi controlla anche che la lattera non sia eiou, se non lo sono e ok   
        print('ok 2')
    if numero <= len(alfabeto_inglese) - 1 and alfabeto_inglese[numero] == lettera: #chiede che se il numero e compreso tra 1 e 25(che  dovrebbe essere 26, ma e' meno 1 quindi e 25)
        # len controlla la lunghezza dell stringa alfbeto inglese che deve essere compresaa traa 1 e 25
        # mentre poi dopo qui ' alfabeto_inglese[numero] == lettera' controlla che la lettera sia compres sempre tra 1 e 25 
        # dopo di che controlla anche  la lettera se e la posizione giusta, altrimenmti va avanti e all'if
        print('ok 3') 
    
        
    else :
        print('no')
 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#la funzione *** isalpha *** cpontrollaa che il carattere scritto sia una lettera dell'alfabeto, se non lo e' staampa 
# false se lo e' invece restituisce True 
# 

carattere = input("Inserisci un carattere: ")

if carattere in "aeiou":
    print("Il carattere inserito è una vocale")
elif carattere.isalpha():
    print("Il carattere inserito è una consonante")
else:
    print("Il carattere inserito non è una lettera")