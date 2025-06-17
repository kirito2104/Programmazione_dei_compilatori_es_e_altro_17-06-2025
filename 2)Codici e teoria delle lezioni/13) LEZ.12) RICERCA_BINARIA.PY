
'''RICERCA BINARIA '''
#La **ricerca binaria** è un algoritmo efficiente utilizzato per trovare un elemento all'interno di una lista **ordinata**.
#Funziona dividendo ripetutamente l'intervallo di ricerca a metà, fino a trovare l'elemento desiderato o determinare che non è presente.

# Come funziona
#Supponiamo di cercare un elemento \( x \) in una lista ordinata \( L \):

#1. **Condizione iniziale**: Si parte con l'intervallo che comprende l'intera lista.
  # - Indici: \( \text{inizio} = 0 \) e \( \text{fine} = \text{lunghezza della lista} - 1 \).

#2. **Passo iterativo**:
  # - Calcola l'indice dell'elemento centrale:  
   #  \( \text{centro} = \lfloor (\text{inizio} + \text{fine}) / 2 \rfloor \).
   #- Confronta l'elemento centrale \( L[\text{centro}] \) con \( x \):
   #  - Se \( L[\text{centro}] == x \): hai trovato l'elemento.
   #  - Se \( L[\text{centro}] < x \): il valore cercato è nella **metà destra** della lista. Aggiorna \( \text{inizio} = \text{centro} + 1 \).
   #  - Se \( L[\text{centro}] > x \): il valore cercato è nella **metà sinistra** della lista. Aggiorna \( \text{fine} = \text{centro} - 1 \).

#3. **Condizione di arresto**:
 #  - Se l'intervallo diventa vuoto (\( \text{inizio} > \text{fine} \)), significa che \( x \) non è nella lista.


# Condizioni d'uso
#1. La lista deve essere **ordinata**.
#2. È più efficace su dataset grandi rispetto a una ricerca lineare (\( O(n) \)).

#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================


'''# In una Ricerca Binaria: '''

# Abbiamo dei valori su una retta ad es, NEL CASO IN CUI DOBBIAMO RICERCARE K=4 
# IN UNA LISTA DI NUMERI LA LISTA DEGLI ELEMENTI SARA' DIVISA IN DIVERSI ELEMENTI 
# OGNI SEGMENTO AVRA' UN RANGE DI NUMERI 
# PARTO DAL PRIMO NUMERO 

'''Rappresentiamo il caso della **ricerca binaria** su questa lista ordinata con i valori:

L=[ − 2 ,3 ,9 ,12 ,13 ]
L'indice corrispondente ai valori è:

Indici= [−1,0,1,2,3,4]
Indici=[− 1 ,0 ,1 ,2 ,3 ,4 ]

### Passaggi della Ricerca Binaria con \( K = 4 \)

1. **Intervallo iniziale**:  
   - Inizio: indice \( -1 \) (corrisponde al valore iniziale immaginario).
   - Fine: \( +INFINITO) (corrisponde al valore massimo).

2. Passo successivo :

L'indice centrale viene calcolato come:
Centro =⌊(inizio + Bene)/2⌋
Centro=⌊( inizio+bene ) /2 ⌋


---

Se vuoi posso fare una rappresentazione dei passaggi completi visivi'''

#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================
#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================
#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================
#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================
#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================
#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================


'''# In una Ricerca Binaria: '''

# Abbiamo dei valori su una retta ad es, NEL CASO IN CUI DOBBIAMO RICERCARE K=4 
# IN UNA LISTA DI NUMERI LA LISTA DEGLI ELEMENTI SARA' DIVISA IN DIVERSI ELEMENTI 
# OGNI SEGMENTO AVRA' UN RANGE DI NUMERI 
# PARTO DAL PRIMO NUMERO DEL SEGMENTO FINO AD ARRIVARE LA FINE 
# SE CI SONO N SEGMENTI IN TEMPO LINEARE IN N, TROVO LA SOLUZIONE 
# CI DA UN INPUT LINEARE , NON E' BUONO PERCHE'  L'INPUT 

# UNA VOLTA CHE K =4   E' STATO CONFRONTATO AD ES CON 9, NON SENSO CONFRONTARLO CON ALTRI 



