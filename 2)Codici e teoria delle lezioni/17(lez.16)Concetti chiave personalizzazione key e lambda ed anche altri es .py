
#Personalizzazione del criterio di ordinamento con parametro key;
#ordinamento multicriterio tramite confronto tra tuple. Funzioni lambda.
#Espressioni condizionali. La funzione incorporata sorted() ed il metodo sort() delle liste.





def merge_sort( a, lx = 0, rx = None ):
    '''
        Input: a una sequenza di elementi che possono essere confrontati
        lx < rx: indice sinistro e destro di a
        Output: None
        Effetto collaterale: ordinare in loco gli elementi di a[lx:rx]
    '''

    def merge(a, lx, cx, rx):
        '''
            Input: a una lista di elementi
            lx, cx e rx indici in a t.c. lx <= cx <= rx
            con la proprietà che a[lx:cx] e a[cx:rx] sono ordinate
            Output: None
            Effetto collaterale: a[lx:rx] è ordinata
        '''

        # i e j sono indici per scorrere rispettivamente le due sottoliste a[lx:cx] e a[cx:rx]
        i, j = lx, cx
        # c è una lista temporanea che conterrà gli elementi uniti e ordinati
        c = []

        # Confronta e unisce gli elementi finché non si raggiunge la fine di una delle due sottoliste
        while i < cx and j < rx:
            if a[i] <= a[j]:
                c.append(a[i])  # Aggiunge l'elemento minore alla lista c
                i += 1
            else:
                c.append(a[j])  # Aggiunge l'elemento minore dalla seconda sottolista
                j += 1

        # Aggiunge eventuali elementi rimanenti dalla prima sottolista
        while i < cx:
            c.append(a[i])
            i += 1

        # Aggiunge eventuali elementi rimanenti dalla seconda sottolista
        while j < rx:
            c.append(a[j])
            j += 1

        # Copia gli elementi ordinati dalla lista temporanea c nella lista originale a
        i = lx
        for e in c:
            a[i] = e
            i += 1

    # Se rx non è specificato, imposta rx alla lunghezza della lista a
    if rx == None:
        rx = len(a)

    # Caso base: se la sottolista ha un solo elemento o meno, è già ordinata
    if lx + 1 >= rx:
        return None

    # Calcola l'indice centrale per dividere la lista in due sottoliste
    cx = int((lx + rx) / 2)

    # Richiama ricorsivamente merge_sort sulle due metà della lista
    merge_sort(a, lx, cx)
    merge_sort(a, cx, rx)

    # Unisce le due sottoliste ordinate
    merge(a, lx, cx, rx)

    
# ' il programma sara piu compatto con la sotto funzione merege al suo interno  
  
  
#===========================================================================================================================================
# In[]
    
a = ['programmazione', 'dei', 'calcolatori', '2024/25']
merge_sort(a)
print(a)
# ordinera nel sequente ordine mettendo prima i numeri e poi ordinando in ordine alfabetico 
# ossia cosi' ['2024/25', 'calcolatori', 'dei', 'programmazione']


#===========================================================================================================================================
# In[] qui invece ordinera' le stringhe in ordine di grandezza



