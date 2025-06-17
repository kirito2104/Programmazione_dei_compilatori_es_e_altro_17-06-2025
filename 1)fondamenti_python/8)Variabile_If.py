
#Variabile IF
# un if si comporta, ponendogli una codizione, maggiore o minore della variabile o numero posta 
#ad esempio cosi'
x = 11
#l'if finche' e' idententato tutte le codizioni faranno rifermento all' if, se non lo sono saranno ulteriori casi
# quindi se sara' l' inverso il maggiore e quando 10 e minore di 11 stampera ossia cosi' 11 > 10 (11 e' maggiore diu 10)
# stampera a schermo quando sara' cosi'
if x < 10 :
    print('x e minore di 10') # cio non verra' stampato, perche non e' maggiore di 10,
    #solo quando lo sara',verra' stampato
    #mentre se si mettera identato in questo caso quando sara' maggiore  di 10 sara' stampato a schermo
print("e maggiore di 10")

#nel caso nell'if in cui si levi c qui sopra il tab, sara' dell'if , mentre cosi' sara' fuori l'if e sara' un altro caso 
# dara' quindi come risultato  soltanto che e' quella
#---------------------------------------------------------------------------------------------------------------------
# Con l'if bisogna comportarsi in modo particolare, ossia bisognera' creare un Else, 
#per far si che le quando ci siano ulteriori casi a quello qui sotto 
# in caso sia infatti maggiore di 10 
# ad es: if 11 < 10, bisogna mettere un else che permettera' di stampare a schermo e dire che non e maggiore 
# con un altro print, perche' se no stamperebbe soltanto quello sotto l'if perche c'e' solo un primo caso
# qui sotto ecco come si comporta l'if
#bisogna creare un altra variabile ossia x 
if 5 < 10 :
    print("5 e' minore di 10") 
else :
    print ('e maggiore di 10')
    
#____________________________________________________________________________________________________________________

#Operatori di comparazione nell'if

#ci sono diversi operatori di comparazione come: 

# sono : == ,!= , <= , >= 





#--------------------------------------------------------------------------------------------------------------------

#Con l'operatore comparazione ' == ' ad esemp:

# == , puo star a significare e' uguale a 10?
x= 5 

if x == 10 :
  print('condizione verificata')
  
#cosi' non stampera' a schermo nulla siccome non e' uguale a 10, mentre se x lo e' lo stampera' a schermo  
#mentre come riportato qui sotto, si potra dire che lo e' siccome e fuori all'if

if x == 10 :
  
  print('condizione verificata')
print('condizione non verificata')
 
#___________________________________________________________________________________________________________________________

# `!=` (diverso da) 
# infatti nel caso in cui sia diveso da 10, STAMPERA' che e' uguale, mentre se non lo e', dira' diverso  
x = 10

if x != 10:
  print('x è diverso da 10')  # Qui controlliamo se x è diverso da 10 usando l'operatore != (diverso).
  #Se la condizione è vera, questa riga verrà eseguita.
else:
  print('x è uguale a 10')  # Se x non è diverso da 10, verrà eseguito il codice qui. Questo significa che x è uguale a 10.


#Il controllo `if x != 10:` verifica se `x` è **diverso** da 10. L'operatore `!=` 
# serve proprio a confrontare se due valori non sono uguali.

# Poiché `x = 5` è diverso da 10, l'output sarà "x è diverso da 10".
#Se `x` fosse stato uguale a 10, l'`else` avrebbe stampato "x è uguale a 10".
 
 #----------------------------------------------------------------------------------------------------------------------------
 
 # <= (minore o uguale)
x =  8
# in questo caso e' verificata  che e' minore o uguale a 10, mentre se era 10 eraa uguale
if x <= 10 :
    print(" e' verificata ")
else:
    print (' Non e verificata ')

# mentre nel caso in cui non sia verificata,bisognera introdurre

#Elese -> che permetera di stampare a schermo e dire che non e' verificata, solo quando non lo sara'
 
 
#-----------------------------------------------------------------------------------------------------------------------------
 w
  
# >= (maggiore uguale) *sempre da sistra va letto*
 
x = 78
# in questo caso e' verificata  che e'maggiore o uguale a 10, mentre se era 10 eraa uguale
if x >= 10 :
    print(" e' verificata ")