'''#Dati iniziali'''

#K = 4 (elemento da cercare)
#α = D[-2, 3, 0, 12, 13] (array ordinato)
#Intervallo su una linea numerica
#− ∞  0  1  2  3  4  +∞

#Valori associati: -2, 3, 9, 12, 13

'''Condizione iniziale'''
#K viene confrontato con i valori 3 e 9 , quindi sarà racchiuso nel range :

#un [ P ]≤E≤una [ P+1 ]



'''DOPO DI CHE, DEFINISCO : L e R '''

#Introduciamo L (Sinistra) e R (Destra) come gli estremi dell'intervallo di ricerca.
#All'inizio:

#Lx = 0 (indice sinistro)
#Rx = len(α) - 1 (indice destro)

'''#Ciclo WHILE'''
#La sequenza continua a dividersi finché non si trova l'intervallo corretto:
#Mentre Lx<La risposta è:

#Calcoliamo il punto medio:

'''La x= 
Lx+La risposta è/2
 
Condizioni di controllo :

Se E=α [ C x ]:

Ritorno 

α [ EP ]
Altrimenti :
Se K non è
α [ C x ], si restringe l'intervallo e si continua a dividere fino a trovare l'intervallo corretto.


'''

#PSUDOCODIFICA : 
'''Lx = 0
Rx = len(α) - 1

While Lx < Rx:
    Cx = (Lx + Rx) / 2
    If K == α[Cx]:
        Return (α[Cx], α[Cx+1])
    ELIF K < A [Cx]
        Rx= Cx-1
    else :
        lx = cx +1 
        
'''

# RAPPRESENTAZIONE GRAFICA : 


'''
Una linea rappresenta l'intervallo corrente, con il punto medio La x come riferimento centrale

Lx       Cx       Cx+1       Rx
|--------|--------|----------|
α[Lx]    K       α[Cx+1]    α[Rx]

Nota :
EP si trova al centro dell'intervallo e rappresenta il valore calcolato dal punto medio.


Lx       Cx       Cx-1       Rx
|--------|--------|----------|
α[Lx]    K       α[Cx-1]    α[Rx]

'''

#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================
#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================
#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================
#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================
#=-=-=-=-==-=--==--==--==--=-=-=-=-=-====================================================================================================================================================================================================================================


'''# In una Ricerca Binaria: '''

# Abbiamo dei valori su una retta ad es, NEL CASO IN CUI DOBBIAMO RICERCARE K=4 
# IN UNA LISTA DI NUMERI LA LISTA DEGLI ELEMENTI SARA' DIVISA IN DIVERSI ELEMENTI 
# OGNI SEGMENTO AVRA' UN RANGE DI NUMERI 
# PARTO DAL PRIMO NUMERO DEL SEGMENTO FINO AD ARRIVARE LA FINE 
# SE CI SONO N SEGMENTI IN TEMPO LINEARE IN N, TROVO LA SOLUZIONE 
# CI DA UN INPUT LINEARE , NON E' BUONO PERCHE'  L'INPUT 

# UNA VOLTA CHE K =4   E' STATO CONFRONTATO AD ES CON 9, NON SENSO CONFRONTARLO CON ALTRI 

#PSUDOCODIFICA : 
'''Lx = 0
Rx = len(a) - 1

While Lx < Rx:
    Cx = (Lx + Rx) / 2
    If K == a[Cx]:
        Return (a[Cx], a[Cx+1])
    ELIF K < A [Cx]
        Rx= Cx-1
    else :
        lx = cx +1 
lx = rx 
1) al  caso prec k < a[cx]  e k>a [cx]
                  (  k < a[cx] <= k <= a[cx] output[lx,cx] )

2) ( a[cx] < k < a[rx] output [cx,rx] )                 
                     



'''
#========================================================================================================================[=====================================================================================================================================================================================================]


''' Ricerca Binaria: '''
# si chiama ricerca binaraia perche' ogni confronto, mi divide l'intervallo in parti uguali, 
# quindi butto un parte dell'input e' mi concentro sui una seconda parte, fintanto che l'ouput non diventa nullo come dimensione 


# la velocita' cresce esponenzialmente sulla velocita' 