def Umerge_sort( a, lx = 0, rx = None ):
    '''
        Input: a una sequenza di elementi che possono essere confrontati
        lx < rx: indice sinistro e destro di a
        Output: None
        Effetto collaterale: ordinare in loco gli elementi di a[lx:rx]
    '''

    def UMerge(a, lx, cx, rx):
        '''
            Input: a una lista di elementi
            lx, cx e rx indici in a t.c. lx <= cx <= rx
            con la proprietà che a[lx:cx] e a[cx:rx] sono ordinate
            Output: None
            Effetto collaterale: a[lx:rx] è ordinata
        '''

        # i e j sono indici per scorrere rispettivamente le due sottoliste a[lx:cx] e a[cx:rx]
        i, j = lx, cx
        # c è una lista temporanea che conterrà gli elementi uniti e ordinati
        c = []

        # Confronta e unisce gli elementi finché non si raggiunge la fine di una delle due sottoliste
        while i < cx and j < rx:
            if len(a[i])<= len(a[j]) :
                # questo if permette di ordinare in mdo che la stringa con meno caratteri sia messa per prima e vice versa 
                
                
                
                
                c.append(a[i])  # Aggiunge l'elemento minore alla lista c
                i += 1
            else:
                c.append(a[j])  # Aggiunge l'elemento minore dalla seconda sottolista
                j += 1

        # Aggiunge eventuali elementi rimanenti dalla prima sottolista
        while i < cx:
            c.append(a[i])
            i += 1

        # Aggiunge eventuali elementi rimanenti dalla seconda sottolista
        while j < rx:
            c.append(a[j])
            j += 1

        # Copia gli elementi ordinati dalla lista temporanea c nella lista originale a
        i = lx
        for e in c:
            a[i] = e
            i += 1

    # Se rx non è specificato, imposta rx alla lunghezza della lista a
    if rx == None:
        rx = len(a)

    # Caso base: se la sottolista ha un solo elemento o meno, è già ordinata
    if lx + 1 >= rx:
        return None

    # Calcola l'indice centrale per dividere la lista in due sottoliste
    cx = int((lx + rx) / 2)

    # Richiama ricorsivamente merge_sort sulle due metà della lista
    Umerge_sort(a, lx, cx)
    Umerge_sort(a, cx, rx)

    # Unisce le due sottoliste ordinate
    UMerge(a, lx, cx, rx)



a = ['programmazione', 'dei', 'calcolatori', '2024/25']
Umerge_sort(a)
print(a)
# ordinera nel sequente ordine mettendo prima i numeri e poi ordinando in ordine alfabetico 
# ossia cosi' ['2024/25', 'calcolatori', 'dei', 'programmazione']

#===============================================================================================================================================================================================================================================================================
#===============================================================================================================================================================================================================================================================================
#===============================================================================================================================================================================================================================================================================
# Funzione merge_sort per ordinare un array in modo ricorsivo
#def merge_sort(a, lx=0, rx=None):
'''
    Input: a una sequenza di elementi che possono essere confrontati
    lx < rx: indice sinistro e destro di a
    Output: None
    Effetto collaterale: ordinare in loco gli elementi di a[lx:rx]
    '''
    # Scopo: Ordina un array a da indice lx a rx in modo ricorsivo.
    # Caso base: Se lx + 1 >= rx, la sottolista ha zero o un elemento e non necessita di ordinamento.
    # Divisione: La lista viene divisa in due metà; il processo ricorsivo viene applicato a ciascuna metà.
    # Merge: Dopo aver ordinato ricorsivamente le due metà, esse vengono fuse insieme in modo ordinato.

# Funzione merge per fondere due sottoliste ordinate
#def merge(a, lx, cx, rx):
'''
    Input: a una lista di elementi
    lx, cx e rx indici in a t.c. lx <= cx <= rx
    con la proprietà che a[lx:cx] e a[cx:rx] sono ordinate
    Output: None
    Effetto collaterale: a[lx:rx] è ordinata
    '''
    # Scopo: Fonde due sottoliste ordinate a[lx:cx] e a[cx:rx].
    # Operazione di merge: Elementi delle due sottoliste vengono confrontati e aggiunti in ordine nella lista temporanea c.
    # Gli elementi rimanenti di una delle due sottoliste (se presenti) vengono aggiunti alla fine.
    # Copia finale: Gli elementi dalla lista temporanea c vengono copiati nella posizione originale di a, sovrascrivendo i valori esistenti.

# Varianti e Uso
# Ordinamento di stringhe per valore e per lunghezza: Viene mostrato come l'algoritmo può essere facilmente adattato per ordinare le stringhe per lunghezza semplicemente modificando il criterio di confronto nel merge.