else:
    print (' Non e verificata ')
    
#---------------------------------------------------------------------------------------------------------------------  
# il ciclo Elif 
#in Python, la struttura elif (abbreviazione di "else if") permette di aggiungere condizioni multiple 
# a una struttura di controllo condizionale. Il comportamento di elif è quello di verificare una nuova 
# condizione solo se le condizioni precedenti nella catena if non sono state soddisfatte.
  
'''Elif serve per creare  un nuova codizione per fare in modo che si possa creare un nuova condizione dopo l'if ''' 
  
y = 9
  
if y < 9 :
    print( 'e minore di di 9')  

elif y > 9 :
    print('e maggiore ')
    
elif y == 9  :
    print('qui il risultato e uguale ') 
    # mmmettendo quest'altra condizione, l' else qui sotto non verra' calcolato perche' l'unicaa conzione e quando e' uguale 
    #solo che facendo cosi' comprendo anche nel caso in cui e' uguale, mentre sotto non e' specificato
else :
    print('non e verificato ') # se nessuna delle due condizioni sono verrificate allora stampera cio',
    #quindi prendde tutte le altre condizioni

  
  
  
  
  
  
    
#-----------------------------------------------------------------------------------------------------------------------

#in quest esempio nel caso in cui e minore dira che nella prima condizione  e vera e quindi stampera' true
# mentre se e' maggiore stampera' false, nel caso in cui e' uguale a 10 stampera il secondo elif
y=13
if y < 10:
    print("True")
elif y > 10:
    print("False")
elif y==10:
    print("E' uguale a 10")

 # s = 3 assegnazione
 # y == verifica se la codizione' euguale a tre
 
 # Si possono anche assegnare piu variabili in if

x= 6
 
if 10 <= x <= 20 <= 30 : # e compreeso tra 10 e 20 ed anche 30 , prende quindi un numero in  mezzo
    print('compreso tra 10 e 20 ')

elif 10 >= x >= 20 :
    print('e compreso tra 10 e 20 ') # e compreso tra 10 e 20 e la stessa cosa 

elif 10 == x == 20: # controlla se e uguale a sia di 10 o 20 
    print(' e uguale a 10 o 20  ')

else :
    print('non e compresa')
 
 #-------------------------------------------------------------------------------------------------------------------
 
 #Operatori logici And e Or
# verifiche che le due condizioni siano per poter far si che possa entrare nel if 

# a differenza di prima uso l'and si puo' usare come confronto per verificare che sia compresa tra 10 e 20, 
x = 23
y = 24 
z= 45
if x >=15 and  y <= 30 and z == 40 : # 23 maggiore di 15 e y deve essere minore  di 30 e
    
    print('compreso tra 15 e 30 ') # nel caso in cui qui entrambi i numeri siano verificati restituira che e' compreso 
elif z == 44: 
    print( ' e ugule a 44') # riportera' qui solo quando sara' uguale a z == 44 
else :
    print('non verificata') # nel caso in cui y o x non siano compresi stampera tale condizione, 
    #anche nel caso in cui non verificata che il valore non e' verificato che sia  z = = 40 
     
#-----------------------------------------------------------------------------------------------------------------------------------------------

# Mentre Or 
'''L'operatore logico `or` in Python serve per combinare due condizioni e restituisce 
`True` se almeno una delle condizioni è vera. In altre parole, l'espressione con `or` 
è vera se **almeno una** delle condizioni è vera, altrimenti è falsa. '''

#L'operatore `and`, al contrario, restituisce `True` solo se **tutte** le condizioni combinate sono vere.
# Se anche una sola delle condizioni è falsa, l'espressione con `and` sarà falsa.

### Esempio con `or` e `if`:

#Immagina di voler verificare se un numero `x` è maggiore di 10 **oppure** è un numero pari. Ecco come potresti scriverlo usando `or`:


x = 8

if x > 10 or x % 2 == 0:
    print("La condizione è verificata: x è maggiore di 10 oppure è un numero pari")
else:
    print("La condizione non è verificata")


### Spiegazione:

#- L'espressione `x > 10 or x % 2 == 0` verifica due condizioni:
#  - **Condizione 1**: `x > 10` (è vero se `x` è maggiore di 10).
#  - **Condizione 2**: `x % 2 == 0` (è vero se `x` è divisibile per 2, cioè pari).
#- L'operatore `or` dice che **basta che una delle due condizioni sia vera** affinché l'intero `if` restituisca `True`.
#- Nel nostro esempio, `x = 8`. La prima condizione `x > 10` è **falsa**, ma la seconda condizione `x % 2 == 0` è **vera** perché 8 è un numero pari.
#- Poiché almeno una delle due condizioni è vera, l'istruzione `print("La condizione è verificata...")` viene eseguita.

### Differenza tra `or` e `and`:

# - **`or`**: L'intera espressione è vera se **almeno una** delle condizioni è vera.
# - **`and`**: L'intera espressione è vera solo se **tutte** le condizioni sono vere.

#### Esempio di differenza con `and`:

#Se modifichiamo l'esempio precedente usando `and` invece di `or`:


x = 8

if x > 10 and x % 2 == 0:
    print("La condizione è verificata: x è maggiore di 10 ed è un numero pari")
else:
    print("La condizione non è verificata")


#- In questo caso, entrambe le condizioni devono essere vere affinché l'intero `if` restituisca `True`.
#- Poiché `x = 8` non è maggiore di 10, l'espressione con `and` restituisce **False**
# e verrà eseguito il blocco `else`, quindi il risultato sarà: `"La condizione non è verificata"`.

#In sintesi:
#- Usa `or` quando vuoi che **almeno una** delle condizioni sia vera.
#- Usa `and` quando **tutte** le condizioni devono essere vere.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

x = 11
y = 5 
#(---- > --- maggiore)
if x > 10 and y > 10: 
    print('condiziione verificata') 
# facendo cosi' non ci resituira nulla perche' 5 non e maggiore o uguale a 10 quindi 
#non rientra in questo caso 
    
#------------------------------------------------------------------------------------  
'''Mentre facendo cosi' ci restiura che non e' verificata, perche l'else comprende tutti i casi i nu cui non e maggiore di 10 '''
x = 11
y = 5 

if x > 10 and y <  10: 
    print('condiziione verificata') 
else: 
    print('non vrificata ')


'''In quest'altro caso non cambia nulla perche' y non e minore di 10 '''
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''' qui invece cambia che comprende tutti i numeri che sono maggiori di 10, qui sono compresi solo quelli minori'''
x = 1
y = 2 

if x < 10 and y <  10: 
    print('condiziione verificata') 
else: 
    print('non vrificata ')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Mentre cosi sara verificata solo quando , y e maggiore di 10 '''
x = 1
y = 48 

if x < 10 and y >  10: 
    print('condiziione verificata') 
else: 
    print('non vrificata ')

# AND FUNZIONA SOLTANTO SE ENTRAMBE LE SOLUZIONI SONO VERIFICATE ALTRIMENTI IN SOSTANZA PASSA DIRETTAMENTE AL ELSE -> CHE STAMPA A 
# SCHERMO SOLO QUANDO NON RISPETTA AND

''' AD ES: TABELLE DELLE VERITA' " AND "
    V | F | F 
    F | V | F
    F | F | F
    V | V | V
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MENTRE L' OR ENTRA NELL'IF A PRESCINDERE CHE UNA CONDIZIONE SIA SBAGLIATA O MENO 

# all'or basta che una delle due condizioni sia verificata per entrare nell'If e  stampare a schermo che e verificata 
# PERO' SE ENTRAMBE NON RISPETTANO LA REGOLA IMPOSTA DARA' A SCHERMO, CHE NON E' VERIFICATA 

x = 1
y = 6 

if x < 10 or y >  10: 
    print('condiziione verificata') 
else: 
    print('non vrificata ')
    