a = [ -2,3, 9 , 12 , 13 ]

k = 4 

lx , rx = 0, len(a)-1 
'''# Inizializzazione degli estremi dell'intervallo di ricerca
Lx = 0                   # Lx (Left): indice sinistro dell'intervallo, inizia da 0
Rx = len(a) - 1          # Rx (Right): indice destro, inizia dall'ultimo elemento dell'array a

'''

while lx <= rx :
     # Calcolo del punto medio (cx)
    cx = int((lx + rx) / 2) 
    # metto int perche' prende solo la parte intera del numero
    # Il punto medio viene calcolato come media tra lx e rx
                             # La funzione int() assicura che il risultato sia un numero intero

'''
quando la sequenza non si potra' piu' dividere  avreo' trovato
l'intervello che conteine il mio punto andro' avanti fino a tanto che si potra' piu' dividere,
voglio diminuire il range e' introduco il punto medio.     
'''


#======================================================================================================================================================================================================================================================================

# Array ordinato di partenza
'''1)inizio del codice e '''
a = [-2, 3, 9, 12, 13]  # Lista ordinata di elementi su cui fare la ricerca
k = 4                   # Elemento da cercare nell'array

# Inizializzazione degli estremi dell'intervallo di ricerca
lx, rx = 0, len(a) - 1   # lx = indice più a sinistra (inizia da 0)
                         # rx = indice più a destra (lunghezza dell'array - 1)

'''
Spiegazione dell'inizializzazione:
- Iniziamo con lx = 0 (primo elemento) e rx = len(a) - 1 (ultimo elemento).
- Questo significa che l'intervallo iniziale copre **tutto l'array**.
- Man mano che il ciclo procede, lx e rx verranno aggiornati per restringere l'intervallo.
'''

# Ciclo di ricerca binaria
while lx < rx:  
    # Calcolo del punto medio (cx)
    cx = int((lx + rx) / 2)  # Il punto medio viene calcolato come media tra lx e rx
                             # La funzione int() assicura che il risultato sia un numero intero

    '''
    Spiegazione del punto medio:
    - Prendiamo il punto medio dell'intervallo [lx, rx].
    - Questo punto divide l'intervallo in due metà:
        - La metà sinistra: da lx a cx
        - La metà destra: da cx+1 a rx
    - A ogni iterazione, controlleremo il valore in posizione cx per determinare 
      quale metà dell'intervallo contiene il valore cercato (k).
    '''     

    if k == a[cx]:  # Controlla se l'elemento cercato K è uguale al valore nell'array a alla posizione cx
    # Se la condizione è vera, significa che abbiamo trovato il valore cercato
        print((a[cx], a[cx+1]))  # Stampa il valore trovato (a[cx]) e il valore successivo nell'array (a[cx+1])
        #stampo una coppia 
        break
    elif k < a[cx]:
        rx = cx -1 
    else : 
        lx = cx +1 
if k < a[cx]:
    print((lx,cx))
elif k > a[cx]:
    print((cx, rx))






#====================================================================================================================================================================
# Array ordinato di partenza
''' 
2) qui completo il codice con pero' un problema nella stampa 
'''
a = [-2, 3, 9, 12, 13]  # Lista ordinata di elementi su cui fare la ricerca
k = 4                   # Elemento da cercare nell'array

# Inizializzazione degli estremi dell'intervallo di ricerca
lx, rx = 0, len(a) - 1   # lx = indice più a sinistra (inizia da 0)
                         # rx = indice più a destra (lunghezza dell'array - 1)

'''
Spiegazione dell'inizializzazione:
- lx rappresenta l'estremo sinistro dell'intervallo da controllare, inizialmente 0 (primo indice dell'array).
- rx rappresenta l'estremo destro dell'intervallo da controllare, inizialmente len(a)-1 (ultimo indice dell'array).
- L'intervallo di ricerca iniziale include tutti gli elementi dell'array.
- Durante il ciclo, lx e rx vengono aggiornati per restringere l'intervallo in cui cercare il valore.
'''