# Esempio di utilizzo
'''
a = ['programmazione', 'dei', 'calcolatori', '2024/25']
merge_sort(a)
print(a)  # Output: ['2024/25', 'calcolatori', 'dei', 'programmazione']

# Funzione Umerge_sort
# Variante personalizzata: Ordina gli elementi basandosi sulla lunghezza delle stringhe.
# Modifica nel confronto: Durante la fusione, il confronto tra gli elementi si basa sulla lunghezza delle stringhe (len(a[i]) <= len(a[j])).

# Uso della funzione personalizzata
a = ['programmazione', 'dei', 'calcolatori', '2024/25']
Umerge_sort(a)
print(a)  # Output: ['dei', '2024/25', 'calcolatori', 'programmazione']

'''
# Conclusione
# Questo codice dimostra l'efficacia e la versatilità del merge sort, mostrando come può essere adattato per vari criteri di ordinamento con modifiche minime.
# La struttura ricorsiva e la fusione efficace di sottoliste ordinate garantiscono che l'algoritmo sia efficiente e robusto per un ampio spettro di applicazioni di ordinamento.
################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################

''' 
Lambda function :  conosciute anche come funzioni anonime, 
sono un tipo di funzione scritta in una sola riga.
Sono chiamate "anonime" perché a differenza delle funzioni definite con def, 
le lambda function non hanno un nome esplicito.
'''

# sintassi, x e' il parametro e' definisce una variabile sensa nome  

v = (lambda x : x**2) (2)# questo e' un valore ossia il risultato definito  con parametro 2 

f = lambda x: x  # E' la funzione  di un parametro edentita' 

'''
La Funzione Lambda ha diverse carattaeristiche 
'''
#Compattezza: Sono generalmente più brevi e più concise rispetto alle funzioni tradizionali definite con def.
# Questo le rende ideali per l'uso in situazioni dove una funzione semplice è necessaria per un breve periodo.


#Funzione in una sola riga: Ogni lambda può essere definita in una singola espressione. Non possono contenere comandi multipli o espressioni complesse.

# Anonimato: Non hanno un nome esplicito, il che le rende utili come funzioni "usa e getta" da utilizzare dove sono necessarie.

#Flessibilità: Possono essere usate ovunque sia richiesta una funzione, come argomenti di funzioni di ordine superiore che richiedono una funzione come input (ad esempio, map(), filter(), sort(), ecc.).

'''
Nell'esercizio :
Sintassi: La funzione inizia con la parola chiave lambda, 
seguita da uno o più parametri (in questo caso solo x), un colon (:),
e poi un'espressione che definisce cosa fa la funzione. Qui, x**2 calcola il quadrato di x.

Esecuzione immediata: La funzione (lambda x: x**2) è definita e poi immediatamente chiamata con l'argomento (2). 
Questo significa che x è sostituito con 2, e il quadrato di 2, che è 4, viene calcolato e restituito.

Utilizzo: L'output della lambda function è assegnato alla variabile v. Quindi, v sarà 4 dopo l'esecuzione di questa riga.

'''

 
###############################################################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################


'''
qui invece a differenza di prima creo una funzione dove faccio la stessa cosa di sopra ma la rendo un parametro ossia key lo definisco uguale a None,
ossia di default che all'interno della funzione identita'.

(ps: ricordati di richiamre, tutti i parametri all'interno della funz)

lo definisco dentro  la sottofunzione merge  

'''