# iN QUESTO CASO, NELL'IF LA PRIMA  CONDIZIONE OSSIA X CIOE' 1 E MINORE COME RICHIESTO, NELLLA SECONDA PERO' VIENE RICHIESTO CHE IL VALORE SIA 
# MAGGIORE DI 10 ED INVECE E' MINORE OSSIA 6 (>) MAGGIORE DI 10 , QUINDI NON EVERIFICA LA SECONDA OPZIONE 
''' LA COSA CHE CAMBIA PERO E' CHE L'OR ACCETTA ANCHE UNA SOLA RISPOSTA GIUSTA PER ANDARE AVANTI '''
''' TABELLE DELLE VERITA' " OR "
    F | F | F 
    V | F | V
    F | V | V
    V | V | V                             
'''
# QUI INVECE L'OR SI COMPORTA, NEL CASO IN CUI NESSUNA SIA GIUSTA RESTIRA' CHE NON E VERIFICATA E QUINDI ESCE DALL'IF 


x = 19
y = 9 

if x < 10 or y >  10: 
    print('condiziione verificata') 
else: 
    print('non vrificata ')
# NON E' VERIFICATA PERCHE' SIA NELLA PRIAM CHE NELLA SECONDA, NON RISPETTANO LE CONDIZIONI QUINDI ESCONO DALL'IF 
# NEL PRIMO VIENE RICHIESTO UN NUMERO PIU' PICCOLO DI 10 ED INVECE L'X E 19 CHE 
# MENTRE NEL SECONDO IL 9 E PIU PICCOLO DEL 10 , MENTRE DOVEVA ESSERE MAGGIORE DI 10  
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''In questo caso rimane comunque verificata perche y ossia 24 e maggiore di 10, mentre la seconda non rispetta la condizione '''

x = 11
y = 24

if x == 10 or y > 10 :
    print('e verificata')
else :
    print('non e verificato ')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Mentre cosi non sara' verificata perche nessuna delle due rispetta la condizione '''
x = 11
y = 24

if x == 10 or y == 10 :
    print('e verificata')
else :
    print('non e verificato ')



#_______________________________________________________________________________________________________________________________________________________________________________________________________________________

# IL NOT  ---->>>> ( UNA NEGAZIONE )

# IL NOT NEGA CIO CHE CHIEDE LA CONDIZIONE, E QUINDI SE LA CONDIZIONE , PUO SEMBRARE ERRATA LEGGE COMUNQUE L'IF E VA AVANTI, LA CONTA COME SE FOSSE VERA 

X= 15 
Y = 29 


if not(X > 30 ):
    print('e verificata')
else :
    print('non e verificata')
    
# ed infatti  dira' che tale condizione e giusta, perche nega la condizione che gli viene data 
# qui diventa quindi not folse 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# mentre in questo  caso la condizione dovrebbe essere ver, con il not davanti diventa l'opposto e quindi va avanti e non legge l'if  

X= 15 
Y = 29 


if not(X < 30 ):
    print('e verificata')
else :
    print('non e verificata')

'''
TAB DELLE VERITA'

V| F
F| V


'''
#__________________________________________________________________________________________________________________________________________________________________________________________________________


# SHORT HAND 

# E QUANDO AD ESEMPIO COME QUI SOTTO NELL'IF SI PUO' METTERE IL PRINTF IN UNA RIGA, PERO' DEVE ESSERE SOLO UNO, se si mette un secondo print non verra calcolato  

if x > 10 : print("ciaooo")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

''' SI PUO' ANCHE  FARE COME QUI SOTTO E METTERE PRIMA  IL PRINT E POI L'IF E L'ESE ED IL SUO PRINT, MA NON E MOLTO OTTIMALE '''

print("ciaoo ") if 2 > 10 else  print(" e min")

#cosi e meno intuitivo 


#_____________________________________________________________________________________________________________________________________________________________________________________________________

# GLI IF  INNESTATI (annidati)

x = 9
y = 4
# i num pari danno resto 0 , i dispari resto 1 , divi per 2 , conta il resto praticamente 

if  y % 2 == 0 : 
    print('num pari')

else :
    print ('num dispari')

# facendo cosi' dira che y e un num poro perche il resto di quattro e 0 , mentre 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# volendo si puo fare anche quando e pari controlla in un nuovo if , verificando che se e minore o pari a 10  stampando cio che ce sotto  l'if 
# mentre nel caso in cui sia solo pari non minore o uguale a 10 scende nel else 

y = 12

if  y % 2 == 0 : 
    if ( y <= 10 ):
        print('il numero e pari e minore di 10  ')
    else :
        print(' e solo paro il numumero.')
        
else :
    print ('num dispari')