# Ciclo di ricerca binaria
while lx < rx:  
    # Calcolo del punto medio (cx)
    cx = int((lx + rx) / 2)  # Il punto medio viene calcolato come media tra lx e rx
                             # La funzione int() assicura che il risultato sia un numero intero

    '''
    Spiegazione del punto medio:
    - cx rappresenta l'indice centrale dell'intervallo corrente.
    - A ogni iterazione, l'intervallo [lx, rx] viene diviso in due metà:
        - Metà sinistra: da lx a cx (incluso cx).
        - Metà destra: da cx+1 a rx.
    - L'algoritmo controlla il valore in cx per determinare se il valore cercato (k):
        - È uguale a a[cx] → abbiamo trovato il valore.
        - È maggiore di a[cx] → ignoriamo la metà sinistra e restringiamo l'intervallo a [cx+1, rx].
        - È minore di a[cx] → ignoriamo la metà destra e restringiamo l'intervallo a [lx, cx-1].
    '''     

    if k == a[cx]:  # Controlla se il valore cercato k è uguale al valore al punto medio
        # Se k è uguale a a[cx], abbiamo trovato il valore cercato
        print((a[cx], a[cx+1]))  # Stampa il valore trovato (a[cx]) e il valore successivo nell'array
        # Stampiamo una coppia contenente il valore trovato e il valore successivo nell'array
        break  # Uscita immediata dal ciclo, poiché il valore è stato trovato
    
    elif k < a[cx]:  # Se k è minore del valore al punto medio
        rx = cx - 1  # Riduciamo l'intervallo spostando rx alla posizione immediatamente precedente al punto medio
        '''
        - Se k è più piccolo di a[cx], possiamo ignorare il valore al punto medio (cx) e tutti i valori a destra di cx.
        - Aggiorniamo rx a cx - 1, restringendo l'intervallo alla metà sinistra escluso il punto medio.
        '''
    else:  # Se k è maggiore del valore al punto medio
        lx = cx + 1  # Riduciamo l'intervallo spostando lx a destra del punto medio
        '''
        - Se k è più grande di a[cx], possiamo ignorare tutti i valori a sinistra di cx (incluso cx stesso).
        - Aggiorniamo lx a cx+1, restringendo l'intervallo alla metà destra.
        '''

# Controllo finale dopo la fine del ciclo
if k < a[cx]:  # Se k è minore del valore al punto medio
    print((lx, cx))  # Stampiamo lx e cx, rappresentando l'intervallo in cui potrebbe trovarsi k
elif k > a[cx]:  # Se k è maggiore del valore al punto medio
    print((cx, rx))  # Stampiamo cx e rx, rappresentando l'intervallo in cui potrebbe trovarsi k

'''
Spiegazione del controllo finale:
- Dopo la fine del ciclo, lx >= rx. Il ciclo termina quando l'intervallo non è più divisibile.
- Se non troviamo il valore k durante il ciclo:
    - Stampiamo un intervallo che identifica il punto in cui k si troverebbe se fosse presente nell'array.
    - Questo intervallo è rappresentato da lx e cx (o cx e rx) in base al confronto finale.
'''

#============================================================================================================================================================


### **Spiegazione Approfondita del Codice**

'''Questo codice implementa una **ricerca binaria** per trovare un valore specifico \( k \) 
in un array ordinato \( a \). La ricerca binaria funziona dividendo ripetutamente l'intervallo 
di ricerca in due metà e concentrandosi su una delle due, basandosi sul confronto tra \( k \)
e l'elemento al centro dell'intervallo.'''



### **Struttura dell'Algoritmo**

''' #1. **Inizializzazione**:
   - Definiamo \( lx \) (indice più a sinistra) e \( rx \) (indice più a destra) per coprire tutto l'array.
   - \( lx = 0 \) → punta al primo elemento.
   - \( rx = len(a) - 1 \) → punta all'ultimo elemento.
   - L'intervallo iniziale è quindi l'intero array.
'''

'''
#2. **Ciclo While**:
   - **Condizione**: \( lx < rx \) → il ciclo continua finché c'è un intervallo da controllare.
   - Calcoliamo il punto medio \( cx \) come cx = int((lx + rx) / 2).
   - Controlliamo il valore ( a[cx] ):
     - **Se \( k == a[cx] \)**: Abbiamo trovato il valore cercato e lo stampiamo.
     - **Se \( k < a[cx] \)**: Riduciamo l'intervallo alla metà sinistra (aggiorniamo \( rx \)).
     - **Se \( k > a[cx] \)**: Riduciamo l'intervallo alla metà destra (aggiorniamo \( lx \)).
'''