# Funzione merge_sort con parametro key per un ordinamento personalizzato
def merge_sort_seconda_modifica_key(a, key=lambda x:x , lx=0, rx=None):
    #**Lambda di x: x** :
    #Questa espressione lambda è la più semplice possibile; prende un argomento `x`
    # e lo restituisce tale e quale. Non apporta modifiche al valore di `x`.

    #**Uso di lambda in merge_sort**
    #Integrare una lambda function in `merge_sort` permette di personalizzare il criterio di confronto 
    # direttamente all'interno della funzione. Per esempio, una lambda come `lambda x: len(x)`
    # fa in modo che `merge_sort` ordini gli elementi (ad esempio stringhe) in base alla loro lunghezza,
    # rendendo il comportamento specifico per quel tipo di dati senza necessità di specificarlo ogni volta che si chiama la funzione.
    
    
    
    
    '''
    Input: 
        a: una sequenza di elementi che possono essere confrontati.
        lx, rx: indici sinistro e destro di a che definiscono la porzione da ordinare.
        key: funzione che definisce il criterio secondo cui gli elementi sono confrontati e ordinati.
    Output: 
        None.
    Effetto collaterale:
        Ordina in loco gli elementi di a[lx:rx] secondo il criterio definito da key.
    '''

    
    '''if key == None:
        key = lambda x : x 
        
    # usando lambda :
    # inserire una lambda function all'interno di una funzione di ordinamento come merge_sort
    # può offrire un modo versatile per personalizzare il criterio di confronto utilizzato nell'ordinamento.
    # Utilizzando una lambda function come parametro key, puoi definire dinamicamente come gli elementi della
    # lista devono essere comparati durante l'ordinamento. Questo approccio è particolarmente utile quando
    # vuoi ordinare oggetti complessi o applicare un criterio di ordinamento non standard.
        
        '''
    
    
    def merge(a, lx, cx, rx):
        '''
        Input:
            a: lista di elementi.
            lx, cx, rx: indici in a tali che lx <= cx <= rx, le porzioni a[lx:cx] e a[cx:rx] sono ordinate.
        Output:
            None.
        Effetto collaterale:
            Fonde e ordina in loco a[lx:rx].
        '''

        # i e j sono indici per scorrere rispettivamente le due sottoliste a[lx:cx] e a[cx:rx].
        i, j = lx, cx
        # c è una lista temporanea che conterrà gli elementi uniti e ordinati.
        c = []

        # Confronta e unisce gli elementi delle due sottoliste finché non si raggiunge la fine di una delle due.
        while i < cx and j < rx:
            
            # Utilizza la funzione key per determinare il valore di confronto degli elementi, se fornita.
            if key(a[i]) <= key(a[j]):
                c.append(a[i])  # Aggiunge l'elemento minore alla lista temporanea.
                i += 1
            else:
                c.append(a[j])  # Aggiunge l'elemento minore dalla seconda sottolista.
                j += 1

        # Aggiunge gli elementi rimanenti della prima sottolista.
        while i < cx:
            c.append(a[i])
            i += 1

        # Aggiunge gli elementi rimanenti della seconda sottolista.
        while j < rx:
            c.append(a[j])
            j += 1

        # Copia gli elementi ordinati dalla lista temporanea c nella lista originale a.
        a[lx:lx+len(c)] = c

    # Imposta rx alla lunghezza di a se non è stato specificato.
    if rx == None:
        rx = len(a)

    # Caso base: se la sottolista ha un solo elemento o meno, è già ordinata.
    if lx + 1 >= rx:
        return

    # Calcola l'indice centrale per dividere la lista in due sottoliste.
    cx = (lx + rx) // 2

    # Richiama ricorsivamente merge_sort sulle due metà della lista.
    merge_sort_seconda_modifica_key(a, key, lx, cx)
    merge_sort_seconda_modifica_key(a, key, cx, rx)

    # Unisce le due sottoliste ordinate.
    merge(a, lx, cx, rx)


a = ['programmazione', 'dei', 'calcolatori', '2024/25']
merge_sort_seconda_modifica_key(a, key=len)
print(a)



''' parametro key aggiunge una funzionalità significativa alla funzione merge_sort,
consentendo di definire un criterio di confronto personalizzato per gli elementi da ordinare.
Nella versione originale del merge_sort, l'ordinamento degli elementi viene effettuato direttamente
basandosi sui valori degli elementi stessi. Con l'introduzione del parametro key, invece, è possibile
specificare una funzione che determina il valore di confronto per ogni elemento.

Questo è particolarmente utile per casi in cui gli elementi dell'array sono strutture complesse
come oggetti o tuple, e si desidera ordinare l'array basandosi su una specifica proprietà o funzione degli elementi
(ad esempio, ordinare persone in base all'età, o stringhe in base alla loro lunghezza).
Il parametro key quindi generalizza e estende l'applicabilità della funzione 
di ordinamento a una vasta gamma di tipi di dati e criteri di ordinamento.'''

