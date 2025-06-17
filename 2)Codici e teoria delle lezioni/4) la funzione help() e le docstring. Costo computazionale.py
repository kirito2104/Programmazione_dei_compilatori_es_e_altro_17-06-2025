
# Data una stringa conta un determinato numero di parole dentro una stringa 


a0 = 'programmazione dei compilatori con lab ee  ee ' 
# La stringa `a0` contiene una frase che rappresenta il testo su cui verrà effettuata l'analisi.

a1 = 'linguaggi di programmazione c:: python. eeeee edd dd d '
# La stringa `a1` rappresenta un'altra sequenza di testo. Probabilmente verrà utilizzata
# come parte del conteggio delle parole o per un confronto.

def lettera(c0):  
    # La funzione `lettera` verifica se un carattere `c0` è una lettera minuscola.
    # Utilizza la condizione `c0 >= 'a' and c0 <= 'z'`, che confronta il valore Unicode
    # del carattere `c0` con i valori delle lettere minuscole dell'alfabeto:
    # - 'a' (97 in Unicode) e 'z' (122 in Unicode).
    # Restituisce `True` se il carattere è una lettera minuscola, altrimenti `False`.
    return c0 >= 'a' and c0 <= 'z'



def conta_parole(a):
    
    '''
    input: a una stringa 
    Return : a numero di parole nella stampa  
    Una parola e' una sequenza massimale di caratteri alfabetici minuscoli 
    '''
    
    # La funzione `conta_parole` calcola il numero di parole nella stringa `a`.
    # Una parola è definita come una sequenza continua di lettere minuscole.

    # Inizializza il contatore delle parole a 0.
    parole = 0

    # Inizializza un flag booleano `in_parola` per monitorare se ci si trova attualmente
    # all'interno di una parola. Questo aiuta a distinguere l'inizio e la fine di una parola.
    in_parola = False  

    for c in a:  
        # Itera su ogni carattere della stringa `a`.
        # La variabile `c` rappresenta il carattere corrente.

        if lettera(c):  # numero costante di operazioni c0 
            
            # Verifica se il carattere corrente è una lettera minuscola utilizzando la funzione `lettera(c)`.
            # Se la funzione restituisce `True`, significa che `c` è una lettera.

            if not in_parola: #numero costante di ops c1
                '''2 , no 3 , no 4 , no 5, alcune volte 4 '''  
                
                # Se non ci si trova già all'interno di una parola (`in_parola == False`),
                # allora questo carattere rappresenta l'inizio di una nuova parola.
                parole += 1  # # num costante di ops c2
                
                # Incrementa il contatore delle parole.

                in_parola = True  #numero di ops costante di ops c3 
                
                # Imposta il flag `in_parola` a `True` per indicare che ora ci si trova
                # all'interno di una parola.

        else:  
            # Se il carattere corrente NON è una lettera:
            # Significa che la parola è terminata o che il carattere è un separatore (spazio, simbolo, ecc.).

            if in_parola:       #num costanti di ops c4
                # Se ci si trovava in una parola (`in_parola == True`), allora:
                
                in_parola = False       #num costante di ops c3
                # Imposta `in_parola` a `False` per indicare che non ci si trova più
                # all'interno di una parola.
                
                print('non e in parola')  
                # Stampa un messaggio per indicare che il carattere corrente non fa parte di una parola.

   
        ''' IL COSTO DEL BLOCCO SARA' 
        **
        *c0 +c1+c2+c3 oppure c0 + c1 oppure c0 + c4 + c5
        **
        *oppure c0 + c4
        *
        *in ogni caso e' costante (dicimo c )
        *
        *IL COSTO SARA QUINDI LINIERA IN QUESTA STRINGA 
        *
        * il costo della funzione e' n*c + d 
        *
        '''
    return parole  # se non ci fosse stata la funzione avrei stampato nel print, le parole 

    # Restituisce il numero totale di parole trovate nella stringa `a`.
    
    '''
    # Il costo della funzione è n*c + d dove d è una costante
    # e rappresenta il costo delle inizializzazione e del return
    # 
    # Al crescere di n, la costante d diventa sempre più ininfluente,
    # quindi va tolta. In generale rimangono soltanto i termini di ordine
    # superiore.
    #
    # Il costo c*n risente dalla costante c che a sua volta può dipendere da
    # fattori incontrollabili (implementazione a basso livello delle operazioni
    # elementari), quindi anche le costanti moltiplicative vengono eliminate
    #
    Rimane l'ordine di grandezza della funzione...
    '''
    