'''
3. **Controllo Finale**:
   - Se il ciclo termina senza trovare il valore:
     - Stampiamo un intervallo \((lx, cx)\) o \((cx, rx)\), che indica dove si troverebbe ( k ) se fosse presente.

'''

### **Esempio Pratico**

#### **Dati**
'''- Array: \( a = [-2, 3, 9, 12, 13] \)
- Valore cercato: \( k = 4 \)
'''
#### **Passaggi dell'Algoritmo**
'''
1. **Inizializzazione**:
   - \( lx = 0 \), \( rx = 4 \) (lunghezza dell'array - 1).
   - Intervallo iniziale: \( [lx, rx] = [0, 4] \).
   
   Intervallo iniziale:
   0     1     2      3      4
[ -2,    3,    9,    12,    13 ]
  lx                          rx
   
   '''

# 2. **Primo Ciclo**:
'''
#    Calcolo del punto medio:
#    cx = int((lx + rx) / 2) = int((0 + 4) / 2) = 2
#    Controllo del valore al punto medio:
#    a[cx] = a[2] = 9.
#    Confronto:
#    k (4) < a[cx] (9) → Riduciamo l'intervallo alla metà sinistra:
#    Aggiorniamo: rx = cx = 2.
#    Nuovo intervallo: [lx, rx] = [0, 2].

Dopo il primo ciclo:
[ -2,    3 ]
  lx    rx

'''

# 3. **Secondo Ciclo**:
'''
#    Calcolo del punto medio:
#    cx = int((lx + rx) / 2) = int((0 + 2) / 2) = 1
#    Controllo del valore al punto medio:
#    a[cx] = a[1] = 3.
#    Confronto:
#    k (4) > a[cx] (3) → Riduciamo l'intervallo alla metà destra:
#    Aggiorniamo lx = cx + 1 = 2.
#    Nuovo intervallo: [lx, rx] = [2, 2].'''

# 4. **Fine del Ciclo**:
'''
#    Ora lx = 2, rx = 2, quindi lx >= rx.
#    Il ciclo termina.
# '''

# 5. **Controllo Finale**:
'''
#    Confrontiamo k con a[cx] = a[2] = 9:
#    k (4) < a[cx] (9) → Stampiamo l'intervallo (lx, cx) = (2, 2).
# '''

# #### **Output**:
'''
# # (2, 2)
# Questo indica che k = 4 non è presente, ma se lo fosse, si troverebbe tra gli indici 2 e 2.
# '''


# ### **Come Divide l'Intervallo**
'''# L'algoritmo divide l'intervallo in **punti medi** e seleziona la metà rilevante per la ricerca.'''

# #### **Diagramma della Divisione**
'''# Supponiamo di avere a = [-2, 3, 9, 12, 13] e di cercare k = 4:'''

# Esempio dettagliato con il caso in cui rx = cx - 1

# #### **Dati Iniziali**
'''# - Array: a = [-2, 3, 9, 12, 13]
# - Valore da cercare: k = 2'''

# #### **Passaggi dell'Algoritmo**

# 1. **Inizializzazione**
'''
#    - lx = 0, rx = 4 (lunghezza dell'array - 1).
#    - Intervallo iniziale: [lx, rx] = [0, 4].

Intervallo iniziale:
[ -2,    3,    9,    12,    13 ]
  lx                          rx
'''

# ---

### 2. **Primo Ciclo**
'''   
# Calcolo del punto medio:
#    cx = int((lx + rx) / 2) = int((0 + 4) / 2) = 2
#    Controllo del valore al punto medio:
#    a[cx] = a[2] = 9.
#    
# Confronto:
#    k (2) < a[cx] (9) → Riduciamo l'intervallo alla metà sinistra:
#    Aggiorniamo rx = cx - 1 = 1.
#    Nuovo intervallo: [lx, rx] = [0, 1].

Dopo il primo ciclo:
[ -2,    3 ]
  lx      rx
'''

# ---