##########################################################
'''Cosa cambia con l'uso della lambda function:'''

#Personalizzazione: La lambda function lambda x: x[1] specifica che l'ordinamento
#deve essere basato sul secondo elemento delle tuple. Senza questo parametro key,
# il merge_sort ordinerebbe le tuple basandosi sul primo elemento per default.

# Versatilità: Utilizzando una lambda function, puoi facilmente cambiare 
# il criterio di ordinamento senza dover riscrivere o modificare la funzione 
# di ordinamento stessa. Questo rende il codice più generico e riutilizzabile.

#Applicabilità: Puoi utilizzare il parametro key per ordinare una vasta gamma 
#di strutture dati basandoti su vari criteri, come lunghezza di stringhe, 
#valori specifici in oggetti complessi, o anche combinazioni più complesse di proprietà.

############################################################################################################################################################################################################



def merge_sort( a, key = lambda x:x, lx = 0, rx = None ):
    '''
        Input: a una sequenza di elementi che possono essere
            confrontati
            lx < rx: indice sinistro e destro di a
        Output: None
        
        Effetto collaterale: ordinare in loco gli elementi di
            a[lx:rx]
    '''
    
    def merge(a, lx, cx, rx):
        '''
            Input: a una lista di elementi
                lx, cx e rx indici in a t.c. lx <= cx <= rx
                con la proprietà che a[lx:cx] e a[cx:rx] sono ordinate
            Output: None
            
            Effetto collaterale a[lx:rx] è ordinata
        '''

        i, j = lx, cx
        c = []
        while i < cx and j < rx:
            if key(a[i]) <= key(a[j]):
                c.append(a[i])
                i += 1
            else:
                c.append(a[j])
                j += 1
        
        while i < cx:
            c.append(a[i])
            i+=1
            
        while j < rx:
            c.append(a[j])
            j += 1
            
        i = lx
        for e in c:
            a[i] = e
            i += 1
    
    if rx == None:
        rx = len(a)
    

    if lx+1 >= rx:
        return None
    
    cx = int((lx+rx)/2)
    
    merge_sort(a, key, lx, cx)
    merge_sort(a, key, cx, rx)
    merge(a, lx, cx, rx)

#===================================================================================================================================================================
'''
in caso abbia numeri e stringhe in questo caso l'ordinamento sara' fatto, 
l'unico problema trasforma i numeri in stringhe non va bene
l'obbiettivo e' quello che le stringhe non dovrebbero essere confrontate con i numeri , trasformati in stringhe 
( ps: quindi devo creare una funz che permette di fare in modo che non venga toccata la funz merge_sort)
( i numeri devo precedere le stringhe sostnzialmente )
( quindi qui se e' una stringa 1 , se e' un numero 0 e' quindi facendo cosi', la funz key assegnera' 0  a tutti i numeri nella funz merge)
'''


''' questo e' quello che esce: [0, 10.4, '2024/25', 3.14, 8, 'calcolatori', 'dei', 'programmazione'] '''

def f(x): 
    # La funzione f accetta un input x e restituisce:
    # 0 se x è di tipo int o float
    # 1 altrimenti
    if type(x) in (int, float):
        return 0 
    else: 
        return 1

# Lista di elementi misti: numeri decimali, stringhe e interi
a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']

# La funzione merge_sort ordina la lista in loco utilizzando la funzione f come chiave.
# key=f specifica che il criterio di ordinamento è determinato dalla funzione f.
merge_sort(a, key=f)  # key diventa una stringa