# Stampa il risultato del conteggio delle parole nella stringa `a1`.
# La funzione `conta_parole` viene chiamata con l'argomento `a1`, e il risultato è stampato.
print('Ecco le parole contate:', conta_parole(a1)) 


#======================================================================================================================================

# la funzione help restituisce : agisce anchesu funzioni non incorporate, non restituissce null

#================================================================================================================================================


'''
La complessità computazionale di questo codice può essere compresa analizzando 
il numero di operazioni eseguite rispetto alla lunghezza della stringa in input. 
Ecco una spiegazione dettagliata:
'''


## **Passo 1: Complessità delle singole operazioni**
#Nel ciclo `for`, per ogni carattere della stringa `a`, 
# vengono eseguite alcune operazioni. Vediamo le principali:

# 1. **Chiamata a `lettera(c)`**:
   #- Questa funzione verifica se un carattere è una lettera minuscola con un confronto:
     
'''     return c0 >= 'a' and c0 <= 'z'\ '''     
   # - Ogni confronto ha **costo costante** \( c_0 \), indipendentemente dal valore di `c`.

# 2. **Controllo `if not in_parola` o `if in_parola`**:
   #- Sono semplici confronti booleani, ciascuno con **costo costante** \( c_1 \).

# 3. **Incremento del contatore `parole += 1`**:
   #- Operazione aritmetica con **costo costante** \( c_2 \).

#4. **Assegnazione a `in_parola`**:
   #- Assegnare `True` o `False` ha un **costo costante** \( c_3 \).

#5. **Stampa di un messaggio**:
   #- La stampa con `print('non e in parola')` ha un **costo costante**, ma con una 
   # dipendenza aggiuntiva dal sistema di I/O (di solito trascurabile nell'analisi asintotica).


### **Passo 2: Ciclo `for`**
#Il ciclo `for` esegue un'iterazione per **ogni carattere** della stringa `a`.
# Se la lunghezza della stringa è \( n \), il ciclo itera \( n \) volte.

'''
Per ogni iterazione:
- Eseguiamo un numero costante di operazioni (\( c_0 + c_1 + c_2 + c_3 \)), indipendentemente dal carattere corrente.

Il **costo complessivo del ciclo** è quindi:
\[ \text{Costo ciclo} = n \cdot c \]

dove \( c \) è la somma dei costi delle operazioni elementari in ciascuna iterazione.
'''



# **Passo 3: Inizializzazioni e Return**
#- L'inizializzazione delle variabili (`parole = 0`, `in_parola = False`) ha un costo **costante** \( d \).
#- Il `return` alla fine della funzione ha anch'esso un costo **costante**.

'''Questi costi costanti (\( d \)) non dipendono dalla lunghezza della stringa e diventano trascurabili al crescere di \( n \). '''


### **Passo 4: Complessità totale**

'''
La complessità totale della funzione è:
\[ T(n) = n \cdot c + d \]
- \( n \): Lunghezza della stringa (numero di caratteri).
- \( c \): Costo costante delle operazioni per ogni iterazione.
- \( d \): Costo costante delle inizializzazioni e del return.
'''
### **Passo 5: Analisi Asintotica**

#Nell'analisi della complessità computazionale, trascuriamo 
#i termini costanti (\( c \) e \( d \)) per concentrarci sull'ordine
#di grandezza dominante, che dipende dalla lunghezza della stringa \( n \).

'''
Di conseguenza, la complessità computazionale è:
\[ T(n) = O(n) \]
- **Lineare** rispetto alla lunghezza della stringa.
'''

# **Perché è lineare?**

#1. Ogni carattere della stringa viene visitato una sola volta (il ciclo itera esattamente \( n \) volte).
#2. Ogni operazione all'interno del ciclo ha un costo costante, indipendente da \( n \).



# **Esempio Pratico**
# Input:

#a = "programmazione dei compilatori"

#Lunghezza di \( a = 30 \) caratteri.

#1. **Iterazioni del ciclo**:
   #- Il ciclo `for` esegue 30 iterazioni.

#2. **Operazioni per iterazione**:
   #- Ogni iterazione include la chiamata a `lettera(c)` e altre operazioni booleane/arimetiche, tutte con costo costante.

#3. **Costo complessivo**:
   #- Totale operazioni: \( 30 \cdot c + d \) (dove \( c \) e \( d \) sono costanti).



### **Conclusione**-=
'''
La complessità computazionale del codice è **lineare**, \( O(n) \), 
rispetto alla lunghezza della stringa \( n \). Ciò significa che 
il tempo necessario per eseguire la funzione cresce proporzionalmente alla dimensione dell'input.
'''

















         






#==========================================================================================================================================










        
        
        
        
        
        
        
        
        
        
        