# 3. **Secondo Ciclo**
'''
#Calcolo del punto medio:
#    cx = int((lx + rx) / 2) = int((0 + 1) / 2) = 0
#    Controllo del valore al punto medio:
#    a[cx] = a[0] = -2.
#    
# Confronto:
#    k (2) > a[cx] (-2) → Riduciamo l'intervallo alla metà destra:
#    Aggiorniamo lx = cx + 1 = 1.
#    Nuovo intervallo: [lx, rx] = [1, 1].

Dopo il secondo ciclo:
[   3   ]
   lx/rx
'''

# ---

# 4. **Terzo Ciclo**
'''
#    Calcolo del punto medio:
#    cx = int((lx + rx) / 2) = int((1 + 1) / 2) = 1
#    Controllo del valore al punto medio:
#    a[cx] = a[1] = 3.
#    Confronto:
#    k (2) < a[cx] (3) → Riduciamo l'intervallo alla metà sinistra:
#    Aggiorniamo rx = cx - 1 = 0.
#    Nuovo intervallo: [lx, rx] = [1, 0].
# '''



# 5. **Fine del Ciclo**
'''#    Ora lx > rx → Il ciclo termina.'''


# #### **Output**
'''
# Poiché k non è presente, stampiamo l'intervallo:
# (0, 1)
# '''



# ### **Diagramma Completo**
'''
1. Inizializzazione:
[ -2,    3,    9,    12,    13 ]
  lx                          rx

2. Primo Ciclo:
[ -2,    3 ]
  lx      rx

3. Secondo Ciclo:
[   3   ]
   lx/rx

4. Fine del Ciclo:
Intervallo vuoto, lx > rx.
'''

# Questo esempio mostra come rx = cx - 1 restringa l'intervallo alla metà sinistra,
# ignorando il punto medio e tutto ciò che si trova a destra.


# ---
# ### **Conclusioni**
'''
# 1. L'algoritmo riduce **progressivamente l'intervallo** di ricerca, dimezzando il numero di elementi da controllare a ogni iterazione.
# 2. Se k è trovato, stampa il valore e il successivo.
# 3. Se k non è trovato, stampa l'intervallo in cui k si troverebbe se fosse presente.
'''


'''1. Inizializzazione:
[ -2,    3,    9,    12,    13 ]
  lx                          rx

2. Primo Ciclo:
[ -2,    3,    9 ]
  lx           rx

3. Secondo Ciclo:
[   9   ]
   lx/rx
   
   '''

#-================================-======-=-=-=-===--=-=-=-==---=-===========================================================================================================

# Array ordinato di partenza

'''
4) qui cambio l'ultimo passaggio ossia l'elif, questa versione ha un problema,
che se il valore e' fra i due estremi da errore 

'''
a = [-2, 3, 9, 12, 13]  # Lista ordinata di elementi su cui fare la ricerca
k = 4                   # Elemento da cercare nell'array

# Inizializzazione degli estremi dell'intervallo di ricerca
lx, rx = 0, len(a) - 1  # lx = primo indice (sinistro), rx = ultimo indice (destro)

# Ciclo di ricerca binaria
while lx <= rx:  
    cx = int((lx + rx) / 2)  # Calcolo del punto medio come media tra lx e rx
    
    if k == a[cx]:  # Se il valore cercato k è uguale al valore al punto medio
        print((a[cx], a[cx+1]))  # Stampiamo il valore trovato e quello successivo
        break  # Uscita immediata dal ciclo poiché abbiamo trovato il valore
    
    elif k < a[cx]:  # Se k è minore del valore al punto medio
        rx = cx - 1  # Restringiamo l'intervallo alla metà sinistra escludendo il punto medio
    
    else:  # Se k è maggiore del valore al punto medio
        lx = cx + 1  # Restringiamo l'intervallo alla metà destra escludendo il punto medio
print(lx,cx,rx)

# Controllo finale dopo la fine del ciclo
if k < a[cx]:  # Se il valore cercato è minore del valore al punto medio
    print((a[cx-1],a[cx]))  # Stampiamo lx e cx per indicare l'intervallo in cui k si troverebbe
elif k > a[cx]:  # Se il valore cercato è maggiore del valore al punto medio
    print((a[cx],a[cx+1]))  # Stampiamo cx e rx per indicare l'intervallo in cui k si troverebbe