# In alternativa, si utilizza una funzione lambda per definire il criterio di ordinamento inline.
# La lambda restituisce 0 per tipi int e float, e 1 altrimenti.
merge_sort(a, key=lambda x: 0 if type(x) in (float, int) else 1)

# Stampa la lista ordinata
print(a)

# facendo cosi' staro' al limite ddell'utilizzo di lambda 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# qui sotto invece voglio ordinare le stringhe in modo alfabetico e i numeri in modo numerico 
def f(x): 
    # Controlla se il tipo di x è un numero, ovvero int (intero) o float (decimale)
    if type(x) in (int, float):  
        # Se x è un numero, restituisce la tupla (0, x).
        # Il primo elemento della tupla (0) serve come "etichetta" per identificare i numeri,
        # mentre il secondo elemento (x) è il valore numerico stesso, usato per l'ordinamento.
        return (0, x)  
    
    # Controlla se il tipo di x è una stringa (str)
    elif type(x) == str:  
        # Se x è una stringa, restituisce la tupla (1, x).
        # Il primo elemento della tupla (1) serve come "etichetta" per identificare le stringhe,
        # mentre il secondo elemento (x) è la stringa stessa, usata per l'ordinamento alfabetico.
        return (1, x)  

# Esempio di utilizzo con merge_sort
# Supponiamo di avere una lista mista di numeri e stringhe


# Applichiamo merge_sort utilizzando la funzione f come chiave di ordinamento
merge_sort(a, key=f)


# Lista di elementi misti: numeri decimali, stringhe e interi
a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']
# Stampa la lista ordinata
print(a)

# La lista sarà ordinata come segue:
# [1.5, 2, 3, 'apple', 'banana']
# I numeri vengono ordinati prima in ordine crescente,
# seguiti dalle stringhe in ordine alfabetico.
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# mentre se volessi ordinare per lunghezza bastera' cambiara' mettendo len(x) su il richiamo del merge_sort

# Applichiamo merge_sort utilizzando la funzione f come chiave di ordinamento

'''merge_sort(a, len(x))'''


# Lista di elementi misti: numeri decimali, stringhe e interi
a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']
# Stampa la lista ordinata
print(a)

#-=================================-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#-=================================-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#-=================================-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#-=================================-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

''' 
La Funz. Sorted :
che e' incorporata nel linguaggio, prende in considerazione un iterabile

il parametro: reverse cordina al contrrario 
il parametro key : puo prenderre diversi valori come : None, key e lambda 

la differenza e' con sorted non va a modificare la lista con un iterabile, ma un oggetto nuovo 
Se io imposto una Tupla : mi restituisce una lista, con gli stessi di una tupla orodinati 

'''
a = [ 10,3,2,45764,42,422]
sorted(a)
#a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']

''' iterabile e' anche una stringa e' ordinaera' anche gli eleemnti di una stringas in modo alfabetico, in modo lessico grafico '''

#print(sorted('python'))
#---------------------------------------------------------------------------------------------------------------------------------------------------
'''mentre qui sotto '''

print(sorted(a, key=str)) #facendo cosi' trrasformo tutto in una stringa )

# l'unica differenza e' che sorted non lavora in loco e quindi crea un nuovo oggetto 
# avra' piu' o meno la stessa complessita' del merge sort

#------------------------------------------------------------------------------------------------------------------------------------------------------

'''
il Metodo Sort:
La diferenza e' un metodo : che intrinseco definito solo per determita tipi di dato, e il primo parametro della funzione 
Quindi e' un metodo del tipo lista, quindi si puo' usare con metodi lista 
 
ordina in base all'ordine in essa : quindi modifichera' la lista 

'''
a = [10,8,0,44,665,88]

a.sort()

print(a)
# ===================================================================================================================================================
''' modifichera una lista mista in tutte stringhe '''

a.sort(key =str )# che modifichera tutti gli elenti in una stringa 


a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']


print(a)

# la complessita' e' la stessa del merge_sort e sorted 

#=======================================================================================================================================================