'''
# La modifica introdotta in questo codice rispetto 
alla versione precedente riguarda ciò che viene
# stampato nel controllo finale dopo il ciclo.
'''
# ### Differenze Chiave

# 1. Prima:
'''
# if k < a[cx]:
#     print((lx, cx))  # Stampavamo gli indici lx e cx
# elif k > a[cx]:
#     print((cx, rx))  # Stampavamo gli indici cx e rx
# - Stampa degli indici:
#   - Veniva indicato l'intervallo sotto forma di indici (lx, cx, rx) in cui k si sarebbe trovato se fosse presente.
#   - Informazione: forniva solo i riferimenti agli indici.
'''
# 2. Adesso:
'''
# if k < a[cx]:
#     print((a[cx-1], a[cx]))  # Stampiamo i valori nell'intervallo
# elif k > a[cx]:
#     print((a[cx], a[cx+1]))  # Stampiamo i valori nell'intervallo
# - Stampa dei valori:
#   - Ora vengono stampati i valori reali corrispondenti agli indici cx-1, cx, cx+1.
#   - Esempio: Se k < a[cx], viene stampata la coppia di valori (a[cx-1], a[cx]),
# indicando che k si troverebbe tra questi due valori.
'''


# ### Cosa Cambia nella Pratica

# 1. Output più leggibile:

'''
#    - La nuova versione stampa direttamente i valori reali dell'array invece degli indici, rendendo più comprensibile
#      dove si collocherebbe k se fosse presente.
'''
# 2. Maggiori informazioni:
'''
#    - Fornendo i valori reali, si può immediatamente capire il contesto numerico.
#    - Esempio: Se k = 4, si potrebbe stampare (3, 9), che indica chiaramente che k si trova tra 3 e 9.
'''
# 3. Necessità di controllo su cx:
'''
#    - Per evitare errori con cx-1 (fuori dal range dell'array), è necessario aggiungere un controllo
#      per gestire i limiti dell'array, specialmente per a[cx-1] e a[cx+1].
'''

# ### Cosa Fare Attenzione
'''
# 1. Verifica del Range:
#    - Quando cx = 0, cx-1 non è valido (indice fuori dal range).
#    - Quando cx = len(a) - 1, cx+1 non è valido.
#    - Soluzione: Aggiungere un controllo condizionale:
#    if k < a[cx]:
#        if cx - 1 >= 0:
#            print((a[cx-1], a[cx]))
#        else:
#            print((None, a[cx]))  # Nessun valore precedente
#    elif k > a[cx]:
#        if cx + 1 < len(a):
#            print((a[cx], a[cx+1]))
#        else:
#            print((a[cx], None))  # Nessun valore successivo

'''

# ### Riassunto
'''
# - La nuova versione rende l'output più intuitivo stampando i valori reali, ma richiede controlli per evitare errori di range.
# - La vecchia versione era più semplice, ma meno leggibile per chi non conosceva gli indici.

'''

#=================================================================================================================================


'''
4) qui risolvo un problema riguardante, quando trova un valore che sta fra i due estremi si blocca 
oltre cioooo modifico la l'algoritmo e' lo faccio diventare una funzione, sostituendo i return 
 

'''

def ricerca_intervallo(a, k):
    # Ciclo di ricerca binaria
    lx, rx = 0, len(a) - 1  # lx = primo indice (sinistro), rx = ultimo indice (destro)
    
    if k < a[0]:  # Controllo se il valore cercato k è minore del primo elemento dell'array
        return ('-if', a[0])  
    # Restituiamo un messaggio per indicare che k è fuori 
    #dai limiti inferiori e il primo valore nell'array

    if k < a[-1]:  # Controllo se il valore cercato k è minore dell'ultimo elemento dell'array
        return (a[-1], '+if') 
    # Restituiamo l'ultimo valore dell'array e 
    #un messaggio per indicare che k è compreso nell'intervallo superiore
 
    while lx <= rx:  
        cx = int((lx + rx) / 2)  # Calcolo del punto medio come media tra lx e rx
        
        if k == a[cx]:  # Se il valore cercato k è uguale al valore al punto medio
            return (a[cx], a[cx+1])  # Stampiamo il valore trovato e quello successivo
           
        elif k < a[cx]:  # Se k è minore del valore al punto medio
            rx = cx - 1  # Restringiamo l'intervallo alla metà sinistra escludendo il punto medio
        
        else:  # Se k è maggiore del valore al punto medio
            lx = cx + 1  # Restringiamo l'intervallo alla metà destra escludendo il punto medio
            
    # Controllo finale dopo la fine del ciclo
    if k < a[cx]:  # Se il valore cercato è minore del valore al punto medio
        return (a[cx-1], a[cx])  # Stampiamo lx e cx per indicare l'intervallo in cui k si troverebbe
    elif k > a[cx]:  # Se il valore cercato è maggiore del valore al punto medio
        return (a[cx], a[cx+1])  # Stampiamo cx e rx per indicare l'intervallo in cui k si troverebbe


a = [-2, 3, 9, 12, 13]  # Lista ordinata di elementi su cui fare la ricerca
k = -2                   # Elemento da cercare nell'array

print(ricerca_intervallo(a, k))


# complessita' spaziale :  O(1) E' costante 

# complessita' temporale : 

#nel caso peggiore e' quando cx corrisponnde subito a k, quindi il k viene eseguito una volta sola 

# nel caso migliore e' quando l'elemento in  posizione cx corrisponde subito a k perche' e' uguale 
# quindi esco subito dal ciclo while 

# oppure quando l'elemento k  e' maggiore sia del massimo che del minimo, il num di op e' costante O(1)

#il caso peggiore e' quando la sequenza tra rx e lx diventa nulla :

'''
quando la sequenza e' lunga per l'intero spazio alla prima iterazione 
- passo 0
         n
|_____________________|
|                     |

alla seconda operazione sara' n/2 - 1
- passo 1
        n/2
|________________|
|                |
alla terza sara' n/4 perche' divido ad ogni esecuzione 
- passo 2
            n/4
        |________|
        |        |
        

- passo 3 
              n/8
            |____|
            |    |
            
- al passo i essimo  sara' 
    n/2 i

#divido sempre di piu' fino ad arrivare a nulla

ad un certo punto la sequenza sara' uguale ad 1 ma anche 2 

- Quindi arrivero' fino ad un certo numero di passi' che non so quindi gli do 't' passi, 
perche' e' il tempo che impiego per terminare l'algoritmo, quindi eseguo t passi per terminarlo 
t e' la mia incognita' t e' uguale a 1 =n/2t(piccolo) , 
# t e' quel numero tale che n/2t= 1  eprche' una volta che i while termina e da il suo risultato 
#e da  il suo risultato quando la sequenza diventa di dimensioni piccole costanti 
quindi  n/2t e  = 2t(piccolo )=  (t sotto n) = t = log_2 n 

             1 =n/2t(piccolo) = 2t(piccolo )= n (t sotto n) = t = log_2 n 
            |_|
            | |
ad ogni passo eseguo un numero di operazioni costanti, quindi la complessita' dell'algoritmo e' O(t)
oppure nel caso peggiore O(log_2 N )
      
'''
# Complessita' spaziale : O(1) perrrche' esegue op costanti 
# Complessita' temporale : nel caso peggiore O(log_2 N )  


# un algoritmo con O(log_2 N ) e' migliore perche' 

'''
differenza tra i due: 

trovano entrambi =delle soluz. che pero' hanno due velocita diverse sia di operazioni che sonio date dalle funz.

        O(n)               O(log_2 N )

* - Quando e' lineare, e' raddopio l'input succede che che raddopio
il tempo di esssecuzione del programma del programma e funzione, 
se sto usando tale raddopiando la dimensione dell'input, raddoppio il tempo di ricerca 

- che succede invece se raddopio la dimensione dell'algoritmo come nel caso della ricerca binaria 
dove ogni volta scarto il resto quando trovo l'estromo migliore, succede che alla prima iterazione 
scarto ed eseguo lo stesso numero di op, quindi scartando automaticamente tot operazioni, significa 
che se raddopio l'input che basta un op in piu', quindi dovro' fare piu' operazioni quindi +1, 
rispetto a O(n)

'''